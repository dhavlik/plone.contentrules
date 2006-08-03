from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='plone.contentrules',
      version=version,
      description="Plone ContentRules Engine",
      long_description="""\
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Markus Fuhrer',
      author_email='mfuhrer@gmx.net',
      url='http://svn.plone.org/svn/plone/plone.contentrules',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
