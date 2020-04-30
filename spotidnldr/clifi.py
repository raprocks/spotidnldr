import click
from spotidnldr.env_checker import *
from spotidnldr.spot import *
from spotidnldr import *
from spotidnldr.cover_download import *
from spotidnldr.youtube_search import *
from spotidnldr.downloader import *
from spotidnldr.tag_embedder import *
from spotidnldr.converter import *
import json

env_list = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIFY_USER_ID", "SPOTIPY_REDIRECT_URI", "YOUTUBE_API_KEY"]
local_vars=locals()
current_envs=os.environ
for var in env_list:
    if var in current_envs:
        print(f"{var} is set in environment.Replacing.")
        locals()[var]=current_envs[var]
        local_vars=locals()
        print(local_vars[var])
    elif var in local_vars:
        print(f"{var} is set in env_vars.py")
    else:
        print(f"{var} is not set")

@click.command()
@click.option("--url", prompt="enter Url of spotify song", help="hi")
def download(url):
    userid=SPOTIFY_USER_ID
    clientid=SPOTIPY_CLIENT_ID
    clientsecret=SPOTIPY_CLIENT_SECRET
    redirecturi=SPOTIPY_REDIRECT_URI
    res = spotr(userid=userid, clientid=clientid, clientsecret=clientsecret, redirecturi=redirecturi).get_song_info(url)
    for each in res:
        os.system("youtube-dl --rm-cache-dir")
        album_cover_url = each["album_data"]["album_cover"]
        name = each["track_data"]["name"]+ " - " + str(each["track_data"]["artists"]).strip("[]").strip("\'").replace("\'", "")
        title = each["track_data"]["name"]
        song_artists = str(each["track_data"]["artists"]).strip("[]").strip("\'").replace("\'", "")
        album_name = each["album_data"]["name"]
        album_artists = str(each["album_data"]["album_artists"]).strip("[]").strip("\'").replace("\'", "")
        track_number = each["track_data"]["track_number"]
        total_tracks = each["album_data"]["total_tracks"]
        release_date = each["album_data"]["album_release_date"]
        if "/" in name:
            name = name.replace("/\\","" )
        img_name = dl_jpg(album_cover_url, "./", name)
        retrived_from_youtube=youtube().search(query=name,order="relevance", limit=10, return_indices=3)
        infile = download_yout(url=retrived_from_youtube[0], file_name=name)
        convert_to_mp3(infile, f"/storage/emulated/0/Songs/{name}.mp3")
        tag_embed(f"/storage/emulated/0/Songs/{name}.mp3", title=title, artists=song_artists, album=album_name, album_artists=album_artists, release_date=release_date, track_number=track_number, total_tracks=total_tracks, img_path=img_name)
        os.remove(img_name)
        os.remove(infile)
    print("done", name)