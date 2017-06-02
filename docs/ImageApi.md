# cvtool_cli_client.ImageApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ImageApi.md#add) | **POST** /images | 
[**list_all**](ImageApi.md#list_all) | **GET** /images | 


# **add**
> ImageResponse add(tenant_id, image_request)



Adds an image to the database.

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cvtool_cli_client.ImageApi()
tenant_id = 'tenant_id_example' # str | tenant id
image_request = cvtool_cli_client.ImageRequest() # ImageRequest | Image to create

try: 
    api_response = api_instance.add(tenant_id, image_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **image_request** | [**ImageRequest**](ImageRequest.md)| Image to create | 

### Return type

[**ImageResponse**](ImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all**
> ImageListResponse list_all(tenant_id, offset=offset, limit=limit)



Adds an image to the database.

### Example 
```python
from __future__ import print_statement
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cvtool_cli_client.ImageApi()
tenant_id = 'tenant_id_example' # str | tenant id
offset = 56 # int | offset (optional)
limit = 56 # int | limit (optional)

try: 
    api_response = api_instance.list_all(tenant_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageApi->list_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 

### Return type

[**ImageListResponse**](ImageListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

