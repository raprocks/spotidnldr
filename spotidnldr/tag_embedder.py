import eyed3


def tag_embed(
        file_to_work,
        title,
        artists,
        album,
        album_artists,
        release_date,
        track_number,
        total_tracks,
        img_path):
    print('[*] adding meta data')
    print('[*] loading audio...', end='')
    audio_file = eyed3.load(str(file_to_work))
    print('Done')
    print('[*] adding title...', end='')
    audio_file.tag.title = title
    print('Done')
    print('[*] adding artist data...', end='')
    audio_file.tag.artist = artists.strip("[]").strip("\'\"")
    print('Done')
    print('[*] adding album data...', end='')
    audio_file.tag.album = album
    print('Done')
    print('[*] adding track number...', end='')
    audio_file.tag.track_num = (track_number, total_tracks)
    print('Done')
    print('[*] adding album artists...', end='')
    audio_file.tag.album_artist = album_artists.strip("[]").strip("\'\"")
    print('Done')
    print('[*] adding release date...', end='')
    audio_file.tag.release_date = release_date
    print('Done')
    print('[*] adding cover art...', end='')
    audio_file.tag.images.set(type_=3,
                              img_data=open(img_path, 'rb').read(),
                              mime_type="image/jpeg",
                              img_url=None)
    print('Done')
    print('[*] saving audio...', end='')
    audio_file.tag.save()
    print('Done')
    return file_to_work
