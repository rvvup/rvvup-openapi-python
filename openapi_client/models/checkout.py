# coding: utf-8

"""
    Rvvup API

    Rvvup Public API

    The version of the OpenAPI document: 2024-03-01
    Contact: info@rvvup.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.address import Address
from openapi_client.models.application_source import ApplicationSource
from openapi_client.models.checkout_status import CheckoutStatus
from openapi_client.models.customer import Customer
from openapi_client.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class Checkout(BaseModel):
    """
    Checkout object
    """ # noqa: E501
    amount: Optional[Money] = None
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    checkout_template_id: StrictStr = Field(description="The ID of the checkout template to use for this checkout.", alias="checkoutTemplateId")
    created_at: datetime = Field(description="The datetime when the checkout was created.", alias="createdAt")
    customer: Optional[Customer] = None
    expires_at: datetime = Field(description="The datetime when the checkout will expire.", alias="expiresAt")
    id: StrictStr = Field(description="The unique ID of the checkout.")
    merchant_id: StrictStr = Field(description="The ID of the merchant that owns this checkout.", alias="merchantId")
    metadata: Dict[str, StrictStr] = Field(description="Key value pairs to store additional information about the checkout.")
    payment_link_id: Optional[StrictStr] = Field(default=None, description="The ID of the payment link that was used to create this checkout.", alias="paymentLinkId")
    payment_session_ids: List[StrictStr] = Field(description="The IDs of the payment sessions that were created for this checkout.", alias="paymentSessionIds")
    reference: Optional[StrictStr] = Field(default=None, description="Your reference to identify the checkout and the subsequently created payment sessions.")
    source: ApplicationSource
    status: CheckoutStatus
    success_url: Optional[StrictStr] = Field(default=None, description="The URL to redirect the customer to after the checkout is completed successfully.", alias="successUrl")
    updated_at: datetime = Field(description="The datetime when the checkout was last updated.", alias="updatedAt")
    url: StrictStr = Field(description="The URL to the hosted checkout page.")
    __properties: ClassVar[List[str]] = ["amount", "billingAddress", "checkoutTemplateId", "createdAt", "customer", "expiresAt", "id", "merchantId", "metadata", "paymentLinkId", "paymentSessionIds", "reference", "source", "status", "successUrl", "updatedAt", "url"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Checkout from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Checkout from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": Money.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "checkoutTemplateId": obj.get("checkoutTemplateId"),
            "createdAt": obj.get("createdAt"),
            "customer": Customer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "expiresAt": obj.get("expiresAt"),
            "id": obj.get("id"),
            "merchantId": obj.get("merchantId"),
            "metadata": obj.get("metadata"),
            "paymentLinkId": obj.get("paymentLinkId"),
            "paymentSessionIds": obj.get("paymentSessionIds"),
            "reference": obj.get("reference"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "successUrl": obj.get("successUrl"),
            "updatedAt": obj.get("updatedAt"),
            "url": obj.get("url")
        })
        return _obj


