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