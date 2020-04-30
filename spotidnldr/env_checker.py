import os

env_list = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIFY_USER_ID", "SPOTIPY_REDIRECT_URI", "YOUTUBE_API_KEY"]

def check_for_env_vars(a, env):
    local_vars=a
    current_envs=env
    for var in env_list:
        if var in current_envs:
            print(f"{var} is set in environment.Replacing.")
            locals()[var]=current_envs[var]
            local_vars=locals()
            print(local_vars[var])
        elif var in local_vars:
            print(f"{var} is set in env_vars.py")
        else:
            print(f"{var} is not set")