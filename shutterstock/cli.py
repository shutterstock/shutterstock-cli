"""
Shutterstock CLI
"""
import click


from .images import images

from .bulk_search import bulk_search

from .videos import videos

from .audio import audio

from .editorial import editorial

from .cv import cv

from .catalog import catalog

from .ai_audio import ai_audio

from .contributors import contributors

from .user import user

from .test import test


@click.group()
def cli():
    """
    For reference information about the endpoints that this CLI calls, see the API reference.
    http://api-reference.shutterstock.com/
    """


cli.add_command(images)

cli.add_command(bulk_search)

cli.add_command(videos)

cli.add_command(audio)

cli.add_command(editorial)

cli.add_command(cv)

cli.add_command(catalog)

cli.add_command(ai_audio)

cli.add_command(contributors)

cli.add_command(user)

cli.add_command(test)


if __name__ == "__main__":
    cli()
