# CheckoutCardSettingsUpdateInput

The Card settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFieldsUpdateInput**](CheckoutCustomerFieldsUpdateInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_card_settings_update_input import CheckoutCardSettingsUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutCardSettingsUpdateInput from a JSON string
checkout_card_settings_update_input_instance = CheckoutCardSettingsUpdateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutCardSettingsUpdateInput.to_json())

# convert the object into a dict
checkout_card_settings_update_input_dict = checkout_card_settings_update_input_instance.to_dict()
# create an instance of CheckoutCardSettingsUpdateInput from a dict
checkout_card_settings_update_input_from_dict = CheckoutCardSettingsUpdateInput.from_dict(checkout_card_settings_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


