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


class AudioLoudnessMtest(object):
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
        'loudness_level': 'float',
        'channels': 'Channels',
        'reject_on_error': 'bool',
        'do_correction': 'bool'
    }

    attribute_map = {
        'loudness_level': 'loudness_level',
        'channels': 'channels',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction'
    }

    def __init__(self, loudness_level=None, channels=None, reject_on_error=None, do_correction=None, local_vars_configuration=None):  # noqa: E501
        """AudioLoudnessMtest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._loudness_level = None
        self._channels = None
        self._reject_on_error = None
        self._do_correction = None
        self.discriminator = None

        if loudness_level is not None:
            self.loudness_level = loudness_level
        if channels is not None:
            self.channels = channels
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction

    @property
    def loudness_level(self):
        """Gets the loudness_level of this AudioLoudnessMtest.  # noqa: E501


        :return: The loudness_level of this AudioLoudnessMtest.  # noqa: E501
        :rtype: float
        """
        return self._loudness_level

    @loudness_level.setter
    def loudness_level(self, loudness_level):
        """Sets the loudness_level of this AudioLoudnessMtest.


        :param loudness_level: The loudness_level of this AudioLoudnessMtest.  # noqa: E501
        :type: float
        """

        self._loudness_level = loudness_level

    @property
    def channels(self):
        """Gets the channels of this AudioLoudnessMtest.  # noqa: E501


        :return: The channels of this AudioLoudnessMtest.  # noqa: E501
        :rtype: Channels
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioLoudnessMtest.


        :param channels: The channels of this AudioLoudnessMtest.  # noqa: E501
        :type: Channels
        """

        self._channels = channels

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this AudioLoudnessMtest.  # noqa: E501


        :return: The reject_on_error of this AudioLoudnessMtest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this AudioLoudnessMtest.


        :param reject_on_error: The reject_on_error of this AudioLoudnessMtest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this AudioLoudnessMtest.  # noqa: E501


        :return: The do_correction of this AudioLoudnessMtest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this AudioLoudnessMtest.


        :param do_correction: The do_correction of this AudioLoudnessMtest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

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
        if not isinstance(other, AudioLoudnessMtest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudioLoudnessMtest):
            return True

        return self.to_dict() != other.to_dict()
