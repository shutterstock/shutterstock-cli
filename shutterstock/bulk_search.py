"""
bulk_search commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def bulk_search():
    """
    bulk_search group.
    """


@click.command()
@click.option(
    "--added-date",
    multiple=False,
    help="Show images added on the specified date",
    type=str,
)
@click.option(
    "--added-date-start",
    multiple=False,
    help="Show images added on or after the specified date",
    type=str,
)
@click.option(
    "--aspect-ratio-min",
    multiple=False,
    help=(
        "Show images with the specified aspect ratio or higher, using a positive"
        " decimal of the width divided by the height, such as 1.7778 for a 16:9 image"
    ),
    type=float,
)
@click.option(
    "--aspect-ratio-max",
    multiple=False,
    help=(
        "Show images with the specified aspect ratio or lower, using a positive decimal"
        " of the width divided by the height, such as 1.7778 for a 16:9 image"
    ),
    type=float,
)
@click.option(
    "--aspect-ratio",
    multiple=False,
    help=(
        "Show images with the specified aspect ratio, using a positive decimal of the"
        " width divided by the height, such as 1.7778 for a 16:9 image"
    ),
    type=float,
)
@click.option(
    "--added-date-end",
    multiple=False,
    help="Show images added before the specified date",
    type=str,
)
@click.option(
    "--category",
    multiple=False,
    help=(
        "Show images with the specified Shutterstock-defined category; specify a"
        " category name or ID"
    ),
    type=str,
)
@click.option(
    "--color",
    multiple=False,
    help=(
        "Specify either a hexadecimal color in the format '4F21EA' or 'grayscale'; the"
        " API returns images that use similar colors"
    ),
    type=str,
)
@click.option(
    "--contributor",
    multiple=True,
    help="Show images with the specified contributor names or IDs, allows multiple",
    type=str,
)
@click.option(
    "--contributor-country",
    multiple=False,
    help=(
        "Show images from contributors in one or more specified countries, or start"
        " with NOT to exclude a country from the search"
    ),
    type=str,
)
@click.option(
    "--fields",
    multiple=False,
    help=(
        "Fields to display in the response; see the documentation for the fields"
        " parameter in the overview section"
    ),
    type=str,
)
@click.option(
    "--height",
    multiple=False,
    help=(
        "(Deprecated; use height_from and height_to instead) Show images with the"
        " specified height"
    ),
    type=int,
)
@click.option(
    "--height-from",
    multiple=False,
    help="Show images with the specified height or larger, in pixels",
    type=int,
)
@click.option(
    "--height-to",
    multiple=False,
    help="Show images with the specified height or smaller, in pixels",
    type=int,
)
@click.option(
    "--image-type", multiple=True, help="Show images of the specified type", type=str
)
@click.option(
    "--keyword-safe-search",
    multiple=False,
    help="Hide results with potentially unsafe keywords",
    type=str,
)
@click.option(
    "--language",
    multiple=False,
    help="Set query and result language (uses Accept-Language header if not set)",
    type=str,
)
@click.option(
    "--license",
    multiple=True,
    help="Show only images with the specified license",
    type=str,
)
@click.option(
    "--model",
    multiple=True,
    help="Show image results with the specified model IDs",
    type=str,
)
@click.option(
    "--orientation",
    multiple=False,
    help="Show image results with horizontal or vertical orientation",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--people-model-released",
    multiple=False,
    help="Show images of people with a signed model release",
    type=str,
)
@click.option(
    "--people-age",
    multiple=False,
    help="Show images that feature people of the specified age category",
    type=str,
)
@click.option(
    "--people-ethnicity",
    multiple=True,
    help=(
        "Show images with people of the specified ethnicities, or start with NOT to"
        " show images without those ethnicities"
    ),
    type=str,
)
@click.option(
    "--people-gender",
    multiple=False,
    help="Show images with people of the specified gender",
    type=str,
)
@click.option(
    "--people-number",
    multiple=False,
    help="Show images with the specified number of people",
    type=int,
)
@click.option(
    "--region",
    multiple=False,
    help=(
        "Raise or lower search result rankings based on the result's relevance to a"
        " specified region; you can provide a country code or an IP address from which"
        " the API infers a country"
    ),
    type=str,
)
@click.option("--safe", multiple=False, help="Enable or disable safe search", type=str)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--spellcheck-query",
    multiple=False,
    help="Spellcheck the search query and return results on suggested spellings",
    type=str,
)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
@click.option(
    "--width",
    multiple=False,
    help=(
        "(Deprecated; use width_from and width_to instead) Show images with the"
        " specified width"
    ),
    type=int,
)
@click.option(
    "--width-from",
    multiple=False,
    help="Show images with the specified width or larger, in pixels",
    type=int,
)
@click.option(
    "--width-to",
    multiple=False,
    help="Show images with the specified width or smaller, in pixels",
    type=int,
)
@click.argument("data")
def bulk_search_images(**kwargs):
    """
    Run multiple image searches
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/bulk_search/images", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


bulk_search.add_command(bulk_search_images)
