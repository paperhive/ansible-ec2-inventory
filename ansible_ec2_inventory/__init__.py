# -*- coding: utf-8 -*-
'''Ansible EC2 inventory module'''

# get version from setup.py
# http://stackoverflow.com/a/17638236/1219479
from pkg_resources import get_distribution, DistributionNotFound
import os.path
try:
    _dist = get_distribution('ansible-ec2-inventory')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'ansible-ec2-inventory')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
except DistributionNotFound:
    __version__ = 'Please install ansible-ec2-inventory with setup.py'
else:
    __version__ = _dist.version

from .ec2inventory import Ec2Inventory
__all__ = ["Ec2Inventory"]
