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


class SiteMembershipRequestWithPerson(object):
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
        'id': 'str',
        'created_at': 'datetime',
        'site': 'Site',
        'person': 'Person',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'site': 'site',
        'person': 'person',
        'message': 'message'
    }

    def __init__(self, id=None, created_at=None, site=None, person=None, message=None, local_vars_configuration=None):  # noqa: E501
        """SiteMembershipRequestWithPerson - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._site = None
        self._person = None
        self._message = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.site = site
        self.person = person
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this SiteMembershipRequestWithPerson.  # noqa: E501


        :return: The id of this SiteMembershipRequestWithPerson.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteMembershipRequestWithPerson.


        :param id: The id of this SiteMembershipRequestWithPerson.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this SiteMembershipRequestWithPerson.  # noqa: E501


        :return: The created_at of this SiteMembershipRequestWithPerson.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SiteMembershipRequestWithPerson.


        :param created_at: The created_at of this SiteMembershipRequestWithPerson.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def site(self):
        """Gets the site of this SiteMembershipRequestWithPerson.  # noqa: E501


        :return: The site of this SiteMembershipRequestWithPerson.  # noqa: E501
        :rtype: Site
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this SiteMembershipRequestWithPerson.


        :param site: The site of this SiteMembershipRequestWithPerson.  # noqa: E501
        :type: Site
        """
        if self.local_vars_configuration.client_side_validation and site is None:  # noqa: E501
            raise ValueError("Invalid value for `site`, must not be `None`")  # noqa: E501

        self._site = site

    @property
    def person(self):
        """Gets the person of this SiteMembershipRequestWithPerson.  # noqa: E501


        :return: The person of this SiteMembershipRequestWithPerson.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this SiteMembershipRequestWithPerson.


        :param person: The person of this SiteMembershipRequestWithPerson.  # noqa: E501
        :type: Person
        """
        if self.local_vars_configuration.client_side_validation and person is None:  # noqa: E501
            raise ValueError("Invalid value for `person`, must not be `None`")  # noqa: E501

        self._person = person

    @property
    def message(self):
        """Gets the message of this SiteMembershipRequestWithPerson.  # noqa: E501


        :return: The message of this SiteMembershipRequestWithPerson.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SiteMembershipRequestWithPerson.


        :param message: The message of this SiteMembershipRequestWithPerson.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, SiteMembershipRequestWithPerson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SiteMembershipRequestWithPerson):
            return True

        return self.to_dict() != other.to_dict()
