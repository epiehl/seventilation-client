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

class ErrorAreasErrors(object):
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
        'mode_errors': 'str',
        'label_errors': 'str',
        'timer_errors': 'str'
    }

    attribute_map = {
        'mode_errors': 'ModeErrors',
        'label_errors': 'LabelErrors',
        'timer_errors': 'TimerErrors'
    }

    def __init__(self, mode_errors=None, label_errors=None, timer_errors=None):  # noqa: E501
        """ErrorAreasErrors - a model defined in Swagger"""  # noqa: E501
        self._mode_errors = None
        self._label_errors = None
        self._timer_errors = None
        self.discriminator = None
        if mode_errors is not None:
            self.mode_errors = mode_errors
        if label_errors is not None:
            self.label_errors = label_errors
        if timer_errors is not None:
            self.timer_errors = timer_errors

    @property
    def mode_errors(self):
        """Gets the mode_errors of this ErrorAreasErrors.  # noqa: E501


        :return: The mode_errors of this ErrorAreasErrors.  # noqa: E501
        :rtype: str
        """
        return self._mode_errors

    @mode_errors.setter
    def mode_errors(self, mode_errors):
        """Sets the mode_errors of this ErrorAreasErrors.


        :param mode_errors: The mode_errors of this ErrorAreasErrors.  # noqa: E501
        :type: str
        """
        allowed_values = ["Field 'areaid' is mandatory and must be an integer between 1 and 6", "Field 'mode' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]"]  # noqa: E501
        if mode_errors not in allowed_values:
            raise ValueError(
                "Invalid value for `mode_errors` ({0}), must be one of {1}"  # noqa: E501
                .format(mode_errors, allowed_values)
            )

        self._mode_errors = mode_errors

    @property
    def label_errors(self):
        """Gets the label_errors of this ErrorAreasErrors.  # noqa: E501


        :return: The label_errors of this ErrorAreasErrors.  # noqa: E501
        :rtype: str
        """
        return self._label_errors

    @label_errors.setter
    def label_errors(self, label_errors):
        """Sets the label_errors of this ErrorAreasErrors.


        :param label_errors: The label_errors of this ErrorAreasErrors.  # noqa: E501
        :type: str
        """
        allowed_values = ["Field 'areaid' is mandatory and must be an integer between 1 and 6", "Field 'label' is mandatory and must contain a string of one of this arrays entries: [${labelArray}]"]  # noqa: E501
        if label_errors not in allowed_values:
            raise ValueError(
                "Invalid value for `label_errors` ({0}), must be one of {1}"  # noqa: E501
                .format(label_errors, allowed_values)
            )

        self._label_errors = label_errors

    @property
    def timer_errors(self):
        """Gets the timer_errors of this ErrorAreasErrors.  # noqa: E501


        :return: The timer_errors of this ErrorAreasErrors.  # noqa: E501
        :rtype: str
        """
        return self._timer_errors

    @timer_errors.setter
    def timer_errors(self, timer_errors):
        """Sets the timer_errors of this ErrorAreasErrors.


        :param timer_errors: The timer_errors of this ErrorAreasErrors.  # noqa: E501
        :type: str
        """
        allowed_values = ["Field 'areaid' is mandatory and must be an integer between 1 and 6", "Field 'timers' is mandatory.", "Sub field '1' of 'timers' is mandatory.", "Sub field '2' of 'timers' is mandatory.", "Sub field '3' of 'timers' is mandatory.", "Sub field '4' of 'timers' is mandatory.", "Sub field '5' of 'timers' is mandatory.", "Sub field 'active' of '1' of 'timers' is mandatory and must be a boolean value.", "Sub field 'mode' of '1' of 'timers' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]", "Sub field 'time' of '1' of 'timers' is mandatory and must contain a string encoding a time value in 'hh:mm'", "Sub field 'active' of '2' of 'timers' is mandatory and must be a boolean value.", "Sub field 'mode' of '2' of 'timers' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]", "Sub field 'time' of '2' of 'timers' is mandatory and must contain a string encoding a time value in 'hh:mm'", "Sub field 'active' of '3' of 'timers' is mandatory and must be a boolean value.", "Sub field 'mode' of '3' of 'timers' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]", "Sub field 'time' of '3' of 'timers' is mandatory and must contain a string encoding a time value in 'hh:mm'", "Sub field 'active' of '4' of 'timers' is mandatory and must be a boolean value.", "Sub field 'mode' of '4' of 'timers' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]", "Sub field 'time' of '4' of 'timers' is mandatory and must contain a string encoding a time value in 'hh:mm'", "Sub field 'active' of '5' of 'timers' is mandatory and must be a boolean value.", "Sub field 'mode' of '5' of 'timers' is mandatory and must contain a string of one of this arrays entries: [${modeArray}]", "Sub field 'time' of '5' of 'timers' is mandatory and must contain a string encoding a time value in 'hh:mm'"]  # noqa: E501
        if timer_errors not in allowed_values:
            raise ValueError(
                "Invalid value for `timer_errors` ({0}), must be one of {1}"  # noqa: E501
                .format(timer_errors, allowed_values)
            )

        self._timer_errors = timer_errors

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
        if issubclass(ErrorAreasErrors, dict):
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
        if not isinstance(other, ErrorAreasErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
