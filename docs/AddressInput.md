# AddressInput

The address details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City. | 
**company** | **str** | Company name. | [optional] 
**country_code** | **str** | Two letter ISO 3166-1 alpha-2 country code. | 
**line1** | **str** | Address line 1. | 
**line2** | **str** | Address line 2. | [optional] 
**name** | **str** | Name. | 
**phone_number** | **str** | Phone number. | [optional] 
**postcode** | **str** | Postcode. | 
**state** | **str** | State. | [optional] 

## Example

```python
from openapi_client.models.address_input import AddressInput

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInput from a JSON string
address_input_instance = AddressInput.from_json(json)
# print the JSON string representation of the object
print(AddressInput.to_json())

# convert the object into a dict
address_input_dict = address_input_instance.to_dict()
# create an instance of AddressInput from a dict
address_input_from_dict = AddressInput.from_dict(address_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


