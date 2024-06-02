# WebhookCreateInput

The input for creating a webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** | Custom headers for the webhook | 
**subscribed_events** | [**List[WebhookEventType]**](WebhookEventType.md) | The events to subscribe to. | 
**url** | **str** | The URL to send the webhook event to. | 

## Example

```python
from openapi_client.models.webhook_create_input import WebhookCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateInput from a JSON string
webhook_create_input_instance = WebhookCreateInput.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateInput.to_json())

# convert the object into a dict
webhook_create_input_dict = webhook_create_input_instance.to_dict()
# create an instance of WebhookCreateInput from a dict
webhook_create_input_from_dict = WebhookCreateInput.from_dict(webhook_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


