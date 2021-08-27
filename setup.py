from setuptools import setup, find_packages

version = "0.0.13"
package_name = "roro"
setup(name=package_name,
	version=version,
	packages=find_packages(exclude=["tests"]),
)
