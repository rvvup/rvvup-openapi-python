# PaymentMethodTotalLimit

Payment method total limit object. Contains min and max limits for a currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | 
**max** | **str** |  | 
**min** | **str** |  | 

## Example

```python
from openapi_client.models.payment_method_total_limit import PaymentMethodTotalLimit

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodTotalLimit from a JSON string
payment_method_total_limit_instance = PaymentMethodTotalLimit.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodTotalLimit.to_json())

# convert the object into a dict
payment_method_total_limit_dict = payment_method_total_limit_instance.to_dict()
# create an instance of PaymentMethodTotalLimit from a dict
payment_method_total_limit_from_dict = PaymentMethodTotalLimit.from_dict(payment_method_total_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


