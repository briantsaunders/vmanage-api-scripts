#!/usr/bin/python3

# import std libs
import argparse
import json
import sys

# import third party libs
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
    device_lib = Device(vmanage_session, args.vmanage_host)
    # Any key within the device status response can be used for the query.
    # Here we are using the host-name.
    device_status = device_lib.get_device_status(args.device_hostname, key="host-name")
    if not device_status:
        sys.exit(f"device {args.device_hostname} not found, exiting.")
    utilities_lib = Utilities(vmanage_session, args.vmanage_host)
    payload = {
        "deviceType": device_status["device-type"],
        "devices": [
            {"deviceId": device_status["uuid"], "deviceIP": device_status["system-ip"]}
        ],
    }
    url = f"https://{args.vmanage_host}:443/dataservice/template/config/device/mode/cli"
    response = HttpMethods(vmanage_session, url).request(
        "POST", payload=json.dumps(payload)
    )
    if "json" in response and "id" in response["json"]:
        action_id = response["json"]["id"]
        utilities_lib.waitfor_action_completion(action_id)


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
        "--device_hostname", required=True, action="store", help="vmanage device"
    )
    args = parser.parse_args()
    sys.exit(main(args))
