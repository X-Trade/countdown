#!/usr/bin/env python

from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="countdown",
    version="1.0.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"],
    keywords="sample, setuptools, development",
    py_modules=["countdown"],
    python_requires=">=2.7, <4",
    extras_require={
        "caffeinate": ["caffeine"]},
    entry_points={
        "console_scripts": [
            "countdown = countdown:main"]},
    project_urls={
        "Bug Reports": "https://github.com/pypa/sampleproject/issues",
        "Source": "https://github.com/pypa/sampleproject/"})
