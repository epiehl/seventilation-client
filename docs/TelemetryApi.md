# swagger_client.TelemetryApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_telemetry_get**](TelemetryApi.md#devices_id_telemetry_get) | **GET** /devices/{id}/telemetry | Returns a device&#x27; telemetry data object

# **devices_id_telemetry_get**
> Telemetry devices_id_telemetry_get(id)

Returns a device' telemetry data object

Returns the device subobject telemetry for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TelemetryApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' telemetry data object
    api_response = api_instance.devices_id_telemetry_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelemetryApi->devices_id_telemetry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Telemetry**](Telemetry.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

