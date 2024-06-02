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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.start_end import StartEnd
from typing import Optional, Set
from typing_extensions import Self

class StatementExportRequest(BaseModel):
    """
    Request statement export.
    """ # noqa: E501
    disbursement_batch_id: Optional[StrictStr] = Field(default=None, alias="disbursementBatchId")
    export_format: StrictStr = Field(description="Format for export.", alias="exportFormat")
    range: Optional[StartEnd] = None
    __properties: ClassVar[List[str]] = ["disbursementBatchId", "exportFormat", "range"]

    @field_validator('export_format')
    def export_format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['OFX_V2']):
            raise ValueError("must be one of enum values ('OFX_V2')")
        return value

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
        """Create an instance of StatementExportRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of range
        if self.range:
            _dict['range'] = self.range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatementExportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disbursementBatchId": obj.get("disbursementBatchId"),
            "exportFormat": obj.get("exportFormat"),
            "range": StartEnd.from_dict(obj["range"]) if obj.get("range") is not None else None
        })
        return _obj


