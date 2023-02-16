"""
catalog commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def catalog():
    """
    catalog group.
    """


@click.command()
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option(
    "--query",
    multiple=False,
    help="One or more search terms separated by spaces",
    type=str,
)
@click.option(
    "--collection-id", multiple=True, help="Filter by collection id", type=str
)
@click.option("--asset-type", multiple=True, help="Filter by asset type", type=str)
def search_catalog(**kwargs):
    """
    Search catalogs for assets
    """

    get(url="/v2/catalog/search", params=kwargs, json_data=None)


catalog.add_command(search_catalog)


@click.command()
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--sort", multiple=False, help="Sort by", type=str)
@click.option(
    "--shared",
    multiple=False,
    help=(
        "Set to true to omit collections that you own and return only collections  that"
        " are shared with you"
    ),
    type=str,
)
def get_collections(**kwargs):
    """
    List catalog collections
    """

    get(url="/v2/catalog/collections", params=kwargs, json_data=None)


catalog.add_command(get_collections)


@click.command()
@click.argument("data")
def create_collection(**kwargs):
    """
    Create catalog collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/catalog/collections", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


catalog.add_command(create_collection)


@click.command()
@click.argument("collection-id")
@click.argument("data")
def update_collection(**kwargs):
    """
    Update collection metadata
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        patch(
            url="/v2/catalog/collections/" + kwargs["collection_id"] + "",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


catalog.add_command(update_collection)


@click.command()
@click.argument("collection-id")
def delete_collection(**kwargs):
    """
    Delete catalog collections
    """

    delete(
        url="/v2/catalog/collections/" + kwargs["collection_id"] + "",
        params=kwargs,
        json_data=None,
    )


catalog.add_command(delete_collection)


@click.command()
@click.argument("collection-id")
@click.argument("data")
def add_to_collection(**kwargs):
    """
    Add items to catalog collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/catalog/collections/" + kwargs["collection_id"] + "/items",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


catalog.add_command(add_to_collection)


@click.command()
@click.argument("collection-id")
@click.argument("data")
def delete_from_collection(**kwargs):
    """
    Remove items from catalog collection
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        delete(
            url="/v2/catalog/collections/" + kwargs["collection_id"] + "/items",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


catalog.add_command(delete_from_collection)
