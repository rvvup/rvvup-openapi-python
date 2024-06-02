# PaymentAction

The list of actions that can be performed on the payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | [**PaymentActionMethod**](PaymentActionMethod.md) |  | 
**type** | [**PaymentActionType**](PaymentActionType.md) |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.payment_action import PaymentAction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAction from a JSON string
payment_action_instance = PaymentAction.from_json(json)
# print the JSON string representation of the object
print(PaymentAction.to_json())

# convert the object into a dict
payment_action_dict = payment_action_instance.to_dict()
# create an instance of PaymentAction from a dict
payment_action_from_dict = PaymentAction.from_dict(payment_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


