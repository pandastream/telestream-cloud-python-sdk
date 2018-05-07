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

from telestream_cloud_qc.models.extra_file import ExtraFile  # noqa: F401,E501


class VideoUploadBody(object):
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
        'file_size': 'int',
        'file_name': 'str',
        'extra_files': 'list[ExtraFile]',
        'profiles': 'str',
        'multi_chunk': 'bool'
    }

    attribute_map = {
        'file_size': 'file_size',
        'file_name': 'file_name',
        'extra_files': 'extra_files',
        'profiles': 'profiles',
        'multi_chunk': 'multi_chunk'
    }

    def __init__(self, file_size=None, file_name=None, extra_files=None, profiles=None, multi_chunk=True):  # noqa: E501
        """VideoUploadBody - a model defined in Swagger"""  # noqa: E501

        self._file_size = None
        self._file_name = None
        self._extra_files = None
        self._profiles = None
        self._multi_chunk = None
        self.discriminator = None

        self.file_size = file_size
        self.file_name = file_name
        if extra_files is not None:
            self.extra_files = extra_files
        if profiles is not None:
            self.profiles = profiles
        if multi_chunk is not None:
            self.multi_chunk = multi_chunk

    @property
    def file_size(self):
        """Gets the file_size of this VideoUploadBody.  # noqa: E501

        Size of the file that will be uploaded in `bytes`.  # noqa: E501

        :return: The file_size of this VideoUploadBody.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this VideoUploadBody.

        Size of the file that will be uploaded in `bytes`.  # noqa: E501

        :param file_size: The file_size of this VideoUploadBody.  # noqa: E501
        :type: int
        """
        if file_size is None:
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

    @property
    def file_name(self):
        """Gets the file_name of this VideoUploadBody.  # noqa: E501

        Name of the file that will be uploaded.  # noqa: E501

        :return: The file_name of this VideoUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this VideoUploadBody.

        Name of the file that will be uploaded.  # noqa: E501

        :param file_name: The file_name of this VideoUploadBody.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def extra_files(self):
        """Gets the extra_files of this VideoUploadBody.  # noqa: E501

        A list of names of additional files that will be uploaded.  # noqa: E501

        :return: The extra_files of this VideoUploadBody.  # noqa: E501
        :rtype: list[ExtraFile]
        """
        return self._extra_files

    @extra_files.setter
    def extra_files(self, extra_files):
        """Sets the extra_files of this VideoUploadBody.

        A list of names of additional files that will be uploaded.  # noqa: E501

        :param extra_files: The extra_files of this VideoUploadBody.  # noqa: E501
        :type: list[ExtraFile]
        """

        self._extra_files = extra_files

    @property
    def profiles(self):
        """Gets the profiles of this VideoUploadBody.  # noqa: E501

        A comma-separated list of profile names or IDs to be used during encoding. Alternatively, specify none so no encodings will created right away.  # noqa: E501

        :return: The profiles of this VideoUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this VideoUploadBody.

        A comma-separated list of profile names or IDs to be used during encoding. Alternatively, specify none so no encodings will created right away.  # noqa: E501

        :param profiles: The profiles of this VideoUploadBody.  # noqa: E501
        :type: str
        """

        self._profiles = profiles

    @property
    def multi_chunk(self):
        """Gets the multi_chunk of this VideoUploadBody.  # noqa: E501


        :return: The multi_chunk of this VideoUploadBody.  # noqa: E501
        :rtype: bool
        """
        return self._multi_chunk

    @multi_chunk.setter
    def multi_chunk(self, multi_chunk):
        """Sets the multi_chunk of this VideoUploadBody.


        :param multi_chunk: The multi_chunk of this VideoUploadBody.  # noqa: E501
        :type: bool
        """

        self._multi_chunk = multi_chunk

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
        if not isinstance(other, VideoUploadBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
