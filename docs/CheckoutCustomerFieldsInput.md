# CheckoutCustomerFieldsInput

The customer fields that are required or optional for the checkout.                      If a field is not required or optional, it will not be shown in the hosted checkout page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The optional customer fields for the checkout. | [optional] 
**required** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The required customer fields for the checkout. | [optional] 

## Example

```python
from openapi_client.models.checkout_customer_fields_input import CheckoutCustomerFieldsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCustomerFieldsInput from a JSON string
checkout_customer_fields_input_instance = CheckoutCustomerFieldsInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutCustomerFieldsInput.to_json())

# convert the object into a dict
checkout_customer_fields_input_dict = checkout_customer_fields_input_instance.to_dict()
# create an instance of CheckoutCustomerFieldsInput from a dict
checkout_customer_fields_input_from_dict = CheckoutCustomerFieldsInput.from_dict(checkout_customer_fields_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


