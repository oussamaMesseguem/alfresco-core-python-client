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
from openapi_client.models.path_info import PathInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestPathInfo(unittest.TestCase):
    """PathInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PathInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.path_info.PathInfo()  # noqa: E501
        if include_optional :
            return PathInfo(
                elements = [
                    openapi_client.models.path_element.PathElement(
                        id = '0', 
                        name = '0', 
                        node_type = '0', 
                        aspect_names = [
                            '0'
                            ], )
                    ], 
                name = '0', 
                is_complete = True
            )
        else :
            return PathInfo(
        )

    def testPathInfo(self):
        """Test PathInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()