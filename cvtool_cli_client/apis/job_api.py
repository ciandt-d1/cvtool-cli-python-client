# coding: utf-8

"""
    Kingpick Admin API

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


class JobApi(object):
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

    def add_step(self, tenant_id, job_id, job_step, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_step(tenant_id, job_id, job_step, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :param JobStep job_step: job step (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_step_with_http_info(tenant_id, job_id, job_step, **kwargs)
        else:
            (data) = self.add_step_with_http_info(tenant_id, job_id, job_step, **kwargs)
            return data

    def add_step_with_http_info(self, tenant_id, job_id, job_step, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_step_with_http_info(tenant_id, job_id, job_step, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :param JobStep job_step: job step (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'job_id', 'job_step']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `add_step`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `add_step`")
        # verify the required parameter 'job_step' is set
        if ('job_step' not in params) or (params['job_step'] is None):
            raise ValueError("Missing the required parameter `job_step` when calling `add_step`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add_step`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add_step`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `add_step`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'job_step' in params:
            body_params = params['job_step']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token']

        return self.api_client.call_api('/jobs/{job_id}/steps', 'POST',
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

    def create(self, tenant_id, new_job_request, **kwargs):
        """
        Adds an new job.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create(tenant_id, new_job_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param NewJobRequest new_job_request: new job request (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_with_http_info(tenant_id, new_job_request, **kwargs)
        else:
            (data) = self.create_with_http_info(tenant_id, new_job_request, **kwargs)
            return data

    def create_with_http_info(self, tenant_id, new_job_request, **kwargs):
        """
        Adds an new job.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_with_http_info(tenant_id, new_job_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param NewJobRequest new_job_request: new job request (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'new_job_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `create`")
        # verify the required parameter 'new_job_request' is set
        if ('new_job_request' not in params) or (params['new_job_request'] is None):
            raise ValueError("Missing the required parameter `new_job_request` when calling `create`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `create`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `create`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `create`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_job_request' in params:
            body_params = params['new_job_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token']

        return self.api_client.call_api('/jobs', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Job',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def end_job(self, tenant_id, job_id, **kwargs):
        """
        Flag the job as finished
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.end_job(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.end_job_with_http_info(tenant_id, job_id, **kwargs)
        else:
            (data) = self.end_job_with_http_info(tenant_id, job_id, **kwargs)
            return data

    def end_job_with_http_info(self, tenant_id, job_id, **kwargs):
        """
        Flag the job as finished
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.end_job_with_http_info(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method end_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `end_job`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `end_job`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `end_job`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `end_job`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `end_job`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token']

        return self.api_client.call_api('/jobs/{job_id}/end', 'POST',
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

    def get(self, tenant_id, job_id, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_with_http_info(tenant_id, job_id, **kwargs)
        else:
            (data) = self.get_with_http_info(tenant_id, job_id, **kwargs)
            return data

    def get_with_http_info(self, tenant_id, job_id, **kwargs):
        """
        Adds an image signature to the database.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_with_http_info(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `get`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `get`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `get`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token']

        return self.api_client.call_api('/jobs/{job_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Job',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def start_job(self, tenant_id, job_id, **kwargs):
        """
        Flag the job as started
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.start_job(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.start_job_with_http_info(tenant_id, job_id, **kwargs)
        else:
            (data) = self.start_job_with_http_info(tenant_id, job_id, **kwargs)
            return data

    def start_job_with_http_info(self, tenant_id, job_id, **kwargs):
        """
        Flag the job as started
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.start_job_with_http_info(tenant_id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tenant_id: tenant id (required)
        :param str job_id: job id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params) or (params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `start_job`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `start_job`")

        if 'tenant_id' in params and len(params['tenant_id']) > 64:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `start_job`, length must be less than or equal to `64`")
        if 'tenant_id' in params and len(params['tenant_id']) < 3:
            raise ValueError("Invalid value for parameter `tenant_id` when calling `start_job`, length must be greater than or equal to `3`")
        if 'tenant_id' in params and not re.search('[a-z0-9-_\\.]{3,64}', params['tenant_id']):
            raise ValueError("Invalid value for parameter `tenant_id` when calling `start_job`, must conform to the pattern `/[a-z0-9-_\\.]{3,64}/`")

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['job_id'] = params['job_id']

        query_params = {}
        if 'tenant_id' in params:
            query_params['tenant_id'] = params['tenant_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['cvtool_token']

        return self.api_client.call_api('/jobs/{job_id}/start', 'POST',
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
