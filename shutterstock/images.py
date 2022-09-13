"""
images commands.
"""

import json
import click

from .utils.request import delete, get, post, patch


@click.group()
def images():
    """
    images group.
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
    "--query",
    multiple=False,
    help=(
        "One or more search terms separated by spaces; you can use NOT to filter out"
        " images that match a term"
    ),
    type=str,
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
def search_images(**kwargs):
    """
    Search for images
    """

    get(url="/v2/images/search", params=kwargs, json_data=None)


images.add_command(search_images)


@click.command()
@click.option(
    "--query",
    multiple=False,
    help="Search term for which you want keyword suggestions",
    type=str,
)
@click.option(
    "--limit", multiple=False, help="Limit the number of suggestions", type=int
)
def get_image_suggestions(**kwargs):
    """
    Get suggestions for a search term
    """

    get(url="/v2/images/search/suggestions", params=kwargs, json_data=None)


images.add_command(get_image_suggestions)


@click.command()
@click.argument("data")
def get_image_keyword_suggestions(**kwargs):
    """
    Get keywords from text
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/images/search/suggestions", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(get_image_keyword_suggestions)


@click.command()
@click.option("--id", multiple=True, help="One or more image IDs", type=str)
@click.option(
    "--view",
    multiple=False,
    help="Amount of detail to render in the response",
    type=str,
)
def get_image_list(**kwargs):
    """
    List images
    """

    get(url="/v2/images", params=kwargs, json_data=None)


images.add_command(get_image_list)


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
def get_image(**kwargs):
    """
    Get details about images
    """

    get(url="/v2/images/" + kwargs["id"] + "", params=kwargs, json_data=None)


images.add_command(get_image)


@click.command()
@click.option(
    "--language",
    multiple=False,
    help="Language for the keywords and categories in the response",
    type=str,
)
def list_image_categories(**kwargs):
    """
    List image categories
    """

    get(url="/v2/images/categories", params=kwargs, json_data=None)


images.add_command(list_image_categories)


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
def list_similar_images(**kwargs):
    """
    List similar images
    """

    get(url="/v2/images/" + kwargs["id"] + "/similar", params=kwargs, json_data=None)


images.add_command(list_similar_images)


@click.command()
@click.option(
    "--subscription-id",
    multiple=False,
    help="Subscription ID to use to license the image",
    type=str,
)
@click.option("--format", multiple=False, help="(Deprecated) Image format", type=str)
@click.option("--size", multiple=False, help="Image size", type=str)
@click.option(
    "--search-id",
    multiple=False,
    help="Search ID that was provided in the results of an image search",
    type=str,
)
@click.argument("data")
def license_images(**kwargs):
    """
    License images
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/images/licenses", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(license_images)


@click.command()
@click.option(
    "--image-id",
    multiple=False,
    help="Show licenses for the specified image ID",
    type=str,
)
@click.option(
    "--license",
    multiple=False,
    help=(
        "Show images that are available with the specified license, such as `standard`"
        " or `enhanced`; prepending a `-` sign excludes results from that license"
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
def get_image_license_list(**kwargs):
    """
    List image licenses
    """

    get(url="/v2/images/licenses", params=kwargs, json_data=None)


images.add_command(get_image_license_list)


@click.command()
@click.argument("id")
@click.argument("data")
def download_image(**kwargs):
    """
    Download images
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/images/licenses/" + kwargs["id"] + "/downloads",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(download_image)


@click.command()
@click.option("--id", multiple=True, help="Image IDs", type=str)
@click.option(
    "--max-items",
    multiple=False,
    help="Maximum number of results returned in the response",
    type=int,
)
@click.option(
    "--safe", multiple=False, help="Restrict results to safe images", type=str
)
def get_image_recommendations(**kwargs):
    """
    List recommended images
    """

    get(url="/v2/images/recommendations", params=kwargs, json_data=None)


images.add_command(get_image_recommendations)


@click.command()
@click.argument("data")
def create_image_collection(**kwargs):
    """
    Create image collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(url="/v2/images/collections", params=kwargs, json_data=json_data)
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(create_image_collection)


@click.command()
@click.option(
    "--embed",
    multiple=True,
    help=(
        "Which sharing information to include in the response, such as a URL to the"
        " collection"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
def get_image_collection_list(**kwargs):
    """
    List image collections
    """

    get(url="/v2/images/collections", params=kwargs, json_data=None)


images.add_command(get_image_collection_list)


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
def get_image_collection(**kwargs):
    """
    Get the details of image collections
    """

    get(
        url="/v2/images/collections/" + kwargs["id"] + "", params=kwargs, json_data=None
    )


images.add_command(get_image_collection)


@click.command()
@click.argument("id")
@click.argument("data")
def rename_image_collection(**kwargs):
    """
    Rename image collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/images/collections/" + kwargs["id"] + "",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(rename_image_collection)


@click.command()
@click.argument("id")
def delete_image_collection(**kwargs):
    """
    Delete image collections
    """

    delete(
        url="/v2/images/collections/" + kwargs["id"] + "", params=kwargs, json_data=None
    )


images.add_command(delete_image_collection)


@click.command()
@click.argument("id")
@click.argument("data")
def add_image_collection_items(**kwargs):
    """
    Add images to collections
    """

    try:
        with open(kwargs["data"], encoding="UTF-8") as input_data:
            json_data = json.load(input_data)

        post(
            url="/v2/images/collections/" + kwargs["id"] + "/items",
            params=kwargs,
            json_data=json_data,
        )
    except json.decoder.JSONDecodeError:
        print(
            "Error loading JSON file. Please pass a valid JSON file as an argument."
            " (Check API reference for more information)"
        )


images.add_command(add_image_collection_items)


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
def get_image_collection_items(**kwargs):
    """
    Get the contents of image collections
    """

    get(
        url="/v2/images/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


images.add_command(get_image_collection_items)


@click.command()
@click.argument("id")
@click.option(
    "--item-id",
    multiple=True,
    help="One or more image IDs to remove from the collection",
    type=str,
)
def delete_image_collection_items(**kwargs):
    """
    Remove images from collections
    """

    delete(
        url="/v2/images/collections/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


images.add_command(delete_image_collection_items)


@click.command()
@click.option(
    "--embed",
    multiple=False,
    help=(
        "Which sharing information to include in the response, such as a URL to the"
        " collection"
    ),
    type=str,
)
@click.option(
    "--type", multiple=True, help="The types of collections to return", type=str
)
@click.option("--asset-hint", multiple=False, help="Cover image size", type=str)
def get_featured_image_collection_list(**kwargs):
    """
    List featured image collections
    """

    get(url="/v2/images/collections/featured", params=kwargs, json_data=None)


images.add_command(get_featured_image_collection_list)


@click.command()
@click.argument("id")
@click.option(
    "--embed",
    multiple=False,
    help=(
        "Which sharing information to include in the response, such as a URL to the"
        " collection"
    ),
    type=str,
)
@click.option("--asset-hint", multiple=False, help="Cover image size", type=str)
def get_featured_image_collection(**kwargs):
    """
    Get the details of featured image collections
    """

    get(
        url="/v2/images/collections/featured/" + kwargs["id"] + "",
        params=kwargs,
        json_data=None,
    )


images.add_command(get_featured_image_collection)


@click.command()
@click.argument("id")
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
def get_featured_image_collection_items(**kwargs):
    """
    Get the contents of featured image collections
    """

    get(
        url="/v2/images/collections/featured/" + kwargs["id"] + "/items",
        params=kwargs,
        json_data=None,
    )


images.add_command(get_featured_image_collection_items)


@click.command()
@click.option(
    "--type",
    multiple=True,
    help=(
        "Show images that were added, deleted, or edited; by default, the endpoint"
        " returns images that were updated in any of these ways"
    ),
    type=str,
)
@click.option(
    "--start-date",
    multiple=False,
    help="Show images updated on or after the specified date",
    type=str,
)
@click.option(
    "--end-date",
    multiple=False,
    help="Show images updated before the specified date",
    type=str,
)
@click.option(
    "--interval",
    multiple=False,
    help=(
        "Show images updated in the specified time period, where the time period is an"
        " interval (like SQL INTERVAL) such as 1 DAY, 6 HOUR, or 30 MINUTE; the default"
        " is 1 HOUR, which shows images that were updated in the hour preceding the"
        " request"
    ),
    type=str,
)
@click.option("--page", multiple=False, help="Page number", type=int)
@click.option("--per-page", multiple=False, help="Number of results per page", type=int)
@click.option("--sort", multiple=False, help="Sort order", type=str)
def get_updated_images(**kwargs):
    """
    List updated images
    """

    get(url="/v2/images/updated", params=kwargs, json_data=None)


images.add_command(get_updated_images)
