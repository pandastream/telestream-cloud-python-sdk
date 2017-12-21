# VideoUploadBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size** | **int** | Size of the file that will be uploaded in &#x60;bytes&#x60;. | 
**file_name** | **str** | Name of the file that will be uploaded. | 
**extra_files** | [**list[ExtraFile]**](ExtraFile.md) | A list of names of additional files that will be uploaded. | [optional] 
**profiles** | **str** | A comma-separated list of profile names or IDs to be used during encoding. Alternatively, specify none so no encodings will created right away. | [optional] 
**path_format** | **str** |  | [optional] 
**payload** | **dict(str, str)** |  | [optional] 
**extra_variables** | **dict(str, str)** |  | [optional] 
**watermark_url** | **str** | URL pointing to an image that will be used asa watermark. | [optional] 
**watermark_left** | **str** | Determines distance between the left edge of a video and the left edge of a watermark image. Can be specified in pixels or percents. This parameter can be set only if watermark_right is not. | [optional] 
**watermark_top** | **str** | Determines distance between the top edge of a video and the top edge of a watermark image. Can be specified in pixels or percents. This parameter can be set only if watermark_bottom is not. | [optional] 
**watermark_right** | **str** | Determines distance between the right edge of a video and the right edge of a watermark image. Can be specified in pixels or percents. This parameter can be set only if watermark_left is not. | [optional] 
**watermark_bottom** | **str** | Determines distance between the bottom edge of a video and the bottom edge of a watermark image. Can be specified in pixels or percents. This parameter can be set only if watermark_top is not. | [optional] 
**watermark_width** | **str** | Determines width of the watermark image. Should be specified in pixels. | [optional] 
**watermark_height** | **str** | Determines width of the watermark image. Should be specified in pixels. | [optional] 
**clip_length** | **str** | Length of the uploaded video. Should be formatted as follows: HH:MM:SS | [optional] 
**clip_offset** | **str** | Clip starts at a specific offset. | [optional] 
**multi_chunk** | **bool** |  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


