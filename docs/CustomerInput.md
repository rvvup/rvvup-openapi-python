# CustomerInput

The customer's details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The customer&#39;s email address. | [optional] 
**given_name** | **str** | The customer&#39;s given name. | [optional] 
**phone_number** | **str** | The customer&#39;s phone number. | [optional] 
**surname** | **str** | The customer&#39;s surname. | [optional] 

## Example

```python
from openapi_client.models.customer_input import CustomerInput

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerInput from a JSON string
customer_input_instance = CustomerInput.from_json(json)
# print the JSON string representation of the object
print(CustomerInput.to_json())

# convert the object into a dict
customer_input_dict = customer_input_instance.to_dict()
# create an instance of CustomerInput from a dict
customer_input_from_dict = CustomerInput.from_dict(customer_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


