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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.payment_method import PaymentMethod
from openapi_client.models.payment_method_limit import PaymentMethodLimit
from openapi_client.models.payment_method_settings import PaymentMethodSettings
from openapi_client.models.payment_method_status import PaymentMethodStatus
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodDetail(BaseModel):
    """
    Payment method object
    """ # noqa: E501
    limits: Optional[PaymentMethodLimit] = None
    logo_url: StrictStr = Field(alias="logoUrl")
    name: PaymentMethod
    settings: PaymentMethodSettings
    status: PaymentMethodStatus
    summary_url: StrictStr = Field(alias="summaryUrl")
    __properties: ClassVar[List[str]] = ["limits", "logoUrl", "name", "settings", "status", "summaryUrl"]

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
        """Create an instance of PaymentMethodDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limits": PaymentMethodLimit.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "logoUrl": obj.get("logoUrl"),
            "name": obj.get("name"),
            "settings": PaymentMethodSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "status": obj.get("status"),
            "summaryUrl": obj.get("summaryUrl")
        })
        return _obj


