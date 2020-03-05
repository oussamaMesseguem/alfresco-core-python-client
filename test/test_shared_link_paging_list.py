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
from openapi_client.models.shared_link_paging_list import SharedLinkPagingList  # noqa: E501
from openapi_client.rest import ApiException

class TestSharedLinkPagingList(unittest.TestCase):
    """SharedLinkPagingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedLinkPagingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.shared_link_paging_list.SharedLinkPagingList()  # noqa: E501
        if include_optional :
            return SharedLinkPagingList(
                pagination = openapi_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ), 
                entries = [
                    openapi_client.models.shared_link_entry.SharedLinkEntry(
                        entry = openapi_client.models.shared_link.SharedLink(
                            id = '0', 
                            expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            node_id = '0', 
                            name = 'a', 
                            title = '0', 
                            description = '0', 
                            modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            modified_by_user = openapi_client.models.user_info.UserInfo(
                                display_name = '0', 
                                id = '0', ), 
                            shared_by_user = openapi_client.models.user_info.UserInfo(
                                display_name = '0', 
                                id = '0', ), 
                            content = openapi_client.models.content_info.ContentInfo(
                                mime_type = '0', 
                                mime_type_name = '0', 
                                size_in_bytes = 56, 
                                encoding = '0', ), 
                            allowable_operations = [
                                '0'
                                ], 
                            allowable_operations_on_target = [
                                '0'
                                ], 
                            is_favorite = True, 
                            properties = openapi_client.models.properties.properties(), 
                            aspect_names = [
                                '0'
                                ], ), )
                    ]
            )
        else :
            return SharedLinkPagingList(
                pagination = openapi_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ),
                entries = [
                    openapi_client.models.shared_link_entry.SharedLinkEntry(
                        entry = openapi_client.models.shared_link.SharedLink(
                            id = '0', 
                            expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            node_id = '0', 
                            name = 'a', 
                            title = '0', 
                            description = '0', 
                            modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            modified_by_user = openapi_client.models.user_info.UserInfo(
                                display_name = '0', 
                                id = '0', ), 
                            shared_by_user = openapi_client.models.user_info.UserInfo(
                                display_name = '0', 
                                id = '0', ), 
                            content = openapi_client.models.content_info.ContentInfo(
                                mime_type = '0', 
                                mime_type_name = '0', 
                                size_in_bytes = 56, 
                                encoding = '0', ), 
                            allowable_operations = [
                                '0'
                                ], 
                            allowable_operations_on_target = [
                                '0'
                                ], 
                            is_favorite = True, 
                            properties = openapi_client.models.properties.properties(), 
                            aspect_names = [
                                '0'
                                ], ), )
                    ],
        )

    def testSharedLinkPagingList(self):
        """Test SharedLinkPagingList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
