# coding=utf-8

# Author: Rafael Menelau Oliveira e Cruz <rafaelmenelau@gmail.com>
#
# License: MIT

"""
The :mod:`deslib.util` This module includes various utilities. They are divided into three parts:

syndata.synthethic_datasets - Provide functions to generate several 2D classification datasets.

syndata.plot_tools - Provides some routines to easily plot datasets and decision borders of a scikit-learn classifier.
"""

from .plot_tools import *
from .synthetic_datasets import *
