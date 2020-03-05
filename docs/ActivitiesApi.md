# openapi_client.ActivitiesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_activities_for_person**](ActivitiesApi.md#list_activities_for_person) | **GET** /people/{personId}/activities | List activities


# **list_activities_for_person**
> ActivityPaging list_activities_for_person(person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)

List activities

Gets a list of activities for person **personId**.  You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user. 

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
    api_instance = openapi_client.ActivitiesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list.  If not supplied then the default value is 100.  (optional) (default to 100)
who = 'who_example' # str | A filter to include the user's activities only `me`, other user's activities only `others`'  (optional)
site_id = 'site_id_example' # str | Include only activity feed entries relating to this site. (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List activities
        api_response = api_instance.list_activities_for_person(person_id, skip_count=skip_count, max_items=max_items, who=who, site_id=site_id, fields=fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActivitiesApi->list_activities_for_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list.  If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list.  If not supplied then the default value is 100.  | [optional] [default to 100]
 **who** | **str**| A filter to include the user&#39;s activities only &#x60;me&#x60;, other user&#39;s activities only &#x60;others&#x60;&#39;  | [optional] 
 **site_id** | **str**| Include only activity feed entries relating to this site. | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**ActivityPaging**](ActivityPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount**, or **who** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have access to the activities for **personId** |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

