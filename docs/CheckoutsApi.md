# openapi_client.CheckoutsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout**](CheckoutsApi.md#create_checkout) | **POST** /api/2024-03-01/{merchantId}/checkouts | Create new checkout
[**get_checkout**](CheckoutsApi.md#get_checkout) | **GET** /api/2024-03-01/{merchantId}/checkouts/{checkoutId} | Get a checkout
[**list_checkout_payment_methods**](CheckoutsApi.md#list_checkout_payment_methods) | **GET** /api/2024-03-01/{merchantId}/checkouts/{checkoutId}/payment-methods | Get payment methods for a checkout
[**list_checkouts**](CheckoutsApi.md#list_checkouts) | **GET** /api/2024-03-01/{merchantId}/checkouts | List checkouts


# **create_checkout**
> Checkout create_checkout(merchant_id, checkout_create_input, idempotency_key=idempotency_key)

Create new checkout

Creates a new checkout.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout import Checkout
from openapi_client.models.checkout_create_input import CheckoutCreateInput
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
    api_instance = openapi_client.CheckoutsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    checkout_create_input = openapi_client.CheckoutCreateInput() # CheckoutCreateInput | The Checkout to create
    idempotency_key = 'idempotency_key_example' # str | Idempotency Key (optional)

    try:
        # Create new checkout
        api_response = api_instance.create_checkout(merchant_id, checkout_create_input, idempotency_key=idempotency_key)
        print("The response of CheckoutsApi->create_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutsApi->create_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **checkout_create_input** | [**CheckoutCreateInput**](CheckoutCreateInput.md)| The Checkout to create | 
 **idempotency_key** | **str**| Idempotency Key | [optional] 

### Return type

[**Checkout**](Checkout.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created checkout |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout**
> Checkout get_checkout(checkout_id, merchant_id, accept=accept)

Get a checkout

Get a checkout by id

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout import Checkout
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
    api_instance = openapi_client.CheckoutsApi(api_client)
    checkout_id = 'checkout_id_example' # str | checkout id
    merchant_id = 'merchant_id_example' # str | merchant id
    accept = 'accept_example' # str | Accept header (optional)

    try:
        # Get a checkout
        api_response = api_instance.get_checkout(checkout_id, merchant_id, accept=accept)
        print("The response of CheckoutsApi->get_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutsApi->get_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| checkout id | 
 **merchant_id** | **str**| merchant id | 
 **accept** | **str**| Accept header | [optional] 

### Return type

[**Checkout**](Checkout.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/schema+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Checkout not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_checkout_payment_methods**
> PaymentMethodDetailsPage list_checkout_payment_methods(checkout_id, merchant_id, offset=offset, limit=limit)

Get payment methods for a checkout

Lists the currently eligible payment methods for a checkout. The payment method status and checkout template settings are used to determine the eligible methods.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_method_details_page import PaymentMethodDetailsPage
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
    api_instance = openapi_client.CheckoutsApi(api_client)
    checkout_id = 'checkout_id_example' # str | checkout id
    merchant_id = 'merchant_id_example' # str | merchant id
    offset = 56 # int | pagination offset (optional)
    limit = 56 # int | pagination limit (optional)

    try:
        # Get payment methods for a checkout
        api_response = api_instance.list_checkout_payment_methods(checkout_id, merchant_id, offset=offset, limit=limit)
        print("The response of CheckoutsApi->list_checkout_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutsApi->list_checkout_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_id** | **str**| checkout id | 
 **merchant_id** | **str**| merchant id | 
 **offset** | **int**| pagination offset | [optional] 
 **limit** | **int**| pagination limit | [optional] 

### Return type

[**PaymentMethodDetailsPage**](PaymentMethodDetailsPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_checkouts**
> CheckoutPage list_checkouts(merchant_id, offset=offset, limit=limit)

List checkouts

List checkouts

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout_page import CheckoutPage
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
    api_instance = openapi_client.CheckoutsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    offset = 56 # int | pagination offset (optional)
    limit = 56 # int | pagination limit (optional)

    try:
        # List checkouts
        api_response = api_instance.list_checkouts(merchant_id, offset=offset, limit=limit)
        print("The response of CheckoutsApi->list_checkouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutsApi->list_checkouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **offset** | **int**| pagination offset | [optional] 
 **limit** | **int**| pagination limit | [optional] 

### Return type

[**CheckoutPage**](CheckoutPage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of checkouts |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

