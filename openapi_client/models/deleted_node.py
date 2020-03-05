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


class DeletedNode(object):
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
        'name': 'str',
        'node_type': 'str',
        'is_folder': 'bool',
        'is_file': 'bool',
        'is_locked': 'bool',
        'modified_at': 'datetime',
        'modified_by_user': 'UserInfo',
        'created_at': 'datetime',
        'created_by_user': 'UserInfo',
        'parent_id': 'str',
        'is_link': 'bool',
        'is_favorite': 'bool',
        'content': 'ContentInfo',
        'aspect_names': 'list[str]',
        'properties': 'object',
        'allowable_operations': 'list[str]',
        'path': 'PathInfo',
        'permissions': 'PermissionsInfo',
        'archived_by_user': 'UserInfo',
        'archived_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'node_type': 'nodeType',
        'is_folder': 'isFolder',
        'is_file': 'isFile',
        'is_locked': 'isLocked',
        'modified_at': 'modifiedAt',
        'modified_by_user': 'modifiedByUser',
        'created_at': 'createdAt',
        'created_by_user': 'createdByUser',
        'parent_id': 'parentId',
        'is_link': 'isLink',
        'is_favorite': 'isFavorite',
        'content': 'content',
        'aspect_names': 'aspectNames',
        'properties': 'properties',
        'allowable_operations': 'allowableOperations',
        'path': 'path',
        'permissions': 'permissions',
        'archived_by_user': 'archivedByUser',
        'archived_at': 'archivedAt'
    }

    def __init__(self, id=None, name=None, node_type=None, is_folder=None, is_file=None, is_locked=False, modified_at=None, modified_by_user=None, created_at=None, created_by_user=None, parent_id=None, is_link=None, is_favorite=None, content=None, aspect_names=None, properties=None, allowable_operations=None, path=None, permissions=None, archived_by_user=None, archived_at=None, local_vars_configuration=None):  # noqa: E501
        """DeletedNode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._node_type = None
        self._is_folder = None
        self._is_file = None
        self._is_locked = None
        self._modified_at = None
        self._modified_by_user = None
        self._created_at = None
        self._created_by_user = None
        self._parent_id = None
        self._is_link = None
        self._is_favorite = None
        self._content = None
        self._aspect_names = None
        self._properties = None
        self._allowable_operations = None
        self._path = None
        self._permissions = None
        self._archived_by_user = None
        self._archived_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.node_type = node_type
        self.is_folder = is_folder
        self.is_file = is_file
        if is_locked is not None:
            self.is_locked = is_locked
        self.modified_at = modified_at
        self.modified_by_user = modified_by_user
        self.created_at = created_at
        self.created_by_user = created_by_user
        if parent_id is not None:
            self.parent_id = parent_id
        if is_link is not None:
            self.is_link = is_link
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if content is not None:
            self.content = content
        if aspect_names is not None:
            self.aspect_names = aspect_names
        if properties is not None:
            self.properties = properties
        if allowable_operations is not None:
            self.allowable_operations = allowable_operations
        if path is not None:
            self.path = path
        if permissions is not None:
            self.permissions = permissions
        self.archived_by_user = archived_by_user
        self.archived_at = archived_at

    @property
    def id(self):
        """Gets the id of this DeletedNode.  # noqa: E501


        :return: The id of this DeletedNode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeletedNode.


        :param id: The id of this DeletedNode.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeletedNode.  # noqa: E501

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :return: The name of this DeletedNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeletedNode.

        The name must not contain spaces or the following special characters: * \" < > \\ / ? : and |. The character . must not be used at the end of the name.   # noqa: E501

        :param name: The name of this DeletedNode.  # noqa: E501
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
        """Gets the node_type of this DeletedNode.  # noqa: E501


        :return: The node_type of this DeletedNode.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this DeletedNode.


        :param node_type: The node_type of this DeletedNode.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501

        self._node_type = node_type

    @property
    def is_folder(self):
        """Gets the is_folder of this DeletedNode.  # noqa: E501


        :return: The is_folder of this DeletedNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this DeletedNode.


        :param is_folder: The is_folder of this DeletedNode.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_folder is None:  # noqa: E501
            raise ValueError("Invalid value for `is_folder`, must not be `None`")  # noqa: E501

        self._is_folder = is_folder

    @property
    def is_file(self):
        """Gets the is_file of this DeletedNode.  # noqa: E501


        :return: The is_file of this DeletedNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_file

    @is_file.setter
    def is_file(self, is_file):
        """Sets the is_file of this DeletedNode.


        :param is_file: The is_file of this DeletedNode.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_file is None:  # noqa: E501
            raise ValueError("Invalid value for `is_file`, must not be `None`")  # noqa: E501

        self._is_file = is_file

    @property
    def is_locked(self):
        """Gets the is_locked of this DeletedNode.  # noqa: E501


        :return: The is_locked of this DeletedNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this DeletedNode.


        :param is_locked: The is_locked of this DeletedNode.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def modified_at(self):
        """Gets the modified_at of this DeletedNode.  # noqa: E501


        :return: The modified_at of this DeletedNode.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this DeletedNode.


        :param modified_at: The modified_at of this DeletedNode.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def modified_by_user(self):
        """Gets the modified_by_user of this DeletedNode.  # noqa: E501


        :return: The modified_by_user of this DeletedNode.  # noqa: E501
        :rtype: UserInfo
        """
        return self._modified_by_user

    @modified_by_user.setter
    def modified_by_user(self, modified_by_user):
        """Sets the modified_by_user of this DeletedNode.


        :param modified_by_user: The modified_by_user of this DeletedNode.  # noqa: E501
        :type: UserInfo
        """
        if self.local_vars_configuration.client_side_validation and modified_by_user is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_by_user`, must not be `None`")  # noqa: E501

        self._modified_by_user = modified_by_user

    @property
    def created_at(self):
        """Gets the created_at of this DeletedNode.  # noqa: E501


        :return: The created_at of this DeletedNode.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DeletedNode.


        :param created_at: The created_at of this DeletedNode.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by_user(self):
        """Gets the created_by_user of this DeletedNode.  # noqa: E501


        :return: The created_by_user of this DeletedNode.  # noqa: E501
        :rtype: UserInfo
        """
        return self._created_by_user

    @created_by_user.setter
    def created_by_user(self, created_by_user):
        """Sets the created_by_user of this DeletedNode.


        :param created_by_user: The created_by_user of this DeletedNode.  # noqa: E501
        :type: UserInfo
        """
        if self.local_vars_configuration.client_side_validation and created_by_user is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by_user`, must not be `None`")  # noqa: E501

        self._created_by_user = created_by_user

    @property
    def parent_id(self):
        """Gets the parent_id of this DeletedNode.  # noqa: E501


        :return: The parent_id of this DeletedNode.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DeletedNode.


        :param parent_id: The parent_id of this DeletedNode.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def is_link(self):
        """Gets the is_link of this DeletedNode.  # noqa: E501


        :return: The is_link of this DeletedNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_link

    @is_link.setter
    def is_link(self, is_link):
        """Sets the is_link of this DeletedNode.


        :param is_link: The is_link of this DeletedNode.  # noqa: E501
        :type: bool
        """

        self._is_link = is_link

    @property
    def is_favorite(self):
        """Gets the is_favorite of this DeletedNode.  # noqa: E501


        :return: The is_favorite of this DeletedNode.  # noqa: E501
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this DeletedNode.


        :param is_favorite: The is_favorite of this DeletedNode.  # noqa: E501
        :type: bool
        """

        self._is_favorite = is_favorite

    @property
    def content(self):
        """Gets the content of this DeletedNode.  # noqa: E501


        :return: The content of this DeletedNode.  # noqa: E501
        :rtype: ContentInfo
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DeletedNode.


        :param content: The content of this DeletedNode.  # noqa: E501
        :type: ContentInfo
        """

        self._content = content

    @property
    def aspect_names(self):
        """Gets the aspect_names of this DeletedNode.  # noqa: E501


        :return: The aspect_names of this DeletedNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._aspect_names

    @aspect_names.setter
    def aspect_names(self, aspect_names):
        """Sets the aspect_names of this DeletedNode.


        :param aspect_names: The aspect_names of this DeletedNode.  # noqa: E501
        :type: list[str]
        """

        self._aspect_names = aspect_names

    @property
    def properties(self):
        """Gets the properties of this DeletedNode.  # noqa: E501


        :return: The properties of this DeletedNode.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DeletedNode.


        :param properties: The properties of this DeletedNode.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def allowable_operations(self):
        """Gets the allowable_operations of this DeletedNode.  # noqa: E501


        :return: The allowable_operations of this DeletedNode.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowable_operations

    @allowable_operations.setter
    def allowable_operations(self, allowable_operations):
        """Sets the allowable_operations of this DeletedNode.


        :param allowable_operations: The allowable_operations of this DeletedNode.  # noqa: E501
        :type: list[str]
        """

        self._allowable_operations = allowable_operations

    @property
    def path(self):
        """Gets the path of this DeletedNode.  # noqa: E501


        :return: The path of this DeletedNode.  # noqa: E501
        :rtype: PathInfo
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DeletedNode.


        :param path: The path of this DeletedNode.  # noqa: E501
        :type: PathInfo
        """

        self._path = path

    @property
    def permissions(self):
        """Gets the permissions of this DeletedNode.  # noqa: E501


        :return: The permissions of this DeletedNode.  # noqa: E501
        :rtype: PermissionsInfo
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this DeletedNode.


        :param permissions: The permissions of this DeletedNode.  # noqa: E501
        :type: PermissionsInfo
        """

        self._permissions = permissions

    @property
    def archived_by_user(self):
        """Gets the archived_by_user of this DeletedNode.  # noqa: E501


        :return: The archived_by_user of this DeletedNode.  # noqa: E501
        :rtype: UserInfo
        """
        return self._archived_by_user

    @archived_by_user.setter
    def archived_by_user(self, archived_by_user):
        """Sets the archived_by_user of this DeletedNode.


        :param archived_by_user: The archived_by_user of this DeletedNode.  # noqa: E501
        :type: UserInfo
        """
        if self.local_vars_configuration.client_side_validation and archived_by_user is None:  # noqa: E501
            raise ValueError("Invalid value for `archived_by_user`, must not be `None`")  # noqa: E501

        self._archived_by_user = archived_by_user

    @property
    def archived_at(self):
        """Gets the archived_at of this DeletedNode.  # noqa: E501


        :return: The archived_at of this DeletedNode.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this DeletedNode.


        :param archived_at: The archived_at of this DeletedNode.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and archived_at is None:  # noqa: E501
            raise ValueError("Invalid value for `archived_at`, must not be `None`")  # noqa: E501

        self._archived_at = archived_at

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
        if not isinstance(other, DeletedNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeletedNode):
            return True

        return self.to_dict() != other.to_dict()