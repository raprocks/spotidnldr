import spotipy
import spotipy.util as util
import sys
from tree import *
import json
def get_userid_from_url(url):
    url = str(url)
    url = url.split('/')
    userid = url[-1]
    if '?' in userid:
        userid = userid.split('?')[0]
    else:
        pass
    print(userid)
    return str(userid)


class spotr:
    def __init__(self, userid):
        try:
            local_token = util.prompt_for_user_token(userid)
        except:
            print("Something seems wrong :( \n Have you set up all of the Enviornment Variables and given your username as input?")
# https://open.spotify.com/user/shcixv399pe9e6dirp62esm93?si=OWXuEM81QdG_jJ91cgYCxg
        self.spotify = spotipy.Spotify(auth=local_token)

    def get_userid_from_url(self, url):
        url = str(url)
        url = url.split('/')
        userid = url[-1]
        if '?' in userid:
            userid = userid.split('?')[0]
        else:
            pass
    #    print(userid)
        return str(userid)
#song_example: "https://open.spotify.com/track/56Y4UR8J9TiYPpwwctOcQh?si=P1IbWC8qTk2USvP38QayS"
#single_song_album_example: "https://open.spotify.com/album/4uq5OQ3FE3mIU9JJtez4EV?si=OAJHCtXeSLKDJYDmExukZA"
#multi_song_album_example:"https://open.spotify.com/album/3vOgbDjgsZBAPwV2M3bNOj?si=Q3HG7aLVSRS211UHo10TRQ"
#artist_example: "https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz"
#playlist_example:"https://open.spotify.com/playlist/37i9dQZF1DWSRc3WJklgBs?si=UAHU5avuTJuhT2oi0CuQ-w"
    def get_characteristics(self, url):
        url = str(url)
        url = url.split('/')
        link_type = str(url[3])
        link_id = str(url[4])
        if '?' in link_id:
            link_id = link_id.split("?")
            link_id = link_id[0]
        else:
            pass
        print(link_type, link_id)
        uri = "spotify:"+str(link_type)+":"+str(link_id)
   #     print(str(uri))
        return [link_type, link_id]

    def get_song_info(self, url):
        characteristics = self.get_characteristics(str(url))
   #     print(url)
        if characteristics[0] == 'track':
        #https://open.spotify.com/track/2YWjW3wwQIBLNhxWKBQd16?si=Gdnokw7BTGSFOAHuAnuvzA
            results = self.spotify.track(characteristics[1])
           # print(json.dumps(results, sort_keys=True, ensure_ascii=False, indent=3))
            #album_data
            album = results["album"]["name"]
            album_artists = [album_artist["name"] for album_artist in results["album"]["artists"]]
            album_url = results["album"]["external_urls"]["spotify"]
            album_cover = results["album"]["images"][0]["url"]
            album_release_date = results["album"]["release_date"]
            total_tracks = results["album"]["total_tracks"]
            #song_data
            name = results["name"]
            artists = [artist["name"] for artist in results["artists"]]
            track_number = results["track_number"]
            track_url = results["external_urls"]["spotify"]
            explicit = results["explicit"]
            return_dict = {"album_data":{"album_name":album, "album_artists":str(album_artists).strip("[").strip("]"), "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks": total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}}
        elif characteristics[0] == 'album':
            results = self.spotify.album_tracks(characteristics[1])
            song_names = [(song["name"] + "-" + str([artist["name"] for artist in song["artists"]]).strip("[").strip("]")) for song in results["items"]]
            for song_name in song_names:
                print(song_name, end=", \n")
        elif characteristics[0] == 'artist':
            results = self.spotify.artist_albums(characteristics[1])
        elif characteristics[0] == 'playlist':
            results = self.spotify.playlist(characteristics[1])
        return results
        return_dict = {"album_data":{},"track_data":{}}


res = spotr('shcixv399pe9eirp62esm93').get_song_info("https://open.spotify.com/album/4otkd9As6YaxxEkIjXPiZ6?si=znyfYGKERvWU-8tbbT0rTw")
#PrintTree().printTree(tree=res)
#with open("f.json", "w+") as f:
#    f.write(str(json.dumps(res, indent=4)))
