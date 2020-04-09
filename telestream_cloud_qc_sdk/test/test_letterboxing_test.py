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
from telestream_cloud_qc.models.letterboxing_test import LetterboxingTest  # noqa: E501
from telestream_cloud_qc.rest import ApiException

class TestLetterboxingTest(unittest.TestCase):
    """LetterboxingTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LetterboxingTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_qc.models.letterboxing_test.LetterboxingTest()  # noqa: E501
        if include_optional :
            return LetterboxingTest(
                ratio_or_lines = 'Ratio', 
                ratio_horizontal = 56, 
                ratio_vertical = 56, 
                lines_top_and_bottom = 56, 
                lines_left_and_right = 56, 
                tolerance = 56, 
                black_level_default_or_custom = 'Default', 
                black_level = 56, 
                reject_on_error = True, 
                checked = True
            )
        else :
            return LetterboxingTest(
        )

    def testLetterboxingTest(self):
        """Test LetterboxingTest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
