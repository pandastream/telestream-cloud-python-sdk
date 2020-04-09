# Telestream Cloud API client

## Getting Started
### Obtain address for TCS api
In order to use TCS api client first you need to get `ApiKey`. Login to [website](https://cloud.telestream.net/console), go to *Flip* service and open *API Access* tab.
You account will be identified by unique *Api Key*, if it is unavailable click *Reset* button.
### Installation

You can install telestream-cloud using pip:

    pip install telestream-cloud

or directly from GitHub:

    pip install git+https://github.com/pandastream/telestream-cloud-python-sdk.git


### Usage
This example show uploading media file to flip service. If you want to use other service refer to [services](#services).

```python
import telestream_cloud_flip as flip

api_key = "tcs_XXX"

client = flip.FlipApi()
client.api_client.configuration.api_key['X-Api-Key'] = api_key

source_url = "https://storage.cloud.google.com/debug_videos/panda.mp4"

create_video_body = flip.CreateVideoBody(
    source_url = source_url,
    profiles = "h264"
)

factory_id = "test"

video = client.create_video(factory_id, create_video_body)

encodings_list = client.list_video_encodings(video.id, factory_id)
encoding_id = encodings_list.encodings[0].id
print("Created encoding with ID: " + encoding_id)

while True:
    time.sleep(5)
    encoding = client.get_encoding(encoding_id, factory_id)
    print("status=" + encoding.status)
    if encoding.status == "fail":
        break
    if encoding.status == "success":
        signed_url_resp = client.signed_encoding_url(encoding_id, factory_id)
        print("Output URL: " + signed_url_resp.signed_url)
        break
```


## Services
Api client is divided into parts corresponding to services provided. Currently supported services include:
- [Flip](telestream_cloud_flip_sdk/README.md) - high-volume media transcoding to multiple formats
- [Timed Text Speech](telestream_cloud_tts_sdk/README.md) - automated captions and subtitles creation
- [Quality Control](telestream_cloud_qc_sdk/README.md) - automated quality control for file base media
