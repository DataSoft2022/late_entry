from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in late_entry/__init__.py
from late_entry import __version__ as version

setup(
	name="late_entry",
	version=version,
	description="Attandance policy",
	author="omneyaeid827@gmail.com",
	author_email="omneyaeid827@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
