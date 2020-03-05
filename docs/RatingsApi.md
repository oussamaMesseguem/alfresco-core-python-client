# openapi_client.RatingsApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rating**](RatingsApi.md#create_rating) | **POST** /nodes/{nodeId}/ratings | Create a rating
[**delete_rating**](RatingsApi.md#delete_rating) | **DELETE** /nodes/{nodeId}/ratings/{ratingId} | Delete a rating
[**get_rating**](RatingsApi.md#get_rating) | **GET** /nodes/{nodeId}/ratings/{ratingId} | Get a rating
[**list_ratings**](RatingsApi.md#list_ratings) | **GET** /nodes/{nodeId}/ratings | List ratings


# **create_rating**
> RatingEntry create_rating(node_id, rating_body_create, fields=fields)

Create a rating

Create a rating for the node with identifier **nodeId**

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
    api_instance = openapi_client.RatingsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
rating_body_create = openapi_client.RatingBody() # RatingBody | For \"myRating\" the type is specific to the rating scheme, boolean for the likes and an integer for the fiveStar.  For example, to \"like\" a file the following body would be used:  ```JSON   {     \"id\": \"likes\",     \"myRating\": true   } ``` 
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a rating
        api_response = api_instance.create_rating(node_id, rating_body_create, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RatingsApi->create_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rating_body_create** | [**RatingBody**](RatingBody.md)| For \&quot;myRating\&quot; the type is specific to the rating scheme, boolean for the likes and an integer for the fiveStar.  For example, to \&quot;like\&quot; a file the following body would be used:  &#x60;&#x60;&#x60;JSON   {     \&quot;id\&quot;: \&quot;likes\&quot;,     \&quot;myRating\&quot;: true   } &#x60;&#x60;&#x60;  | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**RatingEntry**](RatingEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: **ratingBodyCreate** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **nodeId** does not exist  |  -  |
**405** | Cannot rate a node of this type |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rating**
> delete_rating(node_id, rating_id)

Delete a rating

Deletes rating **ratingId** from node **nodeId**.

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
    api_instance = openapi_client.RatingsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
rating_id = 'rating_id_example' # str | The identifier of a rating.

    try:
        # Delete a rating
        api_instance.delete_rating(node_id, rating_id)
    except ApiException as e:
        print("Exception when calling RatingsApi->delete_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rating_id** | **str**| The identifier of a rating. | 

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
**400** | Invalid parameter: unknown rating scheme specified  |  -  |
**401** | Authentication failed |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating**
> RatingEntry get_rating(node_id, rating_id, fields=fields)

Get a rating

Get the specific rating **ratingId** on node **nodeId**.

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
    api_instance = openapi_client.RatingsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
rating_id = 'rating_id_example' # str | The identifier of a rating.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a rating
        api_response = api_instance.get_rating(node_id, rating_id, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RatingsApi->get_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **rating_id** | **str**| The identifier of a rating. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**RatingEntry**](RatingEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: unknown rating scheme specified  |  -  |
**401** | Authentication failed |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ratings**
> RatingPaging list_ratings(node_id, skip_count=skip_count, max_items=max_items, fields=fields)

List ratings

Gets a list of ratings for node **nodeId**.

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
    api_instance = openapi_client.RatingsApi(api_client)
    node_id = 'node_id_example' # str | The identifier of a node.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list.  If not supplied then the default value is 100.  (optional) (default to 100)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List ratings
        api_response = api_instance.list_ratings(node_id, skip_count=skip_count, max_items=max_items, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RatingsApi->list_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list.  If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**RatingPaging**](RatingPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **nodeId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

