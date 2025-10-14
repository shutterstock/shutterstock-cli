""""
HTTP functions.
"""

import json
import os

import requests

from .prettyprint import pretty_print
from .request_helper import RequestHelper

COLORIZE_OUTPUT = os.getenv("SHUTTERSTOCK_CLI_COLORIZE_OUTPUT")


def get(url, params, json_data=None):
    """
    Get resource.
    :param url: URL of the endpoint.
    :param params: Request parameters.
    :param json_data: Request body.
    :return: None
    """
    req = RequestHelper()
    res = requests.get(
        url=f"{req.base_endpoint}{url}",
        params=params,
        headers=req.headers,
        auth=req.auth,
    )
    try:
        if not COLORIZE_OUTPUT:
            print(json.dumps(res.json(), indent=4))
            return
        pretty_print(res.json())
    except json.decoder.JSONDecodeError:
        print(res.content)


def post(url, params, json_data):
    """
    Post resource.
    :param url: URL of the endpoint.
    :param params: Request parameters.
    :param json_data: Request body.
    :return: None
    """
    req = RequestHelper()
    res = requests.post(
        url=f"{req.base_endpoint}{url}",
        params=params,
        json=json_data,
        headers=req.headers,
        auth=req.auth,
    )
    try:
        if not COLORIZE_OUTPUT:
            print(json.dumps(res.json(), indent=4))
            return
        pretty_print(res.json())
    except json.decoder.JSONDecodeError:
        print(res.content)


def delete(url, params, json_data):
    """
    Delete resource.
    :param url: URL of the endpoint.
    :param params: Request parameters.
    :param json_data: Request body.
    :return: None
    """
    req = RequestHelper()
    res = requests.delete(
        url=f"{req.base_endpoint}{url}",
        params=params,
        json=json_data,
        headers=req.headers,
        auth=req.auth,
    )
    try:
        if not COLORIZE_OUTPUT:
            print(json.dumps(res.json(), indent=4))
            return
        pretty_print(res.json())
    except json.decoder.JSONDecodeError:
        print(res.content)


def put(url, params, json_data):
    """
    Put resource.
    :param url: URL of the endpoint.
    :param params: Request parameters.
    :param json_data: Request body.
    :return: None
    """
    req = RequestHelper()
    res = requests.put(
        url=f"{req.base_endpoint}{url}",
        params=params,
        json=json_data,
        headers=req.headers,
        auth=req.auth,
    )
    try:
        if not COLORIZE_OUTPUT:
            print(json.dumps(res.json(), indent=4))
            return
        pretty_print(res.json())
    except json.decoder.JSONDecodeError:
        print(res.content)


def patch(url, params, json_data):
    """
    PATCH resource.
    :param url: URL of the endpoint.
    :param params: Request parameters.
    :param json_data: Request body.
    :return: None
    """
    req = RequestHelper()
    res = requests.patch(
        url=f"{req.base_endpoint}{url}",
        params=params,
        json=json_data,
        headers=req.headers,
        auth=req.auth,
    )
    try:
        if not COLORIZE_OUTPUT:
            print(json.dumps(res.json(), indent=4))
            return
        pretty_print(res.json())
    except json.decoder.JSONDecodeError:
        print(res.content)
