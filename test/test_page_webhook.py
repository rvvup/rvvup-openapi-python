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

from openapi_client.models.page_webhook import PageWebhook

class TestPageWebhook(unittest.TestCase):
    """PageWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageWebhook:
        """Test PageWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageWebhook`
        """
        model = PageWebhook()
        if include_optional:
            return PageWebhook(
                pageable = openapi_client.models.pageable.Pageable(
                    limit = 56, 
                    offset = 56, ),
                results = [
                    openapi_client.models.webhook.Webhook(
                        headers = {
                            'key' : ''
                            }, 
                        id = '', 
                        merchant_id = '', 
                        status = 'ENABLED', 
                        subscribed_events = [
                            '["PAYMENT_SUCCEEDED"]'
                            ], 
                        url = '', )
                    ],
                total = 56
            )
        else:
            return PageWebhook(
                pageable = openapi_client.models.pageable.Pageable(
                    limit = 56, 
                    offset = 56, ),
                results = [
                    openapi_client.models.webhook.Webhook(
                        headers = {
                            'key' : ''
                            }, 
                        id = '', 
                        merchant_id = '', 
                        status = 'ENABLED', 
                        subscribed_events = [
                            '["PAYMENT_SUCCEEDED"]'
                            ], 
                        url = '', )
                    ],
                total = 56,
        )
        """

    def testPageWebhook(self):
        """Test PageWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
