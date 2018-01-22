# Factory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of a Factory. | [optional] 
**name** | **str** | Human-readable identifier of a Factory. | [optional] 
**factory_region** | **str** | A region where the factory is located. | [optional] 
**output_bucket_name** | **str** | A bucket where processed files will be stored. | [optional] 
**acl** | **str** | Specify if your files are public or private (private files need authorization url to access). By default this is not set. | [optional] 
**created_at** | **str** | A date and time when a Factory has been created. | [optional] 
**updated_at** | **str** | A date and time when a Factory has been updated last time. | [optional] 
**url** | **str** | An URL pointing to the output_bucket_name. | [optional] 
**server_side_encryption** | **bool** | Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set. | [optional] 
**input_bucket_name** | **str** | A name of an input bucket. | [optional] 
**input_bucket_watch** | **bool** | Determines whether the Factory should be notified about new files added to the input bucket. | [optional] 
**input_bucket_files_map** | **str** |  | [optional] 
**input_bucket_sync_every_n_min** | **str** | Determines how often the input bucket is synchronised. | [optional] 
**input_bucket_recursive** | **str** |  | [optional] 
**input_bucket_file_pattern** | **str** | A pattern that will be used to locate files in the input bucket. Valid wildcards might be used. | [optional] 
**outputs_path_format** | **str** |  | [optional] 
**storage_provider** | **int** | Specifies which storage provider the factory should use. Available options: S3: 0, Google Cloud Storage: 1, FTP storage: 2, Google Cloud Interoperability Storage: 5, Flip storage: 7, FASP storage: 8, Azure Blob Storage: 9 | [optional] 
**provider_specific_settings** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


