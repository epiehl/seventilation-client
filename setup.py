# coding: utf-8

"""
    SEC Smart API

    This is the API for the <b>SEC Smart System</b>.<br><font color=\"#ff0000\"><b>ACHTUNG:</b> Diese API ist noch nicht für den produktiven Einsatz freigegeben!</font>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="SEC Smart API",
    author_email="",
    url="",
    keywords=["Swagger", "SEC Smart API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the API for the &lt;b&gt;SEC Smart System&lt;/b&gt;.&lt;br&gt;&lt;font color&#x3D;\&quot;#ff0000\&quot;&gt;&lt;b&gt;ACHTUNG:&lt;/b&gt; Diese API ist noch nicht für den produktiven Einsatz freigegeben!&lt;/font&gt;  # noqa: E501
    """
)