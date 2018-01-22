# telestream_cloud_flip.FlipApi

All URIs are relative to *https://api.cloud.telestream.net/api/flip/3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_encoding**](FlipApi.md#cancel_encoding) | **POST** /encodings/{id}/cancel.json | Cancels an Encoding.
[**copy_profile**](FlipApi.md#copy_profile) | **POST** /profiles/{id}/copy.json | Copies a given Profile
[**create_encoding**](FlipApi.md#create_encoding) | **POST** /encodings.json | Creates an Encoding
[**create_factory**](FlipApi.md#create_factory) | **POST** /factories.json | Creates a new factory
[**create_profile**](FlipApi.md#create_profile) | **POST** /profiles.json | Creates a Profile
[**create_video**](FlipApi.md#create_video) | **POST** /videos.json | Creates a Video from a provided source_url.
[**create_workorder**](FlipApi.md#create_workorder) | **POST** /workorders.json | Creates a Workorder.
[**delete_encoding**](FlipApi.md#delete_encoding) | **DELETE** /encodings/{id}.json | Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.
[**delete_profile**](FlipApi.md#delete_profile) | **DELETE** /profiles/{id}.json | Deletes a given Profile
[**delete_video**](FlipApi.md#delete_video) | **DELETE** /videos/{id}.json | Deletes a Video object.
[**delete_video_source**](FlipApi.md#delete_video_source) | **DELETE** /videos/{id}/source.json | Delete a video&#39;s source file.
[**encoding**](FlipApi.md#encoding) | **GET** /encodings/{id}.json | Returns an Encoding object.
[**encodings**](FlipApi.md#encodings) | **GET** /encodings.json | Returns a list of Encoding objects
[**encodings_count**](FlipApi.md#encodings_count) | **GET** /encodings/count.json | Returns a number of Encoding objects created using a given factory.
[**factories**](FlipApi.md#factories) | **GET** /factories.json | Returns a collection of Factory objects.
[**factory**](FlipApi.md#factory) | **GET** /factories/{id}.json | Returns a Factory object.
[**notifications**](FlipApi.md#notifications) | **GET** /notifications.json | Returns a Factory&#39;s notification settings.
[**profile**](FlipApi.md#profile) | **GET** /profiles/{id_or_name}.json | Returns a Profile object.
[**profile_encodings**](FlipApi.md#profile_encodings) | **GET** /profiles/{id_or_name}/encodings.json | Returns a list of Encodings that belong to a Profile.
[**profiles**](FlipApi.md#profiles) | **GET** /profiles.json | Returns a collection of Profile objects.
[**queued_videos**](FlipApi.md#queued_videos) | **GET** /videos/queued.json | Returns a collection of Video objects queued for encoding.
[**resubmit_video**](FlipApi.md#resubmit_video) | **POST** /videos/resubmit.json | Resubmits a video to encode.
[**retry_encoding**](FlipApi.md#retry_encoding) | **POST** /encodings/{id}/retry.json | Retries a failed encoding.
[**signed_encoding_url**](FlipApi.md#signed_encoding_url) | **GET** /encodings/{id}/signed-url.json | Returns a signed url pointing to an Encoding.
[**signed_encoding_urls**](FlipApi.md#signed_encoding_urls) | **GET** /encodings/{id}/signed-urls.json | Returns a list of signed urls pointing to an Encoding&#39;s outputs.
[**signed_video_url**](FlipApi.md#signed_video_url) | **GET** /videos/{id}/signed-url.json | Returns a signed url pointing to a Video.
[**toggle_factory_sync**](FlipApi.md#toggle_factory_sync) | **POST** /factories/{id}/sync.json | Toggles synchronisation settings.
[**update_encoding**](FlipApi.md#update_encoding) | **PUT** /encodings/{id}.json | Updates an Encoding
[**update_factory**](FlipApi.md#update_factory) | **PATCH** /factories/{id}.json | Updates a Factory&#39;s settings. Returns a Factory object.
[**update_notifications**](FlipApi.md#update_notifications) | **PUT** /notifications.json | Updates a Factory&#39;s notification settings.
[**update_profile**](FlipApi.md#update_profile) | **PUT** /profiles/{id}.json | Updates a given Profile
[**upload_video**](FlipApi.md#upload_video) | **POST** /videos/upload.json | Creates an upload session.
[**video**](FlipApi.md#video) | **GET** /videos/{id}.json | Returns a Video object.
[**video_encodings**](FlipApi.md#video_encodings) | **GET** /videos/{id}/encodings.json | Returns a list of Encodings that belong to a Video.
[**video_metadata**](FlipApi.md#video_metadata) | **GET** /videos/{id}/metadata.json | Returns a Video&#39;s metadata
[**videos**](FlipApi.md#videos) | **GET** /videos.json | Returns a collection of Video objects.
[**workflows**](FlipApi.md#workflows) | **GET** /workflows.json | Returns a collection of Workflows that belong to a Factory.


# **cancel_encoding**
> CanceledResponse cancel_encoding(id, factory_id)

Cancels an Encoding.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Cancels an Encoding.
    api_response = api_instance.cancel_encoding(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->cancel_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**CanceledResponse**](CanceledResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_profile**
> Profile copy_profile(id, factory_id, copy_profile_body, expand=expand)

Copies a given Profile

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.
copy_profile_body = telestream_cloud_flip.CopyProfileBody() # CopyProfileBody | 
expand = true # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)

try:
    # Copies a given Profile
    api_response = api_instance.copy_profile(id, factory_id, copy_profile_body, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->copy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 
 **copy_profile_body** | [**CopyProfileBody**](CopyProfileBody.md)|  | 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_encoding**
> Encoding create_encoding(factory_id, create_encoding_body, screenshots=screenshots, precise_status=precise_status)

Creates an Encoding

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
create_encoding_body = telestream_cloud_flip.CreateEncodingBody() # CreateEncodingBody | 
screenshots = true # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = true # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

try:
    # Creates an Encoding
    api_response = api_instance.create_encoding(factory_id, create_encoding_body, screenshots=screenshots, precise_status=precise_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->create_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **create_encoding_body** | [**CreateEncodingBody**](CreateEncodingBody.md)|  | 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_factory**
> Factory create_factory(create_factory_body, with_storage_provider=with_storage_provider)

Creates a new factory

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
create_factory_body = telestream_cloud_flip.FactoryBody() # FactoryBody | 
with_storage_provider = true # bool | if set to `true`, results will include a storage provider's id (optional)

try:
    # Creates a new factory
    api_response = api_instance.create_factory(create_factory_body, with_storage_provider=with_storage_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->create_factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_factory_body** | [**FactoryBody**](FactoryBody.md)|  | 
 **with_storage_provider** | **bool**| if set to &#x60;true&#x60;, results will include a storage provider&#39;s id | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile**
> Profile create_profile(factory_id, create_profile_body, exclude_advanced_services=exclude_advanced_services, expand=expand)

Creates a Profile

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
create_profile_body = telestream_cloud_flip.ProfileBody() # ProfileBody | 
exclude_advanced_services = true # bool |  (optional)
expand = true # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default it is not set. (optional)

try:
    # Creates a Profile
    api_response = api_instance.create_profile(factory_id, create_profile_body, exclude_advanced_services=exclude_advanced_services, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **create_profile_body** | [**ProfileBody**](ProfileBody.md)|  | 
 **exclude_advanced_services** | **bool**|  | [optional] 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default it is not set. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video**
> Video create_video(factory_id, create_video_body)

Creates a Video from a provided source_url.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_workorder**
> create_workorder(factory_id, profile_id=profile_id, file=file, source_url=source_url)

Creates a Workorder.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
profile_id = 'profile_id_example' # str | Id of a Profile. (optional)
file = '/path/to/file.txt' # file | Input file. (optional)
source_url = 'source_url_example' # str | URL pointing to an input file. (optional)

try:
    # Creates a Workorder.
    api_instance.create_workorder(factory_id, profile_id=profile_id, file=file, source_url=source_url)
except ApiException as e:
    print("Exception when calling FlipApi->create_workorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **profile_id** | **str**| Id of a Profile. | [optional] 
 **file** | **file**| Input file. | [optional] 
 **source_url** | **str**| URL pointing to an input file. | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_encoding**
> DeletedResponse delete_encoding(id, factory_id)

Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Deletes an Encoding from both Telestream Cloud and your storage. Returns an information whether the operation was successful.
    api_response = api_instance.delete_encoding(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->delete_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> DeletedResponse delete_profile(id, factory_id)

Deletes a given Profile

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Profile
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Deletes a given Profile
    api_response = api_instance.delete_profile(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->delete_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Profile | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video**
> DeletedResponse delete_video(id, factory_id)

Deletes a Video object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Deletes a Video object.
    api_response = api_instance.delete_video(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->delete_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_source**
> DeletedResponse delete_video_source(id, factory_id)

Delete a video's source file.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Delete a video's source file.
    api_response = api_instance.delete_video_source(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->delete_video_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**DeletedResponse**](DeletedResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encoding**
> Encoding encoding(id, factory_id, screenshots=screenshots, precise_status=precise_status)

Returns an Encoding object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.
screenshots = true # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = true # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

try:
    # Returns an Encoding object.
    api_response = api_instance.encoding(id, factory_id, screenshots=screenshots, precise_status=precise_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encodings**
> PaginatedEncodingsCollection encodings(factory_id, video_id=video_id, status=status, profile_id=profile_id, profile_name=profile_name, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)

Returns a list of Encoding objects

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
video_id = 'video_id_example' # str | Id of a Video. When specified, the resulting list will contain videos that belong to the Video. (optional)
status = 'status_example' # str | One of `success`, `fail`, `processing`. When specified, the resulting list will contain ecodings filtered by status. (optional)
profile_id = 'profile_id_example' # str | Filter by profile_id. (optional)
profile_name = 'profile_name_example' # str | Filter by profile_name. (optional)
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)
screenshots = true # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = true # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

try:
    # Returns a list of Encoding objects
    api_response = api_instance.encodings(factory_id, video_id=video_id, status=status, profile_id=profile_id, profile_name=profile_name, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->encodings: %s\n" % e)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **encodings_count**
> CountResponse encodings_count(factory_id)

Returns a number of Encoding objects created using a given factory.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factories**
> PaginatedFactoryCollection factories(page=page, per_page=per_page, with_storage_provider=with_storage_provider)

Returns a collection of Factory objects.

Returns a collection of Factory objects.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)
with_storage_provider = true # bool | if set to `true`, results will include a storage provider's id (optional)

try:
    # Returns a collection of Factory objects.
    api_response = api_instance.factories(page=page, per_page=per_page, with_storage_provider=with_storage_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->factories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 
 **with_storage_provider** | **bool**| if set to &#x60;true&#x60;, results will include a storage provider&#39;s id | [optional] 

### Return type

[**PaginatedFactoryCollection**](PaginatedFactoryCollection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factory**
> Factory factory(id, with_storage_provider=with_storage_provider)

Returns a Factory object.

Returns a Factory object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | id of a factory
with_storage_provider = true # bool | if set to `true`, results will include a storage provider's id (optional)

try:
    # Returns a Factory object.
    api_response = api_instance.factory(id, with_storage_provider=with_storage_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of a factory | 
 **with_storage_provider** | **bool**| if set to &#x60;true&#x60;, results will include a storage provider&#39;s id | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications**
> CloudNotificationSettings notifications(factory_id)

Returns a Factory's notification settings.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a Factory's notification settings.
    api_response = api_instance.notifications(factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**CloudNotificationSettings**](CloudNotificationSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> Profile profile(id_or_name, factory_id, expand=expand)

Returns a Profile object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id_or_name = 'id_or_name_example' # str | A name or an id of a Profile.
factory_id = 'factory_id_example' # str | Id of a Factory.
expand = true # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)

try:
    # Returns a Profile object.
    api_response = api_instance.profile(id_or_name, factory_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_name** | **str**| A name or an id of a Profile. | 
 **factory_id** | **str**| Id of a Factory. | 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_encodings**
> PaginatedEncodingsCollection profile_encodings(id_or_name, factory_id)

Returns a list of Encodings that belong to a Profile.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profiles**
> PaginatedProfilesCollection profiles(factory_id, exclude_advanced_services=exclude_advanced_services, expand=expand, page=page, per_page=per_page)

Returns a collection of Profile objects.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
exclude_advanced_services = true # bool | Determine whether exclude Advanced Services profiles from the results. By default this is not set. (optional)
expand = true # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

try:
    # Returns a collection of Profile objects.
    api_response = api_instance.profiles(factory_id, exclude_advanced_services=exclude_advanced_services, expand=expand, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->profiles: %s\n" % e)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queued_videos**
> PaginatedVideoCollection queued_videos(factory_id, page=page, per_page=per_page)

Returns a collection of Video objects queued for encoding.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_video**
> resubmit_video(factory_id, resubmit_video_body)

Resubmits a video to encode.

Resubmits the video to encode. Please note that this option will work only for videos in `success` status.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_encoding**
> RetriedResponse retry_encoding(id, factory_id)

Retries a failed encoding.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Retries a failed encoding.
    api_response = api_instance.retry_encoding(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->retry_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**RetriedResponse**](RetriedResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_encoding_url**
> EncodingSignedUrl signed_encoding_url(id, factory_id)

Returns a signed url pointing to an Encoding.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a signed url pointing to an Encoding.
    api_response = api_instance.signed_encoding_url(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->signed_encoding_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**EncodingSignedUrl**](EncodingSignedUrl.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_encoding_urls**
> EncodingSignedUrls signed_encoding_urls(id, factory_id)

Returns a list of signed urls pointing to an Encoding's outputs.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a list of signed urls pointing to an Encoding's outputs.
    api_response = api_instance.signed_encoding_urls(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->signed_encoding_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**EncodingSignedUrls**](EncodingSignedUrls.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_video_url**
> SignedVideoUrl signed_video_url(id, factory_id)

Returns a signed url pointing to a Video.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a signed url pointing to a Video.
    api_response = api_instance.signed_video_url(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->signed_video_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**SignedVideoUrl**](SignedVideoUrl.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_factory_sync**
> FactorySync toggle_factory_sync(id, factory_sync_body)

Toggles synchronisation settings.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | id of the factory
factory_sync_body = telestream_cloud_flip.FactorySyncBody() # FactorySyncBody | 

try:
    # Toggles synchronisation settings.
    api_response = api_instance.toggle_factory_sync(id, factory_sync_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->toggle_factory_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the factory | 
 **factory_sync_body** | [**FactorySyncBody**](FactorySyncBody.md)|  | 

### Return type

[**FactorySync**](FactorySync.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_encoding**
> Encoding update_encoding(id, factory_id, update_encoding_body, screenshots=screenshots, precise_status=precise_status)

Updates an Encoding

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of an Encoding.
factory_id = 'factory_id_example' # str | Id of a Factory.
update_encoding_body = telestream_cloud_flip.UpdateEncodingBody() # UpdateEncodingBody | 
screenshots = true # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = true # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

try:
    # Updates an Encoding
    api_response = api_instance.update_encoding(id, factory_id, update_encoding_body, screenshots=screenshots, precise_status=precise_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->update_encoding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of an Encoding. | 
 **factory_id** | **str**| Id of a Factory. | 
 **update_encoding_body** | [**UpdateEncodingBody**](UpdateEncodingBody.md)|  | 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**Encoding**](Encoding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_factory**
> Factory update_factory(id, update_factory_body, with_storage_provider=with_storage_provider)

Updates a Factory's settings. Returns a Factory object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | id of the factory
update_factory_body = telestream_cloud_flip.FactoryBody() # FactoryBody | 
with_storage_provider = true # bool | if set to `true`, results will include a storage provider's id (optional)

try:
    # Updates a Factory's settings. Returns a Factory object.
    api_response = api_instance.update_factory(id, update_factory_body, with_storage_provider=with_storage_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->update_factory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of the factory | 
 **update_factory_body** | [**FactoryBody**](FactoryBody.md)|  | 
 **with_storage_provider** | **bool**| if set to &#x60;true&#x60;, results will include a storage provider&#39;s id | [optional] 

### Return type

[**Factory**](Factory.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notifications**
> CloudNotificationSettings update_notifications(factory_id, cloud_notification_settings_body)

Updates a Factory's notification settings.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
cloud_notification_settings_body = telestream_cloud_flip.CloudNotificationSettings() # CloudNotificationSettings | 

try:
    # Updates a Factory's notification settings.
    api_response = api_instance.update_notifications(factory_id, cloud_notification_settings_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->update_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **cloud_notification_settings_body** | [**CloudNotificationSettings**](CloudNotificationSettings.md)|  | 

### Return type

[**CloudNotificationSettings**](CloudNotificationSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> Profile update_profile(id, factory_id, update_profile_body, exclude_advanced_services=exclude_advanced_services, expand=expand)

Updates a given Profile

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | 
factory_id = 'factory_id_example' # str | Id of a Factory.
update_profile_body = telestream_cloud_flip.ProfileBody() # ProfileBody | 
exclude_advanced_services = true # bool |  (optional)
expand = true # bool | If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. (optional)

try:
    # Updates a given Profile
    api_response = api_instance.update_profile(id, factory_id, update_profile_body, exclude_advanced_services=exclude_advanced_services, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **factory_id** | **str**| Id of a Factory. | 
 **update_profile_body** | [**ProfileBody**](ProfileBody.md)|  | 
 **exclude_advanced_services** | **bool**|  | [optional] 
 **expand** | **bool**| If expand option is set Profile objects will contain all command parameters, even if their value is default. By default this is not set. | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_video**
> UploadSession upload_video(factory_id, video_upload_body)

Creates an upload session.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
video_upload_body = telestream_cloud_flip.VideoUploadBody() # VideoUploadBody | 

try:
    # Creates an upload session.
    api_response = api_instance.upload_video(factory_id, video_upload_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->upload_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **factory_id** | **str**| Id of a Factory. | 
 **video_upload_body** | [**VideoUploadBody**](VideoUploadBody.md)|  | 

### Return type

[**UploadSession**](UploadSession.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video**
> Video video(id, factory_id)

Returns a Video object.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a Video object.
    api_response = api_instance.video(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**Video**](Video.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_encodings**
> PaginatedEncodingsCollection video_encodings(id, factory_id, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)

Returns a list of Encodings that belong to a Video.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)
screenshots = true # bool | Determines whether the response will include screenshots. By default this is not set. (optional)
precise_status = true # bool | Determines whether the response will include a precise status. By default this is not set. (optional)

try:
    # Returns a list of Encodings that belong to a Video.
    api_response = api_instance.video_encodings(id, factory_id, page=page, per_page=per_page, screenshots=screenshots, precise_status=precise_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->video_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 
 **page** | **int**| A page to be fetched. Default is &#x60;1&#x60;. | [optional] 
 **per_page** | **int**| A number of results per page. Default is &#x60;100&#x60;. | [optional] 
 **screenshots** | **bool**| Determines whether the response will include screenshots. By default this is not set. | [optional] 
 **precise_status** | **bool**| Determines whether the response will include a precise status. By default this is not set. | [optional] 

### Return type

[**PaginatedEncodingsCollection**](PaginatedEncodingsCollection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_metadata**
> VideoMetadata video_metadata(id, factory_id)

Returns a Video's metadata

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
id = 'id_example' # str | Id of a Video.
factory_id = 'factory_id_example' # str | Id of a Factory.

try:
    # Returns a Video's metadata
    api_response = api_instance.video_metadata(id, factory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->video_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of a Video. | 
 **factory_id** | **str**| Id of a Factory. | 

### Return type

[**VideoMetadata**](VideoMetadata.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **videos**
> PaginatedVideoCollection videos(factory_id, page=page, per_page=per_page)

Returns a collection of Video objects.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

try:
    # Returns a collection of Video objects.
    api_response = api_instance.videos(factory_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->videos: %s\n" % e)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows**
> PaginatedWorkflowsCollection workflows(factory_id, page=page, per_page=per_page)

Returns a collection of Workflows that belong to a Factory.

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_flip
from telestream_cloud_flip.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_flip.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_flip.FlipApi(telestream_cloud_flip.ApiClient(configuration))
factory_id = 'factory_id_example' # str | Id of a Factory.
page = 56 # int | A page to be fetched. Default is `1`. (optional)
per_page = 56 # int | A number of results per page. Default is `100`. (optional)

try:
    # Returns a collection of Workflows that belong to a Factory.
    api_response = api_instance.workflows(factory_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FlipApi->workflows: %s\n" % e)
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

