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

class Device(object):
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
        'id': 'str',
        'name': 'str',
        'users': 'Users',
        'areas': 'Areas',
        'telemetry': 'Telemetry',
        'notifications': 'Notifications',
        'controller': 'Controller',
        'gateway': 'Gateway',
        'settings': 'Settings',
        'setup': 'Setup'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'users': 'users',
        'areas': 'areas',
        'telemetry': 'telemetry',
        'notifications': 'notifications',
        'controller': 'controller',
        'gateway': 'gateway',
        'settings': 'settings',
        'setup': 'setup'
    }

    def __init__(self, id=None, name=None, users=None, areas=None, telemetry=None, notifications=None, controller=None, gateway=None, settings=None, setup=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._users = None
        self._areas = None
        self._telemetry = None
        self._notifications = None
        self._controller = None
        self._gateway = None
        self._settings = None
        self._setup = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if users is not None:
            self.users = users
        if areas is not None:
            self.areas = areas
        if telemetry is not None:
            self.telemetry = telemetry
        if notifications is not None:
            self.notifications = notifications
        if controller is not None:
            self.controller = controller
        if gateway is not None:
            self.gateway = gateway
        if settings is not None:
            self.settings = settings
        if setup is not None:
            self.setup = setup

    @property
    def id(self):
        """Gets the id of this Device.  # noqa: E501


        :return: The id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Device.


        :param id: The id of this Device.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501


        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.


        :param name: The name of this Device.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def users(self):
        """Gets the users of this Device.  # noqa: E501


        :return: The users of this Device.  # noqa: E501
        :rtype: Users
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Device.


        :param users: The users of this Device.  # noqa: E501
        :type: Users
        """

        self._users = users

    @property
    def areas(self):
        """Gets the areas of this Device.  # noqa: E501


        :return: The areas of this Device.  # noqa: E501
        :rtype: Areas
        """
        return self._areas

    @areas.setter
    def areas(self, areas):
        """Sets the areas of this Device.


        :param areas: The areas of this Device.  # noqa: E501
        :type: Areas
        """

        self._areas = areas

    @property
    def telemetry(self):
        """Gets the telemetry of this Device.  # noqa: E501


        :return: The telemetry of this Device.  # noqa: E501
        :rtype: Telemetry
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this Device.


        :param telemetry: The telemetry of this Device.  # noqa: E501
        :type: Telemetry
        """

        self._telemetry = telemetry

    @property
    def notifications(self):
        """Gets the notifications of this Device.  # noqa: E501


        :return: The notifications of this Device.  # noqa: E501
        :rtype: Notifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Device.


        :param notifications: The notifications of this Device.  # noqa: E501
        :type: Notifications
        """

        self._notifications = notifications

    @property
    def controller(self):
        """Gets the controller of this Device.  # noqa: E501


        :return: The controller of this Device.  # noqa: E501
        :rtype: Controller
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this Device.


        :param controller: The controller of this Device.  # noqa: E501
        :type: Controller
        """

        self._controller = controller

    @property
    def gateway(self):
        """Gets the gateway of this Device.  # noqa: E501


        :return: The gateway of this Device.  # noqa: E501
        :rtype: Gateway
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Device.


        :param gateway: The gateway of this Device.  # noqa: E501
        :type: Gateway
        """

        self._gateway = gateway

    @property
    def settings(self):
        """Gets the settings of this Device.  # noqa: E501


        :return: The settings of this Device.  # noqa: E501
        :rtype: Settings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Device.


        :param settings: The settings of this Device.  # noqa: E501
        :type: Settings
        """

        self._settings = settings

    @property
    def setup(self):
        """Gets the setup of this Device.  # noqa: E501


        :return: The setup of this Device.  # noqa: E501
        :rtype: Setup
        """
        return self._setup

    @setup.setter
    def setup(self, setup):
        """Sets the setup of this Device.


        :param setup: The setup of this Device.  # noqa: E501
        :type: Setup
        """

        self._setup = setup

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
