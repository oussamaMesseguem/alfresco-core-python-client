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
from openapi_client.models.content_info import ContentInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestContentInfo(unittest.TestCase):
    """ContentInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ContentInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.content_info.ContentInfo()  # noqa: E501
        if include_optional :
            return ContentInfo(
                mime_type = '0', 
                mime_type_name = '0', 
                size_in_bytes = 56, 
                encoding = '0'
            )
        else :
            return ContentInfo(
                mime_type = '0',
                mime_type_name = '0',
                size_in_bytes = 56,
        )

    def testContentInfo(self):
        """Test ContentInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
