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

class AnalogInputCurveParametersYHumidity(object):
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
        'lower': 'int',
        'upper': 'int'
    }

    attribute_map = {
        'lower': 'lower',
        'upper': 'upper'
    }

    def __init__(self, lower=None, upper=None):  # noqa: E501
        """AnalogInputCurveParametersYHumidity - a model defined in Swagger"""  # noqa: E501
        self._lower = None
        self._upper = None
        self.discriminator = None
        if lower is not None:
            self.lower = lower
        if upper is not None:
            self.upper = upper

    @property
    def lower(self):
        """Gets the lower of this AnalogInputCurveParametersYHumidity.  # noqa: E501

        Humidity value in % for humidity regulation mode  to apply at lower setpoint.  # noqa: E501

        :return: The lower of this AnalogInputCurveParametersYHumidity.  # noqa: E501
        :rtype: int
        """
        return self._lower

    @lower.setter
    def lower(self, lower):
        """Sets the lower of this AnalogInputCurveParametersYHumidity.

        Humidity value in % for humidity regulation mode  to apply at lower setpoint.  # noqa: E501

        :param lower: The lower of this AnalogInputCurveParametersYHumidity.  # noqa: E501
        :type: int
        """

        self._lower = lower

    @property
    def upper(self):
        """Gets the upper of this AnalogInputCurveParametersYHumidity.  # noqa: E501

        Humidity value in % for humidity regulation mode  to apply at upper setpoint.  # noqa: E501

        :return: The upper of this AnalogInputCurveParametersYHumidity.  # noqa: E501
        :rtype: int
        """
        return self._upper

    @upper.setter
    def upper(self, upper):
        """Sets the upper of this AnalogInputCurveParametersYHumidity.

        Humidity value in % for humidity regulation mode  to apply at upper setpoint.  # noqa: E501

        :param upper: The upper of this AnalogInputCurveParametersYHumidity.  # noqa: E501
        :type: int
        """

        self._upper = upper

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
        if issubclass(AnalogInputCurveParametersYHumidity, dict):
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
        if not isinstance(other, AnalogInputCurveParametersYHumidity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
