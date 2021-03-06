from distutils.core import setup

setup(
	# Application name:
	name="filemon",

	# Version number (initial):
	version="0.1.0",

	py_modules=['filemon'],

	# Application author details:
	author="Logan Theragon",
	author_email="logantheragon@gmail.com",

	# Packages
	#packages=["app"],

	# Include additional files into the package
	#include_package_data=True,

	# Details
	#url="http://pypi.python.org/pypi/MyApplication_v010/",

	#
	# license="LICENSE.txt",
	#description="Useful towel-related stuff.",

	# long_description=open("README.txt").read(),

	# Dependent packages (distributions)
	install_requires=[
		"pyinotify",
		#"asyncore",
	],
)
