#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from setuptools import setup, find_packages


version = '0.1.1'

setup(name='django-openid-consumer',
    version=version,
    description="django-openid-consumer is a simple consumer only openid implementation for django",
    long_description="""
    django-openid-consumer aims to do only one thing, simple OpenID auth (with all the extension s python-openid supports) for comments on blogs and similar. It doesen't aim to provide any further integration (like for example tighter integration with auth) with Django. 
    """,
    keywords='django openid consumer',
    author='Matjaz Crnko',
    author_email='matjaz.crnko@gmail.com',
    url='http://code.google.com/p/django-openid-consumer/',
    license='BSD',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'python-openid',
        'Django',
    ],
)
