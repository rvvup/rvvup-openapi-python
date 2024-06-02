# PaymentLink

Payment link object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) |  | [optional] 
**checkout_ids** | **List[str]** | The IDs of the checkouts that were created for this payment link. | 
**checkout_template_id** | **str** | The ID of the checkout template to use for this payment link.                          If not provided, the default template will be used. | [optional] 
**created_at** | **datetime** | The datetime when the payment link was created. | 
**id** | **str** | The unique ID of the payment link. | 
**merchant_id** | **str** | The ID of the merchant that owns this checkout. | 
**reference** | **str** | Your reference to identify the payment link and subsequently created checkouts                          and payment sessions. | [optional] 
**reusable** | **bool** | Whether the payment link can be reused for multiple payments. | 
**source** | [**ApplicationSource**](ApplicationSource.md) |  | 
**status** | [**PaymentLinkStatus**](PaymentLinkStatus.md) |  | 
**updated_at** | **datetime** | The datetime when the payment link was last updated. | 
**url** | **str** | The URL to the hosted payment link page. | 

## Example

```python
from openapi_client.models.payment_link import PaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLink from a JSON string
payment_link_instance = PaymentLink.from_json(json)
# print the JSON string representation of the object
print(PaymentLink.to_json())

# convert the object into a dict
payment_link_dict = payment_link_instance.to_dict()
# create an instance of PaymentLink from a dict
payment_link_from_dict = PaymentLink.from_dict(payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


