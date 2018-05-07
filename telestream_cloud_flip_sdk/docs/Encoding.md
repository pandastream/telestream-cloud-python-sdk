# Encoding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of an Encoding. | [optional] 
**audio_bitrate** | **int** | Audio bitrate (in bits/s). | [optional] 
**audio_channels** | **int** | A number of audio channels. | [optional] 
**audio_codec** | **str** | A codec that is used to encode audio streams. | [optional] 
**audio_sample_rate** | **int** | A number of samples of audio carried per second. | [optional] 
**created_at** | **str** | A date and time when the Encoding has been created. | [optional] 
**duration** | **int** |  | [optional] 
**encoding_progress** | **int** |  | [optional] 
**encoding_time** | **int** |  | [optional] 
**error_class** | **str** | A class of an error that has occurred during the encoding process. It is present only if the encoding status is equal to &#x60;fail&#x60;. | [optional] 
**error_message** | **str** | A message that explains why the encoding process has resulted in an error. It is present only if the encoding status is equal to &#x60;fail&#x60;. | [optional] 
**external_id** | **str** |  | [optional] 
**extname** | **str** | Extension of the output file. | [optional] 
**file_size** | **int** | A size of the output file. | [optional] 
**files** | **list[str]** | An array of output file names. | [optional] 
**fps** | **float** | Number of frames per second. | [optional] 
**height** | **int** | Height of the output video. | [optional] 
**width** | **int** | Width of the output video. | [optional] 
**logfile_url** | **str** | An URL pointing to a logfile. | [optional] 
**mime_type** | **str** | A mime type of the encoded file. | [optional] 
**parent_encoding_id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**profile_id** | **str** | An id of a related Profile. | [optional] 
**profile_name** | **str** | A name of the used Profile. | [optional] 
**screenshots** | **list[str]** |  | [optional] 
**started_encoding_at** | **str** | A date and time when the encoding process has been started | [optional] 
**status** | **str** | Determines at what stage the encoding process is at the moment. | [optional] 
**updated_at** | **str** | A date and time when a Encoding has been updated last time. | [optional] 
**video_bitrate** | **int** | video bitrate (in bits/s) | [optional] 
**video_codec** | **str** | A codec that is used to encode video streams. | [optional] 
**video_id** | **str** | An id of a related Video object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


