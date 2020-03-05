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


class SiteBodyUpdate(object):
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
        'title': 'str',
        'description': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'visibility': 'visibility'
    }

    def __init__(self, title=None, description=None, visibility=None, local_vars_configuration=None):  # noqa: E501
        """SiteBodyUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._description = None
        self._visibility = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if visibility is not None:
            self.visibility = visibility

    @property
    def title(self):
        """Gets the title of this SiteBodyUpdate.  # noqa: E501


        :return: The title of this SiteBodyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SiteBodyUpdate.


        :param title: The title of this SiteBodyUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this SiteBodyUpdate.  # noqa: E501


        :return: The description of this SiteBodyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SiteBodyUpdate.


        :param description: The description of this SiteBodyUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def visibility(self):
        """Gets the visibility of this SiteBodyUpdate.  # noqa: E501


        :return: The visibility of this SiteBodyUpdate.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this SiteBodyUpdate.


        :param visibility: The visibility of this SiteBodyUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["PRIVATE", "MODERATED", "PUBLIC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

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
        if not isinstance(other, SiteBodyUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SiteBodyUpdate):
            return True

        return self.to_dict() != other.to_dict()