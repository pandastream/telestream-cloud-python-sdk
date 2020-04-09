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


class VideoSegmentDetectionTest(object):
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
        'black_level_default_or_custom': 'DefaultOrCustomType',
        'black_level': 'int',
        'percentage_of_frame': 'int',
        'min_duration_required': 'float',
        'min_duration_required_secs_or_frames': 'SecsOrFramesType',
        'require_digital_silence': 'bool',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'black_level_default_or_custom': 'black_level_default_or_custom',
        'black_level': 'black_level',
        'percentage_of_frame': 'percentage_of_frame',
        'min_duration_required': 'min_duration_required',
        'min_duration_required_secs_or_frames': 'min_duration_required_secs_or_frames',
        'require_digital_silence': 'require_digital_silence',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, black_level_default_or_custom=None, black_level=None, percentage_of_frame=None, min_duration_required=None, min_duration_required_secs_or_frames=None, require_digital_silence=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """VideoSegmentDetectionTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._black_level_default_or_custom = None
        self._black_level = None
        self._percentage_of_frame = None
        self._min_duration_required = None
        self._min_duration_required_secs_or_frames = None
        self._require_digital_silence = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if black_level_default_or_custom is not None:
            self.black_level_default_or_custom = black_level_default_or_custom
        if black_level is not None:
            self.black_level = black_level
        if percentage_of_frame is not None:
            self.percentage_of_frame = percentage_of_frame
        if min_duration_required is not None:
            self.min_duration_required = min_duration_required
        if min_duration_required_secs_or_frames is not None:
            self.min_duration_required_secs_or_frames = min_duration_required_secs_or_frames
        if require_digital_silence is not None:
            self.require_digital_silence = require_digital_silence
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def black_level_default_or_custom(self):
        """Gets the black_level_default_or_custom of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The black_level_default_or_custom of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: DefaultOrCustomType
        """
        return self._black_level_default_or_custom

    @black_level_default_or_custom.setter
    def black_level_default_or_custom(self, black_level_default_or_custom):
        """Sets the black_level_default_or_custom of this VideoSegmentDetectionTest.


        :param black_level_default_or_custom: The black_level_default_or_custom of this VideoSegmentDetectionTest.  # noqa: E501
        :type: DefaultOrCustomType
        """

        self._black_level_default_or_custom = black_level_default_or_custom

    @property
    def black_level(self):
        """Gets the black_level of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The black_level of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: int
        """
        return self._black_level

    @black_level.setter
    def black_level(self, black_level):
        """Sets the black_level of this VideoSegmentDetectionTest.


        :param black_level: The black_level of this VideoSegmentDetectionTest.  # noqa: E501
        :type: int
        """

        self._black_level = black_level

    @property
    def percentage_of_frame(self):
        """Gets the percentage_of_frame of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The percentage_of_frame of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: int
        """
        return self._percentage_of_frame

    @percentage_of_frame.setter
    def percentage_of_frame(self, percentage_of_frame):
        """Sets the percentage_of_frame of this VideoSegmentDetectionTest.


        :param percentage_of_frame: The percentage_of_frame of this VideoSegmentDetectionTest.  # noqa: E501
        :type: int
        """

        self._percentage_of_frame = percentage_of_frame

    @property
    def min_duration_required(self):
        """Gets the min_duration_required of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The min_duration_required of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: float
        """
        return self._min_duration_required

    @min_duration_required.setter
    def min_duration_required(self, min_duration_required):
        """Sets the min_duration_required of this VideoSegmentDetectionTest.


        :param min_duration_required: The min_duration_required of this VideoSegmentDetectionTest.  # noqa: E501
        :type: float
        """

        self._min_duration_required = min_duration_required

    @property
    def min_duration_required_secs_or_frames(self):
        """Gets the min_duration_required_secs_or_frames of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The min_duration_required_secs_or_frames of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._min_duration_required_secs_or_frames

    @min_duration_required_secs_or_frames.setter
    def min_duration_required_secs_or_frames(self, min_duration_required_secs_or_frames):
        """Sets the min_duration_required_secs_or_frames of this VideoSegmentDetectionTest.


        :param min_duration_required_secs_or_frames: The min_duration_required_secs_or_frames of this VideoSegmentDetectionTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._min_duration_required_secs_or_frames = min_duration_required_secs_or_frames

    @property
    def require_digital_silence(self):
        """Gets the require_digital_silence of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The require_digital_silence of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._require_digital_silence

    @require_digital_silence.setter
    def require_digital_silence(self, require_digital_silence):
        """Sets the require_digital_silence of this VideoSegmentDetectionTest.


        :param require_digital_silence: The require_digital_silence of this VideoSegmentDetectionTest.  # noqa: E501
        :type: bool
        """

        self._require_digital_silence = require_digital_silence

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The reject_on_error of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this VideoSegmentDetectionTest.


        :param reject_on_error: The reject_on_error of this VideoSegmentDetectionTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this VideoSegmentDetectionTest.  # noqa: E501


        :return: The checked of this VideoSegmentDetectionTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this VideoSegmentDetectionTest.


        :param checked: The checked of this VideoSegmentDetectionTest.  # noqa: E501
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
        if not isinstance(other, VideoSegmentDetectionTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoSegmentDetectionTest):
            return True

        return self.to_dict() != other.to_dict()
