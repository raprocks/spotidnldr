# Spotidnldr
### What is it?
A terminal based application written in Python-3, which helps you download songs in MP3 format, with meta-data like artist information and album-arts just like on Spotify.
### Installation
##### Getting the Files
Just clone the git repo using 
```
git clone github.com/raprocks/spotidnldr spotidnldr
```

Then change your working directory to the newly made folder named spotidnldr
```
cd ./spotidnldr
```

Then assuming you have python3 and pip installed and in you Environment Path, Run the Following Command:
```
pip install -r requirements.txt
```

* This installs the required packages from Pypi repo.
  * spotipy - The python wrapper for Spotify's Web API.
  * requests - The HTTP library used to get data from Youtube.
  * youtube-dl - The awesome masterpiece to get audio files.
  * ffmpeg-python - The ffmpeg wrapper for python
  * eyeD3 - The Meta-Data Writer


You will probably need the sudo permissions if you are on a linux system or Mac. Just add **sudo** at the begining of the command and it should work without any issues.

Next, You need to set some Environment Variables on your system because you don't want to type gibberish in everytime you run the program.

**But**, This gibberish helps you contact the Spotify and Youtube API to get data about the Songs you want to Download, like the Meta-Data of the Song.

##### Getting the API keys
###### Spotify API keys:-
1. Go to [Spotify Developers Dashboard](https://developer.spotify.com/dashboard/)
2. Log In using your Spotify Account
3. Click on **CREATE A CLIENT ID**
4. Fill in The Information it asks for and check **I Don't Know** under *What Are You Building*.
5. Now you will see a client ID just copy it and save it somewhere for now.
6. Also, there is a *Show Client Secret* option just click on it and it will give you another AlphaNumeric key save this one too.
7. Done!!
###### Getting Youtube API keys:-
1. Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard). If you are on your phone please enable the Desktop Mode it will help you a Lot.
2. Make a new project and Name it anything you want.
3. Click on *Enable API's and Services*.
4. Find and click on **Youtube Data API v3** and Enable it.
5. On the left side click on *Credentials*.
6. On Top of the page Click on *Create Credentials* and then on *API key*.
7. You will get another AlphaNumeric key, save this too. 
##### Setting the Environment Variables
###### Using the python script. 
1. As we already have the working directory set to spotidnldr, Just type in the following lines on the terminal.
``` 
python env_setup.py
```
2. Follow the instructions on the screen and you will have set the environment variable by the End of the Program :smile:.
