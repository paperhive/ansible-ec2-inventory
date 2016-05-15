# -*- coding: utf-8 -*-

import os
from distutils.core import setup
import codecs

def read(fname):
    '''Read a file'''
    return codecs.open(
        os.path.join(os.path.dirname(__file__), fname),
        encoding='utf-8'
        ).read()

setup(
    name='ansible-ec2-inventory',
    version='0.1.8',
    author='André Gaul',
    author_email='andre@gaul.io',
    packages=['ansible_ec2_inventory'],
    description='Extendable Python module for ansible EC2 inventories',
    long_description=read('README'),
    url='https://github.com/paperhive/ansible-ec2-inventory',
    download_url='https://pypi.python.org/pypi/ansible-ec2-inventory',
    license='License :: OSI Approved :: GNU General Public License v3 or '
            'later (GPLv3+)',
    platforms='any',
    install_requires=['boto'],
    scripts=['scripts/ansible-ec2-inventory'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: System :: Systems Administration'
        ]
    )
