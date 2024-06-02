# PaymentLinkCreateInput

The input for creating a payment link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**checkout_template_id** | **str** | The ID of the checkout template to use for this payment link.                          If not provided, the default template will be used.                          If provided, the template must be available to the merchant. | [optional] 
**reference** | **str** | Your reference to identify the payment link and subsequently created checkouts                          and payment sessions. | [optional] 
**reusable** | **bool** | Whether the payment link can be reused for multiple payments. | [optional] [default to False]
**source** | [**ApplicationSource**](ApplicationSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_link_create_input import PaymentLinkCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkCreateInput from a JSON string
payment_link_create_input_instance = PaymentLinkCreateInput.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkCreateInput.to_json())

# convert the object into a dict
payment_link_create_input_dict = payment_link_create_input_instance.to_dict()
# create an instance of PaymentLinkCreateInput from a dict
payment_link_create_input_from_dict = PaymentLinkCreateInput.from_dict(payment_link_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


