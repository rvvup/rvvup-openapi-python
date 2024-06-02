# PaymentLinkPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[PaymentLink]**](PaymentLink.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.payment_link_page import PaymentLinkPage

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkPage from a JSON string
payment_link_page_instance = PaymentLinkPage.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkPage.to_json())

# convert the object into a dict
payment_link_page_dict = payment_link_page_instance.to_dict()
# create an instance of PaymentLinkPage from a dict
payment_link_page_from_dict = PaymentLinkPage.from_dict(payment_link_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


