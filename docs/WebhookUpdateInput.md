# WebhookUpdateInput

The input for updating a webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, Optional[str]]** | Custom headers for the webhook | [optional] 
**status** | [**WebhookStatus**](WebhookStatus.md) |  | [optional] 
**subscribed_events** | [**List[WebhookEventType]**](WebhookEventType.md) | The events to subscribe to. | [optional] 
**url** | **str** | The URL to send the webhook event to. | [optional] 

## Example

```python
from openapi_client.models.webhook_update_input import WebhookUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUpdateInput from a JSON string
webhook_update_input_instance = WebhookUpdateInput.from_json(json)
# print the JSON string representation of the object
print(WebhookUpdateInput.to_json())

# convert the object into a dict
webhook_update_input_dict = webhook_update_input_instance.to_dict()
# create an instance of WebhookUpdateInput from a dict
webhook_update_input_from_dict = WebhookUpdateInput.from_dict(webhook_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


