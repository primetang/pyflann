#!/usr/bin/env python

from setuptools import setup
import os
import sys

pyflann_package_dir = './pyflann/lib'
if sys.platform.startswith('win32'):
      if sys.maxsize > 2**32:
      	pyflann_package_dir = os.path.join(pyflann_package_dir, 'win32/x64')
      else:
      	pyflann_package_dir = os.path.join(pyflann_package_dir, 'win32/x86')
elif sys.platform.startswith('darwin'):
      pyflann_package_dir = os.path.join(pyflann_package_dir, 'darwin')
elif sys.platform.startswith('linux'):
      pyflann_package_dir = os.path.join(pyflann_package_dir, 'linux')

setup(name='pyflann',
      version='1.6.11',
      description='Fast Library for Approximate Nearest Neighbors',
      author='Marius Muja & Gefu Tang',
      author_email='mariusm@cs.ubc.ca, tanggefu@gmail.com',
      license='BSD',
      keywords="flann",
      url='https://github.com/primetang/pyflann',
      packages=['pyflann', 'pyflann.io', 'pyflann.bindings', 'pyflann.util', 'pyflann.lib'],
      package_dir={'pyflann.lib': pyflann_package_dir },
      package_data={'pyflann.lib': ['libflann.so', 'flann.dll', 'libflann.dll', 'libflann.dylib']},
)