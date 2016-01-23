# -*- coding: utf-8 -*-

import os
from distutils.core import setup
import codecs

from ansible_ec2_inventory import (__version__, __author__, __author_email__,
                                    __website__)


def read(fname):
    '''Read a file'''
    return codecs.open(
        os.path.join(os.path.dirname(__file__), fname),
        encoding='utf-8'
        ).read()

setup(
    name='ansible-ec2-inventory',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=['ansible_ec2_inventory'],
    description='Extendable Python module for ansible EC2 inventories',
    long_description=read('README.rst'),
    url=__website__,
    download_url='https://pypi.python.org/pypi/ansible-ec2-inventory',
    license='License :: OSI Approved :: GNU General Public License v3 or '
            'later (GPLv3+)',
    platforms='any',
    requires=['boto'],
    scripts=['scripts/ansible-ec2-inventory'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: System :: Systems Administration'
        ]
    )
