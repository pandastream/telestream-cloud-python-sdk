# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AudioStream(object):
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
        'duration': 'float',
        'codec': 'str',
        'channels': 'int',
        'program': 'str',
        'bitrate': 'int',
        'sample_rate': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'codec': 'codec',
        'channels': 'channels',
        'program': 'program',
        'bitrate': 'bitrate',
        'sample_rate': 'sample_rate'
    }

    def __init__(self, duration=None, codec=None, channels=None, program=None, bitrate=None, sample_rate=None):  # noqa: E501
        """AudioStream - a model defined in Swagger"""  # noqa: E501

        self._duration = None
        self._codec = None
        self._channels = None
        self._program = None
        self._bitrate = None
        self._sample_rate = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if codec is not None:
            self.codec = codec
        if channels is not None:
            self.channels = channels
        if program is not None:
            self.program = program
        if bitrate is not None:
            self.bitrate = bitrate
        if sample_rate is not None:
            self.sample_rate = sample_rate

    @property
    def duration(self):
        """Gets the duration of this AudioStream.  # noqa: E501

        Audio duration measured in seconds.  # noqa: E501

        :return: The duration of this AudioStream.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AudioStream.

        Audio duration measured in seconds.  # noqa: E501

        :param duration: The duration of this AudioStream.  # noqa: E501
        :type: float
        """

        self._duration = duration

    @property
    def codec(self):
        """Gets the codec of this AudioStream.  # noqa: E501

        Audio codec name.  # noqa: E501

        :return: The codec of this AudioStream.  # noqa: E501
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this AudioStream.

        Audio codec name.  # noqa: E501

        :param codec: The codec of this AudioStream.  # noqa: E501
        :type: str
        """

        self._codec = codec

    @property
    def channels(self):
        """Gets the channels of this AudioStream.  # noqa: E501

        Number of audio channels.  # noqa: E501

        :return: The channels of this AudioStream.  # noqa: E501
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this AudioStream.

        Number of audio channels.  # noqa: E501

        :param channels: The channels of this AudioStream.  # noqa: E501
        :type: int
        """

        self._channels = channels

    @property
    def program(self):
        """Gets the program of this AudioStream.  # noqa: E501


        :return: The program of this AudioStream.  # noqa: E501
        :rtype: str
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this AudioStream.


        :param program: The program of this AudioStream.  # noqa: E501
        :type: str
        """

        self._program = program

    @property
    def bitrate(self):
        """Gets the bitrate of this AudioStream.  # noqa: E501

        Audio bitrate measured in bps  # noqa: E501

        :return: The bitrate of this AudioStream.  # noqa: E501
        :rtype: int
        """
        return self._bitrate

    @bitrate.setter
    def bitrate(self, bitrate):
        """Sets the bitrate of this AudioStream.

        Audio bitrate measured in bps  # noqa: E501

        :param bitrate: The bitrate of this AudioStream.  # noqa: E501
        :type: int
        """

        self._bitrate = bitrate

    @property
    def sample_rate(self):
        """Gets the sample_rate of this AudioStream.  # noqa: E501

        Sample rate measured in Hz.  # noqa: E501

        :return: The sample_rate of this AudioStream.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this AudioStream.

        Sample rate measured in Hz.  # noqa: E501

        :param sample_rate: The sample_rate of this AudioStream.  # noqa: E501
        :type: int
        """

        self._sample_rate = sample_rate

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
        if not isinstance(other, AudioStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
