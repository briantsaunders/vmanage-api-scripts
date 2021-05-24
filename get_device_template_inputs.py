#!/usr/bin/python3

# import std libs
import argparse
import json
import sys

# import third party libs
from vmanage.api.device_templates import DeviceTemplates

# import app libs
from utils import vmanage_login


def main(args):
    """ """
    vmanage_session = vmanage_login(
        host=args.vmanage_host,
        username=args.vmanage_username,
        password=args.vmanage_password,
    )
    device_templates_lib = DeviceTemplates(vmanage_session, args.vmanage_host)
    device_template = device_templates_lib.get_device_template_dict(
        name_list=[args.device_template_name]
    )
    if not args.device_template_name in device_template:
        sys.exit(f"device template {args.device_template_name} not found, exiting")
    device_template_id = device_template[args.device_template_name]["templateId"]
    device_template_inputs = device_templates_lib.get_template_input(device_template_id)
    print(json.dumps(device_template_inputs, indent=4, sort_keys=True))


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
        "--device_template_name",
        required=True,
        action="store",
        help="vmanage device template name",
    )
    args = parser.parse_args()
    sys.exit(main(args))
