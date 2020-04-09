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
from telestream_cloud_flip.models.paginated_encodings_collection import PaginatedEncodingsCollection  # noqa: E501
from telestream_cloud_flip.rest import ApiException

class TestPaginatedEncodingsCollection(unittest.TestCase):
    """PaginatedEncodingsCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedEncodingsCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_flip.models.paginated_encodings_collection.PaginatedEncodingsCollection()  # noqa: E501
        if include_optional :
            return PaginatedEncodingsCollection(
                encodings = [
                    telestream_cloud_flip.models.encoding.Encoding(
                        id = '0', 
                        audio_bitrate = 128, 
                        audio_channels = 56, 
                        audio_codec = '0', 
                        audio_sample_rate = 44100, 
                        created_at = '0', 
                        duration = 56, 
                        encoding_progress = 56, 
                        encoding_time = 56, 
                        error_class = '0', 
                        error_message = '0', 
                        external_id = '0', 
                        extname = '0', 
                        file_size = 56, 
                        files = [
                            '0'
                            ], 
                        fps = 1.337, 
                        height = 56, 
                        width = 56, 
                        logfile_url = '0', 
                        mime_type = '0', 
                        parent_encoding_id = '0', 
                        path = '0', 
                        profile_id = '0', 
                        profile_name = '0', 
                        screenshots = [
                            '0'
                            ], 
                        started_encoding_at = '0', 
                        status = '0', 
                        updated_at = '0', 
                        video_bitrate = 56, 
                        video_codec = '0', 
                        video_id = '0', )
                    ], 
                page = 56, 
                per_page = 56, 
                total = 56
            )
        else :
            return PaginatedEncodingsCollection(
                encodings = [
                    telestream_cloud_flip.models.encoding.Encoding(
                        id = '0', 
                        audio_bitrate = 128, 
                        audio_channels = 56, 
                        audio_codec = '0', 
                        audio_sample_rate = 44100, 
                        created_at = '0', 
                        duration = 56, 
                        encoding_progress = 56, 
                        encoding_time = 56, 
                        error_class = '0', 
                        error_message = '0', 
                        external_id = '0', 
                        extname = '0', 
                        file_size = 56, 
                        files = [
                            '0'
                            ], 
                        fps = 1.337, 
                        height = 56, 
                        width = 56, 
                        logfile_url = '0', 
                        mime_type = '0', 
                        parent_encoding_id = '0', 
                        path = '0', 
                        profile_id = '0', 
                        profile_name = '0', 
                        screenshots = [
                            '0'
                            ], 
                        started_encoding_at = '0', 
                        status = '0', 
                        updated_at = '0', 
                        video_bitrate = 56, 
                        video_codec = '0', 
                        video_id = '0', )
                    ],
                page = 56,
                per_page = 56,
                total = 56,
        )

    def testPaginatedEncodingsCollection(self):
        """Test PaginatedEncodingsCollection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
