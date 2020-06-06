#import numpy as np
#import pyqrcode as pq
import click
import os
import re
#from .functions import wifi_qr, qr2array

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)

class ApiKey(click.ParamType):
    name = 'api-key'

    def convert(self, value, param, ctx):
        found = re.match(r'[0-9a-f]{32}', value)

        if not found:
            self.fail(
                f'{value} is not a 32-character hexadecimal string',
                param,
                ctx,
            )

        return value

def current_rapid(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

@click.group()
@click.option("--django", help="Django Framework.")
@click.option("--version", type=click.Choice(["1", "2", "3"]),
              help='an available version of django')
@click.option(
    '--api-key', '-a',
    type=ApiKey(),
    help='your API key for the OpenWeatherMap API',
)

@click.pass_context
def main(config, django, version):
    """
    CLI to connect with rapidjango
    """

@main.command()
@click.pass_context
def create_mk_virtualenv(config):
    click.echo('create > mkvirtualenv')

@main.command()
@click.pass_context
@click.argument('name')
def create_dj_project(config, name):
    click.echo('create > django-project')

@main.command()
@click.pass_context
def create_app(config):
    click.echo('create > django-app')

#@main.command()
#@click.pass_context
#def terminal(ctx):
#    click.echo(ctx.obj["dj"].terminal())


def start():
    main(obj={})


if __name__ == "__main__":
    start()
