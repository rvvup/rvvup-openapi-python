# Item

List of items that the customer is purchasing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The datetime when the item was created. | 
**id** | **str** | The unique ID for the item. | 
**name** | **str** | The name of the item. | 
**price** | [**Money**](Money.md) |  | 
**price_with_tax** | [**Money**](Money.md) |  | [optional] 
**quantity** | **str** | The quantity of the item being purchased. | 
**restriction** | [**ItemRestriction**](ItemRestriction.md) |  | 
**sku** | **str** | Stock keeping unit - the unique identifier for the item. | 
**tax** | [**Money**](Money.md) |  | [optional] 
**total** | [**Money**](Money.md) |  | 

## Example

```python
from openapi_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


