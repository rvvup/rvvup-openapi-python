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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.application_source import ApplicationSource
from openapi_client.models.money_input import MoneyInput
from typing import Optional, Set
from typing_extensions import Self

class PaymentLinkCreateInput(BaseModel):
    """
    The input for creating a payment link.
    """ # noqa: E501
    amount: Optional[MoneyInput] = None
    checkout_template_id: Optional[StrictStr] = Field(default=None, description="The ID of the checkout template to use for this payment link.                          If not provided, the default template will be used.                          If provided, the template must be available to the merchant.", alias="checkoutTemplateId")
    reference: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Your reference to identify the payment link and subsequently created checkouts                          and payment sessions.")
    reusable: Optional[StrictBool] = Field(default=False, description="Whether the payment link can be reused for multiple payments.")
    source: Optional[ApplicationSource] = None
    __properties: ClassVar[List[str]] = ["amount", "checkoutTemplateId", "reference", "reusable", "source"]

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
        """Create an instance of PaymentLinkCreateInput from a JSON string"""
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
        """Create an instance of PaymentLinkCreateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": MoneyInput.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "checkoutTemplateId": obj.get("checkoutTemplateId"),
            "reference": obj.get("reference"),
            "reusable": obj.get("reusable") if obj.get("reusable") is not None else False,
            "source": obj.get("source")
        })
        return _obj


