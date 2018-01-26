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

from telestream_cloud_tts.models.job import Job  # noqa: F401,E501


class JobsCollection(object):
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
        'jobs': 'list[Job]',
        'page': 'int',
        'per_page': 'int',
        'page_count': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'page': 'page',
        'per_page': 'per_page',
        'page_count': 'page_count',
        'total_count': 'total_count'
    }

    def __init__(self, jobs=None, page=None, per_page=None, page_count=None, total_count=None):  # noqa: E501
        """JobsCollection - a model defined in Swagger"""  # noqa: E501

        self._jobs = None
        self._page = None
        self._per_page = None
        self._page_count = None
        self._total_count = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if page_count is not None:
            self.page_count = page_count
        if total_count is not None:
            self.total_count = total_count

    @property
    def jobs(self):
        """Gets the jobs of this JobsCollection.  # noqa: E501


        :return: The jobs of this JobsCollection.  # noqa: E501
        :rtype: list[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this JobsCollection.


        :param jobs: The jobs of this JobsCollection.  # noqa: E501
        :type: list[Job]
        """

        self._jobs = jobs

    @property
    def page(self):
        """Gets the page of this JobsCollection.  # noqa: E501

        A number of the fetched page.  # noqa: E501

        :return: The page of this JobsCollection.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this JobsCollection.

        A number of the fetched page.  # noqa: E501

        :param page: The page of this JobsCollection.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this JobsCollection.  # noqa: E501

        A number of jobs per page.  # noqa: E501

        :return: The per_page of this JobsCollection.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this JobsCollection.

        A number of jobs per page.  # noqa: E501

        :param per_page: The per_page of this JobsCollection.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def page_count(self):
        """Gets the page_count of this JobsCollection.  # noqa: E501

        A number of pages.  # noqa: E501

        :return: The page_count of this JobsCollection.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this JobsCollection.

        A number of pages.  # noqa: E501

        :param page_count: The page_count of this JobsCollection.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def total_count(self):
        """Gets the total_count of this JobsCollection.  # noqa: E501

        A number of all jobs.  # noqa: E501

        :return: The total_count of this JobsCollection.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this JobsCollection.

        A number of all jobs.  # noqa: E501

        :param total_count: The total_count of this JobsCollection.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, JobsCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
