"""
sfx commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def sfx():
    """
    sfx group.
    """


@click.command()
@click.option(
    "--added-date",
    multiple=False,
    help="Show sound effects added on the specified date",
    type=str,
)
@click.option(
    "--added-date-start",
    multiple=False,
    help="Show sound effects added on or after the specified date",
    type=str,
)
@click.option(
    "--added-date-end",
    multiple=False,
    help="Show sound effects added before the specified date",
    type=str,
)
@click.option(
    "--duration",
    multiple=False,
    help="Show sound effects with the specified duration in seconds",
    type=int,
)
@click.option(
    "--duration-from",
    multiple=False,
    help="Show sound effects with the specified duration or longer in seconds",
    type=int,
)
@click.option(
    "--duration-to",
    multiple=False,
    help="Show sound effects with the specified duration or shorter in seconds",
    type=int,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--query",
    multiple=False,
    help="One or more search terms separated by spaces",
    type=str,
)
@click.option("--safe", multiple=False, help="Enable or disable safe search", type=str)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
@click.option(
    "--language",
    multiple=False,
    help="Set query and result language (uses Accept-Language header if not set)",
    type=str,
)
def search_sfx(**kwargs):
    """
    Search for sound effects
    """

    get(url="/v2/sfx/search", params=kwargs, json_data=None)


sfx.add_command(search_sfx)


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
@click.option("--library", multiple=False, help="Which library to fetch from", type=str)
@click.option(
    "--search-id",
    multiple=False,
    help="The ID of the search that is related to this request",
    type=str,
)
def get_sfx_details(**kwargs):
    """
    Get details about sound effects
    """

    get(url="/v2/sfx/" + kwargs["id"] + "", params=kwargs, json_data=None)


sfx.add_command(get_sfx_details)


@click.command()
@click.option("--id", multiple=True, help="One or more sound effect IDs", type=str)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
@click.option("--library", multiple=False, help="Which library to fetch from", type=str)
@click.option(
    "--search-id",
    multiple=False,
    help="The ID of the search that is related to this request",
    type=str,
)
def get_sfx_list_details(**kwargs):
    """
    List details about sound effects
    """

    get(url="/v2/sfx", params=kwargs, json_data=None)


sfx.add_command(get_sfx_list_details)


@click.command()
@click.option(
    "--sfx-id",
    multiple=False,
    help="Show licenses for the specified sound effects ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help=(
        "Show sound effects that are available with the specified license, such as"
        " `standard` or `enhanced`"
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
@click.option("--license-id", multiple=False, help="Filter by the license ID", type=str)
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
def get_sfx_license_list(**kwargs):
    """
    List sound effects licenses
    """

    get(url="/v2/sfx/licenses", params=kwargs, json_data=None)


sfx.add_command(get_sfx_license_list)


@click.command()
@click.argument("data")
def licenses_sfx(**kwargs):
    """
    License sound effects
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/sfx/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


sfx.add_command(licenses_sfx)


@click.command()
@click.argument("id")
def download_sfx(**kwargs):
    """
    Download sound effects
    """

    post(
        url="/v2/sfx/licenses/" + kwargs["id"] + "/downloads",
        params=kwargs,
        json_data=None,
    )


sfx.add_command(download_sfx)
