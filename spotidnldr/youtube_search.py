from ytmusicapi import YTMusic
import sys


def youtube_search(q):
    print(f"[*] searching {q}")
    print(q)
    client = YTMusic()
    res = client.search(query=str(q), filter="songs")
    try:
        music_id = res[0]["videoId"]
    except KeyError or IndexError as err:
        music_id = ""
        print("couldnt get results, exiting", err)
        sys.exit()

    music_url = f"https://music.youtube.com/watch?v={music_id}"
    return music_url


# https://youtu.be/o1RducJbUdc
# https://music.youtube.com/watch?v=8_Cw99SiHvc
if __name__ == "__main__":
    print("this is not the main program use spoti --help")
