# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.post_template_ok import PostTemplateOK

class TestPostTemplateOK(unittest.TestCase):
    """PostTemplateOK unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostTemplateOK:
        """Test PostTemplateOK
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostTemplateOK`
        """
        model = PostTemplateOK()
        if include_optional:
            return PostTemplateOK(
                data = wildberries_async_api_client.models.post_template_ok_data.PostTemplateOK_data(
                    id = '', ),
                error = True,
                error_text = '',
                additional_errors = [
                    ''
                    ]
            )
        else:
            return PostTemplateOK(
        )
        """

    def testPostTemplateOK(self):
        """Test PostTemplateOK"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
