# telestream_cloud_notifications.NotificationsApi

All URIs are relative to *https://api.cloud.telestream.net/notifications/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](NotificationsApi.md#create_subscription) | **POST** /subscriptions | Create a new subscription
[**delete_subscription**](NotificationsApi.md#delete_subscription) | **DELETE** /subscriptions/{id} | 
[**list_subscriptions**](NotificationsApi.md#list_subscriptions) | **GET** /subscriptions | 


# **create_subscription**
> create_subscription(subscription=subscription)

Create a new subscription



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_notifications.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_notifications.NotificationsApi(telestream_cloud_notifications.ApiClient(configuration))
subscription = telestream_cloud_notifications.Subscription() # Subscription |  (optional)

try:
    # Create a new subscription
    api_instance.create_subscription(subscription=subscription)
except ApiException as e:
    print("Exception when calling NotificationsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_notifications.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_notifications.NotificationsApi(telestream_cloud_notifications.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.delete_subscription(id)
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> list[Subscription] list_subscriptions()



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_notifications.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_notifications.NotificationsApi(telestream_cloud_notifications.ApiClient(configuration))

try:
    api_response = api_instance.list_subscriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->list_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

