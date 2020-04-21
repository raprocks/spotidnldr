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
        #print(link_type, link_id)
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
            return_dict = {"album_data":{"name":album, "album_artists":album_artists, "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks": total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}}
        elif characteristics[0] == 'album':
            results = self.spotify.album(characteristics[1])
            #album data
            album=results["name"]
            album_artists=[artist["name"] for artist in results["artists"]]
            album_url=results["external_urls"]["spotify"]
            album_cover=results["images"][0]["url"]
            album_release_date=results["release_date"]
            total_tracks=results["total_tracks"]
            #track data
            song_names = [song["name"] for song in results["tracks"]["items"]]
#            artists = []
#            for track in results["tracks"]["items"]:
#                artists.append([artist["name"] for artist in track["artists"]])
            artistss = [([artist["name"] for artist in track["artists"]]) for track in results["tracks"]["items"]]
            explicits=[track["explicit"] for track in results["tracks"]["items"]]
            track_urls=[track["external_urls"]["spotify"] for track in results["tracks"]["items"]]
#            for song_name in song_names:
#                print(song_name, end=", \n")
            return_dict=[{"album_data":{"name":album, "album_artists":album_artists, "url":album_url, "album_cover":album_cover, "album_release_date":album_release_date, "total_tracks":total_tracks}, "tracks_data":{"name":song_name, "song_artists":artists, "explicits":explicit, "track_urls":track_url}} for song_name,artists,explicit,track_url in zip(song_names,artistss,explicits,track_urls)]
        elif characteristics[0] == 'artist':
            offset = 0
            return_dict=[]
            results = self.spotify.artist_albums(characteristics[1])
            total_albums = results["total"]
            results_for_artist=self.spotify.artist(characteristics[1])
            Name=results_for_artist["name"]
            while offset<total_albums:
                results = self.spotify.artist_albums(characteristics[1], offset=offset, limit=50)
                albumResults = results['items']
                for item in albumResults:
                    #print("ALBUM: " + item['name'])
                    albumurl = item['external_urls']["spotify"]
                    albumArt = item['images'][0]['url']
                    # Extract track data
                    trackResults = self.get_song_info(albumurl)
                    for item in trackResults:
                        if Name in str(item["tracks_data"]["song_artists"]):
                            #print(item["tracks_data"]["name"])
                            return_dict.append(item)
                print(offset)
                offset+=50
                    

                        
            #return_dict =[{"album_data":{"name":album, "album_artists":str(album_artists).strip("[]"),"url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks":total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}} for album,album_artists, album_url, album_cover, album_release_date, total_tracks, name, artists, track_number, track_url, explicit in zip(albums, album_artistss, album_urls, album_covers, album_release_dates, total_trackss, names, artistss, track_numbers, track_urls, explicits)]
        elif characteristics[0] == 'playlist':
            results = self.spotify.playlist_tracks(characteristics[1])
            tracks=[track["track"] for track in results["items"]]
            #album_data
            albums = [track["album"]["name"] for track in tracks]
            album_artistss = [[album_artist["name"] for album_artist in track["album"]["artists"]] for track in tracks]
            album_urls = [track["album"]["external_urls"]["spotify"] for track in tracks]
            album_covers = [track["album"]["images"][0]["url"] for track in tracks]
            album_release_dates = [track["album"]["release_date"] for track in tracks]
            total_trackss = [track["album"]["total_tracks"] for track in tracks]
            #songs_data
            names = [track["name"] for track in tracks]
            artistss = [([artist["name"] for artist in track["artists"]]) for track in tracks]
            track_numbers = [track["track_number"] for track in tracks]
            track_urls = [track["external_urls"]["spotify"] for track in tracks]
            explicits = [track["explicit"] for track in tracks]
            return_dict =[{"album_data":{"name":album, "album_artists":str(album_artists).strip("[]"), "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks": total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}} for album,album_artists, album_url, album_cover, album_release_date, total_tracks, name, artists, track_number, track_url, explicit in zip(albums, album_artistss, album_urls, album_covers, album_release_dates, total_trackss, names, artistss, track_numbers, track_urls, explicits)]
        return return_dict
#        return_dict = {"album_data":{},"track_data":{}}

if __name__=="__main__":
    res = spotr('shcixv399pe9eirp62esm93').get_song_info(input("enter url to pull data about"))
    #print(res)
    print(json.dumps(res, indent=3))
    print(len(res))
#print(res)
