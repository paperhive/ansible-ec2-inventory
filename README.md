# Ansible EC2 inventory

This Python module is based on the [original Ansible EC2 inventory script](https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py) that is linked in the [Ansible docs](http://docs.ansible.com/ansible/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script).

The Python module in this repo fixes a few issues by being

 * installable via `pip` / PyPi: no need to place code from the Ansible repo in your inventory.
 * extendable for your needs: the class `Ec2Inventory` can be used as a base class for customizations.
