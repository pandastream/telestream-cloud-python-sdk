# telestream_cloud_notifications.NotificationsApi

All URIs are relative to *https://api.cloud.telestream.net/notifications/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](NotificationsApi.md#create_subscription) | **POST** /subscriptions | Create a new subscription
[**delete_subscription**](NotificationsApi.md#delete_subscription) | **DELETE** /subscriptions/{id} | 
[**get_subscription**](NotificationsApi.md#get_subscription) | **GET** /subscriptions/{id} | 
[**list_subscriptions**](NotificationsApi.md#list_subscriptions) | **GET** /subscriptions | 
[**modify_subscription**](NotificationsApi.md#modify_subscription) | **PUT** /subscriptions/{id} | Modify subscription


# **create_subscription**
> Subscription create_subscription(subscription=subscription)

Create a new subscription

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_notifications.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/notifications/v2.0
configuration.host = "https://api.cloud.telestream.net/notifications/v2.0"
# Enter a context with an instance of the API client
with telestream_cloud_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_notifications.NotificationsApi(api_client)
    subscription = telestream_cloud_notifications.Subscription() # Subscription |  (optional)

    try:
        # Create a new subscription
        api_response = api_instance.create_subscription(subscription=subscription)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription created |  -  |
**400** | Invalid input |  -  |
**401** | Not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(id)



### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_notifications.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/notifications/v2.0
configuration.host = "https://api.cloud.telestream.net/notifications/v2.0"
# Enter a context with an instance of the API client
with telestream_cloud_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_notifications.NotificationsApi(api_client)
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription deleted |  -  |
**401** | Not authorized |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(id)



### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_notifications.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/notifications/v2.0
configuration.host = "https://api.cloud.telestream.net/notifications/v2.0"
# Enter a context with an instance of the API client
with telestream_cloud_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_notifications.NotificationsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_subscription(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Not authorized |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> list[Subscription] list_subscriptions(service_type=service_type, type=type)



### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_notifications.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/notifications/v2.0
configuration.host = "https://api.cloud.telestream.net/notifications/v2.0"
# Enter a context with an instance of the API client
with telestream_cloud_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_notifications.NotificationsApi(api_client)
    service_type = 'service_type_example' # str | Service type (qc, tts, flip, vantage-cloud-port) (optional)
type = 'type_example' # str | Subscription type (email, webhook, sns, aeg, pubsub) (optional)

    try:
        api_response = api_instance.list_subscriptions(service_type=service_type, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_type** | **str**| Service type (qc, tts, flip, vantage-cloud-port) | [optional] 
 **type** | **str**| Subscription type (email, webhook, sns, aeg, pubsub) | [optional] 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** | Not authorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_subscription**
> Subscription modify_subscription(id, update_data=update_data)

Modify subscription

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_notifications
from telestream_cloud_notifications.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_notifications.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/notifications/v2.0
configuration.host = "https://api.cloud.telestream.net/notifications/v2.0"
# Enter a context with an instance of the API client
with telestream_cloud_notifications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_notifications.NotificationsApi(api_client)
    id = 'id_example' # str | 
update_data = telestream_cloud_notifications.UpdateData() # UpdateData |  (optional)

    try:
        # Modify subscription
        api_response = api_instance.modify_subscription(id, update_data=update_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotificationsApi->modify_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_data** | [**UpdateData**](UpdateData.md)|  | [optional] 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription updated |  -  |
**401** | Not authorized |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

