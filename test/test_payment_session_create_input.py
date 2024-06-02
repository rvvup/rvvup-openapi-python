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

from openapi_client.models.payment_session_create_input import PaymentSessionCreateInput

class TestPaymentSessionCreateInput(unittest.TestCase):
    """PaymentSessionCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentSessionCreateInput:
        """Test PaymentSessionCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentSessionCreateInput`
        """
        model = PaymentSessionCreateInput()
        if include_optional:
            return PaymentSessionCreateInput(
                billing_address = openapi_client.models.address_input.AddressInput(
                    city = 'London', 
                    company = '0', 
                    country_code = 'GB', 
                    line1 = '10 Downing Street', 
                    line2 = 'Westminster', 
                    name = 'John Doe', 
                    phone_number = '0', 
                    postcode = 'SW1A 2AA', 
                    state = 'Greater London', ),
                customer = openapi_client.models.customer_input.CustomerInput(
                    email = '0', 
                    given_name = 'John', 
                    phone_number = '0', 
                    surname = 'Doe', ),
                discount_total = {"amount":"100.00","currency":"GBP"},
                external_reference = 'REF-12345',
                items = [
                    openapi_client.models.item_input.ItemInput(
                        name = '0', 
                        price = {"amount":"100.00","currency":"GBP"}, 
                        price_with_tax = {"amount":"100.00","currency":"GBP"}, 
                        quantity = '', 
                        restriction = 'ALLOWED', 
                        sku = '0', 
                        tax = {"amount":"100.00","currency":"GBP"}, 
                        total = {"amount":"100.00","currency":"GBP"}, )
                    ],
                payment_capture_type = 'AUTOMATIC_CHECKOUT',
                payment_method = 'FAKE_PAYMENT_METHOD',
                requires_shipping = True,
                session_key = 'DEFC8F15-3BBD-4153-9D6D-3A3D9F06C544',
                shipping_address = openapi_client.models.address_input.AddressInput(
                    city = 'London', 
                    company = '0', 
                    country_code = 'GB', 
                    line1 = '10 Downing Street', 
                    line2 = 'Westminster', 
                    name = 'John Doe', 
                    phone_number = '0', 
                    postcode = 'SW1A 2AA', 
                    state = 'Greater London', ),
                shipping_total = {"amount":"100.00","currency":"GBP"},
                tax_total = {"amount":"100.00","currency":"GBP"},
                total = {"amount":"100.00","currency":"GBP"}
            )
        else:
            return PaymentSessionCreateInput(
                payment_method = 'FAKE_PAYMENT_METHOD',
                session_key = 'DEFC8F15-3BBD-4153-9D6D-3A3D9F06C544',
                total = {"amount":"100.00","currency":"GBP"},
        )
        """

    def testPaymentSessionCreateInput(self):
        """Test PaymentSessionCreateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
