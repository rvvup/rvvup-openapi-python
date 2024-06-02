# CheckoutCardSettingsInput

The Card settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFieldsInput**](CheckoutCustomerFieldsInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_card_settings_input import CheckoutCardSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCardSettingsInput from a JSON string
checkout_card_settings_input_instance = CheckoutCardSettingsInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutCardSettingsInput.to_json())

# convert the object into a dict
checkout_card_settings_input_dict = checkout_card_settings_input_instance.to_dict()
# create an instance of CheckoutCardSettingsInput from a dict
checkout_card_settings_input_from_dict = CheckoutCardSettingsInput.from_dict(checkout_card_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


