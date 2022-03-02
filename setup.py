from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version ='0.1',
    packages = find_packages(exclude = ['tests']),
    lincense = 'MIT',
    description = 'EDSA example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/<username>/<package-name>',
    author = '<Your Name>',
    author_email = '<Your Email>'
)
