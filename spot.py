import spotipy
import spotipy.util as util
import sys
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
            album_artists = []
            for album_artist in results["album"]["artists"]:
                album_artists.append(album_artist["name"])
            album_url = results["album"]["external_urls"]["spotify"]
            album_cover = results["album"]["images"][0]["url"]
            album_release_date = results["album"]["release_date"]
            total_tracks = results["album"]["total_tracks"]
            #song_data
            name = results["name"]
            artists = []
            for artist in results["artists"]:
                artists.append(artist["name"])
            track_number = results["track_number"]
            track_url = results["external_urls"]["spotify"]
            explicit = results["explicit"]
            
        elif characteristics[0] == 'album':
            results = self.spotify.album(characteristics[1])
            print(json.dumps(results, sort_keys=True, ensure_ascii=   False, indent=3))
            for track in results["tracks"]["items"]:
                print(track["name"],
                track["uri"])
            
        elif characteristics[0] == 'artist':
            results = self.spotify.artist_albums(characteristics[1])
        elif characteristics[0] == 'playlist':
            results = self.spotify.playlist(characteristics[1])



res = spotr('shcixv399pe9eirp62esm93').get_song_info(input(">>>>> \t"))