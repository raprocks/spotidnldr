import spotipy
import spotipy.util as util

def get_token(username):
    try:
        local_token = util.prompt_for_user_token(username)
    except:
        print("Something seems wrong :( \n Have you set up all of the Enviornment Variables and given your username as input?")
# https://open.spotify.com/user/shcixv399pe9e6dirp62esm93?si=OWXuEM81QdG_jJ91cgYCxg
def get_username_from_url(url):
    url = str(url)
    url = url.split('/')
    username = url[-1]
    if '?' in username:
        username = username.split('?')[0]
    else:
        pass
    print(username)
    return str(username)

