#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-Versioned
---------------

Add version info to file paths. The default configuration will prefix a
timestamp to and make the path absolute. Paths must be files, if a path
is unexisting or is a directory, an exception will be raised.

Typically used in templates to allow for really long expiration dates of
static content::

    <link rel="stylesheet" href="{{"static/css/style.css"|versioned}}">

Links
`````
* `development version
  <http://github.com/pilt/flask-versioned/zipball/master#egg=Flask-Versioned-dev>`_
"""
from setuptools import setup


setup(
    name='Flask-Versioned',
    version='0.9.2',
    url='http://github.com/pilt/flask-versioned',
    license='BSD',
    author='Simon Pantzare',
    author_email='simon@pewpewlabs.com',
    description='Add version info to file paths.',
    long_description=__doc__,
    packages=[
        'flaskext',
        'flaskext.versioned',
    ],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask',
    ],
    test_suite='test_versioned',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
