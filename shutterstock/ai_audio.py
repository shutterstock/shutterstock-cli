"""
ai_audio commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def ai_audio():
    """
    ai_audio group.
    """


@click.command()
@click.argument("data")
def create_audio_renders(**kwargs):
    """
    Create rendered audio
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/ai/audio/renders", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


ai_audio.add_command(create_audio_renders)


@click.command()
@click.option("--id", multiple=True, help="One or more render IDs", type=str)
def fetch_renders(**kwargs):
    """
    Get details about audio renders
    """

    get(url="/v2/ai/audio/renders", params=kwargs, json_data=None)


ai_audio.add_command(fetch_renders)


@click.command()
@click.option(
    "--id", multiple=True, help="Show instruments with the specified ID", type=str
)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option(
    "--name",
    multiple=False,
    help="Show instruments with the specified name (case-sensitive)",
    type=str,
)
@click.option(
    "--tag",
    multiple=False,
    help=(
        "Show instruments with the specified tag, such as Percussion or Strings"
        " (case-sensitive)"
    ),
    type=str,
)
def list_custom_instruments(**kwargs):
    """
    List computer audio instruments
    """

    get(url="/v2/ai/audio/instruments", params=kwargs, json_data=None)


ai_audio.add_command(list_custom_instruments)


@click.command()
@click.option(
    "--render-speed-over",
    multiple=False,
    help=(
        "Show descriptors with an average render speed that is greater than or equal to"
        " the specified value"
    ),
    type=float,
)
@click.option(
    "--band-id",
    multiple=False,
    help="Show descriptors that contain the specified band (case-sentsitive)",
    type=str,
)
@click.option(
    "--band-name",
    multiple=False,
    help="Show descriptors with the specified band name (case-sensitive)",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--id",
    multiple=True,
    help="Show descriptors with the specified IDs (case-sensitive)",
    type=str,
)
@click.option(
    "--instrument-name",
    multiple=False,
    help="Show descriptors with the specified instrument name (case-sensitive)",
    type=str,
)
@click.option(
    "--instrument-id",
    multiple=False,
    help="Show descriptors with the specified instrument ID (case-sensitive)",
    type=str,
)
@click.option(
    "--tempo",
    multiple=False,
    help=(
        "Show descriptors whose tempo range includes the specified tempo in beats per"
        " minute"
    ),
    type=float,
)
@click.option(
    "--tempo-to",
    multiple=False,
    help=(
        "Show descriptors with a tempo that is less than or equal to the specified"
        " number"
    ),
    type=float,
)
@click.option(
    "--tempo-from",
    multiple=False,
    help=(
        "Show descriptors that have a tempo range that includes the specified tempo in"
        " beats per minute"
    ),
    type=float,
)
@click.option(
    "--name",
    multiple=False,
    help="Show descriptors with the specified name (case-sensitive)",
    type=str,
)
@click.option(
    "--tag",
    multiple=False,
    help=(
        "Show descriptors with the specified tag, such as Cinematic or Roomy"
        " (case-sensitive)"
    ),
    type=str,
)
def list_custom_descriptors(**kwargs):
    """
    List computer audio descriptors
    """

    get(url="/v2/ai/audio/descriptors", params=kwargs, json_data=None)


ai_audio.add_command(list_custom_descriptors)
