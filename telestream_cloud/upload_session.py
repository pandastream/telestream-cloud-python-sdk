import requests
import json
import os
import threading

from .request_v2 import TelestreamCloudRequest, TelestreamCloudException
from .upload_file import UploadFile
CHUNK_SIZE = 5 * 1024 * 1024


class UploadSession(object):

    def __init__(self, credentials, file_name, threads = 8, extra_files = {}, **kwargs):
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

        params.update({'extra_files' : self.__parse_extra_files(extra_files)})

        data = TelestreamCloudRequest('POST', '/videos/upload.json',
                                      self.credentials, params).send()
        json_data = data.json()

        self.location = json_data['location']

        self.files = []


        self.status = "initialized"
        self.video = None
        self.error_message = None

        self.extra_files = json_data['extra_files']

        self.files.append(UploadFile(self.location, int(json_data["parts"]), int(json_data["part_size"]),
                                     file_name, "", threads = threads))

        for key in self.extra_files:
            self.files.append(UploadFile(self.location, int(self.extra_files[key]["parts"]), int(self.extra_files[key]["part_size"]),
                                         self.extra_files[key]["name"],  self.extra_files[key]["tag"], threads = threads))


    def __parse_extra_files(self, files):
        extra_files = []
        file_info = lambda tag, file_name: {
            "tag" : tag,
            "file_name" : file_name,
            "file_size" : os.stat(file_name).st_size,
            }

        for tag, file_name in files.iteritems():
            if isinstance(file_name, type([])):
                for i in range(0, len(file_name)):
                    extra_files.append(file_info("%s.index-%d" % (tag, i),
                                                 file_name[i]))
            else:
                extra_files.append(file_info(tag, file_name))

        return extra_files


    def is_uploaded(self):
        return len(list(filter(lambda x: x.status != "uploaded", self.files))) == 0

    def start(self, pos=0):
        if self.status == "initialized":
            self.status = "uploading"

            for upload_file in self.files:
                if upload_file.status != 'uploaded':
                    upload_file.start(pos)

                if upload_file.video:
                    self.video = upload_file.video

            if self.is_uploaded():
                self.status = 'uploaded'

            return self.video

        else:
            raise KeyError("Already started")


    def resume(self):
        if self.status != 'uploaded':
            self.start()
        else:
            raise TelestreamCloudException('Files already uploaded')

    def abort(self):
        if self.status != 'uploaded':
            self.status = 'aborted'

            for upload_file in self.files:
                upload_file.abort()

            self.error_message = None
            res = requests.delete(self.location)
        else:
            raise TelestreamCloudException('Files already uploaded')
