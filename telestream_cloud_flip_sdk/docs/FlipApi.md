# telestream_cloud_flip.FlipApi

All URIs are relative to *https://api.cloud.telestream.net/flip/3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_encoding**](FlipApi.md#cancel_encoding) | **POST** /encodings/{encoding_id}/cancel.json | Cancels an Encoding.
[**cancel_video**](FlipApi.md#cancel_video) | **POST** /videos/{video_id}/cancel.json | Cancel video and all encodings
[**copy_profile**](FlipApi.md#copy_profile) | **POST** /profiles/{profile_id}/copy.json | Copies a given Profile
[**create_encoding**](FlipApi.md#create_encoding) | **POST** /encodings.json | Creates an Encoding
[**create_factory**](FlipApi.md#create_factory) | **POST** /factories.json | Creates a new factory
[**create_profile**](FlipApi.md#create_profile) | **POST** /profiles.json | Creates a Profile
[**create_video**](FlipApi.md#create_video) | **POST** /videos.json | Creates a Video from a provided source_url.
[**delete_encoding**](FlipApi.md#delete_encoding) | **DELETE** /encodings/{encoding_id}.json | Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.
[**delete_profile**](FlipApi.md#delete_profile) | **DELETE** /profiles/{profile_id}.json | Deletes a given Profile
[**delete_video**](FlipApi.md#delete_video) | **DELETE** /videos/{video_id}.json | Deletes a Video object.
[**delete_video_source**](FlipApi.md#delete_video_source) | **DELETE** /videos/{video_id}/source.json | Delete a video&#39;s source file.
[**encodings_count**](FlipApi.md#encodings_count) | **GET** /encodings/count.json | Returns a number of Encoding objects created using a given factory.
[**get_encoding**](FlipApi.md#get_encoding) | **GET** /encodings/{encoding_id}.json | Returns an Encoding object.
[**get_factory**](FlipApi.md#get_factory) | **GET** /factories/{id}.json | Returns a Factory object.
[**get_profile**](FlipApi.md#get_profile) | **GET** /profiles/{profile_id}.json | Returns a Profile object.
[**get_video**](FlipApi.md#get_video) | **GET** /videos/{video_id}.json | Returns a Video object.
[**list_encodings**](FlipApi.md#list_encodings) | **GET** /encodings.json | Returns a list of Encoding objects
[**list_factories**](FlipApi.md#list_factories) | **GET** /factories.json | Returns a collection of Factory objects.
[**list_profiles**](FlipApi.md#list_profiles) | **GET** /profiles.json | Returns a collection of Profile objects.
[**list_video_encodings**](FlipApi.md#list_video_encodings) | **GET** /videos/{video_id}/encodings.json | Returns a list of Encodings that belong to a Video.
[**list_videos**](FlipApi.md#list_videos) | **GET** /videos.json | Returns a collection of Video objects.
[**list_workflows**](FlipApi.md#list_workflows) | **GET** /workflows.json | Returns a collection of Workflows that belong to a Factory.
[**profile_encodings**](FlipApi.md#profile_encodings) | **GET** /profiles/{id_or_name}/encodings.json | Returns a list of Encodings that belong to a Profile.
[**queued_videos**](FlipApi.md#queued_videos) | **GET** /videos/queued.json | Returns a collection of Video objects queued for encoding.
[**resubmit_video**](FlipApi.md#resubmit_video) | **POST** /videos/resubmit.json | Resubmits a video to encode.
[**retry_encoding**](FlipApi.md#retry_encoding) | **POST** /encodings/{encoding_id}/retry.json | Retries a failed encoding.
[**signed_encoding_url**](FlipApi.md#signed_encoding_url) | **GET** /encodings/{encoding_id}/signed-url.json | Returns a signed url pointing to an Encoding.
[**signed_encoding_urls**](FlipApi.md#signed_encoding_urls) | **GET** /encodings/{encoding_id}/signed-urls.json | Returns a list of signed urls pointing to an Encoding&#39;s outputs.
[**signed_video_url**](FlipApi.md#signed_video_url) | **GET** /videos/{video_id}/signed-url.json | Returns a signed url pointing to a Video.
[**update_encoding**](FlipApi.md#update_encoding) | **PUT** /encodings/{encoding_id}.json | Updates an Encoding
[**update_factory**](FlipApi.md#update_factory) | **PATCH** /factories/{id}.json | Updates a Factory&#39;s settings. Returns a Factory object.
[**update_profile**](FlipApi.md#update_profile) | **PUT** /profiles/{profile_id}.json | Updates a given Profile
[**video_metadata**](FlipApi.md#video_metadata) | **GET** /videos/{video_id}/metadata.json | Returns a Video&#39;s metadata


# **cancel_encoding**
> CanceledResponse cancel_encoding(encoding_id, factory_id)

Cancels an Encoding.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Cancels an Encoding.
        api_response = api_instance.cancel_encoding(encoding_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->cancel_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**CanceledResponse**](CanceledResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encoding has been successfully canceled. |  -  |
**400** | Tried to cancel an Encoding older than 30 days. |  -  |
**403** | Not authorized to cancel the Encoding. |  -  |
**404** | Encoding or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_video**
> CanceledResponse cancel_video(video_id, factory_id)

Cancel video and all encodings

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Cancel video and all encodings
        api_response = api_instance.cancel_video(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->cancel_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**CanceledResponse**](CanceledResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully cancel video |  -  |
**404** | Video or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_profile**
> Profile copy_profile(profile_id, factory_id, copy_profile_body)

Copies a given Profile

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    profile_id = 'profile_id_example' # str | Id of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.
copy_profile_body = telestream_cloud_flip.CopyProfileBody() # CopyProfileBody | 

    try:
        # Copies a given Profile
        api_response = api_instance.copy_profile(profile_id, factory_id, copy_profile_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->copy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 
 **copy_profile_body** | [**CopyProfileBody**](CopyProfileBody.md)|  | 

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully copied the Profile |  -  |
**403** | Unauthorized to copy the Profile |  -  |
**404** | Profile, the old Factory, or the new Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_encoding**
> Encoding create_encoding(factory_id, create_encoding_body)

Creates an Encoding

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
create_encoding_body = telestream_cloud_flip.CreateEncodingBody() # CreateEncodingBody | 

    try:
        # Creates an Encoding
        api_response = api_instance.create_encoding(factory_id, create_encoding_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->create_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **create_encoding_body** | [**CreateEncodingBody**](CreateEncodingBody.md)|  | 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created an Encoding. |  -  |
**400** | Failed to create an Encoding using the provided data or tried to add an Encoding for a failed Video or a Video older than 30 days |  -  |
**403** | Not authorized to create an Encoding |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_factory**
> Factory create_factory(factory=factory)

Creates a new factory

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory = telestream_cloud_flip.Factory() # Factory |  (optional)

    try:
        # Creates a new factory
        api_response = api_instance.create_factory(factory=factory)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->create_factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory** | [**Factory**](Factory.md)|  | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a Factory |  -  |
**400** | Failed to create a Factory |  -  |
**403** | Not authorized to create a Factory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile**
> Profile create_profile(factory_id, profile=profile)

Creates a Profile

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
profile = telestream_cloud_flip.Profile() # Profile |  (optional)

    try:
        # Creates a Profile
        api_response = api_instance.create_profile(factory_id, profile=profile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **profile** | [**Profile**](Profile.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a Profile |  -  |
**400** | Posted incorrect parameters |  -  |
**403** | Not authorized to create a Profile |  -  |
**404** | Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video**
> Video create_video(factory_id, create_video_body)

Creates a Video from a provided source_url.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
create_video_body = telestream_cloud_flip.CreateVideoBody() # CreateVideoBody | 

    try:
        # Creates a Video from a provided source_url.
        api_response = api_instance.create_video(factory_id, create_video_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->create_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **create_video_body** | [**CreateVideoBody**](CreateVideoBody.md)|  | 

### Return type

[**Video**](Video.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Video successfully created. |  -  |
**403** | User not allowed to create videos. |  -  |
**500** | Failed to create a video. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_encoding**
> DeletedResponse delete_encoding(encoding_id, factory_id)

Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.
        api_response = api_instance.delete_encoding(encoding_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->delete_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encoding has been successfully deleted. |  -  |
**400** | Tried to delete an Encoding older than 30 days. |  -  |
**403** | Not authorized to delete the Encoding. |  -  |
**404** | Encoding or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> DeletedResponse delete_profile(profile_id, factory_id)

Deletes a given Profile

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    profile_id = 'profile_id_example' # str | Id of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Deletes a given Profile
        api_response = api_instance.delete_profile(profile_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->delete_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the Profile object has been successfully deleted |  -  |
**403** | Unauthorized to delete the Profile |  -  |
**404** | Profile or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video**
> DeletedResponse delete_video(video_id, factory_id)

Deletes a Video object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Deletes a Video object.
        api_response = api_instance.delete_video(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->delete_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Video object has been successfully deleted. |  -  |
**403** | Unauthorized to delete the Video. |  -  |
**404** | Video or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_source**
> DeletedResponse delete_video_source(video_id, factory_id)

Delete a video's source file.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Delete a video's source file.
        api_response = api_instance.delete_video_source(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->delete_video_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully deleted the Video&#39;s source file. |  -  |
**403** | Not authorized to delete the Video&#39;s source file. |  -  |
**404** | Video or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encodings_count**
> CountResponse encodings_count(factory_id)

Returns a number of Encoding objects created using a given factory.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a number of Encoding objects created using a given factory.
        api_response = api_instance.encodings_count(factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->encodings_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**CountResponse**](CountResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a number of encodings. |  -  |
**404** | Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encoding**
> Encoding get_encoding(encoding_id, factory_id, screenshots=screenshots, precise_status=precise_status)

Returns an Encoding object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.
screenshots = True # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = True # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

    try:
        # Returns an Encoding object.
        api_response = api_instance.get_encoding(encoding_id, factory_id, screenshots=screenshots, precise_status=precise_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->get_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the Encoding |  -  |
**404** | Encoding or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_factory**
> Factory get_factory(id)

Returns a Factory object.

Returns a Factory object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    id = 'id_example' # str | id of a factory

    try:
        # Returns a Factory object.
        api_response = api_instance.get_factory(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->get_factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of a factory | 

### Return type

[**Factory**](Factory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the Factory |  -  |
**403** | Unauthorized to access the Factory |  -  |
**404** | Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> Profile get_profile(profile_id, factory_id, expand=expand)

Returns a Profile object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    profile_id = 'profile_id_example' # str | Id of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.
expand = True # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)

    try:
        # Returns a Profile object.
        api_response = api_instance.get_profile(profile_id, factory_id, expand=expand)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the Profile. |  -  |
**404** | Profile or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video**
> Video get_video(video_id, factory_id)

Returns a Video object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a Video object.
        api_response = api_instance.get_video(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->get_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**Video**](Video.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the Video |  -  |
**403** | Unauthorized to access the Video |  -  |
**404** | Video or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_encodings**
> PaginatedEncodingsCollection list_encodings(factory_id, video_id=video_id, status=status, profile_id=profile_id, profile_name=profile_name, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)

Returns a list of Encoding objects

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
video_id = 'video_id_example' # str | Id of a Video. When specified, the resulting list will contain videos that belong to the Video. (optional)
status = 'status_example' # str | One of `success`, `fail`, `processing`. When specified, the resulting list will contain ecodings filtered by status. (optional)
profile_id = 'profile_id_example' # str | Filter by profile_id. (optional)
profile_name = 'profile_name_example' # str | Filter by profile_name. (optional)
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)
screenshots = True # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = True # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

    try:
        # Returns a list of Encoding objects
        api_response = api_instance.list_encodings(factory_id, video_id=video_id, status=status, profile_id=profile_id, profile_name=profile_name, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **video_id** | **str**| Id of a Video. When specified, the resulting list will contain videos that belong to the Video. | [optional] 
 **status** | **str**| One of &#x60;success&#x60;, &#x60;fail&#x60;, &#x60;processing&#x60;. When specified, the resulting list will contain ecodings filtered by status. | [optional] 
 **profile_id** | **str**| Filter by profile_id. | [optional] 
 **profile_name** | **str**| Filter by profile_name. | [optional] 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**PaginatedEncodingsCollection**](PaginatedEncodingsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a list of Video&#39;s encodings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_factories**
> PaginatedFactoryCollection list_factories(page=page, per_page=per_page)

Returns a collection of Factory objects.

Returns a collection of Factory objects.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

    try:
        # Returns a collection of Factory objects.
        api_response = api_instance.list_factories(page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_factories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 

### Return type

[**PaginatedFactoryCollection**](PaginatedFactoryCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a list of Factories. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_profiles**
> PaginatedProfilesCollection list_profiles(factory_id, exclude_advanced_services=exclude_advanced_services, expand=expand, page=page, per_page=per_page)

Returns a collection of Profile objects.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
exclude_advanced_services = True # bool | Determine whether exclude Advanced Services profiles from the results. By default this is not set. (optional)
expand = True # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

    try:
        # Returns a collection of Profile objects.
        api_response = api_instance.list_profiles(factory_id, exclude_advanced_services=exclude_advanced_services, expand=expand, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **exclude_advanced_services** | **bool**| Determine whether exclude Advanced Services profiles from the results. By default this is not set. | [optional] 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. | [optional] 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 

### Return type

[**PaginatedProfilesCollection**](PaginatedProfilesCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a collection of Profiles |  -  |
**404** | Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_video_encodings**
> PaginatedEncodingsCollection list_video_encodings(video_id, factory_id, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)

Returns a list of Encodings that belong to a Video.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)
screenshots = True # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = True # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

    try:
        # Returns a list of Encodings that belong to a Video.
        api_response = api_instance.list_video_encodings(video_id, factory_id, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_video_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**PaginatedEncodingsCollection**](PaginatedEncodingsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a collection of Encodings. |  -  |
**404** | Video or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_videos**
> PaginatedVideoCollection list_videos(factory_id, page=page, per_page=per_page)

Returns a collection of Video objects.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

    try:
        # Returns a collection of Video objects.
        api_response = api_instance.list_videos(factory_id, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 

### Return type

[**PaginatedVideoCollection**](PaginatedVideoCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Videos successfully fetched. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflows**
> PaginatedWorkflowsCollection list_workflows(factory_id, page=page, per_page=per_page)

Returns a collection of Workflows that belong to a Factory.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

    try:
        # Returns a collection of Workflows that belong to a Factory.
        api_response = api_instance.list_workflows(factory_id, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->list_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 

### Return type

[**PaginatedWorkflowsCollection**](PaginatedWorkflowsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a collection of Workflows that belong to the Factory |  -  |
**404** | Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_encodings**
> PaginatedEncodingsCollection profile_encodings(id_or_name, factory_id)

Returns a list of Encodings that belong to a Profile.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    id_or_name = 'id_or_name_example' # str | Id or name of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a list of Encodings that belong to a Profile.
        api_response = api_instance.profile_encodings(id_or_name, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->profile_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| Id or name of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**PaginatedEncodingsCollection**](PaginatedEncodingsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a collection of Encodings. |  -  |
**404** | Profile or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queued_videos**
> PaginatedVideoCollection queued_videos(factory_id, page=page, per_page=per_page)

Returns a collection of Video objects queued for encoding.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

    try:
        # Returns a collection of Video objects queued for encoding.
        api_response = api_instance.queued_videos(factory_id, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->queued_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 

### Return type

[**PaginatedVideoCollection**](PaginatedVideoCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a collection of Video objects queued for encoding. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_video**
> resubmit_video(factory_id, resubmit_video_body)

Resubmits a video to encode.

Resubmits the video to encode. Please note that this option will work only for videos in `success` status.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    factory_id = 'factory_id_example' # str | Id of a Factory.
resubmit_video_body = telestream_cloud_flip.ResubmitVideoBody() # ResubmitVideoBody | 

    try:
        # Resubmits a video to encode.
        api_instance.resubmit_video(factory_id, resubmit_video_body)
    except ApiException as e:
        print("Exception when calling FlipApi->resubmit_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **resubmit_video_body** | [**ResubmitVideoBody**](ResubmitVideoBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Video successfully resubmitted. |  -  |
**400** | Invalid input. |  -  |
**404** | Video or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_encoding**
> RetriedResponse retry_encoding(encoding_id, factory_id)

Retries a failed encoding.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Retries a failed encoding.
        api_response = api_instance.retry_encoding(encoding_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->retry_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**RetriedResponse**](RetriedResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully requested reprocessing of the Encoding. |  -  |
**403** | Not authorized to retry the Encoding. |  -  |
**404** | Encoding or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_encoding_url**
> EncodingSignedUrl signed_encoding_url(encoding_id, factory_id, expires=expires)

Returns a signed url pointing to an Encoding.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.
expires = 56 # int | Duration in seconds for validity period. (optional)

    try:
        # Returns a signed url pointing to an Encoding.
        api_response = api_instance.signed_encoding_url(encoding_id, factory_id, expires=expires)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->signed_encoding_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 
 **expires** | **int**| Duration in seconds for validity period. | [optional] 

### Return type

[**EncodingSignedUrl**](EncodingSignedUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a signed url. |  -  |
**404** | Encoding or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_encoding_urls**
> EncodingSignedUrls signed_encoding_urls(encoding_id, factory_id)

Returns a list of signed urls pointing to an Encoding's outputs.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a list of signed urls pointing to an Encoding's outputs.
        api_response = api_instance.signed_encoding_urls(encoding_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->signed_encoding_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**EncodingSignedUrls**](EncodingSignedUrls.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a list of signed urls. |  -  |
**404** | Encoding or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_video_url**
> SignedVideoUrl signed_video_url(video_id, factory_id)

Returns a signed url pointing to a Video.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a signed url pointing to a Video.
        api_response = api_instance.signed_video_url(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->signed_video_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**SignedVideoUrl**](SignedVideoUrl.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a signed video url. |  -  |
**404** | Video of Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_encoding**
> Encoding update_encoding(encoding_id, factory_id, update_encoding_body)

Updates an Encoding

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    encoding_id = 'encoding_id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.
update_encoding_body = telestream_cloud_flip.UpdateEncodingBody() # UpdateEncodingBody | 

    try:
        # Updates an Encoding
        api_response = api_instance.update_encoding(encoding_id, factory_id, update_encoding_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->update_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encoding_id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 
 **update_encoding_body** | [**UpdateEncodingBody**](UpdateEncodingBody.md)|  | 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encoding successfully updated. |  -  |
**400** | Tried to update an Encoding older than 30 days. |  -  |
**403** | Not authorized to update the Encoding. |  -  |
**404** | Encoding or Factory not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_factory**
> Factory update_factory(id, factory=factory)

Updates a Factory's settings. Returns a Factory object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    id = 'id_example' # str | id of the factory
factory = telestream_cloud_flip.Factory() # Factory |  (optional)

    try:
        # Updates a Factory's settings. Returns a Factory object.
        api_response = api_instance.update_factory(id, factory=factory)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->update_factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the factory | 
 **factory** | [**Factory**](Factory.md)|  | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | failed to update the Factory |  -  |
**403** | Unauthorized to update the Factory |  -  |
**404** | Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> Profile update_profile(id, factory_id, profile=profile)

Updates a given Profile

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    id = 'id_example' # str | 
factory_id = 'factory_id_example' # str | Id of a Factory.
profile = telestream_cloud_flip.Profile() # Profile |  (optional)

    try:
        # Updates a given Profile
        api_response = api_instance.update_profile(id, factory_id, profile=profile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **factory_id** | **str**| Id of a Factory. | 
 **profile** | [**Profile**](Profile.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the Profile |  -  |
**400** | Posted incorrect parameters |  -  |
**403** | Not authorized to update the Profile |  -  |
**404** | Profile or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_metadata**
> dict(str, object) video_metadata(video_id, factory_id)

Returns a Video's metadata

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_flip.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/flip/3.1
configuration.host = "https://api.cloud.telestream.net/flip/3.1"
# Enter a context with an instance of the API client
with telestream_cloud_flip.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_flip.FlipApi(api_client)
    video_id = 'video_id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

    try:
        # Returns a Video's metadata
        api_response = api_instance.video_metadata(video_id, factory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FlipApi->video_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

**dict(str, object)**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the Video&#39;s metadata |  -  |
**404** | Video or Factory not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

