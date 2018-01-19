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

from telestream_cloud_qc.models.job_details import JobDetails  # noqa: F401,E501


class Job(object):
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
        'id': 'str',
        'status': 'str',
        'duration': 'int',
        'type': 'str',
        'details': 'JobDetails'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'duration': 'duration',
        'type': 'type',
        'details': 'details'
    }

    def __init__(self, id=None, status=None, duration=None, type=None, details=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._status = None
        self._duration = None
        self._type = None
        self._details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if duration is not None:
            self.duration = duration
        if type is not None:
            self.type = type
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501


        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.


        :param id: The id of this Job.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: str
        """
        allowed_values = ["pending", "transfering", "queued", "downloading", "uploading", "processing", "success", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def duration(self):
        """Gets the duration of this Job.  # noqa: E501


        :return: The duration of this Job.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Job.


        :param duration: The duration of this Job.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def type(self):
        """Gets the type of this Job.  # noqa: E501


        :return: The type of this Job.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Job.


        :param type: The type of this Job.  # noqa: E501
        :type: str
        """
        allowed_values = ["vidchecker", "lipsync"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def details(self):
        """Gets the details of this Job.  # noqa: E501


        :return: The details of this Job.  # noqa: E501
        :rtype: JobDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Job.


        :param details: The details of this Job.  # noqa: E501
        :type: JobDetails
        """

        self._details = details

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
