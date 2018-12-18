# telestream_cloud_qc.QcApi

All URIs are relative to *https://api.cloud.telestream.net/qc/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](QcApi.md#cancel_job) | **PUT** /projects/{project_id}/jobs/{job_id}/cancel.json | 
[**create_job**](QcApi.md#create_job) | **POST** /projects/{project_id}/jobs.json | Create a new job
[**create_project**](QcApi.md#create_project) | **POST** /projects.json | Create a new project
[**get_job**](QcApi.md#get_job) | **GET** /projects/{project_id}/jobs/{job_id}.json | Get QC job
[**get_project**](QcApi.md#get_project) | **GET** /projects/{project_id}.json | Get project by Id
[**import_template**](QcApi.md#import_template) | **POST** /projects/import.json | Import Vidchecker template
[**list_jobs**](QcApi.md#list_jobs) | **GET** /projects/{project_id}/jobs.json | Get jobs form projects
[**list_projects**](QcApi.md#list_projects) | **GET** /projects.json | List all projects for an account
[**modify_project**](QcApi.md#modify_project) | **PUT** /projects/{project_id}.json | Modify project
[**proxy**](QcApi.md#proxy) | **GET** /projects/{project_id}/jobs/{job_id}/proxy.json | 
[**remove_job**](QcApi.md#remove_job) | **DELETE** /projects/{project_id}/jobs/{job_id}.json | 
[**remove_project**](QcApi.md#remove_project) | **DELETE** /projects/{project_id}.json | 
[**signed_urls**](QcApi.md#signed_urls) | **GET** /projects/{project_id}/jobs/{job_id}/signed-urls.json | 
[**templates**](QcApi.md#templates) | **GET** /templates.json | List all templates
[**upload_video**](QcApi.md#upload_video) | **POST** /projects/{project_id}/upload.json | Creates an upload session


# **cancel_job**
> cancel_job(project_id, job_id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
job_id = 'job_id_example' # str | A unique identifier of a Job.

try:
    api_instance.cancel_job(project_id, job_id)
except ApiException as e:
    print("Exception when calling QcApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **job_id** | **str**| A unique identifier of a Job. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(project_id, data)

Create a new job

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
data = telestream_cloud_qc.JobData() # JobData | 

try:
    # Create a new job
    api_response = api_instance.create_job(project_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **data** | [**JobData**](JobData.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[api_key](../README.md#api_key)

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

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(project_id, job_id)

Get QC job

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
job_id = 'job_id_example' # str | A unique identifier of a Job.

try:
    # Get QC job
    api_response = api_instance.get_job(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **job_id** | **str**| A unique identifier of a Job. | 

### Return type

[**Job**](Job.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Get project by Id

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.

try:
    # Get project by Id
    api_response = api_instance.get_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_template**
> list[InlineResponse200] import_template(name=name, file=file)

Import Vidchecker template

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
name = 'name_example' # str |  (optional)
file = '/path/to/file.txt' # file |  (optional)

try:
    # Import Vidchecker template
    api_response = api_instance.import_template(name=name, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->import_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: text/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> JobsCollection list_jobs(project_id, expand=expand, status=status, per_page=per_page, page=page)

Get jobs form projects

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
expand = true # bool | Expand details of job (optional)
status = 'status_example' # str | Filter jobs by status (optional)
per_page = 30 # int | Limit number of listed jobs (optional) (default to 30)
page = 56 # int | Index of jobs page to be listed (optional)

try:
    # Get jobs form projects
    api_response = api_instance.list_jobs(project_id, expand=expand, status=status, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **expand** | **bool**| Expand details of job | [optional] 
 **status** | **str**| Filter jobs by status | [optional] 
 **per_page** | **int**| Limit number of listed jobs | [optional] [default to 30]
 **page** | **int**| Index of jobs page to be listed | [optional] 

### Return type

[**JobsCollection**](JobsCollection.md)

### Authorization

[api_key](../README.md#api_key)

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

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))

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

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_project**
> Project modify_project(project_id, data=data)

Modify project

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | 
data = telestream_cloud_qc.Data1() # Data1 |  (optional)

try:
    # Modify project
    api_response = api_instance.modify_project(project_id, data=data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->modify_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **proxy**
> Proxy proxy(project_id, job_id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
job_id = 'job_id_example' # str | A unique identifier of a Job.

try:
    api_response = api_instance.proxy(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **job_id** | **str**| A unique identifier of a Job. | 

### Return type

[**Proxy**](Proxy.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_job**
> remove_job(project_id, job_id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
job_id = 'job_id_example' # str | A unique identifier of a Job.

try:
    api_instance.remove_job(project_id, job_id)
except ApiException as e:
    print("Exception when calling QcApi->remove_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **job_id** | **str**| A unique identifier of a Job. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project**
> remove_project(project_id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | 

try:
    api_instance.remove_project(project_id)
except ApiException as e:
    print("Exception when calling QcApi->remove_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signed_urls**
> dict(str, str) signed_urls(project_id, job_id)



### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
job_id = 'job_id_example' # str | A unique identifier of a Job.

try:
    api_response = api_instance.signed_urls(project_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->signed_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **job_id** | **str**| A unique identifier of a Job. | 

### Return type

**dict(str, str)**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates**
> list[Template] templates()

List all templates

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))

try:
    # List all templates
    api_response = api_instance.templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Template]**](Template.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_video**
> UploadSession upload_video(project_id, video_upload_body)

Creates an upload session

### Example
```python
from __future__ import print_function
import time
import telestream_cloud_qc
from telestream_cloud_qc.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = telestream_cloud_qc.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = telestream_cloud_qc.QcApi(telestream_cloud_qc.ApiClient(configuration))
project_id = 'project_id_example' # str | A unique identifier of a Project.
video_upload_body = telestream_cloud_qc.VideoUploadBody() # VideoUploadBody | 

try:
    # Creates an upload session
    api_response = api_instance.upload_video(project_id, video_upload_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QcApi->upload_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| A unique identifier of a Project. | 
 **video_upload_body** | [**VideoUploadBody**](VideoUploadBody.md)|  | 

### Return type

[**UploadSession**](UploadSession.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

