# cvtool_cli_client
Provides APIs for tenant maintenance

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import cvtool_cli_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cvtool_cli_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cvtool_cli_client
from cvtool_cli_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: google_id_token
cvtool_cli_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = cvtool_cli_client.AuthApi()

try:
    api_response = api_instance.token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kingpick-admin-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**token**](docs/AuthApi.md#token) | **GET** /auth/token | 
*DefaultApi* | [**setup**](docs/DefaultApi.md#setup) | **POST** /setup | 
*ImageApi* | [**add**](docs/ImageApi.md#add) | **POST** /images | 
*ImageApi* | [**list_all**](docs/ImageApi.md#list_all) | **GET** /images | 
*JobApi* | [**add_step**](docs/JobApi.md#add_step) | **POST** /jobs/{job_id}/steps | 
*JobApi* | [**create**](docs/JobApi.md#create) | **POST** /jobs | 
*JobApi* | [**end_job**](docs/JobApi.md#end_job) | **POST** /jobs/{job_id}/end | 
*JobApi* | [**get**](docs/JobApi.md#get) | **GET** /jobs/{job_id} | 
*JobApi* | [**start_job**](docs/JobApi.md#start_job) | **POST** /jobs/{job_id}/start | 
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /projects | Creates a new project
*ProjectApi* | [**get_project**](docs/ProjectApi.md#get_project) | **GET** /projects/{project_id} | 
*ProjectApi* | [**list_projects**](docs/ProjectApi.md#list_projects) | **GET** /projects | 
*ProjectApi* | [**put_project**](docs/ProjectApi.md#put_project) | **PUT** /projects/{project_id} | 
*TenantApi* | [**get_tenant**](docs/TenantApi.md#get_tenant) | **GET** /tenants/{tenant_id} | 
*TenantApi* | [**get_tenants**](docs/TenantApi.md#get_tenants) | **GET** /tenants | 
*TenantApi* | [**post_tenant**](docs/TenantApi.md#post_tenant) | **POST** /tenants | 
*TenantApi* | [**put_tenant**](docs/TenantApi.md#put_tenant) | **PUT** /tenants/{tenant_id} | 


## Documentation For Models

 - [Annotations](docs/Annotations.md)
 - [Error](docs/Error.md)
 - [ImageListResponse](docs/ImageListResponse.md)
 - [ImageRequest](docs/ImageRequest.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [Job](docs/Job.md)
 - [JobInputParameters](docs/JobInputParameters.md)
 - [JobStep](docs/JobStep.md)
 - [MetaListResponse](docs/MetaListResponse.md)
 - [NewJobRequest](docs/NewJobRequest.md)
 - [Project](docs/Project.md)
 - [Projects](docs/Projects.md)
 - [Settings](docs/Settings.md)
 - [Tenant](docs/Tenant.md)
 - [Tenants](docs/Tenants.md)
 - [VisionAnnotations](docs/VisionAnnotations.md)


## Documentation For Authorization


## cvtool_token

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A

## google_id_token

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author



