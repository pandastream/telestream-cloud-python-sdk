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


class FactoryBody(object):
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
        'aws_access_key': 'str',
        'aws_secret_key': 'str',
        'factory_region': 'str',
        'input_bucket_file_pattern': 'str',
        'input_bucket_name': 'str',
        'input_bucket_recursive': 'bool',
        'input_bucket_sync_every_n_min': 'int',
        'input_bucket_watch': 'bool',
        'name': 'str',
        'outputs_path_format': 'str',
        'provider_specific_settings': 'object',
        'acl': 'str',
        'output_bucket_name': 'str',
        'server_side_encryption': 'bool',
        'storage_credential_attributes': 'FactoryBodyStorageCredentialAttributes',
        'storage_provider': 'int'
    }

    attribute_map = {
        'aws_access_key': 'aws_access_key',
        'aws_secret_key': 'aws_secret_key',
        'factory_region': 'factory_region',
        'input_bucket_file_pattern': 'input_bucket_file_pattern',
        'input_bucket_name': 'input_bucket_name',
        'input_bucket_recursive': 'input_bucket_recursive',
        'input_bucket_sync_every_n_min': 'input_bucket_sync_every_n_min',
        'input_bucket_watch': 'input_bucket_watch',
        'name': 'name',
        'outputs_path_format': 'outputs_path_format',
        'provider_specific_settings': 'provider_specific_settings',
        'acl': 'acl',
        'output_bucket_name': 'output_bucket_name',
        'server_side_encryption': 'server_side_encryption',
        'storage_credential_attributes': 'storage_credential_attributes',
        'storage_provider': 'storage_provider'
    }

    def __init__(self, aws_access_key=None, aws_secret_key=None, factory_region=None, input_bucket_file_pattern=None, input_bucket_name=None, input_bucket_recursive=None, input_bucket_sync_every_n_min=None, input_bucket_watch=None, name=None, outputs_path_format=None, provider_specific_settings=None, acl=None, output_bucket_name=None, server_side_encryption=None, storage_credential_attributes=None, storage_provider=None):
        """
        FactoryBody - a model defined in Swagger
        """

        self._aws_access_key = None
        self._aws_secret_key = None
        self._factory_region = None
        self._input_bucket_file_pattern = None
        self._input_bucket_name = None
        self._input_bucket_recursive = None
        self._input_bucket_sync_every_n_min = None
        self._input_bucket_watch = None
        self._name = None
        self._outputs_path_format = None
        self._provider_specific_settings = None
        self._acl = None
        self._output_bucket_name = None
        self._server_side_encryption = None
        self._storage_credential_attributes = None
        self._storage_provider = None

        if aws_access_key is not None:
          self.aws_access_key = aws_access_key
        if aws_secret_key is not None:
          self.aws_secret_key = aws_secret_key
        if factory_region is not None:
          self.factory_region = factory_region
        if input_bucket_file_pattern is not None:
          self.input_bucket_file_pattern = input_bucket_file_pattern
        if input_bucket_name is not None:
          self.input_bucket_name = input_bucket_name
        if input_bucket_recursive is not None:
          self.input_bucket_recursive = input_bucket_recursive
        if input_bucket_sync_every_n_min is not None:
          self.input_bucket_sync_every_n_min = input_bucket_sync_every_n_min
        if input_bucket_watch is not None:
          self.input_bucket_watch = input_bucket_watch
        self.name = name
        if outputs_path_format is not None:
          self.outputs_path_format = outputs_path_format
        if provider_specific_settings is not None:
          self.provider_specific_settings = provider_specific_settings
        if acl is not None:
          self.acl = acl
        if output_bucket_name is not None:
          self.output_bucket_name = output_bucket_name
        if server_side_encryption is not None:
          self.server_side_encryption = server_side_encryption
        if storage_credential_attributes is not None:
          self.storage_credential_attributes = storage_credential_attributes
        if storage_provider is not None:
          self.storage_provider = storage_provider

    @property
    def aws_access_key(self):
        """
        Gets the aws_access_key of this FactoryBody.
        AWS access key.

        :return: The aws_access_key of this FactoryBody.
        :rtype: str
        """
        return self._aws_access_key

    @aws_access_key.setter
    def aws_access_key(self, aws_access_key):
        """
        Sets the aws_access_key of this FactoryBody.
        AWS access key.

        :param aws_access_key: The aws_access_key of this FactoryBody.
        :type: str
        """

        self._aws_access_key = aws_access_key

    @property
    def aws_secret_key(self):
        """
        Gets the aws_secret_key of this FactoryBody.
        AWS secret key.

        :return: The aws_secret_key of this FactoryBody.
        :rtype: str
        """
        return self._aws_secret_key

    @aws_secret_key.setter
    def aws_secret_key(self, aws_secret_key):
        """
        Sets the aws_secret_key of this FactoryBody.
        AWS secret key.

        :param aws_secret_key: The aws_secret_key of this FactoryBody.
        :type: str
        """

        self._aws_secret_key = aws_secret_key

    @property
    def factory_region(self):
        """
        Gets the factory_region of this FactoryBody.
        A region where the factory is located.

        :return: The factory_region of this FactoryBody.
        :rtype: str
        """
        return self._factory_region

    @factory_region.setter
    def factory_region(self, factory_region):
        """
        Sets the factory_region of this FactoryBody.
        A region where the factory is located.

        :param factory_region: The factory_region of this FactoryBody.
        :type: str
        """

        self._factory_region = factory_region

    @property
    def input_bucket_file_pattern(self):
        """
        Gets the input_bucket_file_pattern of this FactoryBody.
        A pattern that will be used to locate files in the input bucket. Valid wildcards might be used.

        :return: The input_bucket_file_pattern of this FactoryBody.
        :rtype: str
        """
        return self._input_bucket_file_pattern

    @input_bucket_file_pattern.setter
    def input_bucket_file_pattern(self, input_bucket_file_pattern):
        """
        Sets the input_bucket_file_pattern of this FactoryBody.
        A pattern that will be used to locate files in the input bucket. Valid wildcards might be used.

        :param input_bucket_file_pattern: The input_bucket_file_pattern of this FactoryBody.
        :type: str
        """

        self._input_bucket_file_pattern = input_bucket_file_pattern

    @property
    def input_bucket_name(self):
        """
        Gets the input_bucket_name of this FactoryBody.
        A name of an input bucket.

        :return: The input_bucket_name of this FactoryBody.
        :rtype: str
        """
        return self._input_bucket_name

    @input_bucket_name.setter
    def input_bucket_name(self, input_bucket_name):
        """
        Sets the input_bucket_name of this FactoryBody.
        A name of an input bucket.

        :param input_bucket_name: The input_bucket_name of this FactoryBody.
        :type: str
        """

        self._input_bucket_name = input_bucket_name

    @property
    def input_bucket_recursive(self):
        """
        Gets the input_bucket_recursive of this FactoryBody.

        :return: The input_bucket_recursive of this FactoryBody.
        :rtype: bool
        """
        return self._input_bucket_recursive

    @input_bucket_recursive.setter
    def input_bucket_recursive(self, input_bucket_recursive):
        """
        Sets the input_bucket_recursive of this FactoryBody.

        :param input_bucket_recursive: The input_bucket_recursive of this FactoryBody.
        :type: bool
        """

        self._input_bucket_recursive = input_bucket_recursive

    @property
    def input_bucket_sync_every_n_min(self):
        """
        Gets the input_bucket_sync_every_n_min of this FactoryBody.
        Determines how often the input bucket is synchronised.

        :return: The input_bucket_sync_every_n_min of this FactoryBody.
        :rtype: int
        """
        return self._input_bucket_sync_every_n_min

    @input_bucket_sync_every_n_min.setter
    def input_bucket_sync_every_n_min(self, input_bucket_sync_every_n_min):
        """
        Sets the input_bucket_sync_every_n_min of this FactoryBody.
        Determines how often the input bucket is synchronised.

        :param input_bucket_sync_every_n_min: The input_bucket_sync_every_n_min of this FactoryBody.
        :type: int
        """

        self._input_bucket_sync_every_n_min = input_bucket_sync_every_n_min

    @property
    def input_bucket_watch(self):
        """
        Gets the input_bucket_watch of this FactoryBody.
        Determines whether the Factory should be notified about new files added to the input bucket.

        :return: The input_bucket_watch of this FactoryBody.
        :rtype: bool
        """
        return self._input_bucket_watch

    @input_bucket_watch.setter
    def input_bucket_watch(self, input_bucket_watch):
        """
        Sets the input_bucket_watch of this FactoryBody.
        Determines whether the Factory should be notified about new files added to the input bucket.

        :param input_bucket_watch: The input_bucket_watch of this FactoryBody.
        :type: bool
        """

        self._input_bucket_watch = input_bucket_watch

    @property
    def name(self):
        """
        Gets the name of this FactoryBody.
        Name of the Factory.

        :return: The name of this FactoryBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FactoryBody.
        Name of the Factory.

        :param name: The name of this FactoryBody.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def outputs_path_format(self):
        """
        Gets the outputs_path_format of this FactoryBody.
        Specify the directory where the output files should be stored. By default it is not set. More info [here](https://cloud.telestream.net/docs#path-format---know-how).

        :return: The outputs_path_format of this FactoryBody.
        :rtype: str
        """
        return self._outputs_path_format

    @outputs_path_format.setter
    def outputs_path_format(self, outputs_path_format):
        """
        Sets the outputs_path_format of this FactoryBody.
        Specify the directory where the output files should be stored. By default it is not set. More info [here](https://cloud.telestream.net/docs#path-format---know-how).

        :param outputs_path_format: The outputs_path_format of this FactoryBody.
        :type: str
        """

        self._outputs_path_format = outputs_path_format

    @property
    def provider_specific_settings(self):
        """
        Gets the provider_specific_settings of this FactoryBody.

        :return: The provider_specific_settings of this FactoryBody.
        :rtype: object
        """
        return self._provider_specific_settings

    @provider_specific_settings.setter
    def provider_specific_settings(self, provider_specific_settings):
        """
        Sets the provider_specific_settings of this FactoryBody.

        :param provider_specific_settings: The provider_specific_settings of this FactoryBody.
        :type: object
        """

        self._provider_specific_settings = provider_specific_settings

    @property
    def acl(self):
        """
        Gets the acl of this FactoryBody.
        Specify if your files are public or private (private files need authorization url to access). By default this is not set.

        :return: The acl of this FactoryBody.
        :rtype: str
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """
        Sets the acl of this FactoryBody.
        Specify if your files are public or private (private files need authorization url to access). By default this is not set.

        :param acl: The acl of this FactoryBody.
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
    def output_bucket_name(self):
        """
        Gets the output_bucket_name of this FactoryBody.
        A bucket where processed files will be stored.

        :return: The output_bucket_name of this FactoryBody.
        :rtype: str
        """
        return self._output_bucket_name

    @output_bucket_name.setter
    def output_bucket_name(self, output_bucket_name):
        """
        Sets the output_bucket_name of this FactoryBody.
        A bucket where processed files will be stored.

        :param output_bucket_name: The output_bucket_name of this FactoryBody.
        :type: str
        """

        self._output_bucket_name = output_bucket_name

    @property
    def server_side_encryption(self):
        """
        Gets the server_side_encryption of this FactoryBody.
        Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set.

        :return: The server_side_encryption of this FactoryBody.
        :rtype: bool
        """
        return self._server_side_encryption

    @server_side_encryption.setter
    def server_side_encryption(self, server_side_encryption):
        """
        Sets the server_side_encryption of this FactoryBody.
        Specify if you want to use multi-factor server-side 256-bit AES-256 data encryption with Amazon S3-managed encryption keys (SSE-S3). Each object is encrypted using a unique key which as an additional safeguard is encrypted itself with a master key that S3 regularly rotates. By default this is not set.

        :param server_side_encryption: The server_side_encryption of this FactoryBody.
        :type: bool
        """

        self._server_side_encryption = server_side_encryption

    @property
    def storage_credential_attributes(self):
        """
        Gets the storage_credential_attributes of this FactoryBody.

        :return: The storage_credential_attributes of this FactoryBody.
        :rtype: FactoryBodyStorageCredentialAttributes
        """
        return self._storage_credential_attributes

    @storage_credential_attributes.setter
    def storage_credential_attributes(self, storage_credential_attributes):
        """
        Sets the storage_credential_attributes of this FactoryBody.

        :param storage_credential_attributes: The storage_credential_attributes of this FactoryBody.
        :type: FactoryBodyStorageCredentialAttributes
        """

        self._storage_credential_attributes = storage_credential_attributes

    @property
    def storage_provider(self):
        """
        Gets the storage_provider of this FactoryBody.
        Specifies which storage provider the factory should use. Available options: S3: 0, Google Cloud Storage: 1, FTP storage: 2, Google Cloud Interoperability Storage: 5, Flip storage: 7, FASP storage: 8, Azure Blob Storage: 9

        :return: The storage_provider of this FactoryBody.
        :rtype: int
        """
        return self._storage_provider

    @storage_provider.setter
    def storage_provider(self, storage_provider):
        """
        Sets the storage_provider of this FactoryBody.
        Specifies which storage provider the factory should use. Available options: S3: 0, Google Cloud Storage: 1, FTP storage: 2, Google Cloud Interoperability Storage: 5, Flip storage: 7, FASP storage: 8, Azure Blob Storage: 9

        :param storage_provider: The storage_provider of this FactoryBody.
        :type: int
        """

        self._storage_provider = storage_provider

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
        if not isinstance(other, FactoryBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
