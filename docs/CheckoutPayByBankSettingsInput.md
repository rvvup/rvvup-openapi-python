# CheckoutPayByBankSettingsInput

The Pay by Bank settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFieldsInput**](CheckoutCustomerFieldsInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_pay_by_bank_settings_input import CheckoutPayByBankSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPayByBankSettingsInput from a JSON string
checkout_pay_by_bank_settings_input_instance = CheckoutPayByBankSettingsInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutPayByBankSettingsInput.to_json())

# convert the object into a dict
checkout_pay_by_bank_settings_input_dict = checkout_pay_by_bank_settings_input_instance.to_dict()
# create an instance of CheckoutPayByBankSettingsInput from a dict
checkout_pay_by_bank_settings_input_from_dict = CheckoutPayByBankSettingsInput.from_dict(checkout_pay_by_bank_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


