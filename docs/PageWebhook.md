# PageWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[Webhook]**](Webhook.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.page_webhook import PageWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PageWebhook from a JSON string
page_webhook_instance = PageWebhook.from_json(json)
# print the JSON string representation of the object
print(PageWebhook.to_json())

# convert the object into a dict
page_webhook_dict = page_webhook_instance.to_dict()
# create an instance of PageWebhook from a dict
page_webhook_from_dict = PageWebhook.from_dict(page_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


