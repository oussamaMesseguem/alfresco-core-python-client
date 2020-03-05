# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.sites_api import SitesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.sites_api.SitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_approve_site_membership_request(self):
        """Test case for approve_site_membership_request

        Approve a site membership request  # noqa: E501
        """
        pass

    def test_create_site(self):
        """Test case for create_site

        Create a site  # noqa: E501
        """
        pass

    def test_create_site_membership(self):
        """Test case for create_site_membership

        Create a site membership  # noqa: E501
        """
        pass

    def test_create_site_membership_request_for_person(self):
        """Test case for create_site_membership_request_for_person

        Create a site membership request  # noqa: E501
        """
        pass

    def test_delete_site(self):
        """Test case for delete_site

        Delete a site  # noqa: E501
        """
        pass

    def test_delete_site_membership(self):
        """Test case for delete_site_membership

        Delete a site membership  # noqa: E501
        """
        pass

    def test_delete_site_membership_for_person(self):
        """Test case for delete_site_membership_for_person

        Delete a site membership  # noqa: E501
        """
        pass

    def test_delete_site_membership_request_for_person(self):
        """Test case for delete_site_membership_request_for_person

        Delete a site membership request  # noqa: E501
        """
        pass

    def test_get_site(self):
        """Test case for get_site

        Get a site  # noqa: E501
        """
        pass

    def test_get_site_container(self):
        """Test case for get_site_container

        Get a site container  # noqa: E501
        """
        pass

    def test_get_site_membership(self):
        """Test case for get_site_membership

        Get a site membership  # noqa: E501
        """
        pass

    def test_get_site_membership_for_person(self):
        """Test case for get_site_membership_for_person

        Get a site membership  # noqa: E501
        """
        pass

    def test_get_site_membership_request_for_person(self):
        """Test case for get_site_membership_request_for_person

        Get a site membership request  # noqa: E501
        """
        pass

    def test_get_site_membership_requests(self):
        """Test case for get_site_membership_requests

        Get site membership requests  # noqa: E501
        """
        pass

    def test_list_site_containers(self):
        """Test case for list_site_containers

        List site containers  # noqa: E501
        """
        pass

    def test_list_site_membership_requests_for_person(self):
        """Test case for list_site_membership_requests_for_person

        List site membership requests  # noqa: E501
        """
        pass

    def test_list_site_memberships(self):
        """Test case for list_site_memberships

        List site memberships  # noqa: E501
        """
        pass

    def test_list_site_memberships_for_person(self):
        """Test case for list_site_memberships_for_person

        List site memberships  # noqa: E501
        """
        pass

    def test_list_sites(self):
        """Test case for list_sites

        List sites  # noqa: E501
        """
        pass

    def test_reject_site_membership_request(self):
        """Test case for reject_site_membership_request

        Reject a site membership request  # noqa: E501
        """
        pass

    def test_update_site(self):
        """Test case for update_site

        Update a site  # noqa: E501
        """
        pass

    def test_update_site_membership(self):
        """Test case for update_site_membership

        Update a site membership  # noqa: E501
        """
        pass

    def test_update_site_membership_request_for_person(self):
        """Test case for update_site_membership_request_for_person

        Update a site membership request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()