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

class Thresholds(object):
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
        'humidity': 'int',
        'co2': 'int'
    }

    attribute_map = {
        'humidity': 'humidity',
        'co2': 'co2'
    }

    def __init__(self, humidity=None, co2=None):  # noqa: E501
        """Thresholds - a model defined in Swagger"""  # noqa: E501
        self._humidity = None
        self._co2 = None
        self.discriminator = None
        if humidity is not None:
            self.humidity = humidity
        if co2 is not None:
            self.co2 = co2

    @property
    def humidity(self):
        """Gets the humidity of this Thresholds.  # noqa: E501

        Threshold for humidity regulation in % relative humidity.  # noqa: E501

        :return: The humidity of this Thresholds.  # noqa: E501
        :rtype: int
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this Thresholds.

        Threshold for humidity regulation in % relative humidity.  # noqa: E501

        :param humidity: The humidity of this Thresholds.  # noqa: E501
        :type: int
        """

        self._humidity = humidity

    @property
    def co2(self):
        """Gets the co2 of this Thresholds.  # noqa: E501

        Threshold for CO² regulation in ppm. Stepsize is 10.  # noqa: E501

        :return: The co2 of this Thresholds.  # noqa: E501
        :rtype: int
        """
        return self._co2

    @co2.setter
    def co2(self, co2):
        """Sets the co2 of this Thresholds.

        Threshold for CO² regulation in ppm. Stepsize is 10.  # noqa: E501

        :param co2: The co2 of this Thresholds.  # noqa: E501
        :type: int
        """

        self._co2 = co2

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
        if issubclass(Thresholds, dict):
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
        if not isinstance(other, Thresholds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
