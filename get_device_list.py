#!/usr/bin/python3

# import std libs
import argparse
import json
import sys

# import third party libs
from vmanage.api.device import Device

# import app libs
from utils import vmanage_login


def main(args):
    vmanage_session = vmanage_login(
        host=args.vmanage_host,
        username=args.vmanage_username,
        password=args.vmanage_password,
    )
    device_lib = Device(vmanage_session, args.vmanage_host)
    # Any key within the device status response can be used for the query.
    # Here we are using the host-name.
    device_list = device_lib.get_device_list(category="vedges")
    if not device_list:
        sys.exit(f"No devices found.")
    print(json.dumps(device_list, indent=4, sort_keys=True))


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
    args = parser.parse_args()
    sys.exit(main(args))