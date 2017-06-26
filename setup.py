"""Setuptools file for piwik-api."""

import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    """Read a file and return the contents."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='piwik-api',
    description='Client library for the Piwik Reporting API',
    long_description=read('README.rst'),
    version='0.1.2',
    author='Anton Sarukhanov',
    author_email='code@ant.sr',
    url='https://github.com/antsar/piwik-api',
    download_url='https://github.com/antsar/piwik-api/archive/master.zip',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests==2.18.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
