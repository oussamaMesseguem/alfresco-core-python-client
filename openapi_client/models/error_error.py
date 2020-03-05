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


class ErrorError(object):
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
        'error_key': 'str',
        'status_code': 'int',
        'brief_summary': 'str',
        'stack_trace': 'str',
        'description_url': 'str',
        'log_id': 'str'
    }

    attribute_map = {
        'error_key': 'errorKey',
        'status_code': 'statusCode',
        'brief_summary': 'briefSummary',
        'stack_trace': 'stackTrace',
        'description_url': 'descriptionURL',
        'log_id': 'logId'
    }

    def __init__(self, error_key=None, status_code=None, brief_summary=None, stack_trace=None, description_url=None, log_id=None, local_vars_configuration=None):  # noqa: E501
        """ErrorError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_key = None
        self._status_code = None
        self._brief_summary = None
        self._stack_trace = None
        self._description_url = None
        self._log_id = None
        self.discriminator = None

        if error_key is not None:
            self.error_key = error_key
        self.status_code = status_code
        self.brief_summary = brief_summary
        self.stack_trace = stack_trace
        self.description_url = description_url
        if log_id is not None:
            self.log_id = log_id

    @property
    def error_key(self):
        """Gets the error_key of this ErrorError.  # noqa: E501


        :return: The error_key of this ErrorError.  # noqa: E501
        :rtype: str
        """
        return self._error_key

    @error_key.setter
    def error_key(self, error_key):
        """Sets the error_key of this ErrorError.


        :param error_key: The error_key of this ErrorError.  # noqa: E501
        :type: str
        """

        self._error_key = error_key

    @property
    def status_code(self):
        """Gets the status_code of this ErrorError.  # noqa: E501


        :return: The status_code of this ErrorError.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ErrorError.


        :param status_code: The status_code of this ErrorError.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and status_code is None:  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

    @property
    def brief_summary(self):
        """Gets the brief_summary of this ErrorError.  # noqa: E501


        :return: The brief_summary of this ErrorError.  # noqa: E501
        :rtype: str
        """
        return self._brief_summary

    @brief_summary.setter
    def brief_summary(self, brief_summary):
        """Sets the brief_summary of this ErrorError.


        :param brief_summary: The brief_summary of this ErrorError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and brief_summary is None:  # noqa: E501
            raise ValueError("Invalid value for `brief_summary`, must not be `None`")  # noqa: E501

        self._brief_summary = brief_summary

    @property
    def stack_trace(self):
        """Gets the stack_trace of this ErrorError.  # noqa: E501


        :return: The stack_trace of this ErrorError.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this ErrorError.


        :param stack_trace: The stack_trace of this ErrorError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and stack_trace is None:  # noqa: E501
            raise ValueError("Invalid value for `stack_trace`, must not be `None`")  # noqa: E501

        self._stack_trace = stack_trace

    @property
    def description_url(self):
        """Gets the description_url of this ErrorError.  # noqa: E501


        :return: The description_url of this ErrorError.  # noqa: E501
        :rtype: str
        """
        return self._description_url

    @description_url.setter
    def description_url(self, description_url):
        """Sets the description_url of this ErrorError.


        :param description_url: The description_url of this ErrorError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description_url is None:  # noqa: E501
            raise ValueError("Invalid value for `description_url`, must not be `None`")  # noqa: E501

        self._description_url = description_url

    @property
    def log_id(self):
        """Gets the log_id of this ErrorError.  # noqa: E501


        :return: The log_id of this ErrorError.  # noqa: E501
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ErrorError.


        :param log_id: The log_id of this ErrorError.  # noqa: E501
        :type: str
        """

        self._log_id = log_id

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
        if not isinstance(other, ErrorError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorError):
            return True

        return self.to_dict() != other.to_dict()