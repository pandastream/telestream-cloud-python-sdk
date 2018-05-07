# CreateVideoBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_url** | **str** | An URL pointing to a source file. | [optional] 
**profiles** | **str** | Comma-separated list of profile names or IDs to be used during encoding. Alternatively, specify none so no encodings are created yet. | [optional] 
**payload** | **str** | Arbitrary string stored along the Video object. | [optional] 
**pipeline** | **str** | String-encoded JSON describing profiles pipeline. | [optional] 
**subtitle_files** | **list[str]** | A list of urls pointing to remote subtitle files. | [optional] 
**extra_files** | **dict(str, list[str])** |  | [optional] 
**extra_variables** | **dict(str, str)** |  | [optional] 
**path_format** | **str** |  | [optional] 
**clip_end** | **str** | Clip ends at a specific time. | [optional] 
**clip_length** | **str** | A clip’s duration. | [optional] 
**clip_offset** | **str** | Clip starts at a specific offset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


