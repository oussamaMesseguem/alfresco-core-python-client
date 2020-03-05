# openapi_client.ProbesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_probe**](ProbesApi.md#get_probe) | **GET** /probes/{probeId} | Check readiness and liveness of the repository


# **get_probe**
> ProbeEntry get_probe(probe_id)

Check readiness and liveness of the repository

**Note:** this endpoint is available in Alfresco 6.0 and newer versions.  Returns a status of 200 to indicate success and 503 for failure.  The readiness probe is normally only used to check repository startup.  The liveness probe should then be used to check the repository is still responding to requests.  **Note:** No authentication is required to call this endpoint. 

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
    api_instance = openapi_client.ProbesApi(api_client)
    probe_id = 'probe_id_example' # str | The name of the probe: * -ready- * -live- 

    try:
        # Check readiness and liveness of the repository
        api_response = api_instance.get_probe(probe_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProbesApi->get_probe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **probe_id** | **str**| The name of the probe: * -ready- * -live-  | 

### Return type

[**ProbeEntry**](ProbeEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | **probeId** does not exist  |  -  |
**503** | Service Unavailable - Probe failure status. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

