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
from openapi_client.models.child_association_body import ChildAssociationBody  # noqa: E501
from openapi_client.rest import ApiException

class TestChildAssociationBody(unittest.TestCase):
    """ChildAssociationBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChildAssociationBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.child_association_body.ChildAssociationBody()  # noqa: E501
        if include_optional :
            return ChildAssociationBody(
                child_id = '0', 
                assoc_type = '0'
            )
        else :
            return ChildAssociationBody(
                child_id = '0',
                assoc_type = '0',
        )

    def testChildAssociationBody(self):
        """Test ChildAssociationBody"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
