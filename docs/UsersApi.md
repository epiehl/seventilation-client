# seventilation_client.UsersApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_users_get**](UsersApi.md#devices_id_users_get) | **GET** /devices/{id}/users | Returns an array containing the email adresses of all users of this device

# **devices_id_users_get**
> Users devices_id_users_get(id)

Returns an array containing the email adresses of all users of this device

Returns an array containing the email adresses of all users of this device.

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
api_instance = seventilation_client.UsersApi(seventilation_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns an array containing the email adresses of all users of this device
    api_response = api_instance.devices_id_users_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->devices_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Users**](Users.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

