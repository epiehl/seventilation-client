# seventilation_client.DevicesApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_get**](DevicesApi.md#devices_get) | **GET** /devices | Returns an object array of all your registered devices.
[**devices_id_get**](DevicesApi.md#devices_id_get) | **GET** /devices/{id} | Returns a device object
[**devices_id_name_put**](DevicesApi.md#devices_id_name_put) | **PUT** /devices/{id}/name | Sets a free choseable name for your device

# **devices_get**
> list[InlineResponse200] devices_get()

Returns an object array of all your registered devices.

Returns an array filled with shortened device objects consisting of type, id and name of SEC Smart systems you are associated with.

### Example
```python
from __future__ import print_function
import time
import seventilation_client
from seventilation_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: myTokenScheme
configuration = seventilation_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = seventilation_client.DevicesApi(seventilation_client.ApiClient(configuration))

try:
    # Returns an object array of all your registered devices.
    api_response = api_instance.devices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_get**
> Device devices_id_get(id)

Returns a device object

Returns a device object with the URL-encoded device ID if you are associated with this particular device.

### Example
```python
from __future__ import print_function
import time
import seventilation_client
from seventilation_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: myTokenScheme
configuration = seventilation_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = seventilation_client.DevicesApi(seventilation_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device object
    api_response = api_instance.devices_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Device**](Device.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_name_put**
> object devices_id_name_put(body, id)

Sets a free choseable name for your device

Set a free choseable name for your device.

### Example
```python
from __future__ import print_function
import time
import seventilation_client
from seventilation_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: myTokenScheme
configuration = seventilation_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = seventilation_client.DevicesApi(seventilation_client.ApiClient(configuration))
body = seventilation_client.IdNameBody() # IdNameBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Sets a free choseable name for your device
    api_response = api_instance.devices_id_name_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_id_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdNameBody**](IdNameBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

