# swagger_client.SetupApi

All URIs are relative to *https://api.sec-smart.app/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_id_setup_areas_put**](SetupApi.md#devices_id_setup_areas_put) | **PUT** /devices/{id}/setup/areas | Set up the assignment what kind of boost mode shall be used in the particular areas
[**devices_id_setup_factory_reset_put**](SetupApi.md#devices_id_setup_factory_reset_put) | **PUT** /devices/{id}/setup/factory-reset | Perform a factory reset of the SEC Smart System
[**devices_id_setup_get**](SetupApi.md#devices_id_setup_get) | **GET** /devices/{id}/setup | Returns a device&#x27; setup data object
[**devices_id_setup_input_ai_put**](SetupApi.md#devices_id_setup_input_ai_put) | **PUT** /devices/{id}/setup/input-ai | Set up the configuration for the analog input
[**devices_id_setup_input_di_put**](SetupApi.md#devices_id_setup_input_di_put) | **PUT** /devices/{id}/setup/input-di | Set up the configuration for the digital input
[**devices_id_setup_output_do_put**](SetupApi.md#devices_id_setup_output_do_put) | **PUT** /devices/{id}/setup/output-do | Set up the configuration for the digital output
[**devices_id_setup_systems_put**](SetupApi.md#devices_id_setup_systems_put) | **PUT** /devices/{id}/setup/systems | Set up the assignment what systems are installed in the particular areas

# **devices_id_setup_areas_put**
> object devices_id_setup_areas_put(body, id)

Set up the assignment what kind of boost mode shall be used in the particular areas

Set up the assignment what kind of boost mode shall be used in the particular areas.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupAreasBody() # SetupAreasBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set up the assignment what kind of boost mode shall be used in the particular areas
    api_response = api_instance.devices_id_setup_areas_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_areas_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupAreasBody**](SetupAreasBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_factory_reset_put**
> object devices_id_setup_factory_reset_put(body, id)

Perform a factory reset of the SEC Smart System

Perform a factory reset of the SEC Smart System.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupFactoryresetBody() # SetupFactoryresetBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Perform a factory reset of the SEC Smart System
    api_response = api_instance.devices_id_setup_factory_reset_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_factory_reset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupFactoryresetBody**](SetupFactoryresetBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_get**
> Setup devices_id_setup_get(id)

Returns a device' setup data object

Returns the device subobject setup for the URL-encoded device ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Returns a device' setup data object
    api_response = api_instance.devices_id_setup_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

[**Setup**](Setup.md)

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_input_ai_put**
> object devices_id_setup_input_ai_put(body, id)

Set up the configuration for the analog input

Set up the configuration for the analog input.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupInputaiBody() # SetupInputaiBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set up the configuration for the analog input
    api_response = api_instance.devices_id_setup_input_ai_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_input_ai_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupInputaiBody**](SetupInputaiBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_input_di_put**
> object devices_id_setup_input_di_put(body, id)

Set up the configuration for the digital input

Set up the configuration for the digital input.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupInputdiBody() # SetupInputdiBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set up the configuration for the digital input
    api_response = api_instance.devices_id_setup_input_di_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_input_di_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupInputdiBody**](SetupInputdiBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_output_do_put**
> object devices_id_setup_output_do_put(body, id)

Set up the configuration for the digital output

Set up the configuration for the digital output.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupOutputdoBody() # SetupOutputdoBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set up the configuration for the digital output
    api_response = api_instance.devices_id_setup_output_do_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_output_do_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupOutputdoBody**](SetupOutputdoBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_id_setup_systems_put**
> object devices_id_setup_systems_put(body, id)

Set up the assignment what systems are installed in the particular areas

Set up the assignment what systems are installed in the particular areas.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SetupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetupSystemsBody() # SetupSystemsBody | 
id = 'id_example' # str | 6-digit-long alphanumerical ID of the device to be adressed

try:
    # Set up the assignment what systems are installed in the particular areas
    api_response = api_instance.devices_id_setup_systems_put(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SetupApi->devices_id_setup_systems_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetupSystemsBody**](SetupSystemsBody.md)|  | 
 **id** | **str**| 6-digit-long alphanumerical ID of the device to be adressed | 

### Return type

**object**

### Authorization

[myTokenScheme](../README.md#myTokenScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

