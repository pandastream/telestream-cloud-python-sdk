# coding: utf-8

"""
    Flip API

    Flip  # noqa: E501

    The version of the OpenAPI document: 3.1
    Contact: cloudsupport@telestream.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_flip.configuration import Configuration


class Video(object):
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
        'id': 'str',
        'audio_bitrate': 'int',
        'audio_channels': 'int',
        'audio_codec': 'str',
        'audio_sample_rate': 'int',
        'created_at': 'str',
        'duration': 'int',
        'encodings_count': 'int',
        'error_class': 'str',
        'error_message': 'str',
        'extname': 'str',
        'file_size': 'int',
        'fps': 'float',
        'height': 'int',
        'width': 'int',
        'mime_type': 'str',
        'original_filename': 'str',
        'path': 'str',
        'payload': 'str',
        'source_url': 'str',
        'status': 'str',
        'updated_at': 'str',
        'video_bitrate': 'int',
        'video_codec': 'str'
    }

    attribute_map = {
        'id': 'id',
        'audio_bitrate': 'audio_bitrate',
        'audio_channels': 'audio_channels',
        'audio_codec': 'audio_codec',
        'audio_sample_rate': 'audio_sample_rate',
        'created_at': 'created_at',
        'duration': 'duration',
        'encodings_count': 'encodings_count',
        'error_class': 'error_class',
        'error_message': 'error_message',
        'extname': 'extname',
        'file_size': 'file_size',
        'fps': 'fps',
        'height': 'height',
        'width': 'width',
        'mime_type': 'mime_type',
        'original_filename': 'original_filename',
        'path': 'path',
        'payload': 'payload',
        'source_url': 'source_url',
        'status': 'status',
        'updated_at': 'updated_at',
        'video_bitrate': 'video_bitrate',
        'video_codec': 'video_codec'
    }

    def __init__(self, id=None, audio_bitrate=None, audio_channels=None, audio_codec=None, audio_sample_rate=None, created_at=None, duration=None, encodings_count=None, error_class=None, error_message=None, extname=None, file_size=None, fps=None, height=None, width=None, mime_type=None, original_filename=None, path=None, payload=None, source_url=None, status=None, updated_at=None, video_bitrate=None, video_codec=None, local_vars_configuration=None):  # noqa: E501
        """Video - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._audio_bitrate = None
        self._audio_channels = None
        self._audio_codec = None
        self._audio_sample_rate = None
        self._created_at = None
        self._duration = None
        self._encodings_count = None
        self._error_class = None
        self._error_message = None
        self._extname = None
        self._file_size = None
        self._fps = None
        self._height = None
        self._width = None
        self._mime_type = None
        self._original_filename = None
        self._path = None
        self._payload = None
        self._source_url = None
        self._status = None
        self._updated_at = None
        self._video_bitrate = None
        self._video_codec = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.audio_bitrate = audio_bitrate
        self.audio_channels = audio_channels
        self.audio_codec = audio_codec
        self.audio_sample_rate = audio_sample_rate
        if created_at is not None:
            self.created_at = created_at
        self.duration = duration
        if encodings_count is not None:
            self.encodings_count = encodings_count
        self.error_class = error_class
        self.error_message = error_message
        self.extname = extname
        self.file_size = file_size
        self.fps = fps
        self.height = height
        self.width = width
        self.mime_type = mime_type
        self.original_filename = original_filename
        if path is not None:
            self.path = path
        self.payload = payload
        self.source_url = source_url
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec

    @property
    def id(self):
        """Gets the id of this Video.  # noqa: E501

        A unique identifier of the Video.  # noqa: E501

        :return: The id of this Video.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Video.

        A unique identifier of the Video.  # noqa: E501

        :param id: The id of this Video.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def audio_bitrate(self):
        """Gets the audio_bitrate of this Video.  # noqa: E501

        audio bitrate (in bits/s)  # noqa: E501

        :return: The audio_bitrate of this Video.  # noqa: E501
        :rtype: int
        """
        return self._audio_bitrate

    @audio_bitrate.setter
    def audio_bitrate(self, audio_bitrate):
        """Sets the audio_bitrate of this Video.

        audio bitrate (in bits/s)  # noqa: E501

        :param audio_bitrate: The audio_bitrate of this Video.  # noqa: E501
        :type: int
        """

        self._audio_bitrate = audio_bitrate

    @property
    def audio_channels(self):
        """Gets the audio_channels of this Video.  # noqa: E501

        A number of audio channels.  # noqa: E501

        :return: The audio_channels of this Video.  # noqa: E501
        :rtype: int
        """
        return self._audio_channels

    @audio_channels.setter
    def audio_channels(self, audio_channels):
        """Sets the audio_channels of this Video.

        A number of audio channels.  # noqa: E501

        :param audio_channels: The audio_channels of this Video.  # noqa: E501
        :type: int
        """

        self._audio_channels = audio_channels

    @property
    def audio_codec(self):
        """Gets the audio_codec of this Video.  # noqa: E501

        A codec that has been used to encode audio streams.  # noqa: E501

        :return: The audio_codec of this Video.  # noqa: E501
        :rtype: str
        """
        return self._audio_codec

    @audio_codec.setter
    def audio_codec(self, audio_codec):
        """Sets the audio_codec of this Video.

        A codec that has been used to encode audio streams.  # noqa: E501

        :param audio_codec: The audio_codec of this Video.  # noqa: E501
        :type: str
        """

        self._audio_codec = audio_codec

    @property
    def audio_sample_rate(self):
        """Gets the audio_sample_rate of this Video.  # noqa: E501

        A number of samples of audio carried per second.  # noqa: E501

        :return: The audio_sample_rate of this Video.  # noqa: E501
        :rtype: int
        """
        return self._audio_sample_rate

    @audio_sample_rate.setter
    def audio_sample_rate(self, audio_sample_rate):
        """Sets the audio_sample_rate of this Video.

        A number of samples of audio carried per second.  # noqa: E501

        :param audio_sample_rate: The audio_sample_rate of this Video.  # noqa: E501
        :type: int
        """

        self._audio_sample_rate = audio_sample_rate

    @property
    def created_at(self):
        """Gets the created_at of this Video.  # noqa: E501

        A date and time when the Video has been created.  # noqa: E501

        :return: The created_at of this Video.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Video.

        A date and time when the Video has been created.  # noqa: E501

        :param created_at: The created_at of this Video.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def duration(self):
        """Gets the duration of this Video.  # noqa: E501

        A duration of the video in seconds.  # noqa: E501

        :return: The duration of this Video.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Video.

        A duration of the video in seconds.  # noqa: E501

        :param duration: The duration of this Video.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def encodings_count(self):
        """Gets the encodings_count of this Video.  # noqa: E501

        A number of related Encoding objects.  # noqa: E501

        :return: The encodings_count of this Video.  # noqa: E501
        :rtype: int
        """
        return self._encodings_count

    @encodings_count.setter
    def encodings_count(self, encodings_count):
        """Sets the encodings_count of this Video.

        A number of related Encoding objects.  # noqa: E501

        :param encodings_count: The encodings_count of this Video.  # noqa: E501
        :type: int
        """

        self._encodings_count = encodings_count

    @property
    def error_class(self):
        """Gets the error_class of this Video.  # noqa: E501

        A class of an error that has occurred during the encoding process. It is present only if the encoding status is equal to `fail`.  # noqa: E501

        :return: The error_class of this Video.  # noqa: E501
        :rtype: str
        """
        return self._error_class

    @error_class.setter
    def error_class(self, error_class):
        """Sets the error_class of this Video.

        A class of an error that has occurred during the encoding process. It is present only if the encoding status is equal to `fail`.  # noqa: E501

        :param error_class: The error_class of this Video.  # noqa: E501
        :type: str
        """

        self._error_class = error_class

    @property
    def error_message(self):
        """Gets the error_message of this Video.  # noqa: E501

        A message that explains why the encoding process has resulted in an error. It is present only if the encoding status is equal to `fail`.  # noqa: E501

        :return: The error_message of this Video.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Video.

        A message that explains why the encoding process has resulted in an error. It is present only if the encoding status is equal to `fail`.  # noqa: E501

        :param error_message: The error_message of this Video.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def extname(self):
        """Gets the extname of this Video.  # noqa: E501

        Extension of the source file.  # noqa: E501

        :return: The extname of this Video.  # noqa: E501
        :rtype: str
        """
        return self._extname

    @extname.setter
    def extname(self, extname):
        """Sets the extname of this Video.

        Extension of the source file.  # noqa: E501

        :param extname: The extname of this Video.  # noqa: E501
        :type: str
        """

        self._extname = extname

    @property
    def file_size(self):
        """Gets the file_size of this Video.  # noqa: E501

        A size of the source file.  # noqa: E501

        :return: The file_size of this Video.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this Video.

        A size of the source file.  # noqa: E501

        :param file_size: The file_size of this Video.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def fps(self):
        """Gets the fps of this Video.  # noqa: E501

        Number of frames per second.  # noqa: E501

        :return: The fps of this Video.  # noqa: E501
        :rtype: float
        """
        return self._fps

    @fps.setter
    def fps(self, fps):
        """Sets the fps of this Video.

        Number of frames per second.  # noqa: E501

        :param fps: The fps of this Video.  # noqa: E501
        :type: float
        """

        self._fps = fps

    @property
    def height(self):
        """Gets the height of this Video.  # noqa: E501

        Height of the output video.  # noqa: E501

        :return: The height of this Video.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Video.

        Height of the output video.  # noqa: E501

        :param height: The height of this Video.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this Video.  # noqa: E501

        Width of the output video.  # noqa: E501

        :return: The width of this Video.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Video.

        Width of the output video.  # noqa: E501

        :param width: The width of this Video.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def mime_type(self):
        """Gets the mime_type of this Video.  # noqa: E501

        A mime type of the source file.  # noqa: E501

        :return: The mime_type of this Video.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this Video.

        A mime type of the source file.  # noqa: E501

        :param mime_type: The mime_type of this Video.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def original_filename(self):
        """Gets the original_filename of this Video.  # noqa: E501

        A name of the source file.  # noqa: E501

        :return: The original_filename of this Video.  # noqa: E501
        :rtype: str
        """
        return self._original_filename

    @original_filename.setter
    def original_filename(self, original_filename):
        """Sets the original_filename of this Video.

        A name of the source file.  # noqa: E501

        :param original_filename: The original_filename of this Video.  # noqa: E501
        :type: str
        """

        self._original_filename = original_filename

    @property
    def path(self):
        """Gets the path of this Video.  # noqa: E501


        :return: The path of this Video.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Video.


        :param path: The path of this Video.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def payload(self):
        """Gets the payload of this Video.  # noqa: E501

        Payload is an arbitrary text of length 256 or shorter that you can store along the Video. It is typically used to retain an association with one of your own DB record ID.  # noqa: E501

        :return: The payload of this Video.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Video.

        Payload is an arbitrary text of length 256 or shorter that you can store along the Video. It is typically used to retain an association with one of your own DB record ID.  # noqa: E501

        :param payload: The payload of this Video.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def source_url(self):
        """Gets the source_url of this Video.  # noqa: E501

        An URL pointing to the source file.  # noqa: E501

        :return: The source_url of this Video.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this Video.

        An URL pointing to the source file.  # noqa: E501

        :param source_url: The source_url of this Video.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def status(self):
        """Gets the status of this Video.  # noqa: E501

        Determines at what stage of importing process the Video is at the moment.  # noqa: E501

        :return: The status of this Video.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Video.

        Determines at what stage of importing process the Video is at the moment.  # noqa: E501

        :param status: The status of this Video.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this Video.  # noqa: E501

        A date and time when a Video has been updated last time.  # noqa: E501

        :return: The updated_at of this Video.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Video.

        A date and time when a Video has been updated last time.  # noqa: E501

        :param updated_at: The updated_at of this Video.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def video_bitrate(self):
        """Gets the video_bitrate of this Video.  # noqa: E501

        video bitrate (in bits/s)  # noqa: E501

        :return: The video_bitrate of this Video.  # noqa: E501
        :rtype: int
        """
        return self._video_bitrate

    @video_bitrate.setter
    def video_bitrate(self, video_bitrate):
        """Sets the video_bitrate of this Video.

        video bitrate (in bits/s)  # noqa: E501

        :param video_bitrate: The video_bitrate of this Video.  # noqa: E501
        :type: int
        """

        self._video_bitrate = video_bitrate

    @property
    def video_codec(self):
        """Gets the video_codec of this Video.  # noqa: E501

        A codec that has been used to encode the input file's video streams.  # noqa: E501

        :return: The video_codec of this Video.  # noqa: E501
        :rtype: str
        """
        return self._video_codec

    @video_codec.setter
    def video_codec(self, video_codec):
        """Sets the video_codec of this Video.

        A codec that has been used to encode the input file's video streams.  # noqa: E501

        :param video_codec: The video_codec of this Video.  # noqa: E501
        :type: str
        """

        self._video_codec = video_codec

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
        if not isinstance(other, Video):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Video):
            return True

        return self.to_dict() != other.to_dict()
