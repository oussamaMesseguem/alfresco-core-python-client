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
from openapi_client.api.actions_api import ActionsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestActionsApi(unittest.TestCase):
    """ActionsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.actions_api.ActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_action_details(self):
        """Test case for action_details

        Retrieve the details of an action definition  # noqa: E501
        """
        pass

    def test_action_exec(self):
        """Test case for action_exec

        Execute an action  # noqa: E501
        """
        pass

    def test_list_actions(self):
        """Test case for list_actions

        Retrieve list of available actions  # noqa: E501
        """
        pass

    def test_node_actions(self):
        """Test case for node_actions

        Retrieve actions for a node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()