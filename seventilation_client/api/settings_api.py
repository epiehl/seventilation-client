# coding: utf-8

"""
    SEC Smart API

    This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from seventilation_client.api_client import ApiClient


class SettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def devices_id_settings_device_time_put(self, body, id, **kwargs):  # noqa: E501
        """Change the time and date adjustments of your device  # noqa: E501

        Change the time and date adjustments of your device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_device_time_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsDevicetimeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_device_time_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_device_time_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_device_time_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Change the time and date adjustments of your device  # noqa: E501

        Change the time and date adjustments of your device.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_device_time_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsDevicetimeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_device_time_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_id_settings_device_time_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_device_time_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings/device-time', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_id_settings_filter_put(self, body, id, **kwargs):  # noqa: E501
        """Set a the filter run time and/or perform a filter reset  # noqa: E501

        If the maxRunTime is submitted only or the reset is set to false just the maxRunTime changes and no reset will be performed. If the reset is set as true, the filter runt time will be reset with the new maxRunTime. If no maxRunTime is commited, but reset is set to true, the filter run time will be reset using the device' internal save value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_filter_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsFilterBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_filter_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_filter_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_filter_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Set a the filter run time and/or perform a filter reset  # noqa: E501

        If the maxRunTime is submitted only or the reset is set to false just the maxRunTime changes and no reset will be performed. If the reset is set as true, the filter runt time will be reset with the new maxRunTime. If no maxRunTime is commited, but reset is set to true, the filter run time will be reset using the device' internal save value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_filter_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsFilterBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_filter_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_id_settings_filter_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_filter_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings/filter', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_id_settings_get(self, id, **kwargs):  # noqa: E501
        """Returns a device' settings data object  # noqa: E501

        Returns the device subobject settings for the URL-encoded device ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: Settings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Returns a device' settings data object  # noqa: E501

        Returns the device subobject settings for the URL-encoded device ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: Settings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Settings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_id_settings_sleep_time_put(self, body, id, **kwargs):  # noqa: E501
        """Set the desired sleep time for sleep time mode  # noqa: E501

        Set the sleep time in minutes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_sleep_time_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSleeptimeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_sleep_time_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_sleep_time_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_sleep_time_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Set the desired sleep time for sleep time mode  # noqa: E501

        Set the sleep time in minutes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_sleep_time_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSleeptimeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_sleep_time_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_id_settings_sleep_time_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_sleep_time_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings/sleep-time', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_id_settings_summermode_put(self, body, id, **kwargs):  # noqa: E501
        """Change the summer ventilation mode.  # noqa: E501

        Turns the summer ventilation mode on or off.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_summermode_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSummermodeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_summermode_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_summermode_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_summermode_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Change the summer ventilation mode.  # noqa: E501

        Turns the summer ventilation mode on or off.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_summermode_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsSummermodeBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_summermode_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_id_settings_summermode_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_summermode_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings/summermode', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def devices_id_settings_thresholds_put(self, body, id, **kwargs):  # noqa: E501
        """Set the threshold values for humidity and CO² regulation mode  # noqa: E501

        Either humidity or co2 or both values can be submitted affecting just the chosen values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_thresholds_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsThresholdsBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.devices_id_settings_thresholds_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.devices_id_settings_thresholds_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def devices_id_settings_thresholds_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Set the threshold values for humidity and CO² regulation mode  # noqa: E501

        Either humidity or co2 or both values can be submitted affecting just the chosen values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.devices_id_settings_thresholds_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsThresholdsBody body: (required)
        :param str id: 6-digit-long alphanumerical ID of the device to be adressed (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method devices_id_settings_thresholds_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `devices_id_settings_thresholds_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `devices_id_settings_thresholds_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['myTokenScheme']  # noqa: E501

        return self.api_client.call_api(
            '/devices/{id}/settings/thresholds', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
