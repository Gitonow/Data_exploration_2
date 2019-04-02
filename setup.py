#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
import sys
from setuptools import setup

if sys.hexversion < 0x02070000:
    raise RuntimeError("Python 2.7 or higher required")

# Replace all instances of `comp-neurosci-skeleton` with the name of your project
setup(
    name="Data-Exploration-PSYC-5270",
    version="0.0.1",
    package_dir={'Data-Exploration-PSYC-5270': 'src'},
    packages=["Data-Exploration-PSYC-5270"],

    description="",
    long_description="",
    install_requires=[
        "numpy>=1.10",
    ],

    author="Damien Chambon and Yash Kalburgi",
    maintainer='Damien Chambon and Yash Kalburgi',
)
