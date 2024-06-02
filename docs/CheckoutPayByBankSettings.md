# CheckoutPayByBankSettings

The Pay by Bank settings to be used for the checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFields**](CheckoutCustomerFields.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_pay_by_bank_settings import CheckoutPayByBankSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPayByBankSettings from a JSON string
checkout_pay_by_bank_settings_instance = CheckoutPayByBankSettings.from_json(json)
# print the JSON string representation of the object
print(CheckoutPayByBankSettings.to_json())

# convert the object into a dict
checkout_pay_by_bank_settings_dict = checkout_pay_by_bank_settings_instance.to_dict()
# create an instance of CheckoutPayByBankSettings from a dict
checkout_pay_by_bank_settings_from_dict = CheckoutPayByBankSettings.from_dict(checkout_pay_by_bank_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


