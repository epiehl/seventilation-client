# coding: utf-8

"""
    SEC Smart API

    This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.notifications_api import NotificationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNotificationsApi(unittest.TestCase):
    """NotificationsApi unit test stubs"""

    def setUp(self):
        self.api = NotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_id_notifications_get(self):
        """Test case for devices_id_notifications_get

        Returns a device' notification data object  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
