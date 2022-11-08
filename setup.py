#!/usr/bin/env python

"""
Bottle-SSLify
------------

Simple Bottle extension to redirect all incoming requests for an app to HTTPS.

"""

from setuptools import setup, find_packages

import re

# gather the package information
main_py = open('bottle_sslify.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", main_py))

# convert the readme to pypi compatible rst
try:
  try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
  except ImportError:
    readme = open('README.md').read()
except:
  print('something went wrong reading the README.md file.')
  readme = ''

setup(
  name='Bottle-SSLify',
  version=metadata['version'],
  url='https://github.com/ali01/bottle-sslify',
  license='MIT License',
  author=metadata['author'],
  author_email=metadata['email'],
  description='Force SSL on any Bottle app.',
  long_description=readme,
  py_modules=['bottle_sslify'],
  include_package_data=True,
  platforms='any',
  install_requires=[
    'bottle==0.10.11',
    'nose==1.2.1',
  ],
  classifiers=[
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
