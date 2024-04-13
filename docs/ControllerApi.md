# seventilation_client.ControllerApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_controller_get**](ControllerApi.md#devices_id_controller_get) | **GET** /devices/{id}/controller | Returns a device&#x27; Controller data object

# **devices_id_controller_get**
> Controller devices_id_controller_get(id)

Returns a device' Controller data object

Returns the device subobject Controller for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import seventilation_client
from seventilation_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = seventilation_client.ControllerApi(seventilation_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' Controller data object
    api_response = api_instance.devices_id_controller_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ControllerApi->devices_id_controller_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Controller**](Controller.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

