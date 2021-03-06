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
from openapi_client.api.favorites_api import FavoritesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestFavoritesApi(unittest.TestCase):
    """FavoritesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.favorites_api.FavoritesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_favorite(self):
        """Test case for create_favorite

        Create a favorite  # noqa: E501
        """
        pass

    def test_create_site_favorite(self):
        """Test case for create_site_favorite

        Create a site favorite  # noqa: E501
        """
        pass

    def test_delete_favorite(self):
        """Test case for delete_favorite

        Delete a favorite  # noqa: E501
        """
        pass

    def test_delete_site_favorite(self):
        """Test case for delete_site_favorite

        Delete a site favorite  # noqa: E501
        """
        pass

    def test_get_favorite(self):
        """Test case for get_favorite

        Get a favorite  # noqa: E501
        """
        pass

    def test_get_favorite_site(self):
        """Test case for get_favorite_site

        Get a favorite site  # noqa: E501
        """
        pass

    def test_list_favorite_sites_for_person(self):
        """Test case for list_favorite_sites_for_person

        List favorite sites  # noqa: E501
        """
        pass

    def test_list_favorites(self):
        """Test case for list_favorites

        List favorites  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
