import eyed3
from eyed3.id3 import Tag
from eyed3.id3.tag import ImagesAccessor


def tag_embed(
    file_to_work,
    title,
    artists,
    album,
    album_artists,
    release_date,
    track_number,
    total_tracks,
    img_path,
):
    print("[*] adding meta data")
    print("[*] loading audio...", end="")
    audio_file = eyed3.load(str(file_to_work))
    if not isinstance(audio_file.tag, Tag):
        print("Tag not found, creating it.")
        return None
    print("Done")
    print("[*] adding title...", end="")
    audio_file.tag.title = title
    print("Done")
    print("[*] adding artist data...", end="")
    audio_file.tag.artist = artists.strip("[]").strip("'\"")
    print("Done")
    print("[*] adding album data...", end="")
    audio_file.tag.album = album
    print("Done")
    print("[*] adding track number...", end="")
    audio_file.tag.track_num = (track_number, total_tracks)
    print("Done")
    print("[*] adding album artists...", end="")
    audio_file.tag.album_artist = album_artists.strip("[]").strip("'\"")
    print("Done")
    print("[*] adding release date...", end="")
    audio_file.tag.release_date = release_date
    print("Done")
    print("[*] adding cover art...", end="")
    if not isinstance(audio_file.tag.images, ImagesAccessor):
        raise Exception("Not supported.")
    audio_file.tag.images.set(
        type_=3,
        img_data=open(img_path, "rb").read(),
        description="thumbnail",
        mime_type="image/jpeg",
        img_url=None,
    )
    print("Done")
    print("[*] saving audio...", end="")
    audio_file.tag.save(version=(1, None, None))
    audio_file.tag.save(version=(2, 3, 0))
    audio_file.tag.save()
    print("Done")
    return file_to_work
