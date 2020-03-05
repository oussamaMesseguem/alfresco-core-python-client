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
from openapi_client.models.node_entry import NodeEntry  # noqa: E501
from openapi_client.rest import ApiException

class TestNodeEntry(unittest.TestCase):
    """NodeEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NodeEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.node_entry.NodeEntry()  # noqa: E501
        if include_optional :
            return NodeEntry(
                entry = openapi_client.models.node.Node(
                    id = '0', 
                    name = 'a', 
                    node_type = '0', 
                    is_folder = True, 
                    is_file = True, 
                    is_locked = True, 
                    modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified_by_user = openapi_client.models.user_info.UserInfo(
                        display_name = '0', 
                        id = '0', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by_user = openapi_client.models.user_info.UserInfo(
                        display_name = '0', 
                        id = '0', ), 
                    parent_id = '0', 
                    is_link = True, 
                    is_favorite = True, 
                    content = openapi_client.models.content_info.ContentInfo(
                        mime_type = '0', 
                        mime_type_name = '0', 
                        size_in_bytes = 56, 
                        encoding = '0', ), 
                    aspect_names = [
                        '0'
                        ], 
                    properties = openapi_client.models.properties.properties(), 
                    allowable_operations = [
                        '0'
                        ], 
                    path = openapi_client.models.path_info.PathInfo(
                        elements = [
                            openapi_client.models.path_element.PathElement(
                                id = '0', 
                                name = '0', 
                                node_type = '0', )
                            ], 
                        name = '0', 
                        is_complete = True, ), 
                    permissions = openapi_client.models.permissions_info.PermissionsInfo(
                        is_inheritance_enabled = True, 
                        inherited = [
                            openapi_client.models.permission_element.PermissionElement(
                                authority_id = '0', 
                                name = '0', 
                                access_status = 'ALLOWED', )
                            ], 
                        locally_set = [
                            openapi_client.models.permission_element.PermissionElement(
                                authority_id = '0', 
                                name = '0', 
                                access_status = 'ALLOWED', )
                            ], 
                        settable = [
                            '0'
                            ], ), )
            )
        else :
            return NodeEntry(
                entry = openapi_client.models.node.Node(
                    id = '0', 
                    name = 'a', 
                    node_type = '0', 
                    is_folder = True, 
                    is_file = True, 
                    is_locked = True, 
                    modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified_by_user = openapi_client.models.user_info.UserInfo(
                        display_name = '0', 
                        id = '0', ), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by_user = openapi_client.models.user_info.UserInfo(
                        display_name = '0', 
                        id = '0', ), 
                    parent_id = '0', 
                    is_link = True, 
                    is_favorite = True, 
                    content = openapi_client.models.content_info.ContentInfo(
                        mime_type = '0', 
                        mime_type_name = '0', 
                        size_in_bytes = 56, 
                        encoding = '0', ), 
                    aspect_names = [
                        '0'
                        ], 
                    properties = openapi_client.models.properties.properties(), 
                    allowable_operations = [
                        '0'
                        ], 
                    path = openapi_client.models.path_info.PathInfo(
                        elements = [
                            openapi_client.models.path_element.PathElement(
                                id = '0', 
                                name = '0', 
                                node_type = '0', )
                            ], 
                        name = '0', 
                        is_complete = True, ), 
                    permissions = openapi_client.models.permissions_info.PermissionsInfo(
                        is_inheritance_enabled = True, 
                        inherited = [
                            openapi_client.models.permission_element.PermissionElement(
                                authority_id = '0', 
                                name = '0', 
                                access_status = 'ALLOWED', )
                            ], 
                        locally_set = [
                            openapi_client.models.permission_element.PermissionElement(
                                authority_id = '0', 
                                name = '0', 
                                access_status = 'ALLOWED', )
                            ], 
                        settable = [
                            '0'
                            ], ), ),
        )

    def testNodeEntry(self):
        """Test NodeEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
