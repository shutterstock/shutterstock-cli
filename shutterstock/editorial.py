"""
editorial commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def editorial():
    """
    editorial group.
    """


@click.command()
@click.option(
    "--query",
    multiple=False,
    help="One or more search terms separated by spaces",
    type=str,
)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--category",
    multiple=False,
    help=(
        "Show editorial content with each of the specified editorial categories;"
        " specify category names in a comma-separated list"
    ),
    type=str,
)
@click.option(
    "--country",
    multiple=False,
    help=(
        "Show only editorial content that is available for distribution in a certain"
        " country"
    ),
    type=str,
)
@click.option(
    "--supplier-code",
    multiple=True,
    help="Show only editorial content from certain suppliers",
    type=str,
)
@click.option(
    "--date-start",
    multiple=False,
    help="Show only editorial content generated on or after a specific date",
    type=str,
)
@click.option(
    "--date-end",
    multiple=False,
    help="Show only editorial content generated on or before a specific date",
    type=str,
)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--cursor",
    multiple=False,
    help=(
        "The cursor of the page with which to start fetching results; this cursor is"
        " returned from previous requests"
    ),
    type=str,
)
def search_editorial_images(**kwargs):
    """
    Search editorial images
    """

    get(url="/v2/editorial/images/search", params=kwargs, json_data=None)


editorial.add_command(search_editorial_images)


@click.command()
def list_editorial_image_categories(**kwargs):
    """
    List editorial categories
    """

    get(url="/v2/editorial/images/categories", params=kwargs, json_data=None)


editorial.add_command(list_editorial_image_categories)


@click.command()
@click.option(
    "--type",
    multiple=False,
    help=(
        "Specify `addition` to return only images that were added or `edit` to return"
        " only images that were edited or deleted"
    ),
    type=str,
)
@click.option(
    "--date-updated-start",
    multiple=False,
    help=(
        "Show images images added, edited, or deleted after the specified date."
        " Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00."
    ),
    type=str,
)
@click.option(
    "--date-updated-end",
    multiple=False,
    help=(
        "Show images images added, edited, or deleted before the specified date."
        " Acceptable range is 1970-01-01T00:00:01 to 2038-01-19T00:00:00."
    ),
    type=str,
)
@click.option(
    "--date-taken-start",
    multiple=False,
    help=(
        "Show images that were taken on or after the specified date; use this parameter"
        " if you want recently created images from the collection instead of updated"
        " older assets"
    ),
    type=str,
)
@click.option(
    "--date-taken-end",
    multiple=False,
    help="Show images that were taken before the specified date",
    type=str,
)
@click.option(
    "--cursor",
    multiple=False,
    help=(
        "The cursor of the page with which to start fetching results; this cursor is"
        " returned from previous requests"
    ),
    type=str,
)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--supplier-code",
    multiple=True,
    help="Show only editorial content from certain suppliers",
    type=str,
)
@click.option(
    "--country",
    multiple=False,
    help=(
        "Show only editorial content that is available for distribution in a certain"
        " country"
    ),
    type=str,
)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
def get_updated_editorial_images(**kwargs):
    """
    List updated content
    """

    get(url="/v2/editorial/images/updated", params=kwargs, json_data=None)


editorial.add_command(get_updated_editorial_images)


@click.command()
@click.argument("id")
@click.option(
    "--country",
    multiple=False,
    help=(
        "Returns only if the content is available for distribution in a certain country"
    ),
    type=str,
)
def get_editorial_image(**kwargs):
    """
    Get editorial content details
    """

    get(url="/v2/editorial/images/" + kwargs["id"] + "", params=kwargs, json_data=None)


editorial.add_command(get_editorial_image)


@click.command()
@click.option(
    "--image-id",
    multiple=False,
    help="Show licenses for the specified editorial image ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help="Show editorial images that are available with the specified license name",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--sort", multiple=False, help="Sort order", type=str)
@click.option(
    "--username",
    multiple=False,
    help="Filter licenses by username of licensee",
    type=str,
)
@click.option(
    "--start-date",
    multiple=False,
    help="Show licenses created on or after the specified date",
    type=str,
)
@click.option(
    "--end-date",
    multiple=False,
    help="Show licenses created before the specified date",
    type=str,
)
@click.option(
    "--download-availability",
    multiple=False,
    help="Filter licenses by download availability",
    type=str,
)
@click.option(
    "--team-history",
    multiple=False,
    help="Set to true to see license history for all members of your team.",
    type=str,
)
def get_editorial_image_license_list(**kwargs):
    """
    List editorial image licenses
    """

    get(url="/v2/editorial/images/licenses", params=kwargs, json_data=None)


editorial.add_command(get_editorial_image_license_list)


@click.command()
@click.argument("data")
def license_editorial_images(**kwargs):
    """
    License editorial content
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/editorial/images/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


editorial.add_command(license_editorial_images)


@click.command()
@click.option(
    "--country",
    multiple=False,
    help=(
        "Returns only livefeeds that are available for distribution in a certain"
        " country"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
def get_editorial_image_livefeed_list(**kwargs):
    """
    Get editorial livefeed list
    """

    get(url="/v2/editorial/images/livefeeds", params=kwargs, json_data=None)


editorial.add_command(get_editorial_image_livefeed_list)


@click.command()
@click.argument("id")
@click.option(
    "--country",
    multiple=False,
    help=(
        "Returns only if the livefeed is available for distribution in a certain"
        " country"
    ),
    type=str,
)
def get_editorial_image_livefeed(**kwargs):
    """
    Get editorial livefeed
    """

    get(
        url="/v2/editorial/images/livefeeds/" + kwargs["id"] + "",
        params=kwargs,
        json_data=None,
    )


editorial.add_command(get_editorial_image_livefeed)


@click.command()
@click.argument("id")
@click.option(
    "--country",
    multiple=False,
    help=(
        "Returns only if the livefeed items are available for distribution in a certain"
        " country"
    ),
    type=str,
)
def get_editorial_image_livefeed_items(**kwargs):
    """
    Get editorial livefeed items
    """

    get(
        url="/v2/editorial/images/livefeeds/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


editorial.add_command(get_editorial_image_livefeed_items)


@click.command()
@click.option(
    "--query",
    multiple=False,
    help="One or more search terms separated by spaces",
    type=str,
)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--category",
    multiple=False,
    help=(
        "Show editorial content with each of the specified editorial categories;"
        " specify category names in a comma-separated list"
    ),
    type=str,
)
@click.option(
    "--country",
    multiple=False,
    help=(
        "Show only editorial video content that is available for distribution in a"
        " certain country"
    ),
    type=str,
)
@click.option(
    "--supplier-code",
    multiple=True,
    help="Show only editorial video content from certain suppliers",
    type=str,
)
@click.option(
    "--date-start",
    multiple=False,
    help="Show only editorial video content generated on or after a specific date",
    type=str,
)
@click.option(
    "--date-end",
    multiple=False,
    help="Show only editorial video content generated on or before a specific date",
    type=str,
)
@click.option(
    "--resolution",
    multiple=False,
    help="Show only editorial video content with specific resolution",
    type=str,
)
@click.option(
    "--fps",
    multiple=False,
    help="Show only editorial video content generated with specific frames per second",
    type=float,
)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--cursor",
    multiple=False,
    help=(
        "The cursor of the page with which to start fetching results; this cursor is"
        " returned from previous requests"
    ),
    type=str,
)
def search_editorial_videos(**kwargs):
    """
    Search editorial video content
    """

    get(url="/v2/editorial/videos/search", params=kwargs, json_data=None)


editorial.add_command(search_editorial_videos)


@click.command()
def list_editorial_video_categories(**kwargs):
    """
    List editorial video categories
    """

    get(url="/v2/editorial/videos/categories", params=kwargs, json_data=None)


editorial.add_command(list_editorial_video_categories)


@click.command()
@click.argument("id")
@click.option(
    "--country",
    multiple=False,
    help=(
        "Returns only if the content is available for distribution in a certain country"
    ),
    type=str,
)
def get_editorial_video(**kwargs):
    """
    Get editorial video content details
    """

    get(url="/v2/editorial/videos/" + kwargs["id"] + "", params=kwargs, json_data=None)


editorial.add_command(get_editorial_video)


@click.command()
@click.option(
    "--video-id",
    multiple=False,
    help="Show licenses for the specified editorial video ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help="Show editorial videos that are available with the specified license name",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--sort", multiple=False, help="Sort order", type=str)
@click.option(
    "--username",
    multiple=False,
    help="Filter licenses by username of licensee",
    type=str,
)
@click.option(
    "--start-date",
    multiple=False,
    help="Show licenses created on or after the specified date",
    type=str,
)
@click.option(
    "--end-date",
    multiple=False,
    help="Show licenses created before the specified date",
    type=str,
)
@click.option(
    "--download-availability",
    multiple=False,
    help="Filter licenses by download availability",
    type=str,
)
@click.option(
    "--team-history",
    multiple=False,
    help="Set to true to see license history for all members of your team.",
    type=str,
)
def get_editorial_video_license_list(**kwargs):
    """
    List editorial video licenses
    """

    get(url="/v2/editorial/videos/licenses", params=kwargs, json_data=None)


editorial.add_command(get_editorial_video_license_list)


@click.command()
@click.argument("data")
def license_editorial_video(**kwargs):
    """
    License editorial video content
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/editorial/videos/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


editorial.add_command(license_editorial_video)
