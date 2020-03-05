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
from openapi_client.api.versions_api import VersionsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestVersionsApi(unittest.TestCase):
    """VersionsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.versions_api.VersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_version(self):
        """Test case for delete_version

        Delete a version  # noqa: E501
        """
        pass

    def test_get_version(self):
        """Test case for get_version

        Get version information  # noqa: E501
        """
        pass

    def test_get_version_content(self):
        """Test case for get_version_content

        Get version content  # noqa: E501
        """
        pass

    def test_list_version_history(self):
        """Test case for list_version_history

        List version history  # noqa: E501
        """
        pass

    def test_revert_version(self):
        """Test case for revert_version

        Revert a version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
