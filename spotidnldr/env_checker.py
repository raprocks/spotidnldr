import os

env_list = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIFY_USER_ID", "SPOTIPY_REDIRECT_URI", "YOUTUBE_API_KEY"]

current_envs= os.environ
local_vars = locals()

def check_for_env_vars():
    for var in env_list:
        if var in current_envs:
            print(f"{var} is set in environment")
            local_vars[var]=current_envs[var]
            print(local_vars[var])
        elif var in local_vars:
            print(f"{var} is set in env_vars.py")
        else:
            print(f"{var} is not set")