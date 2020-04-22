import spotipy
import spotipy.util as util
import json
from cover_download import dl_jpg


class spotr:
    def __init__(self, userid):
        try:
            local_token = util.prompt_for_user_token(userid)
        except:
            print("Something seems wrong :( \n Have you set up all of the Enviornment Variables and given your username as input?")
        self.spotify = spotipy.Spotify(auth=local_token)

    def get_userid_from_url(self, url):
        url = str(url)
        url = url.split('/')
        userid = url[-1]
        if '?' in userid:
            userid = userid.split('?')[0]
        else:
            pass
        return str(userid)
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
        uri = "spotify:"+ str(link_type) + ":" + str(link_id)
        return [link_type, link_id]

    def get_song_info(self, url):
        characteristics = self.get_characteristics(str(url))
        if characteristics[0] == 'track':
            results = self.spotify.track(characteristics[1])
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
            return_dict = [{"album_data":{"name":album, "album_artists":album_artists, "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks": total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}}]
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
            artistss = [([artist["name"] for artist in track["artists"]]) for track in results["tracks"]["items"]]
            explicits=[track["explicit"] for track in results["tracks"]["items"]]
            track_urls=[track["external_urls"]["spotify"] for track in results["tracks"]["items"]]
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
                    albumurl = item['external_urls']["spotify"]
                    albumArt = item['images'][0]['url']
                    # Extract track data
                    trackResults = self.get_song_info(albumurl)
                    for item in trackResults:
                        if Name in str(item["tracks_data"]["song_artists"]):
                            return_dict.append(item)
                print(offset)
                offset+=50
        elif characteristics[0] == 'playlist':
            offset=0
            results = self.spotify.playlist_tracks(characteristics[1])
            total=results["total"]
            return_dict=[]
            while offset<=total:
                results = self.spotify.playlist_tracks(characteristics[1], offset=offset)
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
                return_dict += [{"album_data":{"name":album, "album_artists":str(album_artists).strip("[]"), "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks": total_tracks},"track_data":{"name":name, "artists": artists, "track_number":track_number, "url":track_url, "explicit":explicit}} for album,album_artists, album_url, album_cover, album_release_date, total_tracks, name, artists, track_number, track_url, explicit in zip(albums, album_artistss, album_urls, album_covers, album_release_dates, total_trackss, names, artistss, track_numbers, track_urls, explicits)]
                offset+=100
        return return_dict

if __name__=="__main__":
    res = spotr('shcixv399pe9eirp62esm93').get_song_info("input url >>>>  ")
    print(json.dumps(res, indent=3))
    #print(len(res))
    for each in res:
        url = each["album_data"]["album_cover"]
        path = "./"
        name = each["track_data"]["name"]+ " - " +"\"" + str(each["track_data"]["artists"])
        print(url, path, name)
        if "/" in name:
            name = name.replace("/\\\\","Λ" )
        dl_jpg(url, path, name)
    print("done")