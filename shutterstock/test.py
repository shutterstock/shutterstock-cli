"""
test commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def test():
    """
    test group.
    """


@click.command()
@click.option("--text", multiple=False, help="Text to echo", type=str)
def echo(**kwargs):
    """
    Echo text
    """

    get(url="/v2/test", params=kwargs, json_data=None)


test.add_command(echo)


@click.command()
@click.option("--id", multiple=False, help="Integer ID", type=int)
@click.option("--tag", multiple=True, help="List of tags", type=str)
def validate(**kwargs):
    """
    Validate input
    """

    get(url="/v2/test/validate", params=kwargs, json_data=None)


test.add_command(validate)
