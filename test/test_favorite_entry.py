# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.favorite_entry import FavoriteEntry  # noqa: E501
from openapi_client.rest import ApiException

class TestFavoriteEntry(unittest.TestCase):
    """FavoriteEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FavoriteEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.favorite_entry.FavoriteEntry()  # noqa: E501
        if include_optional :
            return FavoriteEntry(
                entry = openapi_client.models.favorite.Favorite(
                    target_guid = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    target = openapi_client.models.target.target(), 
                    properties = openapi_client.models.properties.properties(), )
            )
        else :
            return FavoriteEntry(
                entry = openapi_client.models.favorite.Favorite(
                    target_guid = '0', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    target = openapi_client.models.target.target(), 
                    properties = openapi_client.models.properties.properties(), ),
        )

    def testFavoriteEntry(self):
        """Test FavoriteEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
