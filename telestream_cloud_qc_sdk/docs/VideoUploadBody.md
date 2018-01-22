# VideoUploadBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_size** | **int** | Size of the file that will be uploaded in &#x60;bytes&#x60;. | 
**file_name** | **str** | Name of the file that will be uploaded. | 
**extra_files** | [**list[ExtraFile]**](ExtraFile.md) | A list of names of additional files that will be uploaded. | [optional] 
**profiles** | **str** | A comma-separated list of profile names or IDs to be used during encoding. Alternatively, specify none so no encodings will created right away. | [optional] 
**multi_chunk** | **bool** |  | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


