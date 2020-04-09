# Topic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | [read-only] Account identifier connected to subscription notification  | [optional] [readonly] 
**service** | **str** | Name of service (qc, flip, tts)  | 
**event** | **str** | Name of the event;  Quality Control (media-passed, media-error, media-warning, media-rejected, media-canceled, job-created, job-progress), Flip (video-created, video-encoded, encoding-complete, encoding-progress), Transcription (job-created, job-completed, job-error, job-progress)  | 
**project** | **str** | (for tts, qc service); Project ID  | [optional] 
**factory** | **str** | (for flip service); Factory ID  | [optional] 
**workflow** | **str** | (for Vantage Cloud Port service); Workflow ID  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


