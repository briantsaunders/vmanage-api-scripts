#!/usr/bin/python3

# import third party libs
from vmanage.api.authentication import Authentication


def vmanage_login(host: str, username: str, password: str):
    """
    """
    return Authentication(
        host=host,
        user=username,
        password=password
    ).login()

