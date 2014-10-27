from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-malaga',
	version=version,
	description="Aspecto Malaga",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Isabel & Francis',
	author_email='datosabiertos@malaga.eu',
	url='http://datosabiertos.malaga.eu',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.malaga'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points="""\	
	[paste.paster_command]
	malaga = ckanext.malaga.commands:malagae
        [ckan.plugins]
        malaga=ckanext.malaga.plugin:malagae
	""",
)

