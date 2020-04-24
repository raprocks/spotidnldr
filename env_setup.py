import os

SPOTIPY_CLIENT_ID="<Your client id>"
SPOTIPY_CLIENT_SECRET="<your client secret>"
SPOTIFY_USER_ID="<your user id>"
SPOTIPY_REDIRECT_URI="https://google.com"
YOUTUBE_API_KEY="<your youtube api key>"

local_vars = locals()
env_vars = os.environ

need_list = ["SPOTIPY_CLIENT_ID","SPOTIPY_CLIENT_SECRET","SPOTIFY_USER_ID","SPOTIPY_REDIRECT_URI","YOUTUBE_API_KEY"]


for var in need_list:
    if os.environ[str(var)]:
        if os.environ[str(var)] == local_vars[var]:
            print(f"{var} is set to the one specified in file, Hence, no replacement will occur")
            print()
        elif os.environ[str(var)] != local_vars[var]:
            while True:
                inp = input(f"The value of {var} is set in the system but is different from the one specified in the file. Do you want to [r]eplace it with the one in the file or do you want to [c]ontinue with the one set in the system >>>  ").upper()
                print()
                if inp=="R":
                    os.environ[str(var)]=local_vars[var]
                    print(f"{var} set to the one in file")
                    print()
                    break
                elif inp=="C":
                    print(f"{var} is still the one set in the system")
                    print()
                    break
                else:
                    print("Wrong Input, Please try again")
                    print()
        else:
            pass
            print()
    else:
        print("Variable is not set by the system, Setting it to the value specified in the file env_setup.py")
        print()
        os.environ[str(var)]=local_vars[var]
        print("Done")
        print()