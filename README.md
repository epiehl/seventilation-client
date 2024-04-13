# swagger-client
This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.sec-smart.app/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AreasApi* | [**devices_id_areas_get**](docs/AreasApi.md#devices_id_areas_get) | **GET** /devices/{id}/areas | Returns a device&#x27; areas object collection
*AreasApi* | [**devices_id_areas_label_put**](docs/AreasApi.md#devices_id_areas_label_put) | **PUT** /devices/{id}/areas/label | Updates the name for the given area
*AreasApi* | [**devices_id_areas_mode_put**](docs/AreasApi.md#devices_id_areas_mode_put) | **PUT** /devices/{id}/areas/mode | Set a ventilation mode for a given area
*AreasApi* | [**devices_id_areas_timeprogram_put**](docs/AreasApi.md#devices_id_areas_timeprogram_put) | **PUT** /devices/{id}/areas/timeprogram | Set a timed program for a given area
*ControllerApi* | [**devices_id_controller_get**](docs/ControllerApi.md#devices_id_controller_get) | **GET** /devices/{id}/controller | Returns a device&#x27; Controller data object
*DevicesApi* | [**devices_get**](docs/DevicesApi.md#devices_get) | **GET** /devices | Returns an object array of all your registered devices.
*DevicesApi* | [**devices_id_get**](docs/DevicesApi.md#devices_id_get) | **GET** /devices/{id} | Returns a device object
*DevicesApi* | [**devices_id_name_put**](docs/DevicesApi.md#devices_id_name_put) | **PUT** /devices/{id}/name | Sets a free choseable name for your device
*GatewayApi* | [**devices_id_gateway_get**](docs/GatewayApi.md#devices_id_gateway_get) | **GET** /devices/{id}/gateway | Returns a device&#x27; Gateway data object
*NotificationsApi* | [**devices_id_notifications_get**](docs/NotificationsApi.md#devices_id_notifications_get) | **GET** /devices/{id}/notifications | Returns a device&#x27; notification data object
*SettingsApi* | [**devices_id_settings_device_time_put**](docs/SettingsApi.md#devices_id_settings_device_time_put) | **PUT** /devices/{id}/settings/device-time | Change the time and date adjustments of your device
*SettingsApi* | [**devices_id_settings_filter_put**](docs/SettingsApi.md#devices_id_settings_filter_put) | **PUT** /devices/{id}/settings/filter | Set a the filter run time and/or perform a filter reset
*SettingsApi* | [**devices_id_settings_get**](docs/SettingsApi.md#devices_id_settings_get) | **GET** /devices/{id}/settings | Returns a device&#x27; settings data object
*SettingsApi* | [**devices_id_settings_sleep_time_put**](docs/SettingsApi.md#devices_id_settings_sleep_time_put) | **PUT** /devices/{id}/settings/sleep-time | Set the desired sleep time for sleep time mode
*SettingsApi* | [**devices_id_settings_summermode_put**](docs/SettingsApi.md#devices_id_settings_summermode_put) | **PUT** /devices/{id}/settings/summermode | Change the summer ventilation mode.
*SettingsApi* | [**devices_id_settings_thresholds_put**](docs/SettingsApi.md#devices_id_settings_thresholds_put) | **PUT** /devices/{id}/settings/thresholds | Set the threshold values for humidity and CO² regulation mode
*SetupApi* | [**devices_id_setup_areas_put**](docs/SetupApi.md#devices_id_setup_areas_put) | **PUT** /devices/{id}/setup/areas | Set up the assignment what kind of boost mode shall be used in the particular areas
*SetupApi* | [**devices_id_setup_factory_reset_put**](docs/SetupApi.md#devices_id_setup_factory_reset_put) | **PUT** /devices/{id}/setup/factory-reset | Perform a factory reset of the SEC Smart System
*SetupApi* | [**devices_id_setup_get**](docs/SetupApi.md#devices_id_setup_get) | **GET** /devices/{id}/setup | Returns a device&#x27; setup data object
*SetupApi* | [**devices_id_setup_input_ai_put**](docs/SetupApi.md#devices_id_setup_input_ai_put) | **PUT** /devices/{id}/setup/input-ai | Set up the configuration for the analog input
*SetupApi* | [**devices_id_setup_input_di_put**](docs/SetupApi.md#devices_id_setup_input_di_put) | **PUT** /devices/{id}/setup/input-di | Set up the configuration for the digital input
*SetupApi* | [**devices_id_setup_output_do_put**](docs/SetupApi.md#devices_id_setup_output_do_put) | **PUT** /devices/{id}/setup/output-do | Set up the configuration for the digital output
*SetupApi* | [**devices_id_setup_systems_put**](docs/SetupApi.md#devices_id_setup_systems_put) | **PUT** /devices/{id}/setup/systems | Set up the assignment what systems are installed in the particular areas
*TelemetryApi* | [**devices_id_telemetry_get**](docs/TelemetryApi.md#devices_id_telemetry_get) | **GET** /devices/{id}/telemetry | Returns a device&#x27; telemetry data object
*UsersApi* | [**devices_id_users_get**](docs/UsersApi.md#devices_id_users_get) | **GET** /devices/{id}/users | Returns an array containing the email adresses of all users of this device

## Documentation For Models

 - [AnalogInput](docs/AnalogInput.md)
 - [AnalogInputCurveParameters](docs/AnalogInputCurveParameters.md)
 - [AnalogInputCurveParametersX](docs/AnalogInputCurveParametersX.md)
 - [AnalogInputCurveParametersYCO2](docs/AnalogInputCurveParametersYCO2.md)
 - [AnalogInputCurveParametersYFanlevel](docs/AnalogInputCurveParametersYFanlevel.md)
 - [AnalogInputCurveParametersYHumidity](docs/AnalogInputCurveParametersYHumidity.md)
 - [AnalogInputCurveParametersYTemp](docs/AnalogInputCurveParametersYTemp.md)
 - [Area](docs/Area.md)
 - [AreaTimers](docs/AreaTimers.md)
 - [Areas](docs/Areas.md)
 - [AreasLabelBody](docs/AreasLabelBody.md)
 - [AreasModeBody](docs/AreasModeBody.md)
 - [AreasTimeprogramBody](docs/AreasTimeprogramBody.md)
 - [BoostMode](docs/BoostMode.md)
 - [Controller](docs/Controller.md)
 - [Device](docs/Device.md)
 - [DevicesidsettingsfilterFilter](docs/DevicesidsettingsfilterFilter.md)
 - [DigitalInput](docs/DigitalInput.md)
 - [DigitalInputAreas](docs/DigitalInputAreas.md)
 - [DigitalOutput](docs/DigitalOutput.md)
 - [Error](docs/Error.md)
 - [ErrorAreasErrors](docs/ErrorAreasErrors.md)
 - [ErrorSettingsErrors](docs/ErrorSettingsErrors.md)
 - [ErrorSetupErrors](docs/ErrorSetupErrors.md)
 - [Filter](docs/Filter.md)
 - [Gateway](docs/Gateway.md)
 - [IdNameBody](docs/IdNameBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [InlineResponse4001](docs/InlineResponse4001.md)
 - [InlineResponse40010](docs/InlineResponse40010.md)
 - [InlineResponse40011](docs/InlineResponse40011.md)
 - [InlineResponse40012](docs/InlineResponse40012.md)
 - [InlineResponse40013](docs/InlineResponse40013.md)
 - [InlineResponse40014](docs/InlineResponse40014.md)
 - [InlineResponse4002](docs/InlineResponse4002.md)
 - [InlineResponse4003](docs/InlineResponse4003.md)
 - [InlineResponse4004](docs/InlineResponse4004.md)
 - [InlineResponse4005](docs/InlineResponse4005.md)
 - [InlineResponse4006](docs/InlineResponse4006.md)
 - [InlineResponse4007](docs/InlineResponse4007.md)
 - [InlineResponse4008](docs/InlineResponse4008.md)
 - [InlineResponse4009](docs/InlineResponse4009.md)
 - [Notifications](docs/Notifications.md)
 - [NotificationsLastMessage](docs/NotificationsLastMessage.md)
 - [Settings](docs/Settings.md)
 - [SettingsDeviceTime](docs/SettingsDeviceTime.md)
 - [SettingsDevicetimeBody](docs/SettingsDevicetimeBody.md)
 - [SettingsFilterBody](docs/SettingsFilterBody.md)
 - [SettingsSleeptimeBody](docs/SettingsSleeptimeBody.md)
 - [SettingsSummermodeBody](docs/SettingsSummermodeBody.md)
 - [SettingsThresholdsBody](docs/SettingsThresholdsBody.md)
 - [Setup](docs/Setup.md)
 - [SetupAreas](docs/SetupAreas.md)
 - [SetupAreasBody](docs/SetupAreasBody.md)
 - [SetupFactoryresetBody](docs/SetupFactoryresetBody.md)
 - [SetupInputaiBody](docs/SetupInputaiBody.md)
 - [SetupInputdiBody](docs/SetupInputdiBody.md)
 - [SetupOutputdoBody](docs/SetupOutputdoBody.md)
 - [SetupSystems](docs/SetupSystems.md)
 - [SetupSystemsBody](docs/SetupSystemsBody.md)
 - [System](docs/System.md)
 - [Telemetry](docs/Telemetry.md)
 - [TelemetryRestSleepTime](docs/TelemetryRestSleepTime.md)
 - [Thresholds](docs/Thresholds.md)
 - [Timer](docs/Timer.md)
 - [Users](docs/Users.md)

## Documentation For Authorization


## myTokenScheme



## Author


