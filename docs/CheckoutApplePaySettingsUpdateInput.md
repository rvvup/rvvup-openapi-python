# CheckoutApplePaySettingsUpdateInput

The Apple Pay settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFieldsUpdateInput**](CheckoutCustomerFieldsUpdateInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_apple_pay_settings_update_input import CheckoutApplePaySettingsUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutApplePaySettingsUpdateInput from a JSON string
checkout_apple_pay_settings_update_input_instance = CheckoutApplePaySettingsUpdateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutApplePaySettingsUpdateInput.to_json())

# convert the object into a dict
checkout_apple_pay_settings_update_input_dict = checkout_apple_pay_settings_update_input_instance.to_dict()
# create an instance of CheckoutApplePaySettingsUpdateInput from a dict
checkout_apple_pay_settings_update_input_from_dict = CheckoutApplePaySettingsUpdateInput.from_dict(checkout_apple_pay_settings_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


