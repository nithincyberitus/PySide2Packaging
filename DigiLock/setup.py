import os
import setuptools
from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="digilock",
    version="0.1",
    author="Nithin Kumar Gollapalli",
    author_email="nithin.gollapalli@cyber-itus.com",
    description=long_description,
    license="Cyber-Itus",
    url="https://github.com/nithincyberitus/PySide2Packaging",
    packages=setuptools.find_packages(),
    zip_safe=False
)