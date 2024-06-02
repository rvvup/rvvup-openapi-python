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

from openapi_client.models.payment_link import PaymentLink

class TestPaymentLink(unittest.TestCase):
    """PaymentLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentLink:
        """Test PaymentLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentLink`
        """
        model = PaymentLink()
        if include_optional:
            return PaymentLink(
                amount = openapi_client.models.money.Money(
                    amount = '', 
                    currency = '', ),
                checkout_ids = [
                    ''
                    ],
                checkout_template_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                merchant_id = '',
                reference = '',
                reusable = True,
                source = 'API',
                status = 'ACTIVE',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = ''
            )
        else:
            return PaymentLink(
                checkout_ids = [
                    ''
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                merchant_id = '',
                reusable = True,
                source = 'API',
                status = 'ACTIVE',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                url = '',
        )
        """

    def testPaymentLink(self):
        """Test PaymentLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
