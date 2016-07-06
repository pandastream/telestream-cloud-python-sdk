Python client for Telestream Cloud
====================

This library provides a low-level interface to the REST API of [**Telestream Cloud**](http://cloud.telestream.net), the online video encoding service.

Installation
-----

You can install telestream-cloud using `pip`:

```bash
pip install telestream-cloud
```

or directly from GitHub:

```
pip install git+https://github.com/pandastream/telestream-cloud-python-sdk.git
```
This module has been tested with Python 2.7 and 3.4.

Usage
-----
To use the module, you need to initialize TelestreamCloud client instance with your credentials (you can obtain them from your account in [**Telestream Cloud console**](https://cloud.telestream.net/console/login)).

```python
from telestream_cloud import TelestreamCloud

tc = TelestreamCloud('your-access-key', 'your-secret-key')
```

Now you need to specify which resource you would like to use. Currently supported resources are:
* `flip`
* additional resources will be available soon, stay tuned ;)

```python
flip = tc.get_resource('flip')
```

`flip` object gives you access to all your Factories, Videos, Encodings and Profiles.


Factories
-----

Available relations:
* `videos` - with `all()`, `find()`, `create()` and `delete()`
* `encodings` - with `all()`, `find()`, `create()` and `delete()`
* `profiles` - with `all()`, `find()`, `create()` and `delete()`

Available methods:
* `get_notifications()` - retrieves data about notifications
* `update_notifications()` - updates notifications data

Retrieving Factories
```python
# list all Factories
for factory in flip.factories.all():
    print(factory)

# retrieve specific factory
factory = flip.factories.find('factory-id')
```

Displaying Factory details
```python
# display all Factory details
>>> print(factory.details)
{'s3_videos_bucket': 'some_bucket', 'updated_at': '2016/01/04 11:10:51 +0000', 'created_at': '2014/12/28 18:17:11 +0000', 'upload_original_video': False, 'id': 'abcdeb2cc233daaa26da6e7dd77eabcd', 's3_private_access': False, 'url': 'http://s3.amazonaws.com/some_bucket/', 'name': 'bucket_name'}

# display specific Factory detail
>>> print(factory.name)
'bucket_name'
>>> print(factory.upload_original_video)
False
```

Factory object gives you access to all Videos, Encodings and Profiles in contains:

```python
# list all videos
for video in factory.videos.all():
    print(video)

# list all encodings
for encoding in factory.encodings.all():
    print(encoding)

# list all profiles
for profile in factory.profiles.all():
    print(profile)

# get specific video (the same can be done for encoding and profile)
video = factory.videos.find('video-id')
```

To modify your Factory details:

```python
factory.name = 'new-name'
factory.upload_original_video = True
factory.save()
```

To display and change modify Factory notifications:

```python
>>> print(factory.get_notifications())
{'delay': 10, 'url': 'http://super-app.io/notifications', 'send_video_payload': False, 'events': {'video_created': False, 'encoding_completed': True, 'encoding_progress': True, 'video_encoded': False}}

>>> factory.update_notifications({
    'delay': 13,
    'send_video_payload': True,
    'events': {
	'video_created': False,
	'video_encoded': False,
	'encoding_progress': False,
	'encoding_completed': False}
  })
```


Videos
-----
Available relations:
* `encodings` - with `all()`, `find()`, `create()` and `delete()`

Available methods:
* `metadata()` - retrives metadata of the given video
* `delete_source_file()` - deletes only the source file from storage

Retrieving Videos and video details
```python
>>> factory.videos.all()
[Video db3f22e498dbbe4bfe631ac39251297e, Video f4c526e2c15a57aebc9721aad258adbd, Video 3fca3b5bc98506178df801281e3e8cf1]

>>> video = factory.videos.find('video-id')
>>> print(video.details)
{'audio_sample_rate': 44100, 'mime_type': 'video/mp4', 'original_filename': 'movie.mp4', 'audio_channels': 2, 'video_codec': 'h264', 'video_bitrate': 344, 'extname': '.mp4', 'source_url': 'https://s3.amazonaws.com/bartek-copper/movie.mp4', 'path': '4147fd6f38fb552c38aba1e2b6923892', 'audio_bitrate': 112, 'updated_at': '2015/12/14 14:22:04 +0000', 'created_at': '2015/12/14 14:21:54 +0000', 'height': 240, 'audio_codec': 'aac', 'status': 'success', 'file_size': 805301, 'id': '4147fd6f38fb552c38aba1e2b6923892', 'width': 300, 'duration': 14014, 'fps': 29.97}

>>> print(video.original_filename)
'movie.mp4'
```

To list all encodings for a selected video:
```python
>>> video.encodings.all()
[Encoding 6e2a18dfa05645cc759f9b9bd51d8c94, Encoding 0b0cbf12f9541c6c2d5d20fdb494ba17, Encoding 73216519c2ff772c668bb85da5976895]
```

To upload new video

```python
# in this case video will be encoded to all profiles available in this factory
video = factory.videos.create(source_url='http://files.com/my_video.mp4')

# use specific profile
video = factory.videos.create(file='/path/to/my_video.mp4', profiles='h264')
```


Encodings
-----

Available methods:
* `video()` - returns corresponding Video object
* `profile()` - return Profile that was used for encoding
* `retry()` - retry a failed encoding
* `cancel()` - cancel encoding
* `delete()` - deletes requested encoding from Telestream Cloud database and your storage

To create a new encoding for a video that already exists:
```python
encoding = factory.encodings.create(video_id='video-id', profile_name='h264')
```

Profiles
-----


Available methods:
* `reload()` - retrieves most up-to-date version of the object
* `delete()` - deletes profile

To create new profile:

```python
profile = factory.profiles.create(preset_name = "h264",
				  name = "h264_1",
				  fps = 45)
```

To update already existing profile:
```python
profile.name = 'new_name'
profile.fps = '60'
profile.save()
```



REST API Examples
----------------

Retrieve a list of all your videos:

```python
from telestream_cloud import TelestreamCloud

tc = TelestreamCloud('your-access-key', 'your-secret-key', factory_id='factory-id')
tc.get('/videos.json')
```

Retrieve a list of profiles you have defined for your account:

```python
tc.get('/profiles.json')
```

Create a new profile:

```python
tc.post('/profiles.json', {
    'title':    'My custom profile',
    'category': 'desktop',
    'extname':  'mp4',
    'width':    320,
    'height':   240,
    'command':  'ffmpeg -i $input_file$ -f mp4 -b 128k $resolution_and_padding$ -y $output_file',
});
```

Upload a video:

```python
tc.post('/videos.json', {
    'source_url': 'http://example.com/path/to/video.mp4',
});
```

Check the status of each encoding (one per profile):

```python
tc.get('/videos/VIDEO_ID/encodings.json');
```

Remove video and profile:

```python
tc.delete('/videos/VIDEO_ID.json');
tc.delete('/profiles/PROFILE_ID.json');
```

Resumable uploads
---------------------

You can upload a local video using `factory.videos.create(file="file.mp4")`. It will attempt to upload the entire file using a single POST request. This is not the best solution for big files, because if the connections brakes right when you reach 95% mark, the entire upload process fails.
This is where reasumable uploads come in handy. First you need create a session object using `upload_session()`. You can start uploading using `start()` method. If the connection brakes, an exception will be raised. You can decide what to do with your session object using `abort()` or `resume()` methods. Current status of the process will be stored in `status` attribute and can have one of following values:
* `initialized` - session ready to start
* `uploading` - upload started
* `error` - something went wrong. You can see the details using `error_message` attribute
* `uploaded` - upload completed
* `aborted` - upload canceled
* `interrupted` - stopped by user during an interactive session
Additionally you can select how many threads will send data, for default it's set to 8 threads.

Usage example:

```python
us = factory.upload_session('/path/to/your/file.mp4', threads = 4)

retry_count = 0
try:
    us.start()
except Exception as e:
    while retry_count < 5 and us.status != "success":
	try:
	    time.sleep(5)
	    us.resume()
	except Exception as e:
	    retry_count += 1
```

Error handling
---------------------
When a `TelestreamCloudException` is raised, it means that something went wrong with the TelestreamCloudRequest you just sent. You can catch this exception an examine no only the error message received, but a full [requests.Response](http://docs.python-requests.org/en/latest/api/?highlight=response#requests.Response) object that will be passed with the exception as `response` attribute:

```python
from telestream_cloud import TelestreamCloudException

try:
    print(factory.profiles.find('some-incorrect-id'))
except TelestreamCloudException as e:
    print(e.response)
    print(e.response)
    print(e.response.status_code)
```

Generating signatures
---------------------

All requests to your Telestream Cloud are signed using HMAC-SHA256, based on a timestamp and your secret key. This is handled transparently. However, sometimes you will want to generate only this signature, in order to make a request by means other than this library. This is the case when using the [JavaScript panda_uploader](https://github.com/pandastream/panda_uploader).

To do this, a method `signed_params()` is provided:

```
from telestream_cloud import TelestreamCloud

tc = TelestreamCloud('your-access-key', 'your-secret-key', factory_id='your-factory-id')

tc.signed_params('POST', '/videos.json')
# => {'access_key': '8df50af4-074f-11df-b278-1231350015b1',
# 'factory_id': 'your-factory-id',
# 'signature': 'LejCdm0O83+jk6/Q5SfGmk14WTO1pB6Sh6Z5eA2w5C0=',
# 'timestamp': '2010-02-26T15:01:46.221513'}

tc.signed_params('GET', '/videos.json', {"some_params": "some_value"})
# => {'access_key': '8df50af4-074f-11df-b278-1231350015b1',
#  'factory_id': 'your-factory-id',
#  'signature': 'uHnGZ+kI9mT3C4vW71Iop9z2N7UKCv38v2l2dvREUIQ=',
#  'some_param': 'some_value',
#  'timestamp': '2010-02-26T15:04:27.039620'}
```
