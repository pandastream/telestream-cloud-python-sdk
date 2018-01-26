# coding: utf-8

"""
    Flip API

    Description  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from telestream_cloud_flip.models.factory import Factory  # noqa: F401,E501


class PaginatedFactoryCollection(object):
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
        'factories': 'list[Factory]',
        'page': 'int',
        'per_page': 'int',
        'total': 'int'
    }

    attribute_map = {
        'factories': 'factories',
        'page': 'page',
        'per_page': 'per_page',
        'total': 'total'
    }

    def __init__(self, factories=None, page=None, per_page=None, total=None):  # noqa: E501
        """PaginatedFactoryCollection - a model defined in Swagger"""  # noqa: E501

        self._factories = None
        self._page = None
        self._per_page = None
        self._total = None
        self.discriminator = None

        if factories is not None:
            self.factories = factories
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page
        if total is not None:
            self.total = total

    @property
    def factories(self):
        """Gets the factories of this PaginatedFactoryCollection.  # noqa: E501


        :return: The factories of this PaginatedFactoryCollection.  # noqa: E501
        :rtype: list[Factory]
        """
        return self._factories

    @factories.setter
    def factories(self, factories):
        """Sets the factories of this PaginatedFactoryCollection.


        :param factories: The factories of this PaginatedFactoryCollection.  # noqa: E501
        :type: list[Factory]
        """

        self._factories = factories

    @property
    def page(self):
        """Gets the page of this PaginatedFactoryCollection.  # noqa: E501

        A number of the fetched page.  # noqa: E501

        :return: The page of this PaginatedFactoryCollection.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PaginatedFactoryCollection.

        A number of the fetched page.  # noqa: E501

        :param page: The page of this PaginatedFactoryCollection.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this PaginatedFactoryCollection.  # noqa: E501

        A number of factories per page.  # noqa: E501

        :return: The per_page of this PaginatedFactoryCollection.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this PaginatedFactoryCollection.

        A number of factories per page.  # noqa: E501

        :param per_page: The per_page of this PaginatedFactoryCollection.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def total(self):
        """Gets the total of this PaginatedFactoryCollection.  # noqa: E501

        A number of all factories stored in the db.  # noqa: E501

        :return: The total of this PaginatedFactoryCollection.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaginatedFactoryCollection.

        A number of all factories stored in the db.  # noqa: E501

        :param total: The total of this PaginatedFactoryCollection.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, PaginatedFactoryCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
