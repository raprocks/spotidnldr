import spotipy
import spotipy.util as util
import json
from cover_download import dl_jpg
from youtube_search import youtube
import os
from tag_embedder import tag_embed
import downloader
from converter import convert_to_mp3
from env_setup import *
from env_checker import *

check_for_env_vars()
class spotr:
    def __init__(self, userid=SPOTIFY_USER_ID):
        print("hello there, ", SPOTIFY_USER_ID)
        try:
            local_token = util.prompt_for_user_token(username=userid)
            self.spotify = spotipy.Spotify(auth=local_token)
        except UnboundLocalError as err:
            print("Something seems wrong :( \n Have you set up all of the Enviornment Variables and given your username as input?")
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
            return_dict=[]
            i=1
            for song_name,artists,explicit,track_url in zip(song_names,artistss,explicits,track_urls):
                return_dict.append({"album_data":{"name":album, "album_artists":str(album_artists).strip("[]"), "url":album_url, "album_cover": album_cover, "album_release_date":album_release_date, "total_tracks":total_tracks},"track_data":{"name":song_name,"artists":artists,"track_number":i,"url":track_url, "explicit":explicit}})
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
                        if Name in str(item["track_data"]["artists"]):
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
    res = spotr().get_song_info(input("input url to dnld🙏🙏 >>> "))
    #print(json.dumps(res, indent=3))
    #print(len(res))
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
        infile = downloader.download(url=retrived_from_youtube[0], file_name=name)
        convert_to_mp3(infile, f"./{name}.mp3")
        tag_embed(f"{name}.mp3", title=title, artists=song_artists, album=album_name, album_artists=album_artists, release_date=release_date, track_number=track_number, total_tracks=total_tracks, img_path=img_name)
        os.remove(img_name)
        os.remove(infile)
    print("done")