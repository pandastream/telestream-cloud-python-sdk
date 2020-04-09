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


class CadenceTest(object):
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
        'check_cadence': 'bool',
        'cadence_required': 'CadenceType',
        'check_cadence_breaks': 'bool',
        'report_cadence': 'bool',
        'check_for_poor_cadence': 'bool',
        'reject_on_error': 'bool',
        'checked': 'bool'
    }

    attribute_map = {
        'check_cadence': 'check_cadence',
        'cadence_required': 'cadence_required',
        'check_cadence_breaks': 'check_cadence_breaks',
        'report_cadence': 'report_cadence',
        'check_for_poor_cadence': 'check_for_poor_cadence',
        'reject_on_error': 'reject_on_error',
        'checked': 'checked'
    }

    def __init__(self, check_cadence=None, cadence_required=None, check_cadence_breaks=None, report_cadence=None, check_for_poor_cadence=None, reject_on_error=None, checked=None, local_vars_configuration=None):  # noqa: E501
        """CadenceTest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._check_cadence = None
        self._cadence_required = None
        self._check_cadence_breaks = None
        self._report_cadence = None
        self._check_for_poor_cadence = None
        self._reject_on_error = None
        self._checked = None
        self.discriminator = None

        if check_cadence is not None:
            self.check_cadence = check_cadence
        if cadence_required is not None:
            self.cadence_required = cadence_required
        if check_cadence_breaks is not None:
            self.check_cadence_breaks = check_cadence_breaks
        if report_cadence is not None:
            self.report_cadence = report_cadence
        if check_for_poor_cadence is not None:
            self.check_for_poor_cadence = check_for_poor_cadence
        if reject_on_error is not None:
            self.reject_on_error = reject_on_error
        if checked is not None:
            self.checked = checked

    @property
    def check_cadence(self):
        """Gets the check_cadence of this CadenceTest.  # noqa: E501


        :return: The check_cadence of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_cadence

    @check_cadence.setter
    def check_cadence(self, check_cadence):
        """Sets the check_cadence of this CadenceTest.


        :param check_cadence: The check_cadence of this CadenceTest.  # noqa: E501
        :type: bool
        """

        self._check_cadence = check_cadence

    @property
    def cadence_required(self):
        """Gets the cadence_required of this CadenceTest.  # noqa: E501


        :return: The cadence_required of this CadenceTest.  # noqa: E501
        :rtype: CadenceType
        """
        return self._cadence_required

    @cadence_required.setter
    def cadence_required(self, cadence_required):
        """Sets the cadence_required of this CadenceTest.


        :param cadence_required: The cadence_required of this CadenceTest.  # noqa: E501
        :type: CadenceType
        """

        self._cadence_required = cadence_required

    @property
    def check_cadence_breaks(self):
        """Gets the check_cadence_breaks of this CadenceTest.  # noqa: E501


        :return: The check_cadence_breaks of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_cadence_breaks

    @check_cadence_breaks.setter
    def check_cadence_breaks(self, check_cadence_breaks):
        """Sets the check_cadence_breaks of this CadenceTest.


        :param check_cadence_breaks: The check_cadence_breaks of this CadenceTest.  # noqa: E501
        :type: bool
        """

        self._check_cadence_breaks = check_cadence_breaks

    @property
    def report_cadence(self):
        """Gets the report_cadence of this CadenceTest.  # noqa: E501


        :return: The report_cadence of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._report_cadence

    @report_cadence.setter
    def report_cadence(self, report_cadence):
        """Sets the report_cadence of this CadenceTest.


        :param report_cadence: The report_cadence of this CadenceTest.  # noqa: E501
        :type: bool
        """

        self._report_cadence = report_cadence

    @property
    def check_for_poor_cadence(self):
        """Gets the check_for_poor_cadence of this CadenceTest.  # noqa: E501


        :return: The check_for_poor_cadence of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._check_for_poor_cadence

    @check_for_poor_cadence.setter
    def check_for_poor_cadence(self, check_for_poor_cadence):
        """Sets the check_for_poor_cadence of this CadenceTest.


        :param check_for_poor_cadence: The check_for_poor_cadence of this CadenceTest.  # noqa: E501
        :type: bool
        """

        self._check_for_poor_cadence = check_for_poor_cadence

    @property
    def reject_on_error(self):
        """Gets the reject_on_error of this CadenceTest.  # noqa: E501


        :return: The reject_on_error of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._reject_on_error

    @reject_on_error.setter
    def reject_on_error(self, reject_on_error):
        """Sets the reject_on_error of this CadenceTest.


        :param reject_on_error: The reject_on_error of this CadenceTest.  # noqa: E501
        :type: bool
        """

        self._reject_on_error = reject_on_error

    @property
    def checked(self):
        """Gets the checked of this CadenceTest.  # noqa: E501


        :return: The checked of this CadenceTest.  # noqa: E501
        :rtype: bool
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this CadenceTest.


        :param checked: The checked of this CadenceTest.  # noqa: E501
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
        if not isinstance(other, CadenceTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CadenceTest):
            return True

        return self.to_dict() != other.to_dict()
