# PaymentMethodDetailsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[PaymentMethodDetail]**](PaymentMethodDetail.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.payment_method_details_page import PaymentMethodDetailsPage

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodDetailsPage from a JSON string
payment_method_details_page_instance = PaymentMethodDetailsPage.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodDetailsPage.to_json())

# convert the object into a dict
payment_method_details_page_dict = payment_method_details_page_instance.to_dict()
# create an instance of PaymentMethodDetailsPage from a dict
payment_method_details_page_from_dict = PaymentMethodDetailsPage.from_dict(payment_method_details_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


