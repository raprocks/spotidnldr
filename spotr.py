import spotipy
import spotipy.util as util
import sys

def get_token(userid):
    try:
        local_token = util.prompt_for_user_token(username)
    except:
        print("Something seems wrong :( \n Have you set up all of the Enviornment Variables and given your username as input?")
# https://open.spotify.com/user/shcixv399pe9e6dirp62esm93?si=OWXuEM81QdG_jJ91cgYCxg
    return local_token


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
#song_example: "https://open.spotify.com/track/56Y4UR8J9TiYPpwwctOcQh?si=P1IbWC8qTk2USvP38QaySw"
#single_song_album_example: "https://open.spotify.com/album/4uq5OQ3FE3mIU9JJtez4EV?si=OAJHCtXeSLKDJYDmExukZA"
#multi_song_album_example:"https://open.spotify.com/album/3vOgbDjgsZBAPwV2M3bNOj?si=Q3HG7aLVSRS211UHo10TRQ"
#artist_example:"https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz?si=fnGyAJq0RaarszzAKtxAhg"
#playlist_example:"https://open.spotify.com/playlist/37i9dQZF1DWSRc3WJklgBs?si=UAHU5avuTJuhT2oi0CuQ-w"
def get_characteristics(url):
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
    print(uri)
    return str(uri)

def get_song_info(userid, url):
    token = get_token(str(userid))
    spotify = spotipy.Spotify(auth=token)
    uri = get_characteristics(str(url))   