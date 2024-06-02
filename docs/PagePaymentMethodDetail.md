# PagePaymentMethodDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[PaymentMethodDetail]**](PaymentMethodDetail.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.page_payment_method_detail import PagePaymentMethodDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PagePaymentMethodDetail from a JSON string
page_payment_method_detail_instance = PagePaymentMethodDetail.from_json(json)
# print the JSON string representation of the object
print(PagePaymentMethodDetail.to_json())

# convert the object into a dict
page_payment_method_detail_dict = page_payment_method_detail_instance.to_dict()
# create an instance of PagePaymentMethodDetail from a dict
page_payment_method_detail_from_dict = PagePaymentMethodDetail.from_dict(page_payment_method_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


