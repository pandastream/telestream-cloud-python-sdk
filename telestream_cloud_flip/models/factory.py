# coding: utf-8

"""
    Flip API

    Description

    OpenAPI spec version: 3.1.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Factory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'factory_region': 'str',
        'output_bucket_name': 'str',
        'acl': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'url': 'str',
        'server_side_encryption': 'bool',
        'input_bucket_name': 'str',
        'input_bucket_watch': 'bool',
        'input_bucket_files_map': 'str',
        'input_bucket_sync_every_n_min': 'str',
        'input_bucket_recursive': 'str',
        'input_bucket_file_pattern': 'str',
        'outputs_path_format': 'str',
        'storage_provider': 'int',
        'provider_specific_settings': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'factory_region': 'factory_region',
        'output_bucket_name': 'output_bucket_name',
        'acl': 'acl',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'url': 'url',
        'server_side_encryption': 'server_side_encryption',
        'input_bucket_name': 'input_bucket_name',
        'input_bucket_watch': 'input_bucket_watch',
        'input_bucket_files_map': 'input_bucket_files_map',
        'input_bucket_sync_every_n_min': 'input_bucket_sync_every_n_min',
        'input_bucket_recursive': 'input_bucket_recursive',
        'input_bucket_file_pattern': 'input_bucket_file_pattern',
        'outputs_path_format': 'outputs_path_format',
        'storage_provider': 'storage_provider',
        'provider_specific_settings': 'provider_specific_settings'
    }

    def __init__(self, id=None, name=None, factory_region=None, output_bucket_name=None, acl=None, created_at=None, updated_at=None, url=None, server_side_encryption=None, input_bucket_name=None, input_bucket_watch=None, input_bucket_files_map=None, input_bucket_sync_every_n_min=None, input_bucket_recursive=None, input_bucket_file_pattern=None, outputs_path_format=None, storage_provider=None, provider_specific_settings=None):
        """
        Factory - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._factory_region = None
        self._output_bucket_name = None
        self._acl = None
        self._created_at = None
        self._updated_at = None
        self._url = None
        self._server_side_encryption = None
        self._input_bucket_name = None
        self._input_bucket_watch = None
        self._input_bucket_files_map = None
        self._input_bucket_sync_every_n_min = None
        self._input_bucket_recursive = None
        self._input_bucket_file_pattern = None
        self._outputs_path_format = None
        self._storage_provider = None
        self._provider_specific_settings = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if factory_region is not None:
          self.factory_region = factory_region
        if output_bucket_name is not None:
          self.output_bucket_name = output_bucket_name
        if acl is not None:
          self.acl = acl
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if url is not None:
          self.url = url
        if server_side_encryption is not None:
          self.server_side_encryption = server_side_encryption
        if input_bucket_name is not None:
          self.input_bucket_name = input_bucket_name
        if input_bucket_watch is not None:
          self.input_bucket_watch = input_bucket_watch
        if input_bucket_files_map is not None:
          self.input_bucket_files_map = input_bucket_files_map
        if input_bucket_sync_every_n_min is not None:
          self.input_bucket_sync_every_n_min = input_bucket_sync_every_n_min
        if input_bucket_recursive is not None:
          self.input_bucket_recursive = input_bucket_recursive
        if input_bucket_file_pattern is not None:
          self.input_bucket_file_pattern = input_bucket_file_pattern
        if outputs_path_format is not None:
          self.outputs_path_format = outputs_path_format
        if storage_provider is not None:
          self.storage_provider = storage_provider
        if provider_specific_settings is not None:
          self.provider_specific_settings = provider_specific_settings

    @property
    def id(self):
        """
        Gets the id of this Factory.
        A unique identifier of a Factory.

        :return: The id of this Factory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Factory.
        A unique identifier of a Factory.

        :param id: The id of this Factory.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Factory.
        Human-readable identifier of a Factory.

        :return: The name of this Factory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Factory.
        Human-readable identifier of a Factory.

        :param name: The name of this Factory.
        :type: str
        """

        self._name = name

    @property
    def factory_region(self):
        """
        Gets the factory_region of this Factory.
        A region where the factory is located.

        :return: The factory_region of this Factory.
        :rtype: str
        """
        return self._factory_region

    @factory_region.setter
    def factory_region(self, factory_region):
        """
        Sets the factory_region of this Factory.
        A region where the factory is located.

        :param factory_region: The factory_region of this Factory.
        :type: str
        """

        self._factory_region = factory_region

    @property
    def output_bucket_name(self):
        """
        Gets the output_bucket_name of this Factory.
        A bucket where processed files will be stored.

        :return: The output_bucket_name of this Factory.
        :rtype: str
        """
        return self._output_bucket_name

    @output_bucket_name.setter
    def output_bucket_name(self, output_bucket_name):
        """
        Sets the output_bucket_name of this Factory.
        A bucket where processed files will be stored.

        :param output_bucket_name: The output_bucket_name of this Factory.
        :type: str
        """

        self._output_bucket_name = output_bucket_name

    @property
    def acl(self):
        """
        Gets the acl of this Factory.
        Specify if your files are public or private (private files need authorization url to access). By default this is not set.

        :return: The acl of this Factory.
        :rtype: str
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """
        Sets the acl of this Factory.
        Specify if your files are public or private (private files need authorization url to access). By default this is not set.

        :param acl: The acl of this Factory.
        :type: str
        """
        allowed_values = ["public", "private"]
        if acl not in allowed_values:
            raise ValueError(
                "Invalid value for `acl` ({0}), must be one of {1}"
                .format(acl, allowed_values)
            )

        self._acl = acl

    @property
    def created_at(self):
        """
        Gets the created_at of this Factory.
        A date and time when a Factory has been created.

        :return: The created_at of this Factory.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Factory.
        A date and time when a Factory has been created.

        :param created_at: The created_at of this Factory.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Factory.
        A date and time when a Factory has been updated last time.

        :return: The updated_at of this Factory.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Factory.
        A date and time when a Factory has been updated last time.

        :param updated_at: The updated_at of this Factory.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def url(self):
        """
        Gets the url of this Factory.
        An URL pointing to the output_bucket_name.

        :return: The url of this Factory.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Factory.
        An URL pointing to the output_bucket_name.

        :param url: The url of this Factory.
        :type: str
        """

        self._url = url

    @property
    def server_side_encryption(self):
        """
        Gets the server_side_encryption of this Factory.
        Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set.

        :return: The server_side_encryption of this Factory.
        :rtype: bool
        """
        return self._server_side_encryption

    @server_side_encryption.setter
    def server_side_encryption(self, server_side_encryption):
        """
        Sets the server_side_encryption of this Factory.
        Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set.

        :param server_side_encryption: The server_side_encryption of this Factory.
        :type: bool
        """

        self._server_side_encryption = server_side_encryption

    @property
    def input_bucket_name(self):
        """
        Gets the input_bucket_name of this Factory.
        A name of an input bucket.

        :return: The input_bucket_name of this Factory.
        :rtype: str
        """
        return self._input_bucket_name

    @input_bucket_name.setter
    def input_bucket_name(self, input_bucket_name):
        """
        Sets the input_bucket_name of this Factory.
        A name of an input bucket.

        :param input_bucket_name: The input_bucket_name of this Factory.
        :type: str
        """

        self._input_bucket_name = input_bucket_name

    @property
    def input_bucket_watch(self):
        """
        Gets the input_bucket_watch of this Factory.
        Determines whether the Factory should be notified about new files added to the input bucket.

        :return: The input_bucket_watch of this Factory.
        :rtype: bool
        """
        return self._input_bucket_watch

    @input_bucket_watch.setter
    def input_bucket_watch(self, input_bucket_watch):
        """
        Sets the input_bucket_watch of this Factory.
        Determines whether the Factory should be notified about new files added to the input bucket.

        :param input_bucket_watch: The input_bucket_watch of this Factory.
        :type: bool
        """

        self._input_bucket_watch = input_bucket_watch

    @property
    def input_bucket_files_map(self):
        """
        Gets the input_bucket_files_map of this Factory.

        :return: The input_bucket_files_map of this Factory.
        :rtype: str
        """
        return self._input_bucket_files_map

    @input_bucket_files_map.setter
    def input_bucket_files_map(self, input_bucket_files_map):
        """
        Sets the input_bucket_files_map of this Factory.

        :param input_bucket_files_map: The input_bucket_files_map of this Factory.
        :type: str
        """

        self._input_bucket_files_map = input_bucket_files_map

    @property
    def input_bucket_sync_every_n_min(self):
        """
        Gets the input_bucket_sync_every_n_min of this Factory.
        Determines how often the input bucket is synchronised.

        :return: The input_bucket_sync_every_n_min of this Factory.
        :rtype: str
        """
        return self._input_bucket_sync_every_n_min

    @input_bucket_sync_every_n_min.setter
    def input_bucket_sync_every_n_min(self, input_bucket_sync_every_n_min):
        """
        Sets the input_bucket_sync_every_n_min of this Factory.
        Determines how often the input bucket is synchronised.

        :param input_bucket_sync_every_n_min: The input_bucket_sync_every_n_min of this Factory.
        :type: str
        """

        self._input_bucket_sync_every_n_min = input_bucket_sync_every_n_min

    @property
    def input_bucket_recursive(self):
        """
        Gets the input_bucket_recursive of this Factory.

        :return: The input_bucket_recursive of this Factory.
        :rtype: str
        """
        return self._input_bucket_recursive

    @input_bucket_recursive.setter
    def input_bucket_recursive(self, input_bucket_recursive):
        """
        Sets the input_bucket_recursive of this Factory.

        :param input_bucket_recursive: The input_bucket_recursive of this Factory.
        :type: str
        """

        self._input_bucket_recursive = input_bucket_recursive

    @property
    def input_bucket_file_pattern(self):
        """
        Gets the input_bucket_file_pattern of this Factory.
        A pattern that will be used to locate files in the input bucket. Valid wildcards might be used.

        :return: The input_bucket_file_pattern of this Factory.
        :rtype: str
        """
        return self._input_bucket_file_pattern

    @input_bucket_file_pattern.setter
    def input_bucket_file_pattern(self, input_bucket_file_pattern):
        """
        Sets the input_bucket_file_pattern of this Factory.
        A pattern that will be used to locate files in the input bucket. Valid wildcards might be used.

        :param input_bucket_file_pattern: The input_bucket_file_pattern of this Factory.
        :type: str
        """

        self._input_bucket_file_pattern = input_bucket_file_pattern

    @property
    def outputs_path_format(self):
        """
        Gets the outputs_path_format of this Factory.

        :return: The outputs_path_format of this Factory.
        :rtype: str
        """
        return self._outputs_path_format

    @outputs_path_format.setter
    def outputs_path_format(self, outputs_path_format):
        """
        Sets the outputs_path_format of this Factory.

        :param outputs_path_format: The outputs_path_format of this Factory.
        :type: str
        """

        self._outputs_path_format = outputs_path_format

    @property
    def storage_provider(self):
        """
        Gets the storage_provider of this Factory.
        Specifies which storage provider the factory should use. Available options: S3: 0, Google Cloud Storage: 1, FTP storage: 2, Google Cloud Interoperability Storage: 5, Flip storage: 7, FASP storage: 8, Azure Blob Storage: 9

        :return: The storage_provider of this Factory.
        :rtype: int
        """
        return self._storage_provider

    @storage_provider.setter
    def storage_provider(self, storage_provider):
        """
        Sets the storage_provider of this Factory.
        Specifies which storage provider the factory should use. Available options: S3: 0, Google Cloud Storage: 1, FTP storage: 2, Google Cloud Interoperability Storage: 5, Flip storage: 7, FASP storage: 8, Azure Blob Storage: 9

        :param storage_provider: The storage_provider of this Factory.
        :type: int
        """

        self._storage_provider = storage_provider

    @property
    def provider_specific_settings(self):
        """
        Gets the provider_specific_settings of this Factory.

        :return: The provider_specific_settings of this Factory.
        :rtype: object
        """
        return self._provider_specific_settings

    @provider_specific_settings.setter
    def provider_specific_settings(self, provider_specific_settings):
        """
        Sets the provider_specific_settings of this Factory.

        :param provider_specific_settings: The provider_specific_settings of this Factory.
        :type: object
        """

        self._provider_specific_settings = provider_specific_settings

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Factory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
