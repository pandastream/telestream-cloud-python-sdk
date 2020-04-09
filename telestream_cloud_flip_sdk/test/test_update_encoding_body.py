# coding: utf-8

"""
    Flip API

    Flip  # noqa: E501

    The version of the OpenAPI document: 3.1
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_flip
from telestream_cloud_flip.models.update_encoding_body import UpdateEncodingBody  # noqa: E501
from telestream_cloud_flip.rest import ApiException

class TestUpdateEncodingBody(unittest.TestCase):
    """UpdateEncodingBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateEncodingBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_flip.models.update_encoding_body.UpdateEncodingBody()  # noqa: E501
        if include_optional :
            return UpdateEncodingBody(
                profile_id = '0', 
                profile_name = '0'
            )
        else :
            return UpdateEncodingBody(
        )

    def testUpdateEncodingBody(self):
        """Test UpdateEncodingBody"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
