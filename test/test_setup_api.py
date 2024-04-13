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
from swagger_client.api.setup_api import SetupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSetupApi(unittest.TestCase):
    """SetupApi unit test stubs"""

    def setUp(self):
        self.api = SetupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_id_setup_areas_put(self):
        """Test case for devices_id_setup_areas_put

        Set up the assignment what kind of boost mode shall be used in the particular areas  # noqa: E501
        """
        pass

    def test_devices_id_setup_factory_reset_put(self):
        """Test case for devices_id_setup_factory_reset_put

        Perform a factory reset of the SEC Smart System  # noqa: E501
        """
        pass

    def test_devices_id_setup_get(self):
        """Test case for devices_id_setup_get

        Returns a device' setup data object  # noqa: E501
        """
        pass

    def test_devices_id_setup_input_ai_put(self):
        """Test case for devices_id_setup_input_ai_put

        Set up the configuration for the analog input  # noqa: E501
        """
        pass

    def test_devices_id_setup_input_di_put(self):
        """Test case for devices_id_setup_input_di_put

        Set up the configuration for the digital input  # noqa: E501
        """
        pass

    def test_devices_id_setup_output_do_put(self):
        """Test case for devices_id_setup_output_do_put

        Set up the configuration for the digital output  # noqa: E501
        """
        pass

    def test_devices_id_setup_systems_put(self):
        """Test case for devices_id_setup_systems_put

        Set up the assignment what systems are installed in the particular areas  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
