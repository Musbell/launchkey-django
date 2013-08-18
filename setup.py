#!/usr/bin/env python
"""
LaunchKey
=========

:copyright: (c) 2013 by the 2013 LaunchKey, Inc.
:license: MIT, see LICENSE.txt for more details.
"""
from setuptools import setup, find_packages

setup(
    name='launchkey-django',
    version='0.1.0',
    author='Andrew McCloud',
    author_email='andrew@launchkey.com',
    url='https://github.com/LaunchKey/launchkey-django',
    description='LaunchKey authentication backend for Django',
    long_description=__doc__,
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    test_suite='runtests.runtests',
    install_requires=[
        'launchkey-python>=1.0.0,<1.1.0', # ~> 1.0.0
    ],
    extras_require={
        'dev': [
            'django>=1.4.0,<1.6.0', # ~> 1.4.0
            'django-debug-toolbar',
        ],
        'test': [
            'pytest',
            'pytest-django',
            'exam',
        ],
    },
    classifiers=[
        'Framework :: Django',
    ],
)
