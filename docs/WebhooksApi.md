# openapi_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /api/2024-03-01/{merchantId}/webhooks | Create a new webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /api/2024-03-01/{merchantId}/webhooks/{webhookId} | Get a webhook by id
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /api/2024-03-01/{merchantId}/webhooks | Get all webhook
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /api/2024-03-01/{merchantId}/webhooks/{webhookId} | Update a webhook


# **create_webhook**
> Webhook create_webhook(merchant_id, webhook_create_input)

Create a new webhook

Create a new webhook

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.webhook import Webhook
from openapi_client.models.webhook_create_input import WebhookCreateInput
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
    api_instance = openapi_client.WebhooksApi(api_client)
    merchant_id = 'merchant_id_example' # str | Merchant ID
    webhook_create_input = openapi_client.WebhookCreateInput() # WebhookCreateInput | The webhook to create

    try:
        # Create a new webhook
        api_response = api_instance.create_webhook(merchant_id, webhook_create_input)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant ID | 
 **webhook_create_input** | [**WebhookCreateInput**](WebhookCreateInput.md)| The webhook to create | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created webhook |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(merchant_id, webhook_id)

Get a webhook by id

Get a webhook by id

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.webhook import Webhook
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
    api_instance = openapi_client.WebhooksApi(api_client)
    merchant_id = 'merchant_id_example' # str | Merchant ID
    webhook_id = 'webhook_id_example' # str | Webhook ID

    try:
        # Get a webhook by id
        api_response = api_instance.get_webhook(merchant_id, webhook_id)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant ID | 
 **webhook_id** | **str**| Webhook ID | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Webhook not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookPage list_webhooks(merchant_id, offset=offset, limit=limit)

Get all webhook

Get all webhook

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.webhook_page import WebhookPage
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
    api_instance = openapi_client.WebhooksApi(api_client)
    merchant_id = 'merchant_id_example' # str | Merchant ID
    offset = 56 # int | pagination offset (optional)
    limit = 56 # int | pagination limit (optional)

    try:
        # Get all webhook
        api_response = api_instance.list_webhooks(merchant_id, offset=offset, limit=limit)
        print("The response of WebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant ID | 
 **offset** | **int**| pagination offset | [optional] 
 **limit** | **int**| pagination limit | [optional] 

### Return type

[**WebhookPage**](WebhookPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(merchant_id, webhook_id, webhook_update_input)

Update a webhook

Update a webhook

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.webhook import Webhook
from openapi_client.models.webhook_update_input import WebhookUpdateInput
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
    api_instance = openapi_client.WebhooksApi(api_client)
    merchant_id = 'merchant_id_example' # str | Merchant ID
    webhook_id = 'webhook_id_example' # str | Webhook ID
    webhook_update_input = openapi_client.WebhookUpdateInput() # WebhookUpdateInput | The webhook to update

    try:
        # Update a webhook
        api_response = api_instance.update_webhook(merchant_id, webhook_id, webhook_update_input)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| Merchant ID | 
 **webhook_id** | **str**| Webhook ID | 
 **webhook_update_input** | [**WebhookUpdateInput**](WebhookUpdateInput.md)| The webhook to update | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated webhook |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

