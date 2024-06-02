# StatementExportRequest

Request statement export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disbursement_batch_id** | **str** |  | [optional] 
**export_format** | **str** | Format for export. | 
**range** | [**StartEnd**](StartEnd.md) |  | [optional] 

## Example

```python
from openapi_client.models.statement_export_request import StatementExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StatementExportRequest from a JSON string
statement_export_request_instance = StatementExportRequest.from_json(json)
# print the JSON string representation of the object
print(StatementExportRequest.to_json())

# convert the object into a dict
statement_export_request_dict = statement_export_request_instance.to_dict()
# create an instance of StatementExportRequest from a dict
statement_export_request_from_dict = StatementExportRequest.from_dict(statement_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


