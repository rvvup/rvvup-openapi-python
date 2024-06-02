# PageCheckoutTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[CheckoutTemplate]**](CheckoutTemplate.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.page_checkout_template import PageCheckoutTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PageCheckoutTemplate from a JSON string
page_checkout_template_instance = PageCheckoutTemplate.from_json(json)
# print the JSON string representation of the object
print(PageCheckoutTemplate.to_json())

# convert the object into a dict
page_checkout_template_dict = page_checkout_template_instance.to_dict()
# create an instance of PageCheckoutTemplate from a dict
page_checkout_template_from_dict = PageCheckoutTemplate.from_dict(page_checkout_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


