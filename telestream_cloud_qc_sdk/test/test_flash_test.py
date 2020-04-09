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
from telestream_cloud_qc.models.flash_test import FlashTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestFlashTest(unittest.TestCase):
    """FlashTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FlashTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.flash_test.FlashTest()  # noqa: E501
        if include_optional :
            return FlashTest(
                check_type = 'PSEStandard', 
                check_for_extended = True, 
                check_for_red = True, 
                check_for_patterns = True, 
                reject_on_error = True, 
                do_correction = True, 
                checked = True
            )
        else :
            return FlashTest(
        )

    def testFlashTest(self):
        """Test FlashTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
