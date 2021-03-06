# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.networks_api import NetworksApi  # noqa: E501
from openapi_client.rest import ApiException


class TestNetworksApi(unittest.TestCase):
    """NetworksApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.networks_api.NetworksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_network(self):
        """Test case for get_network

        Get a network  # noqa: E501
        """
        pass

    def test_get_network_for_person(self):
        """Test case for get_network_for_person

        Get network information  # noqa: E501
        """
        pass

    def test_list_networks_for_person(self):
        """Test case for list_networks_for_person

        List network membership  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
