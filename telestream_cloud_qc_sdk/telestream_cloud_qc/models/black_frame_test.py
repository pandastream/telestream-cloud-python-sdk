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


class BlackFrameTest(object):
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
        'level_default_or_custom': 'DefaultOrCustomType',
        'level': 'int',
        'percentage_of_frame': 'int',
        'start_range_enabled': 'bool',
        'start_time': 'float',
        'end_time': 'float',
        'start_range_tolerance': 'float',
        'time_secs_or_frames': 'SecsOrFramesType',
        'end_range_enabled': 'bool',
        'end_range': 'float',
        'end_range_tolerance': 'float',
        'end_secs_or_frames': 'SecsOrFramesType',
        'not_at_any_other_time': 'bool',
        'max_time_allowed': 'float',
        'max_time_allowed_secs_or_frames': 'SecsOrFramesType',
        'max_time_at_start': 'bool',
        'max_time_allowed_at_start': 'float',
        'max_time_allowed_at_start_secs_or_frames': 'SecsOrFramesType',
        'max_time_at_end': 'bool',
        'max_time_allowed_at_end': 'float',
        'max_time_allowed_at_end_secs_or_frames': 'SecsOrFramesType',
        'reject_on_error': 'bool',
        'do_correction': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'level_default_or_custom': 'level_default_or_custom',
        'level': 'level',
        'percentage_of_frame': 'percentage_of_frame',
        'start_range_enabled': 'start_range_enabled',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'start_range_tolerance': 'start_range_tolerance',
        'time_secs_or_frames': 'time_secs_or_frames',
        'end_range_enabled': 'end_range_enabled',
        'end_range': 'end_range',
        'end_range_tolerance': 'end_range_tolerance',
        'end_secs_or_frames': 'end_secs_or_frames',
        'not_at_any_other_time': 'not_at_any_other_time',
        'max_time_allowed': 'max_time_allowed',
        'max_time_allowed_secs_or_frames': 'max_time_allowed_secs_or_frames',
        'max_time_at_start': 'max_time_at_start',
        'max_time_allowed_at_start': 'max_time_allowed_at_start',
        'max_time_allowed_at_start_secs_or_frames': 'max_time_allowed_at_start_secs_or_frames',
        'max_time_at_end': 'max_time_at_end',
        'max_time_allowed_at_end': 'max_time_allowed_at_end',
        'max_time_allowed_at_end_secs_or_frames': 'max_time_allowed_at_end_secs_or_frames',
        'reject_on_error': 'reject_on_error',
        'do_correction': 'do_correction',
        'checked': 'checked'
    }

    def __init__(self, level_default_or_custom=None, level=None, percentage_of_frame=None, start_range_enabled=None, start_time=None, end_time=None, start_range_tolerance=None, time_secs_or_frames=None, end_range_enabled=None, end_range=None, end_range_tolerance=None, end_secs_or_frames=None, not_at_any_other_time=None, max_time_allowed=None, max_time_allowed_secs_or_frames=None, max_time_at_start=None, max_time_allowed_at_start=None, max_time_allowed_at_start_secs_or_frames=None, max_time_at_end=None, max_time_allowed_at_end=None, max_time_allowed_at_end_secs_or_frames=None, reject_on_error=None, do_correction=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """BlackFrameTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._level_default_or_custom = None
        self._level = None
        self._percentage_of_frame = None
        self._start_range_enabled = None
        self._start_time = None
        self._end_time = None
        self._start_range_tolerance = None
        self._time_secs_or_frames = None
        self._end_range_enabled = None
        self._end_range = None
        self._end_range_tolerance = None
        self._end_secs_or_frames = None
        self._not_at_any_other_time = None
        self._max_time_allowed = None
        self._max_time_allowed_secs_or_frames = None
        self._max_time_at_start = None
        self._max_time_allowed_at_start = None
        self._max_time_allowed_at_start_secs_or_frames = None
        self._max_time_at_end = None
        self._max_time_allowed_at_end = None
        self._max_time_allowed_at_end_secs_or_frames = None
        self._reject_on_error = None
        self._do_correction = None
        self._checked = None
        self.discriminator = None

        if level_default_or_custom is not None:
            self.level_default_or_custom = level_default_or_custom
        if level is not None:
            self.level = level
        if percentage_of_frame is not None:
            self.percentage_of_frame = percentage_of_frame
        if start_range_enabled is not None:
            self.start_range_enabled = start_range_enabled
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if start_range_tolerance is not None:
            self.start_range_tolerance = start_range_tolerance
        if time_secs_or_frames is not None:
            self.time_secs_or_frames = time_secs_or_frames
        if end_range_enabled is not None:
            self.end_range_enabled = end_range_enabled
        if end_range is not None:
            self.end_range = end_range
        if end_range_tolerance is not None:
            self.end_range_tolerance = end_range_tolerance
        if end_secs_or_frames is not None:
            self.end_secs_or_frames = end_secs_or_frames
        if not_at_any_other_time is not None:
            self.not_at_any_other_time = not_at_any_other_time
        if max_time_allowed is not None:
            self.max_time_allowed = max_time_allowed
        if max_time_allowed_secs_or_frames is not None:
            self.max_time_allowed_secs_or_frames = max_time_allowed_secs_or_frames
        if max_time_at_start is not None:
            self.max_time_at_start = max_time_at_start
        if max_time_allowed_at_start is not None:
            self.max_time_allowed_at_start = max_time_allowed_at_start
        if max_time_allowed_at_start_secs_or_frames is not None:
            self.max_time_allowed_at_start_secs_or_frames = max_time_allowed_at_start_secs_or_frames
        if max_time_at_end is not None:
            self.max_time_at_end = max_time_at_end
        if max_time_allowed_at_end is not None:
            self.max_time_allowed_at_end = max_time_allowed_at_end
        if max_time_allowed_at_end_secs_or_frames is not None:
            self.max_time_allowed_at_end_secs_or_frames = max_time_allowed_at_end_secs_or_frames
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if do_correction is not None:
            self.do_correction = do_correction
        if checked is not None:
            self.checked = checked

    @property
    def level_default_or_custom(self):
        """Gets the level_default_or_custom of this BlackFrameTest.  # noqa: E501


        :return: The level_default_or_custom of this BlackFrameTest.  # noqa: E501
        :rtype: DefaultOrCustomType
        """
        return self._level_default_or_custom

    @level_default_or_custom.setter
    def level_default_or_custom(self, level_default_or_custom):
        """Sets the level_default_or_custom of this BlackFrameTest.


        :param level_default_or_custom: The level_default_or_custom of this BlackFrameTest.  # noqa: E501
        :type: DefaultOrCustomType
        """

        self._level_default_or_custom = level_default_or_custom

    @property
    def level(self):
        """Gets the level of this BlackFrameTest.  # noqa: E501


        :return: The level of this BlackFrameTest.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this BlackFrameTest.


        :param level: The level of this BlackFrameTest.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def percentage_of_frame(self):
        """Gets the percentage_of_frame of this BlackFrameTest.  # noqa: E501


        :return: The percentage_of_frame of this BlackFrameTest.  # noqa: E501
        :rtype: int
        """
        return self._percentage_of_frame

    @percentage_of_frame.setter
    def percentage_of_frame(self, percentage_of_frame):
        """Sets the percentage_of_frame of this BlackFrameTest.


        :param percentage_of_frame: The percentage_of_frame of this BlackFrameTest.  # noqa: E501
        :type: int
        """

        self._percentage_of_frame = percentage_of_frame

    @property
    def start_range_enabled(self):
        """Gets the start_range_enabled of this BlackFrameTest.  # noqa: E501


        :return: The start_range_enabled of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._start_range_enabled

    @start_range_enabled.setter
    def start_range_enabled(self, start_range_enabled):
        """Sets the start_range_enabled of this BlackFrameTest.


        :param start_range_enabled: The start_range_enabled of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._start_range_enabled = start_range_enabled

    @property
    def start_time(self):
        """Gets the start_time of this BlackFrameTest.  # noqa: E501


        :return: The start_time of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BlackFrameTest.


        :param start_time: The start_time of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this BlackFrameTest.  # noqa: E501


        :return: The end_time of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BlackFrameTest.


        :param end_time: The end_time of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._end_time = end_time

    @property
    def start_range_tolerance(self):
        """Gets the start_range_tolerance of this BlackFrameTest.  # noqa: E501


        :return: The start_range_tolerance of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._start_range_tolerance

    @start_range_tolerance.setter
    def start_range_tolerance(self, start_range_tolerance):
        """Sets the start_range_tolerance of this BlackFrameTest.


        :param start_range_tolerance: The start_range_tolerance of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._start_range_tolerance = start_range_tolerance

    @property
    def time_secs_or_frames(self):
        """Gets the time_secs_or_frames of this BlackFrameTest.  # noqa: E501


        :return: The time_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._time_secs_or_frames

    @time_secs_or_frames.setter
    def time_secs_or_frames(self, time_secs_or_frames):
        """Sets the time_secs_or_frames of this BlackFrameTest.


        :param time_secs_or_frames: The time_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._time_secs_or_frames = time_secs_or_frames

    @property
    def end_range_enabled(self):
        """Gets the end_range_enabled of this BlackFrameTest.  # noqa: E501


        :return: The end_range_enabled of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._end_range_enabled

    @end_range_enabled.setter
    def end_range_enabled(self, end_range_enabled):
        """Sets the end_range_enabled of this BlackFrameTest.


        :param end_range_enabled: The end_range_enabled of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._end_range_enabled = end_range_enabled

    @property
    def end_range(self):
        """Gets the end_range of this BlackFrameTest.  # noqa: E501


        :return: The end_range of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._end_range

    @end_range.setter
    def end_range(self, end_range):
        """Sets the end_range of this BlackFrameTest.


        :param end_range: The end_range of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._end_range = end_range

    @property
    def end_range_tolerance(self):
        """Gets the end_range_tolerance of this BlackFrameTest.  # noqa: E501


        :return: The end_range_tolerance of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._end_range_tolerance

    @end_range_tolerance.setter
    def end_range_tolerance(self, end_range_tolerance):
        """Sets the end_range_tolerance of this BlackFrameTest.


        :param end_range_tolerance: The end_range_tolerance of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._end_range_tolerance = end_range_tolerance

    @property
    def end_secs_or_frames(self):
        """Gets the end_secs_or_frames of this BlackFrameTest.  # noqa: E501


        :return: The end_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._end_secs_or_frames

    @end_secs_or_frames.setter
    def end_secs_or_frames(self, end_secs_or_frames):
        """Sets the end_secs_or_frames of this BlackFrameTest.


        :param end_secs_or_frames: The end_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._end_secs_or_frames = end_secs_or_frames

    @property
    def not_at_any_other_time(self):
        """Gets the not_at_any_other_time of this BlackFrameTest.  # noqa: E501


        :return: The not_at_any_other_time of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._not_at_any_other_time

    @not_at_any_other_time.setter
    def not_at_any_other_time(self, not_at_any_other_time):
        """Sets the not_at_any_other_time of this BlackFrameTest.


        :param not_at_any_other_time: The not_at_any_other_time of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._not_at_any_other_time = not_at_any_other_time

    @property
    def max_time_allowed(self):
        """Gets the max_time_allowed of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._max_time_allowed

    @max_time_allowed.setter
    def max_time_allowed(self, max_time_allowed):
        """Sets the max_time_allowed of this BlackFrameTest.


        :param max_time_allowed: The max_time_allowed of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._max_time_allowed = max_time_allowed

    @property
    def max_time_allowed_secs_or_frames(self):
        """Gets the max_time_allowed_secs_or_frames of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._max_time_allowed_secs_or_frames

    @max_time_allowed_secs_or_frames.setter
    def max_time_allowed_secs_or_frames(self, max_time_allowed_secs_or_frames):
        """Sets the max_time_allowed_secs_or_frames of this BlackFrameTest.


        :param max_time_allowed_secs_or_frames: The max_time_allowed_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._max_time_allowed_secs_or_frames = max_time_allowed_secs_or_frames

    @property
    def max_time_at_start(self):
        """Gets the max_time_at_start of this BlackFrameTest.  # noqa: E501


        :return: The max_time_at_start of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_time_at_start

    @max_time_at_start.setter
    def max_time_at_start(self, max_time_at_start):
        """Sets the max_time_at_start of this BlackFrameTest.


        :param max_time_at_start: The max_time_at_start of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._max_time_at_start = max_time_at_start

    @property
    def max_time_allowed_at_start(self):
        """Gets the max_time_allowed_at_start of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed_at_start of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._max_time_allowed_at_start

    @max_time_allowed_at_start.setter
    def max_time_allowed_at_start(self, max_time_allowed_at_start):
        """Sets the max_time_allowed_at_start of this BlackFrameTest.


        :param max_time_allowed_at_start: The max_time_allowed_at_start of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._max_time_allowed_at_start = max_time_allowed_at_start

    @property
    def max_time_allowed_at_start_secs_or_frames(self):
        """Gets the max_time_allowed_at_start_secs_or_frames of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed_at_start_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._max_time_allowed_at_start_secs_or_frames

    @max_time_allowed_at_start_secs_or_frames.setter
    def max_time_allowed_at_start_secs_or_frames(self, max_time_allowed_at_start_secs_or_frames):
        """Sets the max_time_allowed_at_start_secs_or_frames of this BlackFrameTest.


        :param max_time_allowed_at_start_secs_or_frames: The max_time_allowed_at_start_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._max_time_allowed_at_start_secs_or_frames = max_time_allowed_at_start_secs_or_frames

    @property
    def max_time_at_end(self):
        """Gets the max_time_at_end of this BlackFrameTest.  # noqa: E501


        :return: The max_time_at_end of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._max_time_at_end

    @max_time_at_end.setter
    def max_time_at_end(self, max_time_at_end):
        """Sets the max_time_at_end of this BlackFrameTest.


        :param max_time_at_end: The max_time_at_end of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._max_time_at_end = max_time_at_end

    @property
    def max_time_allowed_at_end(self):
        """Gets the max_time_allowed_at_end of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed_at_end of this BlackFrameTest.  # noqa: E501
        :rtype: float
        """
        return self._max_time_allowed_at_end

    @max_time_allowed_at_end.setter
    def max_time_allowed_at_end(self, max_time_allowed_at_end):
        """Sets the max_time_allowed_at_end of this BlackFrameTest.


        :param max_time_allowed_at_end: The max_time_allowed_at_end of this BlackFrameTest.  # noqa: E501
        :type: float
        """

        self._max_time_allowed_at_end = max_time_allowed_at_end

    @property
    def max_time_allowed_at_end_secs_or_frames(self):
        """Gets the max_time_allowed_at_end_secs_or_frames of this BlackFrameTest.  # noqa: E501


        :return: The max_time_allowed_at_end_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :rtype: SecsOrFramesType
        """
        return self._max_time_allowed_at_end_secs_or_frames

    @max_time_allowed_at_end_secs_or_frames.setter
    def max_time_allowed_at_end_secs_or_frames(self, max_time_allowed_at_end_secs_or_frames):
        """Sets the max_time_allowed_at_end_secs_or_frames of this BlackFrameTest.


        :param max_time_allowed_at_end_secs_or_frames: The max_time_allowed_at_end_secs_or_frames of this BlackFrameTest.  # noqa: E501
        :type: SecsOrFramesType
        """

        self._max_time_allowed_at_end_secs_or_frames = max_time_allowed_at_end_secs_or_frames

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this BlackFrameTest.  # noqa: E501


        :return: The reject_on_error of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this BlackFrameTest.


        :param reject_on_error: The reject_on_error of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def do_correction(self):
        """Gets the do_correction of this BlackFrameTest.  # noqa: E501


        :return: The do_correction of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._do_correction

    @do_correction.setter
    def do_correction(self, do_correction):
        """Sets the do_correction of this BlackFrameTest.


        :param do_correction: The do_correction of this BlackFrameTest.  # noqa: E501
        :type: bool
        """

        self._do_correction = do_correction

    @property
    def checked(self):
        """Gets the checked of this BlackFrameTest.  # noqa: E501


        :return: The checked of this BlackFrameTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this BlackFrameTest.


        :param checked: The checked of this BlackFrameTest.  # noqa: E501
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
        if not isinstance(other, BlackFrameTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlackFrameTest):
            return True

        return self.to_dict() != other.to_dict()
