# coding: utf-8

"""
    Tts API

    Description  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FragmentVariant(object):
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
        'fragment': 'str',
        'confidence': 'float'
    }

    attribute_map = {
        'fragment': 'fragment',
        'confidence': 'confidence'
    }

    def __init__(self, fragment=None, confidence=None):  # noqa: E501
        """FragmentVariant - a model defined in Swagger"""  # noqa: E501

        self._fragment = None
        self._confidence = None
        self.discriminator = None

        if fragment is not None:
            self.fragment = fragment
        if confidence is not None:
            self.confidence = confidence

    @property
    def fragment(self):
        """Gets the fragment of this FragmentVariant.  # noqa: E501

        An alternative hypothesis for a fragment from the input audio.  # noqa: E501

        :return: The fragment of this FragmentVariant.  # noqa: E501
        :rtype: str
        """
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        """Sets the fragment of this FragmentVariant.

        An alternative hypothesis for a fragment from the input audio.  # noqa: E501

        :param fragment: The fragment of this FragmentVariant.  # noqa: E501
        :type: str
        """

        self._fragment = fragment

    @property
    def confidence(self):
        """Gets the confidence of this FragmentVariant.  # noqa: E501

        The confidence score of the fragment variant hypothesis in the range of 0 to 1.  # noqa: E501

        :return: The confidence of this FragmentVariant.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this FragmentVariant.

        The confidence score of the fragment variant hypothesis in the range of 0 to 1.  # noqa: E501

        :param confidence: The confidence of this FragmentVariant.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

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
        if not isinstance(other, FragmentVariant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
