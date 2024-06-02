# MoneyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount as a string. | 
**currency** | **str** | The three-letter ISO-4217 currency code of the amount. | 

## Example

```python
from openapi_client.models.money_input import MoneyInput

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyInput from a JSON string
money_input_instance = MoneyInput.from_json(json)
# print the JSON string representation of the object
print(MoneyInput.to_json())

# convert the object into a dict
money_input_dict = money_input_instance.to_dict()
# create an instance of MoneyInput from a dict
money_input_from_dict = MoneyInput.from_dict(money_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


