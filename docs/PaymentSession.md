# PaymentSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address** | [**Address**](Address.md) |  | [optional] 
**checkout_id** | **str** | The ID of the checkout that the payment session was created from. | [optional] 
**created_at** | **datetime** | The datetime when the payment session was created. | 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**dashboard_url** | **str** | The URL to the merchant dashboard for the payment session. | 
**discount_total** | [**Money**](Money.md) |  | [optional] 
**external_reference** | **str** | Your reference to identify the payment session. | [optional] 
**id** | **str** | The unique ID for the payment session. | 
**items** | [**List[Item]**](Item.md) | List of items that the customer is purchasing. | 
**merchant_id** | **str** | The ID of the merchant that the payment session was created for. | 
**payment_link_id** | **str** | The ID of the payment link that the payment session was created from. | [optional] 
**payments** | [**List[Payment]**](Payment.md) | List of payments that have been made for the payment session. | 
**requires_shipping** | **bool** | Whether the customer is required to provide a shipping address. | [optional] 
**shipping_address** | [**Address**](Address.md) |  | [optional] 
**shipping_total** | [**Money**](Money.md) |  | [optional] 
**status** | [**PaymentSessionStatus**](PaymentSessionStatus.md) |  | 
**tax_total** | [**Money**](Money.md) |  | [optional] 
**total** | [**Money**](Money.md) |  | 
**updated_at** | **datetime** | The datetime when the payment session was last updated. | 

## Example

```python
from openapi_client.models.payment_session import PaymentSession

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSession from a JSON string
payment_session_instance = PaymentSession.from_json(json)
# print the JSON string representation of the object
print(PaymentSession.to_json())

# convert the object into a dict
payment_session_dict = payment_session_instance.to_dict()
# create an instance of PaymentSession from a dict
payment_session_from_dict = PaymentSession.from_dict(payment_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


