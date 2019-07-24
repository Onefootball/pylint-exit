#!/usr/bin/python
from setuptools import setup
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
   long_description = f.read()

setup(
    name='pylint-exit',
    description='Exit code handler for pylint command line utility.',
    long_description=long_description,
    version='1.0.1',
    author='Jon Grace-Cox',
    author_email='jongracecox@gmail.com',
    py_modules=['pylint_exit'],
    setup_requires=['setuptools', 'wheel'],
    tests_require=[],
    install_requires=['bitarray'],
    data_files=[],
    options={
        'bdist_wheel': {'universal': True}
    },
    url='https://github.com/jongracecox/pylint-exit',
    entry_points={
        'console_scripts': ['pylint-exit=pylint_exit:main'],
    }
)
