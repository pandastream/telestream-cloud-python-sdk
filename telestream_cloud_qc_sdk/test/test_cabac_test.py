# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_qc
from telestream_cloud_qc.models.cabac_test import CabacTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestCabacTest(unittest.TestCase):
    """CabacTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CabacTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.cabac_test.CabacTest()  # noqa: E501
        if include_optional :
            return CabacTest(
                cabac_required = True, 
                reject_on_error = True, 
                checked = True
            )
        else :
            return CabacTest(
        )

    def testCabacTest(self):
        """Test CabacTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
