# swagger_client.SettingsApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_settings_device_time_put**](SettingsApi.md#devices_id_settings_device_time_put) | **PUT** /devices/{id}/settings/device-time | Change the time and date adjustments of your device
[**devices_id_settings_filter_put**](SettingsApi.md#devices_id_settings_filter_put) | **PUT** /devices/{id}/settings/filter | Set a the filter run time and/or perform a filter reset
[**devices_id_settings_get**](SettingsApi.md#devices_id_settings_get) | **GET** /devices/{id}/settings | Returns a device&#x27; settings data object
[**devices_id_settings_sleep_time_put**](SettingsApi.md#devices_id_settings_sleep_time_put) | **PUT** /devices/{id}/settings/sleep-time | Set the desired sleep time for sleep time mode
[**devices_id_settings_summermode_put**](SettingsApi.md#devices_id_settings_summermode_put) | **PUT** /devices/{id}/settings/summermode | Change the summer ventilation mode.
[**devices_id_settings_thresholds_put**](SettingsApi.md#devices_id_settings_thresholds_put) | **PUT** /devices/{id}/settings/thresholds | Set the threshold values for humidity and CO² regulation mode

# **devices_id_settings_device_time_put**
> object devices_id_settings_device_time_put(body, id)

Change the time and date adjustments of your device

Change the time and date adjustments of your device.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsDevicetimeBody() # SettingsDevicetimeBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Change the time and date adjustments of your device
    api_response = api_instance.devices_id_settings_device_time_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_device_time_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsDevicetimeBody**](SettingsDevicetimeBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_settings_filter_put**
> object devices_id_settings_filter_put(body, id)

Set a the filter run time and/or perform a filter reset

If the maxRunTime is submitted only or the reset is set to false just the maxRunTime changes and no reset will be performed. If the reset is set as true, the filter runt time will be reset with the new maxRunTime. If no maxRunTime is commited, but reset is set to true, the filter run time will be reset using the device' internal save value.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsFilterBody() # SettingsFilterBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set a the filter run time and/or perform a filter reset
    api_response = api_instance.devices_id_settings_filter_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_filter_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsFilterBody**](SettingsFilterBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_settings_get**
> Settings devices_id_settings_get(id)

Returns a device' settings data object

Returns the device subobject settings for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' settings data object
    api_response = api_instance.devices_id_settings_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Settings**](Settings.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_settings_sleep_time_put**
> object devices_id_settings_sleep_time_put(body, id)

Set the desired sleep time for sleep time mode

Set the sleep time in minutes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsSleeptimeBody() # SettingsSleeptimeBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set the desired sleep time for sleep time mode
    api_response = api_instance.devices_id_settings_sleep_time_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_sleep_time_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSleeptimeBody**](SettingsSleeptimeBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_settings_summermode_put**
> object devices_id_settings_summermode_put(body, id)

Change the summer ventilation mode.

Turns the summer ventilation mode on or off.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsSummermodeBody() # SettingsSummermodeBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Change the summer ventilation mode.
    api_response = api_instance.devices_id_settings_summermode_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_summermode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsSummermodeBody**](SettingsSummermodeBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_settings_thresholds_put**
> object devices_id_settings_thresholds_put(body, id)

Set the threshold values for humidity and CO² regulation mode

Either humidity or co2 or both values can be submitted affecting just the chosen values.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SettingsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsThresholdsBody() # SettingsThresholdsBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set the threshold values for humidity and CO² regulation mode
    api_response = api_instance.devices_id_settings_thresholds_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->devices_id_settings_thresholds_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsThresholdsBody**](SettingsThresholdsBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

