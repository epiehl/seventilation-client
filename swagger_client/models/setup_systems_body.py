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

class SetupSystemsBody(object):
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
        'systems': 'Setuppropertiessystems'
    }

    attribute_map = {
        'systems': 'systems'
    }

    def __init__(self, systems=None):  # noqa: E501
        """SetupSystemsBody - a model defined in Swagger"""  # noqa: E501
        self._systems = None
        self.discriminator = None
        if systems is not None:
            self.systems = systems

    @property
    def systems(self):
        """Gets the systems of this SetupSystemsBody.  # noqa: E501


        :return: The systems of this SetupSystemsBody.  # noqa: E501
        :rtype: Setuppropertiessystems
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this SetupSystemsBody.


        :param systems: The systems of this SetupSystemsBody.  # noqa: E501
        :type: Setuppropertiessystems
        """

        self._systems = systems

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
        if issubclass(SetupSystemsBody, dict):
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
        if not isinstance(other, SetupSystemsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other