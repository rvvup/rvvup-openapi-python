# PageCheckout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[Checkout]**](Checkout.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.page_checkout import PageCheckout

# TODO update the JSON string below
json = "{}"
# create an instance of PageCheckout from a JSON string
page_checkout_instance = PageCheckout.from_json(json)
# print the JSON string representation of the object
print(PageCheckout.to_json())

# convert the object into a dict
page_checkout_dict = page_checkout_instance.to_dict()
# create an instance of PageCheckout from a dict
page_checkout_from_dict = PageCheckout.from_dict(page_checkout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


