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
from openapi_client.models.deleted_nodes_paging_list import DeletedNodesPagingList  # noqa: E501
from openapi_client.rest import ApiException

class TestDeletedNodesPagingList(unittest.TestCase):
    """DeletedNodesPagingList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeletedNodesPagingList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.deleted_nodes_paging_list.DeletedNodesPagingList()  # noqa: E501
        if include_optional :
            return DeletedNodesPagingList(
                pagination = openapi_client.models.pagination.Pagination(
                    count = 56, 
                    has_more_items = True, 
                    total_items = 56, 
                    skip_count = 56, 
                    max_items = 56, ), 
                entries = [
                    openapi_client.models.deleted_node_entry.DeletedNodeEntry(
                        entry = null, )
                    ]
            )
        else :
            return DeletedNodesPagingList(
        )

    def testDeletedNodesPagingList(self):
        """Test DeletedNodesPagingList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
