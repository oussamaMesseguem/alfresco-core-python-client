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


class NodeBodyCreate(object):
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
        'name': 'str',
        'node_type': 'str',
        'aspect_names': 'list[str]',
        'properties': 'object',
        'permissions': 'PermissionsBody',
        'relative_path': 'str',
        'association': 'NodeBodyCreateAssociation',
        'secondary_children': 'list[ChildAssociationBody]',
        'targets': 'list[AssociationBody]'
    }

    attribute_map = {
        'name': 'name',
        'node_type': 'nodeType',
        'aspect_names': 'aspectNames',
        'properties': 'properties',
        'permissions': 'permissions',
        'relative_path': 'relativePath',
        'association': 'association',
        'secondary_children': 'secondaryChildren',
        'targets': 'targets'
    }

    def __init__(self, name=None, node_type=None, aspect_names=None, properties=None, permissions=None, relative_path=None, association=None, secondary_children=None, targets=None, local_vars_configuration=None):  # noqa: E501
        """NodeBodyCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._node_type = None
        self._aspect_names = None
        self._properties = None
        self._permissions = None
        self._relative_path = None
        self._association = None
        self._secondary_children = None
        self._targets = None
        self.discriminator = None

        self.name = name
        self.node_type = node_type
        if aspect_names is not None:
            self.aspect_names = aspect_names
        if properties is not None:
            self.properties = properties
        if permissions is not None:
            self.permissions = permissions
        if relative_path is not None:
            self.relative_path = relative_path
        if association is not None:
            self.association = association
        if secondary_children is not None:
            self.secondary_children = secondary_children
        if targets is not None:
            self.targets = targets

    @property
    def name(self):
        """Gets the name of this NodeBodyCreate.  # noqa: E501

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :return: The name of this NodeBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeBodyCreate.

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :param name: The name of this NodeBodyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^(?!(.*[\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^(?!(.*[\"\*\\\>\<\?\/\:\|]+.*)|(.*[\.]?.*[\.]+$)|(.*[ ]+$))/`")  # noqa: E501

        self._name = name

    @property
    def node_type(self):
        """Gets the node_type of this NodeBodyCreate.  # noqa: E501


        :return: The node_type of this NodeBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this NodeBodyCreate.


        :param node_type: The node_type of this NodeBodyCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501

        self._node_type = node_type

    @property
    def aspect_names(self):
        """Gets the aspect_names of this NodeBodyCreate.  # noqa: E501


        :return: The aspect_names of this NodeBodyCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._aspect_names

    @aspect_names.setter
    def aspect_names(self, aspect_names):
        """Sets the aspect_names of this NodeBodyCreate.


        :param aspect_names: The aspect_names of this NodeBodyCreate.  # noqa: E501
        :type: list[str]
        """

        self._aspect_names = aspect_names

    @property
    def properties(self):
        """Gets the properties of this NodeBodyCreate.  # noqa: E501


        :return: The properties of this NodeBodyCreate.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NodeBodyCreate.


        :param properties: The properties of this NodeBodyCreate.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def permissions(self):
        """Gets the permissions of this NodeBodyCreate.  # noqa: E501


        :return: The permissions of this NodeBodyCreate.  # noqa: E501
        :rtype: PermissionsBody
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this NodeBodyCreate.


        :param permissions: The permissions of this NodeBodyCreate.  # noqa: E501
        :type: PermissionsBody
        """

        self._permissions = permissions

    @property
    def relative_path(self):
        """Gets the relative_path of this NodeBodyCreate.  # noqa: E501


        :return: The relative_path of this NodeBodyCreate.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this NodeBodyCreate.


        :param relative_path: The relative_path of this NodeBodyCreate.  # noqa: E501
        :type: str
        """

        self._relative_path = relative_path

    @property
    def association(self):
        """Gets the association of this NodeBodyCreate.  # noqa: E501


        :return: The association of this NodeBodyCreate.  # noqa: E501
        :rtype: NodeBodyCreateAssociation
        """
        return self._association

    @association.setter
    def association(self, association):
        """Sets the association of this NodeBodyCreate.


        :param association: The association of this NodeBodyCreate.  # noqa: E501
        :type: NodeBodyCreateAssociation
        """

        self._association = association

    @property
    def secondary_children(self):
        """Gets the secondary_children of this NodeBodyCreate.  # noqa: E501


        :return: The secondary_children of this NodeBodyCreate.  # noqa: E501
        :rtype: list[ChildAssociationBody]
        """
        return self._secondary_children

    @secondary_children.setter
    def secondary_children(self, secondary_children):
        """Sets the secondary_children of this NodeBodyCreate.


        :param secondary_children: The secondary_children of this NodeBodyCreate.  # noqa: E501
        :type: list[ChildAssociationBody]
        """

        self._secondary_children = secondary_children

    @property
    def targets(self):
        """Gets the targets of this NodeBodyCreate.  # noqa: E501


        :return: The targets of this NodeBodyCreate.  # noqa: E501
        :rtype: list[AssociationBody]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this NodeBodyCreate.


        :param targets: The targets of this NodeBodyCreate.  # noqa: E501
        :type: list[AssociationBody]
        """

        self._targets = targets

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
        if not isinstance(other, NodeBodyCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeBodyCreate):
            return True

        return self.to_dict() != other.to_dict()
