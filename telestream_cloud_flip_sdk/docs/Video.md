# Video

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the Video. | [optional] 
**audio_bitrate** | **int** | audio bitrate (in bits/s) | [optional] 
**audio_channels** | **int** | A number of audio channels. | [optional] 
**audio_codec** | **str** | A codec that has been used to encode audio streams. | [optional] 
**audio_sample_rate** | **int** | A number of samples of audio carried per second. | [optional] 
**created_at** | **str** | A date and time when the Video has been created. | [optional] 
**duration** | **int** | A duration of the video in seconds. | [optional] 
**encodings_count** | **int** | A number of related Encoding objects. | [optional] 
**error_class** | **str** | A class of an error that has occurred during the encoding process. It is present only if the encoding status is equal to &#x60;fail&#x60;. | [optional] 
**error_message** | **str** | A message that explains why the encoding process has resulted in an error. It is present only if the encoding status is equal to &#x60;fail&#x60;. | [optional] 
**extname** | **str** | Extension of the source file. | [optional] 
**file_size** | **int** | A size of the source file. | [optional] 
**fps** | **float** | Number of frames per second. | [optional] 
**height** | **int** | Height of the output video. | [optional] 
**width** | **int** | Width of the output video. | [optional] 
**mime_type** | **str** | A mime type of the source file. | [optional] 
**original_filename** | **str** | A name of the source file. | [optional] 
**path** | **str** |  | [optional] 
**payload** | **str** | Payload is an arbitrary text of length 256 or shorter that you can store along the Video. It is typically used to retain an association with one of your own DB record ID. | [optional] 
**source_url** | **str** | An URL pointing to the source file. | [optional] 
**status** | **str** | Determines at what stage of importing process the Video is at the moment. | [optional] 
**updated_at** | **str** | A date and time when a Video has been updated last time. | [optional] 
**video_bitrate** | **int** | video bitrate (in bits/s) | [optional] 
**video_codec** | **str** | A codec that has been used to encode the input file&#39;s video streams. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


