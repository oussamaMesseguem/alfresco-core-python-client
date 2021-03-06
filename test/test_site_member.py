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
from openapi_client.models.site_member import SiteMember  # noqa: E501
from openapi_client.rest import ApiException

class TestSiteMember(unittest.TestCase):
    """SiteMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SiteMember
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.site_member.SiteMember()  # noqa: E501
        if include_optional :
            return SiteMember(
                id = '0', 
                person = openapi_client.models.person.Person(
                    id = '0', 
                    first_name = '0', 
                    last_name = '0', 
                    display_name = '0', 
                    description = '0', 
                    avatar_id = '0', 
                    email = '0', 
                    skype_id = '0', 
                    google_id = '0', 
                    instant_message_id = '0', 
                    job_title = '0', 
                    location = '0', 
                    company = openapi_client.models.company.Company(
                        organization = '0', 
                        address1 = '0', 
                        address2 = '0', 
                        address3 = '0', 
                        postcode = '0', 
                        telephone = '0', 
                        fax = '0', 
                        email = '0', ), 
                    mobile = '0', 
                    telephone = '0', 
                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_status = '0', 
                    enabled = True, 
                    email_notifications_enabled = True, 
                    aspect_names = [
                        '0'
                        ], 
                    properties = openapi_client.models.properties.properties(), 
                    capabilities = openapi_client.models.capabilities.capabilities(), ), 
                role = 'SiteConsumer'
            )
        else :
            return SiteMember(
                id = '0',
                person = openapi_client.models.person.Person(
                    id = '0', 
                    first_name = '0', 
                    last_name = '0', 
                    display_name = '0', 
                    description = '0', 
                    avatar_id = '0', 
                    email = '0', 
                    skype_id = '0', 
                    google_id = '0', 
                    instant_message_id = '0', 
                    job_title = '0', 
                    location = '0', 
                    company = openapi_client.models.company.Company(
                        organization = '0', 
                        address1 = '0', 
                        address2 = '0', 
                        address3 = '0', 
                        postcode = '0', 
                        telephone = '0', 
                        fax = '0', 
                        email = '0', ), 
                    mobile = '0', 
                    telephone = '0', 
                    status_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    user_status = '0', 
                    enabled = True, 
                    email_notifications_enabled = True, 
                    aspect_names = [
                        '0'
                        ], 
                    properties = openapi_client.models.properties.properties(), 
                    capabilities = openapi_client.models.capabilities.capabilities(), ),
                role = 'SiteConsumer',
        )

    def testSiteMember(self):
        """Test SiteMember"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
