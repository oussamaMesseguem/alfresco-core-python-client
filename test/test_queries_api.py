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
from openapi_client.api.queries_api import QueriesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestQueriesApi(unittest.TestCase):
    """QueriesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.queries_api.QueriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_nodes(self):
        """Test case for find_nodes

        Find nodes  # noqa: E501
        """
        pass

    def test_find_people(self):
        """Test case for find_people

        Find people  # noqa: E501
        """
        pass

    def test_find_sites(self):
        """Test case for find_sites

        Find sites  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
