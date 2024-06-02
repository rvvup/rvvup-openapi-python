# openapi_client.PaymentLinksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_link**](PaymentLinksApi.md#create_payment_link) | **POST** /api/2024-03-01/{merchantId}/payment-links | Create new payment link
[**deactivate_payment_link**](PaymentLinksApi.md#deactivate_payment_link) | **DELETE** /api/2024-03-01/{merchantId}/payment-links/{paymentLinkId} | Deactivate a payment link
[**get_payment_link**](PaymentLinksApi.md#get_payment_link) | **GET** /api/2024-03-01/{merchantId}/payment-links/{paymentLinkId} | Get a payment link
[**list_payment_links**](PaymentLinksApi.md#list_payment_links) | **GET** /api/2024-03-01/{merchantId}/payment-links | List payment links


# **create_payment_link**
> PaymentLink create_payment_link(merchant_id, payment_link_create_input, idempotency_key=idempotency_key)

Create new payment link

Creates a new payment link. User can choose whether to make it reusable

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_link import PaymentLink
from openapi_client.models.payment_link_create_input import PaymentLinkCreateInput
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
    api_instance = openapi_client.PaymentLinksApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    payment_link_create_input = openapi_client.PaymentLinkCreateInput() # PaymentLinkCreateInput | The Payment Link to create
    idempotency_key = 'idempotency_key_example' # str | Idempotency Key (optional)

    try:
        # Create new payment link
        api_response = api_instance.create_payment_link(merchant_id, payment_link_create_input, idempotency_key=idempotency_key)
        print("The response of PaymentLinksApi->create_payment_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->create_payment_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **payment_link_create_input** | [**PaymentLinkCreateInput**](PaymentLinkCreateInput.md)| The Payment Link to create | 
 **idempotency_key** | **str**| Idempotency Key | [optional] 

### Return type

[**PaymentLink**](PaymentLink.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created payment link |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_payment_link**
> PaymentLink deactivate_payment_link(payment_link_id, merchant_id)

Deactivate a payment link

Deactivate a payment link

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_link import PaymentLink
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
    api_instance = openapi_client.PaymentLinksApi(api_client)
    payment_link_id = 'payment_link_id_example' # str | payment link id
    merchant_id = 'merchant_id_example' # str | merchant id

    try:
        # Deactivate a payment link
        api_response = api_instance.deactivate_payment_link(payment_link_id, merchant_id)
        print("The response of PaymentLinksApi->deactivate_payment_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->deactivate_payment_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_link_id** | **str**| payment link id | 
 **merchant_id** | **str**| merchant id | 

### Return type

[**PaymentLink**](PaymentLink.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment link |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Payment link not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_link**
> PaymentLink get_payment_link(payment_link_id, merchant_id)

Get a payment link

Get a payment link by id

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_link import PaymentLink
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
    api_instance = openapi_client.PaymentLinksApi(api_client)
    payment_link_id = 'payment_link_id_example' # str | payment link id
    merchant_id = 'merchant_id_example' # str | merchant id

    try:
        # Get a payment link
        api_response = api_instance.get_payment_link(payment_link_id, merchant_id)
        print("The response of PaymentLinksApi->get_payment_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->get_payment_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_link_id** | **str**| payment link id | 
 **merchant_id** | **str**| merchant id | 

### Return type

[**PaymentLink**](PaymentLink.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment link |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Payment link not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_links**
> PaymentLinkPage list_payment_links(merchant_id, offset=offset, limit=limit)

List payment links

List payment links

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_link_page import PaymentLinkPage
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
    api_instance = openapi_client.PaymentLinksApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    offset = 56 # int | pagination offset (optional)
    limit = 56 # int | pagination limit (optional)

    try:
        # List payment links
        api_response = api_instance.list_payment_links(merchant_id, offset=offset, limit=limit)
        print("The response of PaymentLinksApi->list_payment_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentLinksApi->list_payment_links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **offset** | **int**| pagination offset | [optional] 
 **limit** | **int**| pagination limit | [optional] 

### Return type

[**PaymentLinkPage**](PaymentLinkPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of payment links |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

