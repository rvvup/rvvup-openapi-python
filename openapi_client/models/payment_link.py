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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.application_source import ApplicationSource
from openapi_client.models.money import Money
from openapi_client.models.payment_link_status import PaymentLinkStatus
from typing import Optional, Set
from typing_extensions import Self

class PaymentLink(BaseModel):
    """
    Payment link object
    """ # noqa: E501
    amount: Optional[Money] = None
    checkout_ids: List[StrictStr] = Field(description="The IDs of the checkouts that were created for this payment link.", alias="checkoutIds")
    checkout_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the checkout template to use for this payment link.                          If not provided, the default template will be used.", alias="checkoutTemplateId")
    created_at: datetime = Field(description="The datetime when the payment link was created.", alias="createdAt")
    id: StrictStr = Field(description="The unique ID of the payment link.")
    merchant_id: StrictStr = Field(description="The ID of the merchant that owns this checkout.", alias="merchantId")
    reference: Optional[StrictStr] = Field(default=None, description="Your reference to identify the payment link and subsequently created checkouts                          and payment sessions.")
    reusable: StrictBool = Field(description="Whether the payment link can be reused for multiple payments.")
    source: ApplicationSource
    status: PaymentLinkStatus
    updated_at: datetime = Field(description="The datetime when the payment link was last updated.", alias="updatedAt")
    url: StrictStr = Field(description="The URL to the hosted payment link page.")
    __properties: ClassVar[List[str]] = ["amount", "checkoutIds", "checkoutTemplateId", "createdAt", "id", "merchantId", "reference", "reusable", "source", "status", "updatedAt", "url"]

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
        """Create an instance of PaymentLink from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": Money.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "checkoutIds": obj.get("checkoutIds"),
            "checkoutTemplateId": obj.get("checkoutTemplateId"),
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "merchantId": obj.get("merchantId"),
            "reference": obj.get("reference"),
            "reusable": obj.get("reusable"),
            "source": obj.get("source"),
            "status": obj.get("status"),
            "updatedAt": obj.get("updatedAt"),
            "url": obj.get("url")
        })
        return _obj


