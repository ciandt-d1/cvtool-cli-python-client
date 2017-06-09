# coding: utf-8

"""
    CVTool CLI API

    Provides APIs for tenant maintenance

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ImageApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add(self, tenant_id, image_request, **kwargs):
        """
        Adds an image to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add(tenant_id, image_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param ImageRequest image_request: Image to create (required)
        :return: ImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_with_http_info(tenant_id, image_request, **kwargs)
        else:
            (data) = self.add_with_http_info(tenant_id, image_request, **kwargs)
            return data

    def add_with_http_info(self, tenant_id, image_request, **kwargs):
        """
        Adds an image to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_with_http_info(tenant_id, image_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param ImageRequest image_request: Image to create (required)
        :return: ImageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'image_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `add`")
        # verify the required parameter 'image_request' is set
        if ('image_request' not in params) or (params['image_request'] is None):
            raise ValueError("Missing the required parameter `image_request` when calling `add`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'image_request' in params:
            body_params = params['image_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token', 'gae_default_service_account']

        return self.api_client.call_api('/images', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ImageResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def export(self, tenant_id, **kwargs):
        """
        Export all images to BQ.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.export_with_http_info(tenant_id, **kwargs)
        else:
            (data) = self.export_with_http_info(tenant_id, **kwargs)
            return data

    def export_with_http_info(self, tenant_id, **kwargs):
        """
        Export all images to BQ.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_with_http_info(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `export`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `export`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `export`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `export`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token', 'gae_default_service_account']

        return self.api_client.call_api('/images/{tenant_id}/export', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_all(self, tenant_id, **kwargs):
        """
        Adds an image to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_all(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param int offset: offset
        :param int limit: limit
        :return: ImageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_all_with_http_info(tenant_id, **kwargs)
        else:
            (data) = self.list_all_with_http_info(tenant_id, **kwargs)
            return data

    def list_all_with_http_info(self, tenant_id, **kwargs):
        """
        Adds an image to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_all_with_http_info(tenant_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param int offset: offset
        :param int limit: limit
        :return: ImageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'offset', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `list_all`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `list_all`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `list_all`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `list_all`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `list_all`, must be a value greater than or equal to `0`")
        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `list_all`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `list_all`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token', 'gae_default_service_account']

        return self.api_client.call_api('/images', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ImageListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
