# coding: utf-8

"""
    Notifications API

    Notifications  # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import telestream_cloud_notifications
from telestream_cloud_notifications.models.subscription import Subscription  # noqa: E501
from telestream_cloud_notifications.rest import ApiException

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = telestream_cloud_notifications.models.subscription.Subscription()  # noqa: E501
        if include_optional :
            return Subscription(
                id = '0', 
                type = '0', 
                topic = telestream_cloud_notifications.models.topic.topic(
                    account = '0', 
                    service = '0', 
                    event = '0', 
                    project = '0', 
                    factory = '0', 
                    workflow = '0', ), 
                params = telestream_cloud_notifications.models.params.params(
                    addresses = [
                        '0'
                        ], 
                    url = '0', 
                    method = 'GET', 
                    retries = 56, 
                    content_type = 'application/json', 
                    topic_arn = '0', 
                    role_arn = '0', 
                    topic_endpoint = '0', 
                    access_key = '0', 
                    project_id = '0', 
                    topic_name = '0', )
            )
        else :
            return Subscription(
                type = '0',
                topic = telestream_cloud_notifications.models.topic.topic(
                    account = '0', 
                    service = '0', 
                    event = '0', 
                    project = '0', 
                    factory = '0', 
                    workflow = '0', ),
                params = telestream_cloud_notifications.models.params.params(
                    addresses = [
                        '0'
                        ], 
                    url = '0', 
                    method = 'GET', 
                    retries = 56, 
                    content_type = 'application/json', 
                    topic_arn = '0', 
                    role_arn = '0', 
                    topic_endpoint = '0', 
                    access_key = '0', 
                    project_id = '0', 
                    topic_name = '0', ),
        )

    def testSubscription(self):
        """Test Subscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
