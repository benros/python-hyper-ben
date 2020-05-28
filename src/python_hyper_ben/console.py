import textwrap

import click
import requests

from . import __version__


API_URL = "https://{lang}.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
@click.option("--language-edition", default="en", help="the language edition of Wikipedia API")
def main(language_edition: str):
    """The Hyper python project"""
    NEW_API_URL = API_URL.format(lang=language_edition)
    try:
        with requests.get(NEW_API_URL) as response:
            response.raise_for_status()
            data = response.json()

        title = data["title"]
        extract = data["extract"]
    except:
        title = "API NOT FOUND"
        extract = "The API URL is not reachable"


    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
