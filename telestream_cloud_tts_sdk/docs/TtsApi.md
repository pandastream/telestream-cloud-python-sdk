# telestream_cloud_tts.TtsApi

All URIs are relative to *https://api.cloud.telestream.net/tts/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_corpus**](TtsApi.md#create_corpus) | **POST** /projects/{projectID}/corpora/{name} | Creates a new Corpus
[**create_job**](TtsApi.md#create_job) | **POST** /projects/{projectID}/jobs | Creates a new Job
[**create_project**](TtsApi.md#create_project) | **POST** /projects | Creates a new Project
[**delete_corpus**](TtsApi.md#delete_corpus) | **DELETE** /projects/{projectID}/corpora/{name} | Creates a new Corpus
[**delete_job**](TtsApi.md#delete_job) | **DELETE** /projects/{projectID}/jobs/{jobID} | Deletes the Job
[**delete_project**](TtsApi.md#delete_project) | **DELETE** /projects/{projectID} | Deletes the Project
[**get_job**](TtsApi.md#get_job) | **GET** /projects/{projectID}/jobs/{jobID} | Returns the Job
[**get_project**](TtsApi.md#get_project) | **GET** /projects/{projectID} | Returns the Project
[**getget_corpus**](TtsApi.md#getget_corpus) | **GET** /projects/{projectID}/corpora/{name} | Returns the Corpus
[**job_outputs**](TtsApi.md#job_outputs) | **GET** /projects/{projectID}/jobs/{jobID}/outputs | Returns the Job Outputs
[**job_result**](TtsApi.md#job_result) | **GET** /projects/{projectID}/jobs/{jobID}/result | Returns the Job Result
[**list_corpora**](TtsApi.md#list_corpora) | **GET** /projects/{projectID}/corpora | Returns a collection of Corpora
[**list_jobs**](TtsApi.md#list_jobs) | **GET** /projects/{projectID}/jobs | Returns a collection of Jobs
[**list_projects**](TtsApi.md#list_projects) | **GET** /projects | Returns a collection of Projects
[**train_project**](TtsApi.md#train_project) | **POST** /projects/{projectID}/train | Queues training
[**update_project**](TtsApi.md#update_project) | **PUT** /projects/{projectID} | Updates an existing Project


# **create_corpus**
> create_corpus(project_id, name, body)

Creates a new Corpus

Creates a new Corpus

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
name = 'name_example' # str | Corpus name
body = 'body_example' # str | 

    try:
        # Creates a new Corpus
        api_instance.create_corpus(project_id, name, body)
    except ApiException as e:
        print("Exception when calling TtsApi->create_corpus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **name** | **str**| Corpus name | 
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(project_id, job)

Creates a new Job

Creates a new Job

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
job = telestream_cloud_tts.Job() # Job | 

    try:
        # Creates a new Job
        api_response = api_instance.create_job(project_id, job)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **job** | [**Job**](Job.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid request body |  -  |
**422** | Invalid request params |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(project)

Creates a new Project

Creates a new Project

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project = telestream_cloud_tts.Project() # Project | 

    try:
        # Creates a new Project
        api_response = api_instance.create_project(project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Invalid request body |  -  |
**422** | Invalid request params |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_corpus**
> delete_corpus(project_id, name)

Creates a new Corpus

Creates a new Corpus

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
name = 'name_example' # str | Corpus name

    try:
        # Creates a new Corpus
        api_instance.delete_corpus(project_id, name)
    except ApiException as e:
        print("Exception when calling TtsApi->delete_corpus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **name** | **str**| Corpus name | 

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
**204** | Deleted |  -  |
**409** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> delete_job(project_id, job_id)

Deletes the Job

Deletes the Job

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
job_id = 'job_id_example' # str | 

    try:
        # Deletes the Job
        api_instance.delete_job(project_id, job_id)
    except ApiException as e:
        print("Exception when calling TtsApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **job_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Deletes the Project

Deletes the Project

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project

    try:
        # Deletes the Project
        api_instance.delete_project(project_id)
    except ApiException as e:
        print("Exception when calling TtsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(project_id, job_id)

Returns the Job

Returns the Job

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
job_id = 'job_id_example' # str | 

    try:
        # Returns the Job
        api_response = api_instance.get_job(project_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **job_id** | **str**|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Returns the Project

Returns the Project

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project

    try:
        # Returns the Project
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getget_corpus**
> Corpus getget_corpus(project_id, name)

Returns the Corpus

Returns the Corpus

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
name = 'name_example' # str | Corpus name

    try:
        # Returns the Corpus
        api_response = api_instance.getget_corpus(project_id, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->getget_corpus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **name** | **str**| Corpus name | 

### Return type

[**Corpus**](Corpus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_outputs**
> list[JobOutput] job_outputs(project_id, job_id)

Returns the Job Outputs

Returns the Job Outputs

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
job_id = 'job_id_example' # str | 

    try:
        # Returns the Job Outputs
        api_response = api_instance.job_outputs(project_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->job_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **job_id** | **str**|  | 

### Return type

[**list[JobOutput]**](JobOutput.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_result**
> JobResult job_result(project_id, job_id)

Returns the Job Result

Returns the Job Result

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
job_id = 'job_id_example' # str | 

    try:
        # Returns the Job Result
        api_response = api_instance.job_result(project_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->job_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **job_id** | **str**|  | 

### Return type

[**JobResult**](JobResult.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_corpora**
> CorporaCollection list_corpora(project_id)

Returns a collection of Corpora

Returns a collection of Corpora

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project

    try:
        # Returns a collection of Corpora
        api_response = api_instance.list_corpora(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->list_corpora: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 

### Return type

[**CorporaCollection**](CorporaCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobsCollection list_jobs(project_id, page=page, per_page=per_page)

Returns a collection of Jobs

Returns a collection of Jobs

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
page = 56 # int | page number (optional)
per_page = 56 # int | number of records per page (optional)

    try:
        # Returns a collection of Jobs
        api_response = api_instance.list_jobs(project_id, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| number of records per page | [optional] 

### Return type

[**JobsCollection**](JobsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ProjectsCollection list_projects()

Returns a collection of Projects

Returns a collection of Projects

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    
    try:
        # Returns a collection of Projects
        api_response = api_instance.list_projects()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectsCollection**](ProjectsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **train_project**
> train_project(project_id)

Queues training

Queues training

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project

    try:
        # Queues training
        api_instance.train_project(project_id)
    except ApiException as e:
        print("Exception when calling TtsApi->train_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 

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
**200** | OK |  -  |
**409** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id, project)

Updates an existing Project

Updates an existing Project

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import telestream_cloud_tts
from telestream_cloud_tts.rest import ApiException
from pprint import pprint
configuration = telestream_cloud_tts.Configuration()
# Configure API key authorization: apiKey
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Defining host is optional and default to https://api.cloud.telestream.net/tts/v1.0
configuration.host = "https://api.cloud.telestream.net/tts/v1.0"
# Enter a context with an instance of the API client
with telestream_cloud_tts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telestream_cloud_tts.TtsApi(api_client)
    project_id = 'project_id_example' # str | ID of the Project
project = telestream_cloud_tts.Project() # Project | 

    try:
        # Updates an existing Project
        api_response = api_instance.update_project(project_id, project)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TtsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the Project | 
 **project** | [**Project**](Project.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request body |  -  |
**422** | Invalid request params |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

