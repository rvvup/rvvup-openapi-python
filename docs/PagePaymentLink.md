# PagePaymentLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[PaymentLink]**](PaymentLink.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.page_payment_link import PagePaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of PagePaymentLink from a JSON string
page_payment_link_instance = PagePaymentLink.from_json(json)
# print the JSON string representation of the object
print(PagePaymentLink.to_json())

# convert the object into a dict
page_payment_link_dict = page_payment_link_instance.to_dict()
# create an instance of PagePaymentLink from a dict
page_payment_link_from_dict = PagePaymentLink.from_dict(page_payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


