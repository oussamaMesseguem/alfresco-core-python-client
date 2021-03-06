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
from openapi_client.models.site_role_paging_list import SiteRolePagingList  # noqa: E501
from openapi_client.rest import ApiException

class TestSiteRolePagingList(unittest.TestCase):
    """SiteRolePagingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SiteRolePagingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.site_role_paging_list.SiteRolePagingList()  # noqa: E501
        if include_optional :
            return SiteRolePagingList(
                pagination = openapi_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ), 
                entries = [
                    openapi_client.models.site_role_entry.SiteRoleEntry(
                        entry = openapi_client.models.site_role.SiteRole(
                            site = openapi_client.models.site.Site(
                                id = '0', 
                                guid = '0', 
                                title = '0', 
                                description = '0', 
                                visibility = 'PRIVATE', 
                                preset = '0', 
                                role = 'SiteConsumer', ), 
                            id = '0', 
                            guid = '0', 
                            role = 'SiteConsumer', ), )
                    ]
            )
        else :
            return SiteRolePagingList(
                pagination = openapi_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ),
                entries = [
                    openapi_client.models.site_role_entry.SiteRoleEntry(
                        entry = openapi_client.models.site_role.SiteRole(
                            site = openapi_client.models.site.Site(
                                id = '0', 
                                guid = '0', 
                                title = '0', 
                                description = '0', 
                                visibility = 'PRIVATE', 
                                preset = '0', 
                                role = 'SiteConsumer', ), 
                            id = '0', 
                            guid = '0', 
                            role = 'SiteConsumer', ), )
                    ],
        )

    def testSiteRolePagingList(self):
        """Test SiteRolePagingList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
