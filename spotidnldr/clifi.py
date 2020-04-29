import click
from spotidnldr.env_setup import *
from spotidnldr.env_checker import *
from spotidnldr.spot import *



@click.command()
@click.option("--url", prompt="enter Url of spotify song", help="hi")
def download(url):
    s = spotr().get_song_info(url)
    print(s)