# Checkout

Checkout object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) |  | [optional] 
**billing_address** | [**Address**](Address.md) |  | [optional] 
**checkout_template_id** | **str** | The ID of the checkout template to use for this checkout. | 
**created_at** | **datetime** | The datetime when the checkout was created. | 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**expires_at** | **datetime** | The datetime when the checkout will expire. | 
**id** | **str** | The unique ID of the checkout. | 
**merchant_id** | **str** | The ID of the merchant that owns this checkout. | 
**metadata** | **Dict[str, str]** | Key value pairs to store additional information about the checkout. | 
**payment_link_id** | **str** | The ID of the payment link that was used to create this checkout. | [optional] 
**payment_session_ids** | **List[str]** | The IDs of the payment sessions that were created for this checkout. | 
**reference** | **str** | Your reference to identify the checkout and the subsequently created payment sessions. | [optional] 
**source** | [**ApplicationSource**](ApplicationSource.md) |  | 
**status** | [**CheckoutStatus**](CheckoutStatus.md) |  | 
**success_url** | **str** | The URL to redirect the customer to after the checkout is completed successfully. | [optional] 
**updated_at** | **datetime** | The datetime when the checkout was last updated. | 
**url** | **str** | The URL to the hosted checkout page. | 

## Example

```python
from openapi_client.models.checkout import Checkout

# TODO update the JSON string below
json = "{}"
# create an instance of Checkout from a JSON string
checkout_instance = Checkout.from_json(json)
# print the JSON string representation of the object
print(Checkout.to_json())

# convert the object into a dict
checkout_dict = checkout_instance.to_dict()
# create an instance of Checkout from a dict
checkout_from_dict = Checkout.from_dict(checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


