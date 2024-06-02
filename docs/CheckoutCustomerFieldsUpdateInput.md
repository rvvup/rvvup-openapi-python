# CheckoutCustomerFieldsUpdateInput

The customer fields that are required or optional for the checkout.                      If a field is not required or optional, it will not be shown in the hosted checkout page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The optional customer fields for the checkout. | [optional] 
**required** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The required customer fields for the checkout. | [optional] 

## Example

```python
from openapi_client.models.checkout_customer_fields_update_input import CheckoutCustomerFieldsUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCustomerFieldsUpdateInput from a JSON string
checkout_customer_fields_update_input_instance = CheckoutCustomerFieldsUpdateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutCustomerFieldsUpdateInput.to_json())

# convert the object into a dict
checkout_customer_fields_update_input_dict = checkout_customer_fields_update_input_instance.to_dict()
# create an instance of CheckoutCustomerFieldsUpdateInput from a dict
checkout_customer_fields_update_input_from_dict = CheckoutCustomerFieldsUpdateInput.from_dict(checkout_customer_fields_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


