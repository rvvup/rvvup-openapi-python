# openapi_client.StatementExportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_statement**](StatementExportsApi.md#export_statement) | **POST** /api/2024-03-01/{merchantId}/statements/export | Export a statement


# **export_statement**
> export_statement(merchant_id, statement_export_request)

Export a statement

Export statements in different formats.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.statement_export_request import StatementExportRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): apiKey
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatementExportsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    statement_export_request = openapi_client.StatementExportRequest() # StatementExportRequest | Statement export filters

    try:
        # Export a statement
        api_instance.export_statement(merchant_id, statement_export_request)
    except Exception as e:
        print("Exception when calling StatementExportsApi->export_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **statement_export_request** | [**StatementExportRequest**](StatementExportRequest.md)| Statement export filters | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The export statement |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

