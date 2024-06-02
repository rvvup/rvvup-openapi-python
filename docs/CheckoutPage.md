# CheckoutPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[Checkout]**](Checkout.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.checkout_page import CheckoutPage

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutPage from a JSON string
checkout_page_instance = CheckoutPage.from_json(json)
# print the JSON string representation of the object
print(CheckoutPage.to_json())

# convert the object into a dict
checkout_page_dict = checkout_page_instance.to_dict()
# create an instance of CheckoutPage from a dict
checkout_page_from_dict = CheckoutPage.from_dict(checkout_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


