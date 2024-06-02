# PaymentMethodAsset

Payment method assets object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type** | [**PaymentMethodAssetType**](PaymentMethodAssetType.md) |  | 
**attributes** | **Dict[str, str]** |  | 
**url** | **str** |  | 

## Example

```python
from openapi_client.models.payment_method_asset import PaymentMethodAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodAsset from a JSON string
payment_method_asset_instance = PaymentMethodAsset.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodAsset.to_json())

# convert the object into a dict
payment_method_asset_dict = payment_method_asset_instance.to_dict()
# create an instance of PaymentMethodAsset from a dict
payment_method_asset_from_dict = PaymentMethodAsset.from_dict(payment_method_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


