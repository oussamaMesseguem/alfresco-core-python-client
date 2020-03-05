# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class QueriesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_nodes(self, term, **kwargs):  # noqa: E501
        """Find nodes  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of nodes that match the given search criteria.  The search term is used to look for nodes that match against name, title, description, full text content or tags.  The search term: - must contain a minimum of 3 alphanumeric characters - allows \"quoted term\" - can optionally use '*' for wildcard matching  By default, file and folder types will be searched unless a specific type is provided as a query parameter.  By default, the search will be across the repository unless a specific root node id is provided to start the search from.  You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * name * modifiedAt * createdAt   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_nodes(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for. (required)
        :param str root_node_id: The id of the node to start the search from.  Supports the aliases -my-, -root- and -shared-. 
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param str node_type: Restrict the returned results to only those of the given node type and its sub-types 
        :param list[str] include: Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * isLink * isFavorite * isLocked * path * properties 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NodePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_nodes_with_http_info(term, **kwargs)  # noqa: E501

    def find_nodes_with_http_info(self, term, **kwargs):  # noqa: E501
        """Find nodes  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of nodes that match the given search criteria.  The search term is used to look for nodes that match against name, title, description, full text content or tags.  The search term: - must contain a minimum of 3 alphanumeric characters - allows \"quoted term\" - can optionally use '*' for wildcard matching  By default, file and folder types will be searched unless a specific type is provided as a query parameter.  By default, the search will be across the repository unless a specific root node id is provided to start the search from.  You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * name * modifiedAt * createdAt   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_nodes_with_http_info(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for. (required)
        :param str root_node_id: The id of the node to start the search from.  Supports the aliases -my-, -root- and -shared-. 
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param str node_type: Restrict the returned results to only those of the given node type and its sub-types 
        :param list[str] include: Returns additional information about the node. The following optional fields can be requested: * allowableOperations * aspectNames * isLink * isFavorite * isLocked * path * properties 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NodePaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['term', 'root_node_id', 'skip_count', 'max_items', 'node_type', 'include', 'order_by', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_nodes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'term' is set
        if self.api_client.client_side_validation and ('term' not in local_var_params or  # noqa: E501
                                                        local_var_params['term'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `term` when calling `find_nodes`")  # noqa: E501

        if self.api_client.client_side_validation and 'skip_count' in local_var_params and local_var_params['skip_count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip_count` when calling `find_nodes`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `find_nodes`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'term' in local_var_params and local_var_params['term'] is not None:  # noqa: E501
            query_params.append(('term', local_var_params['term']))  # noqa: E501
        if 'root_node_id' in local_var_params and local_var_params['root_node_id'] is not None:  # noqa: E501
            query_params.append(('rootNodeId', local_var_params['root_node_id']))  # noqa: E501
        if 'skip_count' in local_var_params and local_var_params['skip_count'] is not None:  # noqa: E501
            query_params.append(('skipCount', local_var_params['skip_count']))  # noqa: E501
        if 'max_items' in local_var_params and local_var_params['max_items'] is not None:  # noqa: E501
            query_params.append(('maxItems', local_var_params['max_items']))  # noqa: E501
        if 'node_type' in local_var_params and local_var_params['node_type'] is not None:  # noqa: E501
            query_params.append(('nodeType', local_var_params['node_type']))  # noqa: E501
        if 'include' in local_var_params and local_var_params['include'] is not None:  # noqa: E501
            query_params.append(('include', local_var_params['include']))  # noqa: E501
            collection_formats['include'] = 'csv'  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
            collection_formats['orderBy'] = 'csv'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/queries/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodePaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_people(self, term, **kwargs):  # noqa: E501
        """Find people  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of people that match the given search criteria.  The search term is used to look for matches against person id, firstname and lastname.  The search term: - must contain a minimum of 2 alphanumeric characters - can optionally use '*' for wildcard matching within the term  You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * id * firstName * lastName          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_people(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for.  (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PersonPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_people_with_http_info(term, **kwargs)  # noqa: E501

    def find_people_with_http_info(self, term, **kwargs):  # noqa: E501
        """Find people  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of people that match the given search criteria.  The search term is used to look for matches against person id, firstname and lastname.  The search term: - must contain a minimum of 2 alphanumeric characters - can optionally use '*' for wildcard matching within the term  You can sort the result list using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * id * firstName * lastName          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_people_with_http_info(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for.  (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PersonPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['term', 'skip_count', 'max_items', 'fields', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_people" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'term' is set
        if self.api_client.client_side_validation and ('term' not in local_var_params or  # noqa: E501
                                                        local_var_params['term'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `term` when calling `find_people`")  # noqa: E501

        if self.api_client.client_side_validation and 'skip_count' in local_var_params and local_var_params['skip_count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip_count` when calling `find_people`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `find_people`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'term' in local_var_params and local_var_params['term'] is not None:  # noqa: E501
            query_params.append(('term', local_var_params['term']))  # noqa: E501
        if 'skip_count' in local_var_params and local_var_params['skip_count'] is not None:  # noqa: E501
            query_params.append(('skipCount', local_var_params['skip_count']))  # noqa: E501
        if 'max_items' in local_var_params and local_var_params['max_items'] is not None:  # noqa: E501
            query_params.append(('maxItems', local_var_params['max_items']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
            collection_formats['orderBy'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/queries/people', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PersonPaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_sites(self, term, **kwargs):  # noqa: E501
        """Find sites  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of sites that match the given search criteria.  The search term is used to look for sites that match against site id, title or description.  The search term: - must contain a minimum of 2 alphanumeric characters - can optionally use '*' for wildcard matching within the term  The default sort order for the returned list is for sites to be sorted by ascending id.  You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * id * title * description   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_sites(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for. (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SitePaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_sites_with_http_info(term, **kwargs)  # noqa: E501

    def find_sites_with_http_info(self, term, **kwargs):  # noqa: E501
        """Find sites  # noqa: E501

        **Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets a list of sites that match the given search criteria.  The search term is used to look for sites that match against site id, title or description.  The search term: - must contain a minimum of 2 alphanumeric characters - can optionally use '*' for wildcard matching within the term  The default sort order for the returned list is for sites to be sorted by ascending id.  You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter: * id * title * description   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_sites_with_http_info(term, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str term: The term to search for. (required)
        :param int skip_count: The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0. 
        :param int max_items: The maximum number of items to return in the list.  If not supplied then the default value is 100. 
        :param list[str] order_by: A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field. 
        :param list[str] fields: A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SitePaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['term', 'skip_count', 'max_items', 'order_by', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_sites" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'term' is set
        if self.api_client.client_side_validation and ('term' not in local_var_params or  # noqa: E501
                                                        local_var_params['term'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `term` when calling `find_sites`")  # noqa: E501

        if self.api_client.client_side_validation and 'skip_count' in local_var_params and local_var_params['skip_count'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `skip_count` when calling `find_sites`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_items' in local_var_params and local_var_params['max_items'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_items` when calling `find_sites`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'term' in local_var_params and local_var_params['term'] is not None:  # noqa: E501
            query_params.append(('term', local_var_params['term']))  # noqa: E501
        if 'skip_count' in local_var_params and local_var_params['skip_count'] is not None:  # noqa: E501
            query_params.append(('skipCount', local_var_params['skip_count']))  # noqa: E501
        if 'max_items' in local_var_params and local_var_params['max_items'] is not None:  # noqa: E501
            query_params.append(('maxItems', local_var_params['max_items']))  # noqa: E501
        if 'order_by' in local_var_params and local_var_params['order_by'] is not None:  # noqa: E501
            query_params.append(('orderBy', local_var_params['order_by']))  # noqa: E501
            collection_formats['orderBy'] = 'csv'  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/queries/sites', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SitePaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
