"""
videos commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def videos():
    """
    videos group.
    """


@click.command()
@click.option(
    "--added-date",
    multiple=False,
    help="Show videos added on the specified date",
    type=str,
)
@click.option(
    "--added-date-start",
    multiple=False,
    help="Show videos added on or after the specified date",
    type=str,
)
@click.option(
    "--added-date-end",
    multiple=False,
    help="Show videos added before the specified date",
    type=str,
)
@click.option(
    "--aspect-ratio",
    multiple=False,
    help="Show videos with the specified aspect ratio",
    type=str,
)
@click.option(
    "--category",
    multiple=False,
    help=(
        "Show videos with the specified Shutterstock-defined category; specify a"
        " category name or ID"
    ),
    type=str,
)
@click.option(
    "--contributor",
    multiple=True,
    help="Show videos with the specified artist names or IDs",
    type=str,
)
@click.option(
    "--contributor-country",
    multiple=True,
    help="Show videos from contributors in one or more specified countries",
    type=str,
)
@click.option(
    "--duration",
    multiple=False,
    help=(
        "(Deprecated; use duration_from and duration_to instead) Show videos with the"
        " specified duration in seconds"
    ),
    type=int,
)
@click.option(
    "--duration-from",
    multiple=False,
    help="Show videos with the specified duration or longer in seconds",
    type=int,
)
@click.option(
    "--duration-to",
    multiple=False,
    help="Show videos with the specified duration or shorter in seconds",
    type=int,
)
@click.option(
    "--fps",
    multiple=False,
    help=(
        "(Deprecated; use fps_from and fps_to instead) Show videos with the specified"
        " frames per second"
    ),
    type=float,
)
@click.option(
    "--fps-from",
    multiple=False,
    help="Show videos with the specified frames per second or more",
    type=float,
)
@click.option(
    "--fps-to",
    multiple=False,
    help="Show videos with the specified frames per second or fewer",
    type=float,
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
    help="Show only videos with the specified license or licenses",
    type=str,
)
@click.option(
    "--model",
    multiple=True,
    help="Show videos with each of the specified models",
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--people-age",
    multiple=False,
    help="Show videos that feature people of the specified age range",
    type=str,
)
@click.option(
    "--people-ethnicity",
    multiple=True,
    help="Show videos with people of the specified ethnicities",
    type=str,
)
@click.option(
    "--people-gender",
    multiple=False,
    help="Show videos with people with the specified gender",
    type=str,
)
@click.option(
    "--people-number",
    multiple=False,
    help="Show videos with the specified number of people",
    type=int,
)
@click.option(
    "--people-model-released",
    multiple=False,
    help="Show only videos of people with a signed model release",
    type=str,
)
@click.option(
    "--query",
    multiple=False,
    help=(
        "One or more search terms separated by spaces; you can use NOT to filter out"
        " videos that match a term"
    ),
    type=str,
)
@click.option(
    "--resolution",
    multiple=False,
    help="Show videos with the specified resolution",
    type=str,
)
@click.option("--safe", multiple=False, help="Enable or disable safe search", type=str)
@click.option(
    "--sort", multiple=False, help="Sort by one of these categories", type=str
)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def search_videos(**kwargs):
    """
    Search for videos
    """

    get(url="/v2/videos/search", params=kwargs, json_data=None)


videos.add_command(search_videos)


@click.command()
@click.option(
    "--query",
    multiple=False,
    help="Search term for which you want keyword suggestions",
    type=str,
)
@click.option(
    "--limit", multiple=False, help="Limit the number of the suggestions", type=int
)
def get_video_suggestions(**kwargs):
    """
    Get suggestions for a search term
    """

    get(url="/v2/videos/search/suggestions", params=kwargs, json_data=None)


videos.add_command(get_video_suggestions)


@click.command()
@click.option("--id", multiple=True, help="One or more video IDs", type=str)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_video_list(**kwargs):
    """
    List videos
    """

    get(url="/v2/videos", params=kwargs, json_data=None)


videos.add_command(get_video_list)


@click.command()
@click.argument("id")
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_video(**kwargs):
    """
    Get details about videos
    """

    get(url="/v2/videos/" + kwargs["id"] + "", params=kwargs, json_data=None)


videos.add_command(get_video)


@click.command()
@click.option(
    "--subscription-id",
    multiple=False,
    help="The subscription ID to use for licensing",
    type=str,
)
@click.option(
    "--size", multiple=False, help="The size of the video to license", type=str
)
@click.option(
    "--search-id",
    multiple=False,
    help="The Search ID that led to this licensing event",
    type=str,
)
@click.argument("data")
def license_videos(**kwargs):
    """
    License videos
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/videos/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


videos.add_command(license_videos)


@click.command()
@click.option(
    "--video-id",
    multiple=False,
    help="Show licenses for the specified video ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help=(
        "Show videos that are available with the specified license, such as `standard`"
        " or `enhanced`; prepending a `-` sign excludes results from that license"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--sort", multiple=False, help="Sort by oldest or newest videos first", type=str
)
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
def get_video_license_list(**kwargs):
    """
    List video licenses
    """

    get(url="/v2/videos/licenses", params=kwargs, json_data=None)


videos.add_command(get_video_license_list)


@click.command()
@click.argument("id")
@click.argument("data")
def download_videos(**kwargs):
    """
    Download videos
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/videos/licenses/" + kwargs["id"] + "/downloads",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


videos.add_command(download_videos)


@click.command()
@click.argument("data")
def create_video_collection(**kwargs):
    """
    Create video collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/videos/collections", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


videos.add_command(create_video_collection)


@click.command()
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--embed",
    multiple=True,
    help=(
        "Which sharing information to include in the response, such as a URL to the"
        " collection"
    ),
    type=str,
)
def get_video_collection_list(**kwargs):
    """
    List video collections
    """

    get(url="/v2/videos/collections", params=kwargs, json_data=None)


videos.add_command(get_video_collection_list)


@click.command()
@click.argument("id")
@click.option(
    "--embed",
    multiple=True,
    help=(
        "Which sharing information to include in the response, such as a URL to the"
        " collection"
    ),
    type=str,
)
@click.option(
    "--share-code",
    multiple=False,
    help="Code to retrieve a shared collection",
    type=str,
)
def get_video_collection(**kwargs):
    """
    Get the details of video collections
    """

    get(
        url="/v2/videos/collections/" + kwargs["id"] + "", params=kwargs, json_data=None
    )


videos.add_command(get_video_collection)


@click.command()
@click.argument("id")
@click.argument("data")
def rename_video_collection(**kwargs):
    """
    Rename video collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/videos/collections/" + kwargs["id"] + "",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


videos.add_command(rename_video_collection)


@click.command()
@click.argument("id")
def delete_video_collection(**kwargs):
    """
    Delete video collections
    """

    delete(
        url="/v2/videos/collections/" + kwargs["id"] + "", params=kwargs, json_data=None
    )


videos.add_command(delete_video_collection)


@click.command()
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
def list_video_categories(**kwargs):
    """
    List video categories
    """

    get(url="/v2/videos/categories", params=kwargs, json_data=None)


videos.add_command(list_video_categories)


@click.command()
@click.argument("id")
@click.argument("data")
def add_video_collection_items(**kwargs):
    """
    Add videos to collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/videos/collections/" + kwargs["id"] + "/items",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


videos.add_command(add_video_collection_items)


@click.command()
@click.argument("id")
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--share-code",
    multiple=False,
    help="Code to retrieve the contents of a shared collection",
    type=str,
)
@click.option("--sort", multiple=False, help="Sort order", type=str)
def get_video_collection_items(**kwargs):
    """
    Get the contents of video collections
    """

    get(
        url="/v2/videos/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


videos.add_command(get_video_collection_items)


@click.command()
@click.argument("id")
@click.option(
    "--item-id",
    multiple=True,
    help="One or more video IDs to remove from the collection",
    type=str,
)
def delete_video_collection_items(**kwargs):
    """
    Remove videos from collections
    """

    delete(
        url="/v2/videos/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


videos.add_command(delete_video_collection_items)


@click.command()
@click.option(
    "--embed",
    multiple=False,
    help="What information to include in the response, such as a URL to the collection",
    type=str,
)
def get_featured_video_collection_list(**kwargs):
    """
    List featured video collections
    """

    get(url="/v2/videos/collections/featured", params=kwargs, json_data=None)


videos.add_command(get_featured_video_collection_list)


@click.command()
@click.argument("id")
@click.option(
    "--embed",
    multiple=False,
    help="What information to include in the response, such as a URL to the collection",
    type=str,
)
def get_featured_video_collection(**kwargs):
    """
    Get the details of featured video collections
    """

    get(
        url="/v2/videos/collections/featured/" + kwargs["id"] + "",
        params=kwargs,
        json_data=None,
    )


videos.add_command(get_featured_video_collection)


@click.command()
@click.argument("id")
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
def get_featured_video_collection_items(**kwargs):
    """
    Get the contents of featured video collections
    """

    get(
        url="/v2/videos/collections/featured/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


videos.add_command(get_featured_video_collection_items)


@click.command()
@click.argument("id")
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
def find_similar_videos(**kwargs):
    """
    List similar videos
    """

    get(url="/v2/videos/" + kwargs["id"] + "/similar", params=kwargs, json_data=None)


videos.add_command(find_similar_videos)


@click.command()
@click.option(
    "--start-date",
    multiple=False,
    help="Show videos updated on or after the specified date",
    type=str,
)
@click.option(
    "--end-date",
    multiple=False,
    help="Show videos updated before the specified date",
    type=str,
)
@click.option(
    "--interval",
    multiple=False,
    help=(
        "Show videos updated in the specified time period, where the time period is an"
        " interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default"
        " is 1 HOUR, which shows videos that were updated in the hour preceding the"
        " request"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--sort", multiple=False, help="Sort by oldest or newest videos first", type=str
)
def get_updated_videos(**kwargs):
    """
    List updated videos
    """

    get(url="/v2/videos/updated", params=kwargs, json_data=None)


videos.add_command(get_updated_videos)
