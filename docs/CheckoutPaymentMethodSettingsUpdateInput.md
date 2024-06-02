# CheckoutPaymentMethodSettingsUpdateInput

The payment method settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_pay** | [**CheckoutApplePaySettingsUpdateInput**](CheckoutApplePaySettingsUpdateInput.md) |  | [optional] 
**card** | [**CheckoutCardSettingsUpdateInput**](CheckoutCardSettingsUpdateInput.md) |  | [optional] 
**pay_by_bank** | [**CheckoutPayByBankSettingsUpdateInput**](CheckoutPayByBankSettingsUpdateInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_payment_method_settings_update_input import CheckoutPaymentMethodSettingsUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPaymentMethodSettingsUpdateInput from a JSON string
checkout_payment_method_settings_update_input_instance = CheckoutPaymentMethodSettingsUpdateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutPaymentMethodSettingsUpdateInput.to_json())

# convert the object into a dict
checkout_payment_method_settings_update_input_dict = checkout_payment_method_settings_update_input_instance.to_dict()
# create an instance of CheckoutPaymentMethodSettingsUpdateInput from a dict
checkout_payment_method_settings_update_input_from_dict = CheckoutPaymentMethodSettingsUpdateInput.from_dict(checkout_payment_method_settings_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


