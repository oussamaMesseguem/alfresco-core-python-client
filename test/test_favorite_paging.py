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
from openapi_client.models.favorite_paging import FavoritePaging  # noqa: E501
from openapi_client.rest import ApiException

class TestFavoritePaging(unittest.TestCase):
    """FavoritePaging unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FavoritePaging
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.favorite_paging.FavoritePaging()  # noqa: E501
        if include_optional :
            return FavoritePaging(
                list = openapi_client.models.favorite_paging_list.FavoritePaging_list(
                    pagination = openapi_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        openapi_client.models.favorite_entry.FavoriteEntry(
                            entry = openapi_client.models.favorite.Favorite(
                                target_guid = '0', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                target = openapi_client.models.target.target(), 
                                properties = openapi_client.models.properties.properties(), ), )
                        ], )
            )
        else :
            return FavoritePaging(
                list = openapi_client.models.favorite_paging_list.FavoritePaging_list(
                    pagination = openapi_client.models.pagination.Pagination(
                        count = 56, 
                        has_more_items = True, 
                        total_items = 56, 
                        skip_count = 56, 
                        max_items = 56, ), 
                    entries = [
                        openapi_client.models.favorite_entry.FavoriteEntry(
                            entry = openapi_client.models.favorite.Favorite(
                                target_guid = '0', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                target = openapi_client.models.target.target(), 
                                properties = openapi_client.models.properties.properties(), ), )
                        ], ),
        )

    def testFavoritePaging(self):
        """Test FavoritePaging"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()