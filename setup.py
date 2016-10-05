#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyflann',
    version='1.6.13',
    description='pyflann is the python bindings for FLANN - Fast Library for Approximate Nearest Neighbors.',
    author='Marius Muja & Gefu Tang',
    author_email='mariusm@cs.ubc.ca, tanggefu@gmail.com',
    license='BSD',
    keywords="flann",
    url='https://github.com/primetang/pyflann',
    packages=['pyflann', 'pyflann.io', 'pyflann.bindings',
              'pyflann.util', 'pyflann.lib'],
    package_dir={'pyflann.lib': 'pyflann/lib'},
    package_data={'pyflann.lib': [
        'darwin/*.dylib', 'win32/x86/*.dll', 'win32/x64/*.dll', 'linux/*.so']},
)
