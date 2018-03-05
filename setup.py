#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
import os
import codecs

setup_path = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(setup_path, 'README.rst'), encoding='utf-16') as f:
    README = f.read()

setup(name='synthetic_dataset',
      version='0.1.dev',
      url='https://github.com/Menelau/synthethic_dataset',
      maintainer='Rafael M. O. Cruz',
      maintainer_email='rafaelmenelau@gmail.com',
      description='Synthetic dataset generation',
      long_description=README,
      author='Rafael M. O. Cruz',
      author_email='rafaelmenelau@gmail.com',
      license='MIT',

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      install_requires=[
          'scikit-learn>=0.19.0',
          'numpy>=1.10.4',
          'scipy>=0.13.3',
          'matplotlib',
      ],
      python_requires='>=3',

      packages=find_packages())

