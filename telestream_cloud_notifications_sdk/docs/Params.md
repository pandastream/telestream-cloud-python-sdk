# Params

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **list[str]** | (for email subscription type);  E-mail addresses  | [optional] 
**url** | **str** | (for webhook subscription type);  Webhook URL  | [optional] 
**method** | **str** | (for webhook subscription type);  HTTP method; default: POST (GET, POST)  | [optional] 
**retries** | **int** | (for webhook subscription type);  Number of retries before forgetting the notification; default: 0  | [optional] 
**content_type** | **str** | (for webhook subscription type); default: application/json (application/json, application/x-www-form-urlencoded)  | [optional] 
**topic_arn** | **str** | (for sns subscription type) identifier of an AWS SNS Topic that events will be posted to.  | [optional] 
**role_arn** | **str** | (for sns subscription type) identifier of an AWS IAM Role that will be used for authorization.  | [optional] 
**topic_endpoint** | **str** | (for aeg subscription type) address of an Azure Event Grid Topic that events will be posted to.  | [optional] 
**access_key** | **str** | (for aeg subscription type) secret access key that authorizes Telestream Cloud to write to an Azure Event Grid Topic.  | [optional] 
**project_id** | **str** | (for pubsub subscription type) id of a Google Cloud project that hosts the topic.  | [optional] 
**topic_name** | **str** | (for pubsub subscription type) name of a Google Cloud Pub/Sub topic to which notifications will be published.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


