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
from openapi_client.models.version import Version  # noqa: E501
from openapi_client.rest import ApiException

class TestVersion(unittest.TestCase):
    """Version unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Version
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.version.Version()  # noqa: E501
        if include_optional :
            return Version(
                id = '0', 
                version_comment = '0', 
                name = 'a', 
                node_type = '0', 
                is_folder = True, 
                is_file = True, 
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by_user = openapi_client.models.user_info.UserInfo(
                    display_name = '0', 
                    id = '0', ), 
                content = openapi_client.models.content_info.ContentInfo(
                    mime_type = '0', 
                    mime_type_name = '0', 
                    size_in_bytes = 56, 
                    encoding = '0', ), 
                aspect_names = [
                    '0'
                    ], 
                properties = openapi_client.models.properties.properties()
            )
        else :
            return Version(
                id = '0',
                name = 'a',
                node_type = '0',
                is_folder = True,
                is_file = True,
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_by_user = openapi_client.models.user_info.UserInfo(
                    display_name = '0', 
                    id = '0', ),
        )

    def testVersion(self):
        """Test Version"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
