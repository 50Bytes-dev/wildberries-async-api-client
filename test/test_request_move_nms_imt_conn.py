# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.request_move_nms_imt_conn import RequestMoveNmsImtConn

class TestRequestMoveNmsImtConn(unittest.TestCase):
    """RequestMoveNmsImtConn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestMoveNmsImtConn:
        """Test RequestMoveNmsImtConn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestMoveNmsImtConn`
        """
        model = RequestMoveNmsImtConn()
        if include_optional:
            return RequestMoveNmsImtConn(
                target_imt = 123,
                nm_ids = [837459235,828572090]
            )
        else:
            return RequestMoveNmsImtConn(
                target_imt = 123,
                nm_ids = [837459235,828572090],
        )
        """

    def testRequestMoveNmsImtConn(self):
        """Test RequestMoveNmsImtConn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
