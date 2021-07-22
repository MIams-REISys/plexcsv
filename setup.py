import os
import sys
from setuptools import setup

def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(
    name='plexcsv',
    version='1.0.0',
    description='music playlist builder and maintainer',
    author='Steven Wills',
    author_email='steven@swills.me',
    url='',
    license='MIT',
    platforms='ALL',
    long_description=_read('README.rst'),
    test_suite='',
    zip_safe=False,
    include_package_data=True, 

    packages=[
        'plexcsv',
    ],

entry_points={
        'console_scripts': [
            # command = package.module:function
            'cli = plexcsv.commands:main',
        ],
    },    

install_requires=[
        #'musicbrainzngs>=0.4',
    ]
)

