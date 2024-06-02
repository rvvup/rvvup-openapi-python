# PaymentSessionCreateInput

Input for creating a payment session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**AddressInput**](AddressInput.md) |  | [optional] 
**customer** | [**CustomerInput**](CustomerInput.md) |  | [optional] 
**discount_total** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**external_reference** | **str** | Your reference to identify the payment session. | [optional] 
**items** | [**List[ItemInput]**](ItemInput.md) | List of items that the customer is purchasing. | [optional] 
**payment_capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**requires_shipping** | **bool** | Whether the customer is required to provide a shipping address. | [optional] [default to False]
**session_key** | **str** | The unique identifier for the payment session. If the same session key has been used,                          the existing payment session will be updated with the new values. | 
**shipping_address** | [**AddressInput**](AddressInput.md) |  | [optional] 
**shipping_total** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**tax_total** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**total** | [**MoneyInput**](MoneyInput.md) |  | 

## Example

```python
from openapi_client.models.payment_session_create_input import PaymentSessionCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSessionCreateInput from a JSON string
payment_session_create_input_instance = PaymentSessionCreateInput.from_json(json)
# print the JSON string representation of the object
print(PaymentSessionCreateInput.to_json())

# convert the object into a dict
payment_session_create_input_dict = payment_session_create_input_instance.to_dict()
# create an instance of PaymentSessionCreateInput from a dict
payment_session_create_input_from_dict = PaymentSessionCreateInput.from_dict(payment_session_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


