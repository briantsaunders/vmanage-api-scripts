# vManage API Python Script Examples

This repo contains example scripts for interacting with the Cisco vManage API in python.  These scripts leverage the [python-viptela](https://github.com/CiscoDevNet/python-viptela) library.

## Getting Started

### Install

```shell
pip install -r requirements.txt
```

## Scripts

### get_device_status.py

Retrieves device status from vManage.  Below is an example of how to run.  Update the args to match your environment.

```shell
python get_device_status.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_hostname device
```

### get_device_template_inputs.py

Retrieves device template inputs from vManage.  Below is an example of how to run.  Update the args to match your environment.

```shell
python get_device_template_inputs.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_template_name template_name
```

### attach_device_template_custom.py

Attaches the specified device template to the specified device uuid.  Device does not have to be joined to fabric or online.  In this example the template property names are used instead of the variable name, there are certain situations where vManage will not let you change the variable name or you have duplicate variable names.  In those situations you'll want to reference the property name instead.  So in your `templates_inputs_file` you should have something that looks like the following when using this script:

```yaml
---
//system/host-name: dc-edge-test
//system/system-ip: "1.1.10.100"
//system/site-id: "100"
/0/vpn_if_name_Default_vEdge_DHCP_Tunnel_Interface/interface/if-name: GigabitEthernet1
/1/vpn1a_if_name/interface/if-name: GigabitEthernet2
/1/vpn1a_if_name/interface/ip/address: 10.20.0.1/24
/1/vpn1a_if_name//dhcp-server/lease-time: "12000"
/1/vpn1b_if_name/interface/if-name: GigabitEthernet3
/1/vpn1b_if_name/interface/ip/address: 10.20.1.1/24
/1/vpn1b_if_name//dhcp-server/lease-time: "12000"
```

If you aren't sure what inputs are required you can run the `get_device_template_inputs.py` script and all the `property` values are what you will want to define.

Below is an example of how to run.  Update the args to match your environment.

```shell
python attach_device_template.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_uuid device_uuid \
--device_template_name template_name \
--device_template_inputs_file template_inputs_file

### attach_device_template_to_offline_device.py

Attaches the specified device template to the specified device uuid.  Device does not have to be joined to fabric or online.

If your template requires inputs you need to provide a yaml file defining those inputs.  [Here](https://github.com/briantsaunders/vmanage-api-scripts/blob/main/example_template_inputs.yaml) is an example yaml file defining the inputs for a template.  If you aren't sure what inputs are required you can run the `get_device_template_inputs.py` script and all the `variable` values are what you will want to define.

Below is an example of how to run.  Update the args to match your environment.

```shell
python attach_device_template.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_uuid device_uuid \
--device_template_name template_name \
--device_template_inputs_file template_inputs_file
```

### attach_device_template_to_online_device.py

Attaches the specified device template to the specified device.  Device must be joined to fabric.

If your template requires inputs you need to provide a yaml file defining those inputs.  [Here](https://github.com/briantsaunders/vmanage-api-scripts/blob/main/example_template_inputs.yaml) is an example yaml file defining the inputs for a template.  If you aren't sure what inputs are required you can run the `get_device_template_inputs.py` script and all the `variable` values are what you will want to define.

Below is an example of how to run.  Update the args to match your environment.

```shell
python attach_device_template.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_hostname device \
--device_template_name template_name \
--device_template_inputs_file template_inputs_file
```

### detach_device_template.py

Changes the specified device to CLI mode in vManage.  Below is an example of how to run.  Update the args to match your environment.

```shell
python detach_device_template.py \
--vmanage_host x.x.x.x \
--vmanage_username username \
--vmanage_password password \
--device_hostname device
```