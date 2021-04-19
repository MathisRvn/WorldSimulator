from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='WorldSimulator',
    version='0.0.1',
    description='World simulator which handle forces',
    long_description=readme,
    author='Mathis Revenu',
    license=license,
    packages=find_packages()
)
