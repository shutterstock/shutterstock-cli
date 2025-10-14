"""
user commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def user():
    """
    user group.
    """


@click.command()
def get_user(**kwargs):
    """
    Get user details
    """

    get(url="/v2/user", params=kwargs, json_data=None)


user.add_command(get_user)


@click.command()
def get_access_token(**kwargs):
    """
    Get access token details
    """

    get(url="/v2/user/access_token", params=kwargs, json_data=None)


user.add_command(get_access_token)


@click.command()
def get_user_subscription_list(**kwargs):
    """
    List user subscriptions
    """

    get(url="/v2/user/subscriptions", params=kwargs, json_data=None)


user.add_command(get_user_subscription_list)
