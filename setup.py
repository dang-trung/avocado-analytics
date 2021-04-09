#!/usr/bin/env python
"""A setuptools based setup module.

Setup the [sample-project].
"""

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='[sample-project]',
    version='0.0.0',
    description='A short description of the project.',
    long_description=readme,
    author='Trung Dang',
    author_email='dangtrung96@gmail.com',
    url='https://github.com/dang-trung/[sample-project]',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
