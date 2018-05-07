# coding: utf-8

"""
    Tts API

    Description  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "telestream-cloud-tts"
VERSION = "2.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "requests"]

setup(
    name=NAME,
    version=VERSION,
    description="Tts API",
    author_email="cloudsupport@telestream.net",
    url="https://github.com/telestream/telestream-cloud-python-sdk",
    keywords=["Swagger", "Tts API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Description  # noqa: E501
    """
)
