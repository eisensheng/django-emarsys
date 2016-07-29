#!/usr/bin/env python

from setuptools import setup

setup(name='django_emarsys',
      version='0.26',
      description='Django and Oscar glue for Emarsys events',
      license="MIT",
      author='Markus Bertheau',
      author_email='mbertheau@gmail.com',
      long_description=open('README.md').read(),
      packages=['django_emarsys',
                'django_emarsys.management',
                'django_emarsys.management.commands',
                'django_emarsys.migrations',
                'oscar_emarsys',
                'oscar_emarsys.dashboard',
                'oscar_emarsys.dashboard.emarsys'],
      include_package_data=True,
      install_requires=[
          'Django>=1.8.14,<1.10',
          'python-emarsys~=0.3',
          'jsonfield~=1.0.3',
          'six~=1.10.0'
      ])
