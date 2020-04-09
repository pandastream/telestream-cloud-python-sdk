# Factory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of a Factory. | [optional] 
**name** | **str** | Human-readable identifier of a Factory. | [optional] 
**created_at** | **str** | A date and time when a Factory has been created. | [optional] 
**updated_at** | **str** | A date and time when a Factory has been updated last time. | [optional] 
**url** | **str** | An URL pointing to the output_bucket_name. | [optional] 
**server_side_encryption** | **bool** | Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set. | [optional] 
**outputs_path_format** | **str** | Specify the directory where the output files should be stored. By default it is not set. More info [here](https://cloud.telestream.net/docs#path-format---know-how). | [optional] 
**store_id** | **str** | Unique ID of a store defined in the stores service that will be used as a destination for all of the outputs created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


