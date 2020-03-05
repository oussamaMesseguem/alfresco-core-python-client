# openapi_client.VersionsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version**](VersionsApi.md#delete_version) | **DELETE** /nodes/{nodeId}/versions/{versionId} | Delete a version
[**get_version**](VersionsApi.md#get_version) | **GET** /nodes/{nodeId}/versions/{versionId} | Get version information
[**get_version_content**](VersionsApi.md#get_version_content) | **GET** /nodes/{nodeId}/versions/{versionId}/content | Get version content
[**list_version_history**](VersionsApi.md#list_version_history) | **GET** /nodes/{nodeId}/versions | List version history
[**revert_version**](VersionsApi.md#revert_version) | **POST** /nodes/{nodeId}/versions/{versionId}/revert | Revert a version


# **delete_version**
> delete_version(node_id, version_id)

Delete a version

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Delete the version identified by **versionId** and **nodeId*.  If the version is successfully deleted then the content and metadata for that versioned node will be deleted and will no longer appear in the version history. This operation cannot be undone.  If the most recent version is deleted the live node will revert to the next most recent version.  We currently do not allow the last version to be deleted. If you wish to clear the history then you can remove the \"cm:versionable\" aspect (via update node) which will also disable versioning. In this case, you can re-enable versioning by adding back the \"cm:versionable\" aspect or using the version  params (majorVersion and comment) on a subsequent file content update. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
configuration.host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.VersionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.

    try:
        # Delete a version
        api_instance.delete_version(node_id, version_id)
    except ApiException as e:
        print("Exception when calling VersionsApi->delete_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or exists but does not identify a file, or **versionId** is invalid       |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to delete the versioned node |  -  |
**404** | **nodeId** or **versionId** does not exist  |  -  |
**422** | Cannot delete the last remaining version |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionEntry get_version(node_id, version_id)

Get version information

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version information for **versionId** of file node **nodeId**. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
configuration.host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.VersionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.

    try:
        # Get version information
        api_response = api_instance.get_version(node_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 

### Return type

[**VersionEntry**](VersionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or it exists but does not identify a file, or **versionId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** or **versionId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_content**
> file get_version_content(node_id, version_id, attachment=attachment, if_modified_since=if_modified_since, range=range)

Get version content

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version content for **versionId** of file node **nodeId**. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
configuration.host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.VersionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
attachment = True # bool | **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  (optional) (default to True)
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, `Wed, 09 Mar 2016 16:56:34 GMT`.  (optional)
range = 'range_example' # str | The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes=1-10.  (optional)

    try:
        # Get version content
        api_response = api_instance.get_version_content(node_id, version_id, attachment=attachment, if_modified_since=if_modified_since, range=range)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsApi->get_version_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **attachment** | **bool**| **true** enables a web browser to download the file as an attachment. **false** means a web browser may preview the file in a new tab or window, but not download the file.  You can only set this parameter to **false** if the content type of the file is in the supported list; for example, certain image files and PDF files.  If the content type is not supported for preview, then a value of **false**  is ignored, and the attachment will be returned in the response.  | [optional] [default to True]
 **if_modified_since** | **datetime**| Only returns the content if it has been modified since the date provided. Use the date format defined by HTTP. For example, &#x60;Wed, 09 Mar 2016 16:56:34 GMT&#x60;.  | [optional] 
 **range** | **str**| The Range header indicates the part of a document that the server should return. Single part request supported, for example: bytes&#x3D;1-10.  | [optional] 

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**206** | Partial Content |  -  |
**304** | Content has not been modified since the date provided in the If-Modified-Since header |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or is not a file, or **versionId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | **nodeId** or **versionId** does not exist  |  -  |
**416** | Range Not Satisfiable |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_history**
> VersionPaging list_version_history(node_id, include=include, fields=fields, skip_count=skip_count, max_items=max_items)

List version history

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Gets the version history as an ordered list of versions for the specified **nodeId**.  The list is ordered in descending modified order. So the most recent version is first and  the original version is last in the list.  

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
configuration.host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.VersionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
include = ['include_example'] # list[str] | Returns additional information about the version node. The following optional fields can be requested: * properties * aspectNames  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list.  If not supplied then the default value is 100.  (optional) (default to 100)

    try:
        # List version history
        api_response = api_instance.list_version_history(node_id, include=include, fields=fields, skip_count=skip_count, max_items=max_items)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsApi->list_version_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the version node. The following optional fields can be requested: * properties * aspectNames  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list.  If not supplied then the default value is 100.  | [optional] [default to 100]

### Return type

[**VersionPaging**](VersionPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format              |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission for **nodeId** |  -  |
**404** | Target **nodeId** does not exist |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_version**
> VersionEntry revert_version(node_id, version_id, revert_body, fields=fields)

Revert a version

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.  Attempts to revert the version identified by **versionId** and **nodeId** to the live node.  If the node is successfully reverted then the content and metadata for that versioned node will be promoted to the live node and a new version will appear in the version history. 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
configuration.host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.VersionsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
version_id = 'version_id_example' # str | The identifier of a version, ie. version label, within the version history of a node.
revert_body = openapi_client.RevertBody() # RevertBody | Optionally, specify a version comment and whether this should be a major version, or not.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Revert a version
        api_response = api_instance.revert_version(node_id, version_id, revert_body, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionsApi->revert_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **version_id** | **str**| The identifier of a version, ie. version label, within the version history of a node. | 
 **revert_body** | [**RevertBody**](RevertBody.md)| Optionally, specify a version comment and whether this should be a major version, or not. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**VersionEntry**](VersionEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **nodeId** is not a valid format, or it exists  but does not identify a file, or **versionId** is invalid, or **revertBody** invalid            |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to revert the versioned node |  -  |
**404** | **nodeId** or **versionId** does not exist  |  -  |
**422** | Model integrity exception trying to revert the node |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

