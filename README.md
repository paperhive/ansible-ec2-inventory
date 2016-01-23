# Ansible EC2 inventory

This Python module is based on the [original Ansible EC2 inventory script](https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py) that is linked in the [Ansible docs](http://docs.ansible.com/ansible/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script).

The Python module in this repo fixes a few issues by being

 * installable via `pip` / PyPi: no need to place code from the Ansible repo in your inventory.
 * extendable for your needs: the class `Ec2Inventory` can be used as a base class for customizations.

## Installation
```
pip install ansible-ec2-inventory
```
## Usage
### As a script
```
ansible-ec2-inventory --config ec2.ini
```
*Note:* if you want to provide a boto profile, prefix the command with
`AWS_PROFILE=myprofile`.

### As a Python module
Example:
```python
from ansible_ec2_inventory import Ec2Inventory
import json

def main():
    # get path of ec2.ini
    path = os.path.dirname(os.path.realpath(__file__))

    # get inventory
    ec2inventory = Ec2Inventory(configfile=path + '/ec2.ini')
    data = ec2inventory.get_inventory()

    # print json
    print(json.dumps(data, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
```
