# coding: utf-8

"""
    Rvvup API

    Rvvup Public API

    The version of the OpenAPI document: 2024-03-01
    Contact: info@rvvup.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.payment_link_create_input import PaymentLinkCreateInput

class TestPaymentLinkCreateInput(unittest.TestCase):
    """PaymentLinkCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentLinkCreateInput:
        """Test PaymentLinkCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentLinkCreateInput`
        """
        model = PaymentLinkCreateInput()
        if include_optional:
            return PaymentLinkCreateInput(
                amount = {"amount":"100.00","currency":"GBP"},
                checkout_template_id = '',
                reference = 'INVOICE-12345',
                reusable = False,
                source = 'API'
            )
        else:
            return PaymentLinkCreateInput(
        )
        """

    def testPaymentLinkCreateInput(self):
        """Test PaymentLinkCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
