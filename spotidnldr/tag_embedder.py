import eyed3

def tag_embed(file,title,artists,album,album_artists,release_date,track_number,total_tracks, img_path):
    audio_file = eyed3.load(str(file))
    audio_file.tag.title = title
    audio_file.tag.artist = artists.strip("[]").strip("\'\"")
    audio_file.tag.album = album 
    audio_file.tag.track_num = (track_number, total_tracks)
    audio_file.tag.album_artist = album_artists.strip("[]").strip("\'\"")
    audio_file.tag.release_date = release_date
    audio_file.tag.images.set(type_=3, img_data=open(img_path, 'rb').read(), mime_type="image/jpeg", description=u"album cover", img_url=None)
    audio_file.tag.save()
    #print(file, title ,artists, album, album_artists, release_date, track_number, total_tracks, img_path)