import requests
import json
import os
import threading

from .request import TelestreamCloudRequest, TelestreamCloudException

CHUNK_SIZE = 5 * 1024 * 1024


class UploadSession(object):

    def __init__(self, credentials, file_name, **kwargs):
        """
        PARAMS
          multi_chunk - if set to "true" use Multi Chunk to upload video
        """
        self.credentials = credentials
        self.file_name = file_name
        self.file_size = os.stat(file_name).st_size
        params = {
            "file_size": self.file_size,
            "file_name": file_name,
            "profiles": "h264",
            "multi_chunk": "true",
        }
        params.update(kwargs)

        data = TelestreamCloudRequest('POST', '/videos/upload.json',
                                      self.credentials, params).send()
        json_data = data.json()

        self.location = json_data['location']

        if params["multi_chunk"] == "true":
            self.part_size = int(json_data["part_size"])
            self.parts = int(json_data["parts"])
            self.uploader = MultiChunkUpload(self)
        else :
            self.uploader = SingleChunkUpload(self)

        self.status = "initialized"
        self.video = None
        self.error_message = None


    def start(self, pos=0):
        if self.status == "initialized":
            self.status = "uploading"
            self.uploader.start(pos)
        else:
            raise KeyError("Already started")

    def resume(self):
        if self.status != 'uploaded':
            self.uploader.resume()
        else:
            raise TelestreamCloudException('File already uploaded')

    def abort(self):
        if self.status != 'uploaded':
            self.status = 'aborted'
            self.error_message = None
            res = requests.delete(self.location)
        else:
            raise TelestreamCloudException('File already uploaded')


class SingleChunkUpload(object):

    def __init__(self, session):
        self.session = session

    def read_chunks(self, file_object, id = 0):
        i = 0

        while True:
            data = file_object.read(CHUNK_SIZE)

            if not data:
                break

            yield (data, i)

            i = i + 1

    def send_chunks(self, pos = 0):
        with open(self.file_name, 'rb') as f:
            f.seek(pos)
            try:
                for chunk, i in self._read_chunks(f):
                    index = i * CHUNK_SIZE
                    res = requests.post(self.location, headers = {
                        'Content-Type': 'application/octet-stream',
                        'Cache-Control': 'no-cache',
                        'Content-Range': "bytes {0}-{1}/{2}".format(pos+index, pos+index+CHUNK_SIZE-1, self.file_size),
                        'Content-Length': str(CHUNK_SIZE)
                    }, data=chunk)
                    if res.status_code == 200:
                        self.status = "uploaded"
                        from .models import Video
                        self.video = Video(self.credentials, res.json())
                    elif res.status_code != 204:
                        self.status = "error"
                        break
            except Exception as e:
                self.status = "error"
                self.error_message = str(e)
                raise e
            except KeyboardInterrupt:
                self.status = "error"
                self.error_message = "interrupted"

    def start(self, pos = 0):
        self.send_chunks(pos)

    def resume(self):
        res = requests.post(self.location, headers = {
            'Content-Type': 'application/octet-stream',
            'Cache-Control': 'no-cache',
            'Content-Range': "bytes */{0}".format(self.file_size),
            'Content-Length': "0"
        })
        if 'Range' not in res.headers:
            raise TelestreamCloudException('Nothing to resume. This file has not been uploaded before.')
        pos = int(res.headers['Range'].split("-")[1])
        self.status = 'initialized'
        self.start(pos=pos)


class MultiChunkUpload(object):

    def __init__(self, session):
        self.session = session
        self.nthreads = 4
        self.parts = range(0, self.session.parts)

    def read_chunks(self, file_object, parts = []):
        for i in parts:
            file_object.seek(i * self.session.part_size)
            data = file_object.read(self.session.part_size)

            if not data:
                break

            yield (data,i)

    def send_chunks(self, pos):
        with open(self.session.file_name, "rb") as fh:

            for chunk, i in self.read_chunks(fh, self.parts[pos::self.nthreads]):
                if self.session.status == "aborted":
                    break

                res = requests.post(self.session.location, headers={
                    'Content-Type': 'application/octet-stream',
                    'Cache-Control': 'no-cache',
                    'X-Part' : str(i),
                    'Content-Length' : str(min(self.session.part_size, len(chunk))), },
                           data = chunk)

                if res.text and loads(res.text)["status"] in ("processing"):
                    self.session.status = "uploaded"
                    self.session.video = Video(self.session.panda, json_attr=res.json())

    def start(self, pos = 0):
        threads = []
        for i in range(0, self.nthreads):
            thread = threading.Thread(name="Thread-%d" % i, target=self.send_chunks, args=(i,))
            threads.append(thread)
            thread.start()


        for thread in threads:
            thread.join()

        self.parts = []

        data = requests.get(self.session.location)

        if data.text:
            json_data = json.loads(data)
            if json_data.has_key('missing_parts'):
                self.parts = ['missing_parts']
                raise TelestreamCloudException('Failed to upload some parts, missing parts: %s' % self.parts)

    def resume(self):
        self.start()
