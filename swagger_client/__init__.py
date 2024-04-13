# coding: utf-8

# flake8: noqa

"""
    SEC Smart API

    This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.areas_api import AreasApi
from swagger_client.api.controller_api import ControllerApi
from swagger_client.api.devices_api import DevicesApi
from swagger_client.api.gateway_api import GatewayApi
from swagger_client.api.notifications_api import NotificationsApi
from swagger_client.api.settings_api import SettingsApi
from swagger_client.api.setup_api import SetupApi
from swagger_client.api.telemetry_api import TelemetryApi
from swagger_client.api.users_api import UsersApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.analog_input import AnalogInput
from swagger_client.models.analog_input_curve_parameters import AnalogInputCurveParameters
from swagger_client.models.analog_input_curve_parameters_x import AnalogInputCurveParametersX
from swagger_client.models.analog_input_curve_parameters_yco2 import AnalogInputCurveParametersYCO2
from swagger_client.models.analog_input_curve_parameters_y_fanlevel import AnalogInputCurveParametersYFanlevel
from swagger_client.models.analog_input_curve_parameters_y_humidity import AnalogInputCurveParametersYHumidity
from swagger_client.models.analog_input_curve_parameters_y_temp import AnalogInputCurveParametersYTemp
from swagger_client.models.area import Area
from swagger_client.models.area_timers import AreaTimers
from swagger_client.models.areas import Areas
from swagger_client.models.areas_label_body import AreasLabelBody
from swagger_client.models.areas_mode_body import AreasModeBody
from swagger_client.models.areas_timeprogram_body import AreasTimeprogramBody
from swagger_client.models.boost_mode import BoostMode
from swagger_client.models.controller import Controller
from swagger_client.models.device import Device
from swagger_client.models.devicesidsettingsfilter_filter import DevicesidsettingsfilterFilter
from swagger_client.models.digital_input import DigitalInput
from swagger_client.models.digital_input_areas import DigitalInputAreas
from swagger_client.models.digital_output import DigitalOutput
from swagger_client.models.error import Error
from swagger_client.models.error_areas_errors import ErrorAreasErrors
from swagger_client.models.error_settings_errors import ErrorSettingsErrors
from swagger_client.models.error_setup_errors import ErrorSetupErrors
from swagger_client.models.filter import Filter
from swagger_client.models.gateway import Gateway
from swagger_client.models.id_name_body import IdNameBody
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response400 import InlineResponse400
from swagger_client.models.inline_response4001 import InlineResponse4001
from swagger_client.models.inline_response40010 import InlineResponse40010
from swagger_client.models.inline_response40011 import InlineResponse40011
from swagger_client.models.inline_response40012 import InlineResponse40012
from swagger_client.models.inline_response40013 import InlineResponse40013
from swagger_client.models.inline_response40014 import InlineResponse40014
from swagger_client.models.inline_response4002 import InlineResponse4002
from swagger_client.models.inline_response4003 import InlineResponse4003
from swagger_client.models.inline_response4004 import InlineResponse4004
from swagger_client.models.inline_response4005 import InlineResponse4005
from swagger_client.models.inline_response4006 import InlineResponse4006
from swagger_client.models.inline_response4007 import InlineResponse4007
from swagger_client.models.inline_response4008 import InlineResponse4008
from swagger_client.models.inline_response4009 import InlineResponse4009
from swagger_client.models.notifications import Notifications
from swagger_client.models.notifications_last_message import NotificationsLastMessage
from swagger_client.models.settings import Settings
from swagger_client.models.settings_device_time import SettingsDeviceTime
from swagger_client.models.settings_devicetime_body import SettingsDevicetimeBody
from swagger_client.models.settings_filter_body import SettingsFilterBody
from swagger_client.models.settings_sleeptime_body import SettingsSleeptimeBody
from swagger_client.models.settings_summermode_body import SettingsSummermodeBody
from swagger_client.models.settings_thresholds_body import SettingsThresholdsBody
from swagger_client.models.setup import Setup
from swagger_client.models.setup_areas import SetupAreas
from swagger_client.models.setup_areas_body import SetupAreasBody
from swagger_client.models.setup_factoryreset_body import SetupFactoryresetBody
from swagger_client.models.setup_inputai_body import SetupInputaiBody
from swagger_client.models.setup_inputdi_body import SetupInputdiBody
from swagger_client.models.setup_outputdo_body import SetupOutputdoBody
from swagger_client.models.setup_systems import SetupSystems
from swagger_client.models.setup_systems_body import SetupSystemsBody
from swagger_client.models.system import System
from swagger_client.models.telemetry import Telemetry
from swagger_client.models.telemetry_rest_sleep_time import TelemetryRestSleepTime
from swagger_client.models.thresholds import Thresholds
from swagger_client.models.timer import Timer
from swagger_client.models.users import Users