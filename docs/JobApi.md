# cvtool_cli_client.JobApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_step**](JobApi.md#add_step) | **POST** /jobs/{job_id}/steps | 
[**create**](JobApi.md#create) | **POST** /jobs | 
[**end_job**](JobApi.md#end_job) | **POST** /jobs/{job_id}/end | 
[**get**](JobApi.md#get) | **GET** /jobs/{job_id} | 
[**start_job**](JobApi.md#start_job) | **POST** /jobs/{job_id}/start | 


# **add_step**
> add_step(tenant_id, job_id, job_step)



Adds an image signature to the database.

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: cvtool_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cvtool_cli_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
job_id = 'job_id_example' # str | job id
job_step = cvtool_cli_client.JobStep() # JobStep | job step

try: 
    api_instance.add_step(tenant_id, job_id, job_step)
except ApiException as e:
    print("Exception when calling JobApi->add_step: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **job_id** | **str**| job id | 
 **job_step** | [**JobStep**](JobStep.md)| job step | 

### Return type

void (empty response body)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Job create(tenant_id, new_job_request)



Adds an new job.

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: cvtool_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cvtool_cli_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
new_job_request = cvtool_cli_client.NewJobRequest() # NewJobRequest | new job request

try: 
    api_response = api_instance.create(tenant_id, new_job_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **new_job_request** | [**NewJobRequest**](NewJobRequest.md)| new job request | 

### Return type

[**Job**](Job.md)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_job**
> end_job(tenant_id, job_id)



Flag the job as finished

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: cvtool_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cvtool_cli_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
job_id = 'job_id_example' # str | job id

try: 
    api_instance.end_job(tenant_id, job_id)
except ApiException as e:
    print("Exception when calling JobApi->end_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **job_id** | **str**| job id | 

### Return type

void (empty response body)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Job get(tenant_id, job_id)



Adds an image signature to the database.

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: cvtool_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cvtool_cli_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
job_id = 'job_id_example' # str | job id

try: 
    api_response = api_instance.get(tenant_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **job_id** | **str**| job id | 

### Return type

[**Job**](Job.md)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_job**
> start_job(tenant_id, job_id)



Flag the job as started

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: cvtool_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = cvtool_cli_client.JobApi()
tenant_id = 'tenant_id_example' # str | tenant id
job_id = 'job_id_example' # str | job id

try: 
    api_instance.start_job(tenant_id, job_id)
except ApiException as e:
    print("Exception when calling JobApi->start_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **job_id** | **str**| job id | 

### Return type

void (empty response body)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

