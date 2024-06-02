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
import json
from enum import Enum
from typing_extensions import Self


class PaymentSettlementStatus(str, Enum):
    """
    The settlement status of the payment.
    """

    """
    allowed enum values
    """
    NOT_INITIATED = 'NOT_INITIATED'
    ACCEPTED = 'ACCEPTED'
    SETTLED = 'SETTLED'
    FUNDS_RECEIVED = 'FUNDS_RECEIVED'
    SETTLED_EXTERNALLY = 'SETTLED_EXTERNALLY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentSettlementStatus from a JSON string"""
        return cls(json.loads(json_str))


