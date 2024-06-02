# ItemInput

An item that the customer is purchasing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the item. | 
**price** | [**MoneyInput**](MoneyInput.md) |  | 
**price_with_tax** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**quantity** | **str** | The quantity of the item being purchased. | 
**restriction** | [**ItemRestriction**](ItemRestriction.md) |  | [optional] 
**sku** | **str** | Stock keeping unit - the unique identifier for the item. | 
**tax** | [**MoneyInput**](MoneyInput.md) |  | [optional] 
**total** | [**MoneyInput**](MoneyInput.md) |  | 

## Example

```python
from openapi_client.models.item_input import ItemInput

# TODO update the JSON string below
json = "{}"
# create an instance of ItemInput from a JSON string
item_input_instance = ItemInput.from_json(json)
# print the JSON string representation of the object
print(ItemInput.to_json())

# convert the object into a dict
item_input_dict = item_input_instance.to_dict()
# create an instance of ItemInput from a dict
item_input_from_dict = ItemInput.from_dict(item_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


