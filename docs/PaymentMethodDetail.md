# PaymentMethodDetail

Payment method object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**PaymentMethodLimit**](PaymentMethodLimit.md) |  | [optional] 
**logo_url** | **str** |  | 
**name** | [**PaymentMethod**](PaymentMethod.md) |  | 
**settings** | [**PaymentMethodSettings**](PaymentMethodSettings.md) |  | 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | 
**summary_url** | **str** |  | 

## Example

```python
from openapi_client.models.payment_method_detail import PaymentMethodDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDetail from a JSON string
payment_method_detail_instance = PaymentMethodDetail.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodDetail.to_json())

# convert the object into a dict
payment_method_detail_dict = payment_method_detail_instance.to_dict()
# create an instance of PaymentMethodDetail from a dict
payment_method_detail_from_dict = PaymentMethodDetail.from_dict(payment_method_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


