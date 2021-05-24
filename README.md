# vManage API Python Script Examples

This repo contains example scripts for interacting with the Cisco vManage API in python.  These scripts leverage the [python-viptela](https://github.com/CiscoDevNet/python-viptela) library.

## Getting Started

### Install

```shell
pip install -r requirements.txt
```

## Scripts

### get_device_status.py

Retrieves device status from vManage.

```shell
python get_device_status.py --vmanage_host x.x.x.x --vmanage_username username --vmanage_password password --device_hostname device
```