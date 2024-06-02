# PaymentSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_manually_capturable** | **bool** | Whether the payment can be captured manually later. | 
**is_refundable** | **bool** | Whether the payment is refundable. | 
**is_voidable** | **bool** | Whether the payment is voidable. | 
**payment_actions** | [**List[PaymentAction]**](PaymentAction.md) | The list of actions that can be performed on the payment. | 
**refundable_amount** | [**Money**](Money.md) |  | 

## Example

```python
from openapi_client.models.payment_summary import PaymentSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentSummary from a JSON string
payment_summary_instance = PaymentSummary.from_json(json)
# print the JSON string representation of the object
print(PaymentSummary.to_json())

# convert the object into a dict
payment_summary_dict = payment_summary_instance.to_dict()
# create an instance of PaymentSummary from a dict
payment_summary_from_dict = PaymentSummary.from_dict(payment_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


