"""
editor commands.
"""

import json
import click

from .utils.request import delete, get, post


@click.group()
def editor():
    """
    editor group.
    """


@click.command()
@click.argument("data")
def register_editor_instance(**kwargs):
    """
    Register instances of the video editor
    """

    try:
        with open(kwargs["data"]) as input_data:
            json_data = json.load(input_data)

        post(url="/v2/editor/customers", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


editor.add_command(register_editor_instance)


@click.command()
@click.argument("data")
def update_editor_instance(**kwargs):
    """
    Update instances of the video editor
    """

    try:
        with open(kwargs["data"]) as input_data:
            json_data = json.load(input_data)

        patch(url="/v2/editor/customers", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


editor.add_command(update_editor_instance)


@click.command()
@click.argument("data")
def auth_video_editor(**kwargs):
    """
    Get video editor access tokens
    """

    try:
        with open(kwargs["data"]) as input_data:
            json_data = json.load(input_data)

        post(url="/v2/editor/auth", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


editor.add_command(auth_video_editor)
