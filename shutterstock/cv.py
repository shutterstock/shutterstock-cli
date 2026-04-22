"""
cv commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def cv():
    """
    cv group.
    """


@click.command()
@click.argument("data")
def upload_image(**kwargs):
    """
    Upload images
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/cv/images", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


cv.add_command(upload_image)


@click.command()
@click.option(
    "--asset-id",
    multiple=False,
    help="The asset ID or upload ID to find similar images for",
    type=str,
)
@click.option(
    "--license",
    multiple=True,
    help="Show only images with the specified license",
    type=str,
)
@click.option("--safe", multiple=False, help="Enable or disable safe search", type=str)
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_similar_images(**kwargs):
    """
    List similar images
    """

    get(url="/v2/cv/similar/images", params=kwargs, json_data=None)


cv.add_command(get_similar_images)


@click.command()
@click.option(
    "--asset-id",
    multiple=False,
    help="The asset ID or upload ID to find similar videos for",
    type=str,
)
@click.option(
    "--license",
    multiple=True,
    help="Show only videos with the specified license",
    type=str,
)
@click.option("--safe", multiple=False, help="Enable or disable safe search", type=str)
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_similar_videos(**kwargs):
    """
    List similar videos
    """

    get(url="/v2/cv/similar/videos", params=kwargs, json_data=None)


cv.add_command(get_similar_videos)


@click.command()
@click.option(
    "--asset-id",
    multiple=False,
    help="The asset ID or upload ID to suggest keywords for",
    type=str,
)
def get_keywords(**kwargs):
    """
    List suggested keywords
    """

    get(url="/v2/cv/keywords", params=kwargs, json_data=None)


cv.add_command(get_keywords)
