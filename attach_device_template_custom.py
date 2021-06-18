#!/usr/bin/python3

# import std libs
import argparse
import json
import sys
from pathlib import Path

# import third party libs
import yaml
from vmanage.api.device import Device
from vmanage.api.device_templates import DeviceTemplates
from vmanage.api.http_methods import HttpMethods
from vmanage.api.utilities import Utilities

# import app libs
from utils import vmanage_login


def main(args):
    vmanage_session = vmanage_login(
        host=args.vmanage_host,
        username=args.vmanage_username,
        password=args.vmanage_password,
    )
    # Verify device uuid exists
    device_lib = Device(vmanage_session, args.vmanage_host)
    device_list = device_lib.get_device_list(category="vedges")
    device_uuid_found = False
    for device in device_list:
        if device["uuid"] == args.device_uuid:
            device_uuid_found = True
    if not device_uuid_found:
        sys.exit(f"device {args.device_uuid} not found, exiting.")
    device_templates_lib = DeviceTemplates(vmanage_session, args.vmanage_host)
    # Verify that the template exists and get the template id.
    device_template = device_templates_lib.get_device_template_dict(
        name_list=[args.device_template_name]
    )
    if not args.device_template_name in device_template:
        sys.exit(f"device template {args.device_template_name} not found, exiting")
    device_template_id = device_template[args.device_template_name]["templateId"]
    device_template_inputs_file = Path(args.device_template_inputs_file)
    if not device_template_inputs_file.is_file():
        sys.exit(
            f"device templates input file {device_template_inputs_file} not found, exiting."
        )
    with open(device_template_inputs_file) as file:
        device_template_inputs = yaml.safe_load(file)
    device_template_variables = {
        "csv-status": "complete",
        "csv-deviceId": args.device_uuid,
        "csv-deviceIP": device_template_inputs["//system/system-ip"],
        "csv-host-name": device_template_inputs["//system/host-name"]
    }
    # add device template inputs to device template variables
    for k,v in device_template_inputs.items():
        device_template_variables[k] = v
    # most append device template vars to list
    # could append multiple if wanting to attach more than one device
    # to the same template
    device_template_variables_list = [device_template_variables]
    payload = {
        "deviceTemplateList": [{
            "templateId": device_template_id,
            "device": device_template_variables_list,
            "isEdited": False,
            "isMasterEdited": False
        }]
    }
    base_url = f"https://{args.vmanage_host}:443/dataservice/"
    url = f"{base_url}template/device/config/attachfeature"
    utils = Utilities(vmanage_session, args.vmanage_host)
    response = HttpMethods(vmanage_session, url).request('POST', payload=json.dumps(payload))
    if 'json' in response and 'id' in response['json']:
        action_id = response['json']['id']
        utils.waitfor_action_completion(action_id)
    else:
        raise Exception('Did not get action ID after attaching device to template.')
    print(action_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Example vManage API Script")
    parser.add_argument(
        "--vmanage_host", required=True, action="store", help="vmanage host"
    )
    parser.add_argument(
        "--vmanage_username", required=True, action="store", help="vmanage username"
    )
    parser.add_argument(
        "--vmanage_password", required=True, action="store", help="vmanage password"
    )
    parser.add_argument(
        "--device_uuid", required=True, action="store", help="vmanage device uuid"
    )
    parser.add_argument(
        "--device_template_name",
        required=True,
        action="store",
        help="vmanage device template name",
    )
    parser.add_argument(
        "--device_template_inputs_file",
        required=True,
        action="store",
        help="vmanage device templates inputs file",
    )
    args = parser.parse_args()
    sys.exit(main(args))
