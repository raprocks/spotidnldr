from ytm import YouTubeMusic


def youtube_search(q):
    print(f'[*] searching {q}')
    client = YouTubeMusic()
    res = client.search(q)
    music_id = res['songs'][0]['id']
    music_url = f"https://music.youtube.com/watch?v={music_id}"
    return music_url


# https://youtu.be/o1RducJbUdc
# https://music.youtube.com/watch?v=8_Cw99SiHvc
if __name__ == "__main__":
    print("this is not the main program use spoti --help")
