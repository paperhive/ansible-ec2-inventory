# -*- coding: utf-8 -*-
'''Ansible EC2 inventory module'''

from .ec2inventory import Ec2Inventory

# metadata
__version__ = '0.1.6'
__author__ = 'André Gaul'
__author_email__ = 'andre@gaul.io'
__website__ = 'https://github.com/paperhive/ansible-ec2-inventory'

__all__ = ["Ec2Inventory"]
