# CheckoutCustomerFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The optional customer fields for the checkout. | [optional] 
**required** | [**List[CheckoutCustomerFieldType]**](CheckoutCustomerFieldType.md) | The required customer fields for the checkout. | [optional] 

## Example

```python
from openapi_client.models.checkout_customer_fields import CheckoutCustomerFields

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCustomerFields from a JSON string
checkout_customer_fields_instance = CheckoutCustomerFields.from_json(json)
# print the JSON string representation of the object
print(CheckoutCustomerFields.to_json())

# convert the object into a dict
checkout_customer_fields_dict = checkout_customer_fields_instance.to_dict()
# create an instance of CheckoutCustomerFields from a dict
checkout_customer_fields_from_dict = CheckoutCustomerFields.from_dict(checkout_customer_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


