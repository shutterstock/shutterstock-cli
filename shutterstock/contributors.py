"""
contributors commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def contributors():
    """
    contributors group.
    """


@click.command()
@click.option("--id", multiple=True, help="One or more contributor IDs", type=str)
def get_contributor_list(**kwargs):
    """
    Get details about multiple contributors
    """

    get(url="/v2/contributors", params=kwargs, json_data=None)


contributors.add_command(get_contributor_list)


@click.command()
@click.argument("contributor-id")
def get_contributor(**kwargs):
    """
    Get details about a single contributor
    """

    get(
        url="/v2/contributors/" + kwargs["contributor_id"] + "",
        params=kwargs,
        json_data=None,
    )


contributors.add_command(get_contributor)


@click.command()
@click.argument("contributor-id")
@click.option("--sort", multiple=False, help="Sort order", type=str)
def get_contributor_collections_list(**kwargs):
    """
    List contributors' collections
    """

    get(
        url="/v2/contributors/" + kwargs["contributor_id"] + "/collections",
        params=kwargs,
        json_data=None,
    )


contributors.add_command(get_contributor_collections_list)


@click.command()
@click.argument("contributor-id")
@click.argument("id")
def get_contributor_collections(**kwargs):
    """
    Get details about contributors' collections
    """

    get(
        url="/v2/contributors/"
        + kwargs["contributor_id"]
        + "/collections/"
        + kwargs["id"]
        + "",
        params=kwargs,
        json_data=None,
    )


contributors.add_command(get_contributor_collections)


@click.command()
@click.argument("contributor-id")
@click.argument("id")
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--sort", multiple=False, help="Sort order", type=str)
def get_contributor_collection_items(**kwargs):
    """
    Get the items in contributors' collections
    """

    get(
        url="/v2/contributors/"
        + kwargs["contributor_id"]
        + "/collections/"
        + kwargs["id"]
        + "/items",
        params=kwargs,
        json_data=None,
    )


contributors.add_command(get_contributor_collection_items)
