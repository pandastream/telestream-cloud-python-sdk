# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_qc.models.job_details_result import JobDetailsResult  # noqa: F401,E501
from telestream_cloud_qc.models.media import Media  # noqa: F401,E501


class JobDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'media': 'list[Media]',
        'result': 'JobDetailsResult'
    }

    attribute_map = {
        'media': 'media',
        'result': 'result'
    }

    def __init__(self, media=None, result=None):  # noqa: E501
        """JobDetails - a model defined in Swagger"""  # noqa: E501

        self._media = None
        self._result = None
        self.discriminator = None

        if media is not None:
            self.media = media
        if result is not None:
            self.result = result

    @property
    def media(self):
        """Gets the media of this JobDetails.  # noqa: E501


        :return: The media of this JobDetails.  # noqa: E501
        :rtype: list[Media]
        """
        return self._media

    @media.setter
    def media(self, media):
        """Sets the media of this JobDetails.


        :param media: The media of this JobDetails.  # noqa: E501
        :type: list[Media]
        """

        self._media = media

    @property
    def result(self):
        """Gets the result of this JobDetails.  # noqa: E501


        :return: The result of this JobDetails.  # noqa: E501
        :rtype: JobDetailsResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this JobDetails.


        :param result: The result of this JobDetails.  # noqa: E501
        :type: JobDetailsResult
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
