# coding: utf-8

"""
    SEC Smart API

    This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Error(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_errors': 'str',
        'areas_errors': 'ErrorAreasErrors',
        'settings_errors': 'ErrorSettingsErrors',
        'setup_errors': 'ErrorSetupErrors'
    }

    attribute_map = {
        'device_errors': 'DeviceErrors',
        'areas_errors': 'AreasErrors',
        'settings_errors': 'SettingsErrors',
        'setup_errors': 'SetupErrors'
    }

    def __init__(self, device_errors=None, areas_errors=None, settings_errors=None, setup_errors=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._device_errors = None
        self._areas_errors = None
        self._settings_errors = None
        self._setup_errors = None
        self.discriminator = None
        if device_errors is not None:
            self.device_errors = device_errors
        if areas_errors is not None:
            self.areas_errors = areas_errors
        if settings_errors is not None:
            self.settings_errors = settings_errors
        if setup_errors is not None:
            self.setup_errors = setup_errors

    @property
    def device_errors(self):
        """Gets the device_errors of this Error.  # noqa: E501


        :return: The device_errors of this Error.  # noqa: E501
        :rtype: str
        """
        return self._device_errors

    @device_errors.setter
    def device_errors(self, device_errors):
        """Sets the device_errors of this Error.


        :param device_errors: The device_errors of this Error.  # noqa: E501
        :type: str
        """
        allowed_values = ["Field 'name' must be a string with 3 to 32 characters."]  # noqa: E501
        if device_errors not in allowed_values:
            raise ValueError(
                "Invalid value for `device_errors` ({0}), must be one of {1}"  # noqa: E501
                .format(device_errors, allowed_values)
            )

        self._device_errors = device_errors

    @property
    def areas_errors(self):
        """Gets the areas_errors of this Error.  # noqa: E501


        :return: The areas_errors of this Error.  # noqa: E501
        :rtype: ErrorAreasErrors
        """
        return self._areas_errors

    @areas_errors.setter
    def areas_errors(self, areas_errors):
        """Sets the areas_errors of this Error.


        :param areas_errors: The areas_errors of this Error.  # noqa: E501
        :type: ErrorAreasErrors
        """

        self._areas_errors = areas_errors

    @property
    def settings_errors(self):
        """Gets the settings_errors of this Error.  # noqa: E501


        :return: The settings_errors of this Error.  # noqa: E501
        :rtype: ErrorSettingsErrors
        """
        return self._settings_errors

    @settings_errors.setter
    def settings_errors(self, settings_errors):
        """Sets the settings_errors of this Error.


        :param settings_errors: The settings_errors of this Error.  # noqa: E501
        :type: ErrorSettingsErrors
        """

        self._settings_errors = settings_errors

    @property
    def setup_errors(self):
        """Gets the setup_errors of this Error.  # noqa: E501


        :return: The setup_errors of this Error.  # noqa: E501
        :rtype: ErrorSetupErrors
        """
        return self._setup_errors

    @setup_errors.setter
    def setup_errors(self, setup_errors):
        """Sets the setup_errors of this Error.


        :param setup_errors: The setup_errors of this Error.  # noqa: E501
        :type: ErrorSetupErrors
        """

        self._setup_errors = setup_errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Error, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
