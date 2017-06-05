# cvtool_cli_client.ExportApi

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export**](ExportApi.md#export) | **POST** /images/{tenant_id}/export | 


# **export**
> export(tenant_id)



Export all images to BQ.

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
api_instance = cvtool_cli_client.ExportApi()
tenant_id = 'tenant_id_example' # str | tenant id

try: 
    api_instance.export(tenant_id)
except ApiException as e:
    print("Exception when calling ExportApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 

### Return type

void (empty response body)

### Authorization

[cvtool_token](../README.md#cvtool_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

