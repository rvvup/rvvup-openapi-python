# CheckoutTemplateUpdateInput

The input for updating a checkout template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | [**CheckoutAmountType**](CheckoutAmountType.md) |  | [optional] 
**customer_fields** | [**CheckoutCustomerFieldsUpdateInput**](CheckoutCustomerFieldsUpdateInput.md) |  | [optional] 
**enabled_payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) | Ordered list of payment methods that are enabled for the checkout. | [optional] 
**name** | **str** | The name of the checkout template. | [optional] 
**notify_customer** | **bool** | Whether the customer should be notified on payment completion. | [optional] [default to False]
**notify_merchant** | **bool** | Whether you should be notified on payment completion. | [optional] [default to False]
**payment_method_settings** | [**CheckoutPaymentMethodSettingsUpdateInput**](CheckoutPaymentMethodSettingsUpdateInput.md) |  | [optional] 

## Example

```python
from openapi_client.models.checkout_template_update_input import CheckoutTemplateUpdateInput

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutTemplateUpdateInput from a JSON string
checkout_template_update_input_instance = CheckoutTemplateUpdateInput.from_json(json)
# print the JSON string representation of the object
print(CheckoutTemplateUpdateInput.to_json())

# convert the object into a dict
checkout_template_update_input_dict = checkout_template_update_input_instance.to_dict()
# create an instance of CheckoutTemplateUpdateInput from a dict
checkout_template_update_input_from_dict = CheckoutTemplateUpdateInput.from_dict(checkout_template_update_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


