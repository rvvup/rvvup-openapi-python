# WebhookPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageable** | [**Pageable**](Pageable.md) |  | 
**results** | [**List[Webhook]**](Webhook.md) |  | 
**total** | **int** |  | 

## Example

```python
from openapi_client.models.webhook_page import WebhookPage

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPage from a JSON string
webhook_page_instance = WebhookPage.from_json(json)
# print the JSON string representation of the object
print(WebhookPage.to_json())

# convert the object into a dict
webhook_page_dict = webhook_page_instance.to_dict()
# create an instance of WebhookPage from a dict
webhook_page_from_dict = WebhookPage.from_dict(webhook_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


