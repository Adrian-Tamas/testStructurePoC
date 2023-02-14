from typing import List

from setuptools import setup, find_packages

from version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements: List[str] = f.readlines()

setup(
    name='email_helper',
    packages=find_packages(exclude=[""]),
    package_data={'': ['']},
    version=__version__,
    description='email_helper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Adrian Tamas',
    author_email='adi.tamas@outlook.com',
    license='MIT',
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    url="",
    install_requires=requirements
)
