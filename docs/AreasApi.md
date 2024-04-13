# swagger_client.AreasApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_areas_get**](AreasApi.md#devices_id_areas_get) | **GET** /devices/{id}/areas | Returns a device&#x27; areas object collection
[**devices_id_areas_label_put**](AreasApi.md#devices_id_areas_label_put) | **PUT** /devices/{id}/areas/label | Updates the name for the given area
[**devices_id_areas_mode_put**](AreasApi.md#devices_id_areas_mode_put) | **PUT** /devices/{id}/areas/mode | Set a ventilation mode for a given area
[**devices_id_areas_timeprogram_put**](AreasApi.md#devices_id_areas_timeprogram_put) | **PUT** /devices/{id}/areas/timeprogram | Set a timed program for a given area

# **devices_id_areas_get**
> Areas devices_id_areas_get(id)

Returns a device' areas object collection

Returns the device subobject areas for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AreasApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' areas object collection
    api_response = api_instance.devices_id_areas_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->devices_id_areas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Areas**](Areas.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_areas_label_put**
> object devices_id_areas_label_put(body, id)

Updates the name for the given area

Updates the name for the given area.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AreasApi(swagger_client.ApiClient(configuration))
body = swagger_client.AreasLabelBody() # AreasLabelBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Updates the name for the given area
    api_response = api_instance.devices_id_areas_label_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->devices_id_areas_label_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AreasLabelBody**](AreasLabelBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_areas_mode_put**
> object devices_id_areas_mode_put(body, id)

Set a ventilation mode for a given area

Sets the ventilation mode for the given area.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AreasApi(swagger_client.ApiClient(configuration))
body = swagger_client.AreasModeBody() # AreasModeBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set a ventilation mode for a given area
    api_response = api_instance.devices_id_areas_mode_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->devices_id_areas_mode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AreasModeBody**](AreasModeBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_areas_timeprogram_put**
> object devices_id_areas_timeprogram_put(body, id)

Set a timed program for a given area

Sets a timed program for the given area.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AreasApi(swagger_client.ApiClient(configuration))
body = swagger_client.AreasTimeprogramBody() # AreasTimeprogramBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set a timed program for a given area
    api_response = api_instance.devices_id_areas_timeprogram_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AreasApi->devices_id_areas_timeprogram_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AreasTimeprogramBody**](AreasTimeprogramBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

