import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Test",
    version = "0.0.4",
    author = "Deepak Kumar",
    author_email = "ABC@gmail.com",
    description = ("Test function to add two nummbers"),
    license = "BSD",
    keywords = "example documentation tutorial",
    install_requires = ['setuptools'],
    #packages=['an_examp/le_pypi_project', 'tests'],
    # long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)