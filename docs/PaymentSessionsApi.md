# openapi_client.PaymentSessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_session**](PaymentSessionsApi.md#create_payment_session) | **POST** /api/2024-03-01/{merchantId}/checkouts/{checkoutId}/payment-sessions | Create a payment session
[**get_payment_session**](PaymentSessionsApi.md#get_payment_session) | **GET** /api/2024-03-01/{merchantId}/checkouts/{checkoutId}/payment-sessions/{paymentSessionId} | Get a payment session


# **create_payment_session**
> PaymentSession create_payment_session(merchant_id, checkout_id, payment_session_create_input)

Create a payment session

Creates a payment session with a new active payment.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_session import PaymentSession
from openapi_client.models.payment_session_create_input import PaymentSessionCreateInput
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
    api_instance = openapi_client.PaymentSessionsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    checkout_id = 'checkout_id_example' # str | checkout id
    payment_session_create_input = openapi_client.PaymentSessionCreateInput() # PaymentSessionCreateInput | The Payment Session to create

    try:
        # Create a payment session
        api_response = api_instance.create_payment_session(merchant_id, checkout_id, payment_session_create_input)
        print("The response of PaymentSessionsApi->create_payment_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSessionsApi->create_payment_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **checkout_id** | **str**| checkout id | 
 **payment_session_create_input** | [**PaymentSessionCreateInput**](PaymentSessionCreateInput.md)| The Payment Session to create | 

### Return type

[**PaymentSession**](PaymentSession.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created payment session |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_session**
> PaymentSession get_payment_session(merchant_id, checkout_id, payment_session_id)

Get a payment session

Get a payment session by id.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.payment_session import PaymentSession
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
    api_instance = openapi_client.PaymentSessionsApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    checkout_id = 'checkout_id_example' # str | checkout id
    payment_session_id = 'payment_session_id_example' # str | payment session id

    try:
        # Get a payment session
        api_response = api_instance.get_payment_session(merchant_id, checkout_id, payment_session_id)
        print("The response of PaymentSessionsApi->get_payment_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentSessionsApi->get_payment_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **checkout_id** | **str**| checkout id | 
 **payment_session_id** | **str**| payment session id | 

### Return type

[**PaymentSession**](PaymentSession.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Session |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

