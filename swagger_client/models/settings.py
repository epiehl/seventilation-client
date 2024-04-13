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

class Settings(object):
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
        'filter': 'Filter',
        'thresholds': 'Thresholds',
        'sleep_time': 'int',
        'device_time': 'SettingsDeviceTime',
        'summermode': 'bool'
    }

    attribute_map = {
        'filter': 'filter',
        'thresholds': 'thresholds',
        'sleep_time': 'sleepTime',
        'device_time': 'deviceTime',
        'summermode': 'summermode'
    }

    def __init__(self, filter=None, thresholds=None, sleep_time=None, device_time=None, summermode=None):  # noqa: E501
        """Settings - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._thresholds = None
        self._sleep_time = None
        self._device_time = None
        self._summermode = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if thresholds is not None:
            self.thresholds = thresholds
        if sleep_time is not None:
            self.sleep_time = sleep_time
        if device_time is not None:
            self.device_time = device_time
        if summermode is not None:
            self.summermode = summermode

    @property
    def filter(self):
        """Gets the filter of this Settings.  # noqa: E501


        :return: The filter of this Settings.  # noqa: E501
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Settings.


        :param filter: The filter of this Settings.  # noqa: E501
        :type: Filter
        """

        self._filter = filter

    @property
    def thresholds(self):
        """Gets the thresholds of this Settings.  # noqa: E501


        :return: The thresholds of this Settings.  # noqa: E501
        :rtype: Thresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """Sets the thresholds of this Settings.


        :param thresholds: The thresholds of this Settings.  # noqa: E501
        :type: Thresholds
        """

        self._thresholds = thresholds

    @property
    def sleep_time(self):
        """Gets the sleep_time of this Settings.  # noqa: E501

        Duration of the sleep mode in minutes.  # noqa: E501

        :return: The sleep_time of this Settings.  # noqa: E501
        :rtype: int
        """
        return self._sleep_time

    @sleep_time.setter
    def sleep_time(self, sleep_time):
        """Sets the sleep_time of this Settings.

        Duration of the sleep mode in minutes.  # noqa: E501

        :param sleep_time: The sleep_time of this Settings.  # noqa: E501
        :type: int
        """

        self._sleep_time = sleep_time

    @property
    def device_time(self):
        """Gets the device_time of this Settings.  # noqa: E501


        :return: The device_time of this Settings.  # noqa: E501
        :rtype: SettingsDeviceTime
        """
        return self._device_time

    @device_time.setter
    def device_time(self, device_time):
        """Sets the device_time of this Settings.


        :param device_time: The device_time of this Settings.  # noqa: E501
        :type: SettingsDeviceTime
        """

        self._device_time = device_time

    @property
    def summermode(self):
        """Gets the summermode of this Settings.  # noqa: E501

        Activation state of the summer ventilation functionality. If active no heat recovery happens.  # noqa: E501

        :return: The summermode of this Settings.  # noqa: E501
        :rtype: bool
        """
        return self._summermode

    @summermode.setter
    def summermode(self, summermode):
        """Sets the summermode of this Settings.

        Activation state of the summer ventilation functionality. If active no heat recovery happens.  # noqa: E501

        :param summermode: The summermode of this Settings.  # noqa: E501
        :type: bool
        """

        self._summermode = summermode

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
        if issubclass(Settings, dict):
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
        if not isinstance(other, Settings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
