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
from openapi_client.api.downloads_api import DownloadsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDownloadsApi(unittest.TestCase):
    """DownloadsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.downloads_api.DownloadsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_download(self):
        """Test case for cancel_download

        Cancel a download  # noqa: E501
        """
        pass

    def test_create_download(self):
        """Test case for create_download

        Create a new download  # noqa: E501
        """
        pass

    def test_get_download(self):
        """Test case for get_download

        Get a download  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
