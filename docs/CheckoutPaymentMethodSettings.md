# CheckoutPaymentMethodSettings

The payment method settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_pay** | [**CheckoutApplePaySettings**](CheckoutApplePaySettings.md) |  | [optional] 
**card** | [**CheckoutCardSettings**](CheckoutCardSettings.md) |  | [optional] 
**pay_by_bank** | [**CheckoutPayByBankSettings**](CheckoutPayByBankSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_payment_method_settings import CheckoutPaymentMethodSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPaymentMethodSettings from a JSON string
checkout_payment_method_settings_instance = CheckoutPaymentMethodSettings.from_json(json)
# print the JSON string representation of the object
print(CheckoutPaymentMethodSettings.to_json())

# convert the object into a dict
checkout_payment_method_settings_dict = checkout_payment_method_settings_instance.to_dict()
# create an instance of CheckoutPaymentMethodSettings from a dict
checkout_payment_method_settings_from_dict = CheckoutPaymentMethodSettings.from_dict(checkout_payment_method_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


