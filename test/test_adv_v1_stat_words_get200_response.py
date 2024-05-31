# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wildberries_async_api_client.models.adv_v1_stat_words_get200_response import AdvV1StatWordsGet200Response

class TestAdvV1StatWordsGet200Response(unittest.TestCase):
    """AdvV1StatWordsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvV1StatWordsGet200Response:
        """Test AdvV1StatWordsGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvV1StatWordsGet200Response`
        """
        model = AdvV1StatWordsGet200Response()
        if include_optional:
            return AdvV1StatWordsGet200Response(
                words = wildberries_async_api_client.models._adv_v1_stat_words_get_200_response_words._adv_v1_stat_words_get_200_response_words(
                    phrase = [
                        ''
                        ], 
                    strong = [
                        ''
                        ], 
                    excluded = [
                        ''
                        ], 
                    pluse = [
                        ''
                        ], 
                    keywords = [
                        wildberries_async_api_client.models._adv_v1_stat_words_get_200_response_words_keywords_inner._adv_v1_stat_words_get_200_response_words_keywords_inner(
                            keyword = '', 
                            count = 56, )
                        ], 
                    fixed = True, ),
                stat = [
                    wildberries_async_api_client.models._adv_v1_stat_words_get_200_response_stat_inner._adv_v1_stat_words_get_200_response_stat_inner(
                        advert_id = 56, 
                        keyword = '', 
                        advert_name = '', 
                        campaign_name = '', 
                        begin = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        views = 56, 
                        clicks = 56, 
                        frq = 56, 
                        ctr = 1.337, 
                        cpc = 1.337, 
                        duration = 56, 
                        sum = 1.337, )
                    ]
            )
        else:
            return AdvV1StatWordsGet200Response(
        )
        """

    def testAdvV1StatWordsGet200Response(self):
        """Test AdvV1StatWordsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
