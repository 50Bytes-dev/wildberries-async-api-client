# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.event_attachments import EventAttachments

class TestEventAttachments(unittest.TestCase):
    """EventAttachments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventAttachments:
        """Test EventAttachments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventAttachments`
        """
        model = EventAttachments()
        if include_optional:
            return EventAttachments(
                good_card = wildberries_async_api_client.models.good_card.GoodCard(
                    date = '', 
                    need_refund = True, 
                    nm_id = 56, 
                    price = 56, 
                    price_currency = '', 
                    rid = '', 
                    size = '', 
                    status_id = 56, ),
                files = [
                    wildberries_async_api_client.models.file.File(
                        content_type = '', 
                        date = '', 
                        name = '', 
                        url = '', 
                        size = 56, )
                    ],
                images = [
                    wildberries_async_api_client.models.image.Image(
                        date = '', 
                        url = '', )
                    ]
            )
        else:
            return EventAttachments(
        )
        """

    def testEventAttachments(self):
        """Test EventAttachments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
