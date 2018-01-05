# telestream_cloud_qc.QcApi

All URIs are relative to *https://api.cloud.telestream.net/qc/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](QcApi.md#cancel_job) | **PUT** /projects/{project}/jobs/{job}/cancel.json | 
[**create_job**](QcApi.md#create_job) | **POST** /projects/{project}/jobs.json | Create a new job
[**create_project**](QcApi.md#create_project) | **POST** /projects.json | Create a new project
[**get_job**](QcApi.md#get_job) | **GET** /projects/{project}/jobs/{job}.json | Get QC job
[**get_project**](QcApi.md#get_project) | **GET** /projects/{project}.json | Get project by Id
[**list_jobs**](QcApi.md#list_jobs) | **GET** /projects/{project}/jobs.json | Get jobs form projects
[**list_projects**](QcApi.md#list_projects) | **GET** /projects.json | List all projects for an account
[**modify_project**](QcApi.md#modify_project) | **PUT** /projects/{project}.json | Modify project
[**proxy**](QcApi.md#proxy) | **GET** /projects/{project}/jobs/{job}/proxy.json | 
[**remove_job**](QcApi.md#remove_job) | **DELETE** /projects/{project}/jobs/{job}.json | 
[**remove_project**](QcApi.md#remove_project) | **DELETE** /projects/{project}.json | 
[**signed_urls**](QcApi.md#signed_urls) | **GET** /projects/{project}/jobs/{job}/signed-urls.json | 
[**upload_video**](QcApi.md#upload_video) | **POST** /projects/{project}/upload.json | Creates an upload session


# **cancel_job**
> cancel_job(project, job)



### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
job = 'job_example' # str | A unique identifier of a Job.

try: 
    api_instance.cancel_job(project, job)
except ApiException as e:
    print("Exception when calling QcApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **job** | **str**| A unique identifier of a Job. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(project, data)

Create a new job

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
data = telestream_cloud_qc.JobData() # JobData | 

try: 
    # Create a new job
    api_response = api_instance.create_job(project, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **data** | [**JobData**](JobData.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(data=data)

Create a new project

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
data = telestream_cloud_qc.Data() # Data |  (optional)

try: 
    # Create a new project
    api_response = api_instance.create_project(data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(project, job)

Get QC job

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
job = 'job_example' # str | A unique identifier of a Job.

try: 
    # Get QC job
    api_response = api_instance.get_job(project, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **job** | **str**| A unique identifier of a Job. | 

### Return type

[**Job**](Job.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project)

Get project by Id

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.

try: 
    # Get project by Id
    api_response = api_instance.get_project(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobsCollection list_jobs(project, expand=expand, status=status, per_page=per_page, page=page)

Get jobs form projects

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
expand = true # bool | Expand details of job (optional)
status = 'status_example' # str | Filter jobs by status (optional)
per_page = 30 # int | Limit number of listed jobs (optional) (default to 30)
page = 56 # int | Index of jobs page to be listed (optional)

try: 
    # Get jobs form projects
    api_response = api_instance.list_jobs(project, expand=expand, status=status, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **expand** | **bool**| Expand details of job | [optional] 
 **status** | **str**| Filter jobs by status | [optional] 
 **per_page** | **int**| Limit number of listed jobs | [optional] [default to 30]
 **page** | **int**| Index of jobs page to be listed | [optional] 

### Return type

[**JobsCollection**](JobsCollection.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects()

List all projects for an account

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()

try: 
    # List all projects for an account
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_project**
> Project modify_project(project, data=data)

Modify project

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | 
data = telestream_cloud_qc.Data1() # Data1 |  (optional)

try: 
    # Modify project
    api_response = api_instance.modify_project(project, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->modify_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy**
> Proxy proxy(project, job)



### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
job = 'job_example' # str | A unique identifier of a Job.

try: 
    api_response = api_instance.proxy(project, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **job** | **str**| A unique identifier of a Job. | 

### Return type

[**Proxy**](Proxy.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_job**
> remove_job(project, job)



### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
job = 'job_example' # str | A unique identifier of a Job.

try: 
    api_instance.remove_job(project, job)
except ApiException as e:
    print("Exception when calling QcApi->remove_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **job** | **str**| A unique identifier of a Job. | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project**
> remove_project(project)



### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | 

try: 
    api_instance.remove_project(project)
except ApiException as e:
    print("Exception when calling QcApi->remove_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_urls**
> dict(str, str) signed_urls(project, job)



### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
job = 'job_example' # str | A unique identifier of a Job.

try: 
    api_response = api_instance.signed_urls(project, job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->signed_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **job** | **str**| A unique identifier of a Job. | 

### Return type

[**dict(str, str)**](dict.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_video**
> UploadSession upload_video(project, video_upload_body)

Creates an upload session

### Example 
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
telestream_cloud_qc.configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# telestream_cloud_qc.configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi()
project = 'project_example' # str | A unique identifier of a Project.
video_upload_body = telestream_cloud_qc.VideoUploadBody() # VideoUploadBody | 

try: 
    # Creates an upload session
    api_response = api_instance.upload_video(project, video_upload_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->upload_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| A unique identifier of a Project. | 
 **video_upload_body** | [**VideoUploadBody**](VideoUploadBody.md)|  | 

### Return type

[**UploadSession**](UploadSession.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

