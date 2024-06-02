# openapi_client.CheckoutTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout_template**](CheckoutTemplatesApi.md#create_checkout_template) | **POST** /api/2024-03-01/{merchantId}/checkout-templates | Create new checkout template
[**get_checkout_template**](CheckoutTemplatesApi.md#get_checkout_template) | **GET** /api/2024-03-01/{merchantId}/checkout-templates/{checkoutTemplateId} | Get a checkout template
[**list_checkout_templates**](CheckoutTemplatesApi.md#list_checkout_templates) | **GET** /api/2024-03-01/{merchantId}/checkout-templates | List checkout templates
[**update_checkout_template**](CheckoutTemplatesApi.md#update_checkout_template) | **PATCH** /api/2024-03-01/{merchantId}/checkout-templates/{checkoutTemplateId} | Update a checkout template


# **create_checkout_template**
> CheckoutTemplate create_checkout_template(merchant_id, checkout_template_create_input)

Create new checkout template

Creates a new checkout template.

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout_template import CheckoutTemplate
from openapi_client.models.checkout_template_create_input import CheckoutTemplateCreateInput
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
    api_instance = openapi_client.CheckoutTemplatesApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    checkout_template_create_input = openapi_client.CheckoutTemplateCreateInput() # CheckoutTemplateCreateInput | The checkout template to create

    try:
        # Create new checkout template
        api_response = api_instance.create_checkout_template(merchant_id, checkout_template_create_input)
        print("The response of CheckoutTemplatesApi->create_checkout_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutTemplatesApi->create_checkout_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **checkout_template_create_input** | [**CheckoutTemplateCreateInput**](CheckoutTemplateCreateInput.md)| The checkout template to create | 

### Return type

[**CheckoutTemplate**](CheckoutTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created checkout template |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout_template**
> CheckoutTemplate get_checkout_template(checkout_template_id, merchant_id)

Get a checkout template

Get a checkout template by id

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout_template import CheckoutTemplate
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
    api_instance = openapi_client.CheckoutTemplatesApi(api_client)
    checkout_template_id = 'checkout_template_id_example' # str | checkout template id
    merchant_id = 'merchant_id_example' # str | merchant id

    try:
        # Get a checkout template
        api_response = api_instance.get_checkout_template(checkout_template_id, merchant_id)
        print("The response of CheckoutTemplatesApi->get_checkout_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutTemplatesApi->get_checkout_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_template_id** | **str**| checkout template id | 
 **merchant_id** | **str**| merchant id | 

### Return type

[**CheckoutTemplate**](CheckoutTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout Template |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Checkout template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_checkout_templates**
> CheckoutTemplatePage list_checkout_templates(merchant_id, offset=offset, limit=limit)

List checkout templates

List checkout templates

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout_template_page import CheckoutTemplatePage
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
    api_instance = openapi_client.CheckoutTemplatesApi(api_client)
    merchant_id = 'merchant_id_example' # str | merchant id
    offset = 56 # int | pagination offset (optional)
    limit = 56 # int | pagination limit (optional)

    try:
        # List checkout templates
        api_response = api_instance.list_checkout_templates(merchant_id, offset=offset, limit=limit)
        print("The response of CheckoutTemplatesApi->list_checkout_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutTemplatesApi->list_checkout_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **str**| merchant id | 
 **offset** | **int**| pagination offset | [optional] 
 **limit** | **int**| pagination limit | [optional] 

### Return type

[**CheckoutTemplatePage**](CheckoutTemplatePage.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of checkout templates |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_checkout_template**
> CheckoutTemplate update_checkout_template(checkout_template_id, merchant_id, checkout_template_update_input)

Update a checkout template

Update a checkout template

### Example

* Bearer (JWT) Authentication (apiKey):

```python
import openapi_client
from openapi_client.models.checkout_template import CheckoutTemplate
from openapi_client.models.checkout_template_update_input import CheckoutTemplateUpdateInput
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
    api_instance = openapi_client.CheckoutTemplatesApi(api_client)
    checkout_template_id = 'checkout_template_id_example' # str | checkout template id
    merchant_id = 'merchant_id_example' # str | merchant id
    checkout_template_update_input = openapi_client.CheckoutTemplateUpdateInput() # CheckoutTemplateUpdateInput | The checkout template to update

    try:
        # Update a checkout template
        api_response = api_instance.update_checkout_template(checkout_template_id, merchant_id, checkout_template_update_input)
        print("The response of CheckoutTemplatesApi->update_checkout_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutTemplatesApi->update_checkout_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_template_id** | **str**| checkout template id | 
 **merchant_id** | **str**| merchant id | 
 **checkout_template_update_input** | [**CheckoutTemplateUpdateInput**](CheckoutTemplateUpdateInput.md)| The checkout template to update | 

### Return type

[**CheckoutTemplate**](CheckoutTemplate.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Checkout Template |  -  |
**400** | Validation failed |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission |  -  |
**404** | Checkout template not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

