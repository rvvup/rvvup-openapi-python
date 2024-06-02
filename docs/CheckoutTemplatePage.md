# CheckoutTemplatePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[CheckoutTemplate]**](CheckoutTemplate.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.checkout_template_page import CheckoutTemplatePage

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutTemplatePage from a JSON string
checkout_template_page_instance = CheckoutTemplatePage.from_json(json)
# print the JSON string representation of the object
print(CheckoutTemplatePage.to_json())

# convert the object into a dict
checkout_template_page_dict = checkout_template_page_instance.to_dict()
# create an instance of CheckoutTemplatePage from a dict
checkout_template_page_from_dict = CheckoutTemplatePage.from_dict(checkout_template_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


