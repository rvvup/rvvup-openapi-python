# Payment

List of payments that have been made for the payment session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) |  | 
**authorization_expires_at** | **datetime** | The datetime when the payment&#39;s authorization expires. | [optional] 
**capture_type** | [**PaymentCaptureType**](PaymentCaptureType.md) |  | [optional] 
**created_at** | **datetime** | The datetime when the payment was created. | 
**decline_reason** | [**PaymentDeclineReason**](PaymentDeclineReason.md) |  | [optional] 
**id** | **str** | The unique ID for the payment. | 
**method** | [**PaymentMethod**](PaymentMethod.md) |  | 
**payment_session_id** | **str** | The ID of the payment session that the payment was created in. | 
**settlement_status** | [**PaymentSettlementStatus**](PaymentSettlementStatus.md) |  | 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | 
**summary** | [**PaymentSummary**](PaymentSummary.md) |  | 
**updated_at** | **datetime** | The datetime when the payment was last updated. | 
**void_reason** | [**PaymentVoidReason**](PaymentVoidReason.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment import Payment

# TODO update the JSON string below
json = "{}"
# create an instance of Payment from a JSON string
payment_instance = Payment.from_json(json)
# print the JSON string representation of the object
print(Payment.to_json())

# convert the object into a dict
payment_dict = payment_instance.to_dict()
# create an instance of Payment from a dict
payment_from_dict = Payment.from_dict(payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


