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

class SetupOutputdoBody(object):
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
        'digital_output': 'SetuppropertiesoutputDo'
    }

    attribute_map = {
        'digital_output': 'digitalOutput'
    }

    def __init__(self, digital_output=None):  # noqa: E501
        """SetupOutputdoBody - a model defined in Swagger"""  # noqa: E501
        self._digital_output = None
        self.discriminator = None
        if digital_output is not None:
            self.digital_output = digital_output

    @property
    def digital_output(self):
        """Gets the digital_output of this SetupOutputdoBody.  # noqa: E501


        :return: The digital_output of this SetupOutputdoBody.  # noqa: E501
        :rtype: SetuppropertiesoutputDo
        """
        return self._digital_output

    @digital_output.setter
    def digital_output(self, digital_output):
        """Sets the digital_output of this SetupOutputdoBody.


        :param digital_output: The digital_output of this SetupOutputdoBody.  # noqa: E501
        :type: SetuppropertiesoutputDo
        """

        self._digital_output = digital_output

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
        if issubclass(SetupOutputdoBody, dict):
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
        if not isinstance(other, SetupOutputdoBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other