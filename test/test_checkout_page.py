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

from openapi_client.models.checkout_page import CheckoutPage

class TestCheckoutPage(unittest.TestCase):
    """CheckoutPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckoutPage:
        """Test CheckoutPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckoutPage`
        """
        model = CheckoutPage()
        if include_optional:
            return CheckoutPage(
                pageable = openapi_client.models.pageable.Pageable(
                    limit = 56, 
                    offset = 56, ),
                results = [
                    openapi_client.models.checkout.Checkout(
                        amount = openapi_client.models.money.Money(
                            amount = '', 
                            currency = '', ), 
                        billing_address = openapi_client.models.address.Address(
                            city = '', 
                            company = '', 
                            country_code = '', 
                            line1 = '', 
                            line2 = '', 
                            name = '', 
                            phone_number = '', 
                            postcode = '', 
                            state = '', ), 
                        checkout_template_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customer = openapi_client.models.customer.Customer(
                            email = '', 
                            given_name = '', 
                            phone_number = '', 
                            surname = '', ), 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        merchant_id = '', 
                        metadata = {
                            'key' : ''
                            }, 
                        payment_link_id = '', 
                        payment_session_ids = [
                            ''
                            ], 
                        reference = '', 
                        source = 'API', 
                        status = 'ACTIVE', 
                        success_url = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', )
                    ],
                total = 56
            )
        else:
            return CheckoutPage(
                pageable = openapi_client.models.pageable.Pageable(
                    limit = 56, 
                    offset = 56, ),
                results = [
                    openapi_client.models.checkout.Checkout(
                        amount = openapi_client.models.money.Money(
                            amount = '', 
                            currency = '', ), 
                        billing_address = openapi_client.models.address.Address(
                            city = '', 
                            company = '', 
                            country_code = '', 
                            line1 = '', 
                            line2 = '', 
                            name = '', 
                            phone_number = '', 
                            postcode = '', 
                            state = '', ), 
                        checkout_template_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        customer = openapi_client.models.customer.Customer(
                            email = '', 
                            given_name = '', 
                            phone_number = '', 
                            surname = '', ), 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        merchant_id = '', 
                        metadata = {
                            'key' : ''
                            }, 
                        payment_link_id = '', 
                        payment_session_ids = [
                            ''
                            ], 
                        reference = '', 
                        source = 'API', 
                        status = 'ACTIVE', 
                        success_url = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        url = '', )
                    ],
                total = 56,
        )
        """

    def testCheckoutPage(self):
        """Test CheckoutPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
