import os
import pathlib
import logging
import click
from spotidnldr.spot import spotr
import spotidnldr.env_setup as e
from spotidnldr.cover_download import dl_jpg
from spotidnldr.youtube_search import youtube_search
from spotidnldr.downloader import YDL
from spotidnldr.tag_embedder import tag_embed
from spotidnldr.converter import convert_to_mp3


@click.group()
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False,
              help="flag for verbosity, usage of this flag gives more\
                   output use this for sending or finding errors.")
@click.option('-o', "--output",
              help="provide a output path for the song explicitly.",
              default="./",
              type=click.Path(),
              show_default=True,
              envvar="SPOTIFY_DOWNLOAD_PATH"
              )
@click.argument("url",
                required=True,
                type=str)
@click.version_option(version='v1.3.0', prog_name='spotidnldr')
def download(url, output, verbose):
    """
    Downloads Songs from URL.

    URL must be a valid spotify link of a song, album or a playlist.
    """
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        pass
    print('saving Songs to', output)
    clientid = e.SPOTIPY_CLIENT_ID
    clientsecret = e.SPOTIPY_CLIENT_SECRET
    res = spotr(
        clientid=clientid,
        clientsecret=clientsecret).get_song_info(url)
    for each in res:
        album_cover_url = each["album_data"]["album_cover"]
        name = each["track_data"]["name"] + " - " + \
            str(each["track_data"]["artists"]).strip(
                "[]").strip("\'").replace("\'", "")
        title = each["track_data"]["name"]
        song_artists = str(each["track_data"]["artists"]).strip(
            "[]").strip("\'").replace("\'", "")
        album_name = each["album_data"]["name"]
        album_artists = str(each["album_data"]["album_artists"]).strip(
            "[]").strip("\'").replace("\'", "")
        track_number = each["track_data"]["track_number"]
        total_tracks = each["album_data"]["total_tracks"]
        release_date = each["album_data"]["album_release_date"]
        if "/" in name:
            name = name.replace('/', "")
            name = name.replace("/\\", "")
        if f"{name}.mp3" in str(os.listdir(output)):
            print(f"a file named {name} already in {output}")
            overwrite = input(
                "Do you still want to Overwrite \
                    and Download the File Again? Y/N")
            if 'y' == overwrite.lower():
                os.remove(os.path.abspath(os.path.join(output, name+".mp3")))
                print("deleted")
            else:
                continue
        if ".temp" not in os.listdir():
            os.mkdir(".temp")
        print("got info from spotify")
        img_save_path = pathlib.Path('./.temp')
        img_name = dl_jpg(album_cover_url, img_save_path, name)
        print("got image")
        retrived_from_youtube = youtube_search(q=name)
        print("got youtube url", retrived_from_youtube)
        infile = YDL(retrived_from_youtube).downloader(filename=name)
        print("downloaded from youtube", infile)
        print("in :", infile)
        print("out :", output)
        convert_to_mp3(infile,
                       os.path.join(output, f"{name}.mp3"),
                       verbose=verbose)
        print("converted")
        _ = tag_embed(os.path.join(output,
                                   f"{name}.mp3"),
                      title=title, artists=song_artists,
                      album=album_name,
                      album_artists=album_artists,
                      release_date=release_date,
                      track_number=track_number,
                      total_tracks=total_tracks,
                      img_path=img_name)
        print("added metadata")
        # os.remove(img_name)
        os.remove(infile)
        print("cleanup complete")
        print("\n", name, "Done")

