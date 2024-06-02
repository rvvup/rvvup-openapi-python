# CheckoutPaymentMethodSettingsInput

The payment method settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_pay** | [**CheckoutApplePaySettingsInput**](CheckoutApplePaySettingsInput.md) |  | [optional] 
**card** | [**CheckoutCardSettingsInput**](CheckoutCardSettingsInput.md) |  | [optional] 
**pay_by_bank** | [**CheckoutPayByBankSettingsInput**](CheckoutPayByBankSettingsInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_payment_method_settings_input import CheckoutPaymentMethodSettingsInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPaymentMethodSettingsInput from a JSON string
checkout_payment_method_settings_input_instance = CheckoutPaymentMethodSettingsInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutPaymentMethodSettingsInput.to_json())

# convert the object into a dict
checkout_payment_method_settings_input_dict = checkout_payment_method_settings_input_instance.to_dict()
# create an instance of CheckoutPaymentMethodSettingsInput from a dict
checkout_payment_method_settings_input_from_dict = CheckoutPaymentMethodSettingsInput.from_dict(checkout_payment_method_settings_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


