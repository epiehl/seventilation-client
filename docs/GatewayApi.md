# seventilation_client.GatewayApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_gateway_get**](GatewayApi.md#devices_id_gateway_get) | **GET** /devices/{id}/gateway | Returns a device&#x27; Gateway data object

# **devices_id_gateway_get**
> Gateway devices_id_gateway_get(id)

Returns a device' Gateway data object

Returns the device subobject Gateway for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import seventilation_client
from seventilation_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = seventilation_client.GatewayApi(seventilation_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' Gateway data object
    api_response = api_instance.devices_id_gateway_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayApi->devices_id_gateway_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Gateway**](Gateway.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

