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

class Timer(object):
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
        'active': 'bool',
        'mode': 'Areapropertiesmode',
        'time': 'str'
    }

    attribute_map = {
        'active': 'active',
        'mode': 'mode',
        'time': 'time'
    }

    def __init__(self, active=None, mode=None, time=None):  # noqa: E501
        """Timer - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._mode = None
        self._time = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if mode is not None:
            self.mode = mode
        if time is not None:
            self.time = time

    @property
    def active(self):
        """Gets the active of this Timer.  # noqa: E501


        :return: The active of this Timer.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Timer.


        :param active: The active of this Timer.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def mode(self):
        """Gets the mode of this Timer.  # noqa: E501


        :return: The mode of this Timer.  # noqa: E501
        :rtype: Areapropertiesmode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Timer.


        :param mode: The mode of this Timer.  # noqa: E501
        :type: Areapropertiesmode
        """

        self._mode = mode

    @property
    def time(self):
        """Gets the time of this Timer.  # noqa: E501


        :return: The time of this Timer.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Timer.


        :param time: The time of this Timer.  # noqa: E501
        :type: str
        """

        self._time = time

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
        if issubclass(Timer, dict):
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
        if not isinstance(other, Timer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other