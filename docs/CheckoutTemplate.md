# CheckoutTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | [**CheckoutAmountType**](CheckoutAmountType.md) |  | 
**created_at** | **datetime** | The datetime when the checkout template was created. | 
**customer_fields** | [**CheckoutCustomerFields**](CheckoutCustomerFields.md) |  | [optional] 
**enabled_payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) | Ordered list of payment methods that are enabled for the checkout. | [optional] 
**id** | **str** | The unique ID of the checkout template. | 
**merchant_id** | **str** | The ID of the merchant that owns this checkout template. | 
**name** | **str** | The name of the checkout template. | 
**notify_customer** | **bool** | Whether the customer should be notified on payment completion. | 
**notify_merchant** | **bool** | Whether you should be notified on payment completion. | 
**payment_method_settings** | [**CheckoutPaymentMethodSettings**](CheckoutPaymentMethodSettings.md) |  | [optional] 
**source** | [**ApplicationSource**](ApplicationSource.md) |  | 
**updated_at** | **datetime** | The datetime when the checkout template was last updated. | 

## Example

```python
from openapi_client.models.checkout_template import CheckoutTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutTemplate from a JSON string
checkout_template_instance = CheckoutTemplate.from_json(json)
# print the JSON string representation of the object
print(CheckoutTemplate.to_json())

# convert the object into a dict
checkout_template_dict = checkout_template_instance.to_dict()
# create an instance of CheckoutTemplate from a dict
checkout_template_from_dict = CheckoutTemplate.from_dict(checkout_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


