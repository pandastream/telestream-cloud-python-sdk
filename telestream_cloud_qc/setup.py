# coding: utf-8

"""
    Qc API

    QC API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "telestream-cloud-qc"
VERSION = "1.0.0"
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
    description="Qc API",
    author_email="cloudsupport@telestream.net",
    url="",
    keywords=["Swagger", "Qc API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    QC API  # noqa: E501
    """
)
