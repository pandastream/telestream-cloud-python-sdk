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


class Template(object):
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
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'produces': 'dict(str, str)',
        'takes': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'produces': 'produces',
        'takes': 'takes'
    }

    def __init__(self, name=None, type=None, description=None, produces=None, takes=None):  # noqa: E501
        """Template - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._description = None
        self._produces = None
        self._takes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if produces is not None:
            self.produces = produces
        if takes is not None:
            self.takes = takes

    @property
    def name(self):
        """Gets the name of this Template.  # noqa: E501


        :return: The name of this Template.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Template.


        :param name: The name of this Template.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Template.  # noqa: E501


        :return: The type of this Template.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Template.


        :param type: The type of this Template.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this Template.  # noqa: E501


        :return: The description of this Template.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Template.


        :param description: The description of this Template.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def produces(self):
        """Gets the produces of this Template.  # noqa: E501


        :return: The produces of this Template.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._produces

    @produces.setter
    def produces(self, produces):
        """Sets the produces of this Template.


        :param produces: The produces of this Template.  # noqa: E501
        :type: dict(str, str)
        """

        self._produces = produces

    @property
    def takes(self):
        """Gets the takes of this Template.  # noqa: E501


        :return: The takes of this Template.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._takes

    @takes.setter
    def takes(self, takes):
        """Sets the takes of this Template.


        :param takes: The takes of this Template.  # noqa: E501
        :type: dict(str, str)
        """

        self._takes = takes

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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
