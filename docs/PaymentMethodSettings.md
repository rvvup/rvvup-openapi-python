# PaymentMethodSettings

Payment method settings object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[PaymentMethodAsset]**](PaymentMethodAsset.md) |  | 
**description** | **str** |  | 
**display_name** | **str** |  | 

## Example

```python
from openapi_client.models.payment_method_settings import PaymentMethodSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodSettings from a JSON string
payment_method_settings_instance = PaymentMethodSettings.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodSettings.to_json())

# convert the object into a dict
payment_method_settings_dict = payment_method_settings_instance.to_dict()
# create an instance of PaymentMethodSettings from a dict
payment_method_settings_from_dict = PaymentMethodSettings.from_dict(payment_method_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


