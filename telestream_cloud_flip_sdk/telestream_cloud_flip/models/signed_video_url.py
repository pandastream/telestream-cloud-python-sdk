# coding: utf-8

"""
    Flip API

    Description  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SignedVideoUrl(object):
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
        'signed_url': 'str'
    }

    attribute_map = {
        'signed_url': 'signed_url'
    }

    def __init__(self, signed_url=None):  # noqa: E501
        """SignedVideoUrl - a model defined in Swagger"""  # noqa: E501

        self._signed_url = None
        self.discriminator = None

        if signed_url is not None:
            self.signed_url = signed_url

    @property
    def signed_url(self):
        """Gets the signed_url of this SignedVideoUrl.  # noqa: E501

        An URL pointing to the Video file. It contains a valid authentication token.  # noqa: E501

        :return: The signed_url of this SignedVideoUrl.  # noqa: E501
        :rtype: str
        """
        return self._signed_url

    @signed_url.setter
    def signed_url(self, signed_url):
        """Sets the signed_url of this SignedVideoUrl.

        An URL pointing to the Video file. It contains a valid authentication token.  # noqa: E501

        :param signed_url: The signed_url of this SignedVideoUrl.  # noqa: E501
        :type: str
        """

        self._signed_url = signed_url

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
        if not isinstance(other, SignedVideoUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
