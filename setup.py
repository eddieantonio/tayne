#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from distutils.core import setup
from tayne import __version__

def slurp(filename):
    with open(filename) as f:
        return f.read()


setup(name='tayne',
      version=__version__,
      description='companion to entr(1)',
      author='Eddie Antonio Santos',
      author_email='easantos@ualberta.ca',
      url='https://github.com/eddieantonio/tayne',
      long_description=slurp('README.rst'),
      py_modules=['tayne'])
