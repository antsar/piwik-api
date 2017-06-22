"""Setuptools file for piwik-reporting."""

import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    """Read a file and return the contents."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='piwik-reporting',
    description=read('README.md'),
    version='0.1',
    author='Anton Sarukhanov',
    author_email='antsar@oit.rutgers.edu',
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
