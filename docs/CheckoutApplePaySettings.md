# CheckoutApplePaySettings

The Apple Pay settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFields**](CheckoutCustomerFields.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_apple_pay_settings import CheckoutApplePaySettings

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutApplePaySettings from a JSON string
checkout_apple_pay_settings_instance = CheckoutApplePaySettings.from_json(json)
# print the JSON string representation of the object
print(CheckoutApplePaySettings.to_json())

# convert the object into a dict
checkout_apple_pay_settings_dict = checkout_apple_pay_settings_instance.to_dict()
# create an instance of CheckoutApplePaySettings from a dict
checkout_apple_pay_settings_from_dict = CheckoutApplePaySettings.from_dict(checkout_apple_pay_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


