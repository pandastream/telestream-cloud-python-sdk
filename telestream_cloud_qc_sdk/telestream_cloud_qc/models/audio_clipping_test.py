# coding: utf-8

"""
    Qc API

    Qc API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_qc.configuration import Configuration


class AudioClippingTest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sensitivity': 'SensitivityType',
        'channels': 'Channels',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'sensitivity': 'sensitivity',
        'channels': 'channels',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, sensitivity=None, channels=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """AudioClippingTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sensitivity = None
        self._channels = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if sensitivity is not None:
            self.sensitivity = sensitivity
        if channels is not None:
            self.channels = channels
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def sensitivity(self):
        """Gets the sensitivity of this AudioClippingTest.  # noqa: E501


        :return: The sensitivity of this AudioClippingTest.  # noqa: E501
        :rtype: SensitivityType
        """
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity):
        """Sets the sensitivity of this AudioClippingTest.


        :param sensitivity: The sensitivity of this AudioClippingTest.  # noqa: E501
        :type: SensitivityType
        """

        self._sensitivity = sensitivity

    @property
    def channels(self):
        """Gets the channels of this AudioClippingTest.  # noqa: E501


        :return: The channels of this AudioClippingTest.  # noqa: E501
        :rtype: Channels
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioClippingTest.


        :param channels: The channels of this AudioClippingTest.  # noqa: E501
        :type: Channels
        """

        self._channels = channels

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this AudioClippingTest.  # noqa: E501


        :return: The reject_on_error of this AudioClippingTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this AudioClippingTest.


        :param reject_on_error: The reject_on_error of this AudioClippingTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this AudioClippingTest.  # noqa: E501


        :return: The checked of this AudioClippingTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this AudioClippingTest.


        :param checked: The checked of this AudioClippingTest.  # noqa: E501
        :type: bool
        """

        self._checked = checked

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, AudioClippingTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudioClippingTest):
            return True

        return self.to_dict() != other.to_dict()
