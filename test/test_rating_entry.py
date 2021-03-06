# coding: utf-8

"""
    Alfresco Content Services REST API

    **Core API**  Provides access to the core features of Alfresco Content Services.   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.rating_entry import RatingEntry  # noqa: E501
from openapi_client.rest import ApiException

class TestRatingEntry(unittest.TestCase):
    """RatingEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RatingEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.rating_entry.RatingEntry()  # noqa: E501
        if include_optional :
            return RatingEntry(
                entry = openapi_client.models.rating.Rating(
                    id = '0', 
                    aggregate = openapi_client.models.rating_aggregate.Rating_aggregate(
                        number_of_ratings = 56, 
                        average = 56, ), 
                    rated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    my_rating = '0', )
            )
        else :
            return RatingEntry(
                entry = openapi_client.models.rating.Rating(
                    id = '0', 
                    aggregate = openapi_client.models.rating_aggregate.Rating_aggregate(
                        number_of_ratings = 56, 
                        average = 56, ), 
                    rated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    my_rating = '0', ),
        )

    def testRatingEntry(self):
        """Test RatingEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
