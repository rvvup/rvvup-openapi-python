# CheckoutCreateInput

The input to create a new checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**billing_address** | [**AddressInput**](AddressInput.md) |  | [optional] 
**checkout_template_id** | **str** | The ID of the checkout template to use for this checkout.                          If not provided, the default template will be used.                          If provided, the template must be available to the merchant. | [optional] 
**customer** | [**CustomerInput**](CustomerInput.md) |  | [optional] 
**metadata** | **Dict[str, str]** | Key value pairs to store additional information about the checkout. | [optional] 
**reference** | **str** | Your reference to identify the checkout and the subsequently created payment sessions. | [optional] 
**source** | [**ApplicationSource**](ApplicationSource.md) |  | [optional] 
**success_url** | **str** | The URL to redirect the user to after the checkout is completed successfully.                          This field supports the template variable &#x60;{{CHECKOUT_ID}}&#x60; which will be replaced with the                          created checkouts ID. | [optional] 

## Example

```python
from openapi_client.models.checkout_create_input import CheckoutCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCreateInput from a JSON string
checkout_create_input_instance = CheckoutCreateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutCreateInput.to_json())

# convert the object into a dict
checkout_create_input_dict = checkout_create_input_instance.to_dict()
# create an instance of CheckoutCreateInput from a dict
checkout_create_input_from_dict = CheckoutCreateInput.from_dict(checkout_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


