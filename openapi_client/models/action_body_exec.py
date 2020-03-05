# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ActionBodyExec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'action_definition_id': 'str',
        'target_id': 'str',
        'params': 'object'
    }

    attribute_map = {
        'action_definition_id': 'actionDefinitionId',
        'target_id': 'targetId',
        'params': 'params'
    }

    def __init__(self, action_definition_id=None, target_id=None, params=None, local_vars_configuration=None):  # noqa: E501
        """ActionBodyExec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_definition_id = None
        self._target_id = None
        self._params = None
        self.discriminator = None

        self.action_definition_id = action_definition_id
        if target_id is not None:
            self.target_id = target_id
        if params is not None:
            self.params = params

    @property
    def action_definition_id(self):
        """Gets the action_definition_id of this ActionBodyExec.  # noqa: E501


        :return: The action_definition_id of this ActionBodyExec.  # noqa: E501
        :rtype: str
        """
        return self._action_definition_id

    @action_definition_id.setter
    def action_definition_id(self, action_definition_id):
        """Sets the action_definition_id of this ActionBodyExec.


        :param action_definition_id: The action_definition_id of this ActionBodyExec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_definition_id is None:  # noqa: E501
            raise ValueError("Invalid value for `action_definition_id`, must not be `None`")  # noqa: E501

        self._action_definition_id = action_definition_id

    @property
    def target_id(self):
        """Gets the target_id of this ActionBodyExec.  # noqa: E501

        The entity upon which to execute the action, typically a node ID or similar.  # noqa: E501

        :return: The target_id of this ActionBodyExec.  # noqa: E501
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this ActionBodyExec.

        The entity upon which to execute the action, typically a node ID or similar.  # noqa: E501

        :param target_id: The target_id of this ActionBodyExec.  # noqa: E501
        :type: str
        """

        self._target_id = target_id

    @property
    def params(self):
        """Gets the params of this ActionBodyExec.  # noqa: E501


        :return: The params of this ActionBodyExec.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ActionBodyExec.


        :param params: The params of this ActionBodyExec.  # noqa: E501
        :type: object
        """

        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionBodyExec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionBodyExec):
            return True

        return self.to_dict() != other.to_dict()