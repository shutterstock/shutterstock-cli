"""
audio commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def audio():
    """
    audio group.
    """


@click.command()
@click.option(
    "--artists",
    multiple=True,
    help="Show tracks with one of the specified artist names or IDs",
    type=str,
)
@click.option(
    "--bpm",
    multiple=False,
    help=(
        "(Deprecated; use bpm_from and bpm_to instead) Show tracks with the specified"
        " beats per minute"
    ),
    type=int,
)
@click.option(
    "--bpm-from",
    multiple=False,
    help="Show tracks with the specified beats per minute or faster",
    type=int,
)
@click.option(
    "--bpm-to",
    multiple=False,
    help="Show tracks with the specified beats per minute or slower",
    type=int,
)
@click.option(
    "--duration",
    multiple=False,
    help="Show tracks with the specified duration in seconds",
    type=int,
)
@click.option(
    "--duration-from",
    multiple=False,
    help="Show tracks with the specified duration or longer in seconds",
    type=int,
)
@click.option(
    "--duration-to",
    multiple=False,
    help="Show tracks with the specified duration or shorter in seconds",
    type=int,
)
@click.option(
    "--genre",
    multiple=True,
    help=(
        "Show tracks with each of the specified genres; to get the list of genres, use"
        " `GET /v2/audio/genres`"
    ),
    type=str,
)
@click.option(
    "--is-instrumental", multiple=False, help="Show instrumental music only", type=str
)
@click.option(
    "--instruments",
    multiple=True,
    help=(
        "Show tracks with each of the specified instruments; to get the list of"
        " instruments, use `GET /v2/audio/instruments`"
    ),
    type=str,
)
@click.option(
    "--moods",
    multiple=True,
    help=(
        "Show tracks with each of the specified moods; to get the list of moods, use"
        " `GET /v2/audio/moods`"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--query",
    multiple=False,
    help="One or more search terms separated by spaces",
    type=str,
)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option("--sort-order", multiple=False, help="Sort order", type=str)
@click.option(
    "--vocal-description",
    multiple=False,
    help="Show tracks with the specified vocal description (male, female)",
    type=str,
)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
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
@click.option("--library", multiple=False, help="Which library to search", type=str)
@click.option(
    "--language", multiple=False, help="Which language to search in", type=str
)
def search_tracks(**kwargs):
    """
    Search for tracks
    """

    get(url="/v2/audio/search", params=kwargs, json_data=None)


audio.add_command(search_tracks)


@click.command()
@click.option(
    "--language",
    multiple=False,
    help="Which language the genres will be returned",
    type=str,
)
def list_genres(**kwargs):
    """
    List audio genres
    """

    get(url="/v2/audio/genres", params=kwargs, json_data=None)


audio.add_command(list_genres)


@click.command()
@click.option(
    "--language",
    multiple=False,
    help="Which language the moods will be returned in",
    type=str,
)
def list_instruments(**kwargs):
    """
    List audio instruments
    """

    get(url="/v2/audio/instruments", params=kwargs, json_data=None)


audio.add_command(list_instruments)


@click.command()
@click.option(
    "--language",
    multiple=False,
    help="Which language the moods will be returned in",
    type=str,
)
def list_moods(**kwargs):
    """
    List audio moods
    """

    get(url="/v2/audio/moods", params=kwargs, json_data=None)


audio.add_command(list_moods)


@click.command()
@click.option("--id", multiple=True, help="One or more audio IDs", type=str)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_track_list(**kwargs):
    """
    List audio tracks
    """

    get(url="/v2/audio", params=kwargs, json_data=None)


audio.add_command(get_track_list)


@click.command()
@click.argument("id")
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_track(**kwargs):
    """
    Get details about audio tracks
    """

    get(url="/v2/audio/" + kwargs["id"] + "", params=kwargs, json_data=None)


audio.add_command(get_track)


@click.command()
@click.option("--license", multiple=False, help="License type", type=str)
@click.option(
    "--search-id",
    multiple=False,
    help="The ID of the search that led to licensing this track",
    type=str,
)
@click.argument("data")
def license_track(**kwargs):
    """
    License audio tracks
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/audio/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


audio.add_command(license_track)


@click.command()
@click.option(
    "--audio-id",
    multiple=False,
    help="Show licenses for the specified track ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help=(
        "Restrict results by license. Prepending a `-` sign will exclude results by"
        " license"
    ),
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
def get_track_license_list(**kwargs):
    """
    List audio licenses
    """

    get(url="/v2/audio/licenses", params=kwargs, json_data=None)


audio.add_command(get_track_license_list)


@click.command()
@click.argument("id")
def download_tracks(**kwargs):
    """
    Download audio tracks
    """

    post(
        url="/v2/audio/licenses/" + kwargs["id"] + "/downloads",
        params=kwargs,
        json_data=None,
    )


audio.add_command(download_tracks)


@click.command()
@click.argument("data")
def create_track_collection(**kwargs):
    """
    Create audio collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/audio/collections", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


audio.add_command(create_track_collection)


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
def get_track_collection_list(**kwargs):
    """
    List audio collections
    """

    get(url="/v2/audio/collections", params=kwargs, json_data=None)


audio.add_command(get_track_collection_list)


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
def get_track_collection(**kwargs):
    """
    Get the details of audio collections
    """

    get(url="/v2/audio/collections/" + kwargs["id"] + "", params=kwargs, json_data=None)


audio.add_command(get_track_collection)


@click.command()
@click.argument("id")
@click.argument("data")
def rename_track_collection(**kwargs):
    """
    Rename audio collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/audio/collections/" + kwargs["id"] + "",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


audio.add_command(rename_track_collection)


@click.command()
@click.argument("id")
def delete_track_collection(**kwargs):
    """
    Delete audio collections
    """

    delete(
        url="/v2/audio/collections/" + kwargs["id"] + "", params=kwargs, json_data=None
    )


audio.add_command(delete_track_collection)


@click.command()
@click.argument("id")
@click.argument("data")
def add_track_collection_items(**kwargs):
    """
    Add audio tracks to collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/audio/collections/" + kwargs["id"] + "/items",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


audio.add_command(add_track_collection_items)


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
def get_track_collection_items(**kwargs):
    """
    Get the contents of audio collections
    """

    get(
        url="/v2/audio/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


audio.add_command(get_track_collection_items)


@click.command()
@click.argument("id")
@click.option(
    "--item-id",
    multiple=True,
    help="One or more item IDs to remove from the collection",
    type=str,
)
def delete_track_collection_items(**kwargs):
    """
    Remove audio tracks from collections
    """

    delete(
        url="/v2/audio/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


audio.add_command(delete_track_collection_items)
