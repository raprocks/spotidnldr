# Spotidnldr
### What is it?
A terminal based application written in Python-3, which helps you download songs in MP3 format, with meta-data like artist information and album-arts just like on Spotify.
### Installation
### For Termux on Android
I made this whole thing in Termux only. So i should give back to it. 
So to install in termux just copy below command and paste it but first read the getting the api keys section and obviously get the api keys.
```bash
curl https://raw.githubusercontent.com/raprocks/spotidnldr/master/termux_setup.sh >> "term.sh" && bash term.sh
```
You are good to go now.
#### Getting the Files
Just clone the git repo using 
```
git clone https://github.com/raprocks/spotidnldr.git spotidnldr
```

Then change your working directory to the newly made folder named spotidnldr
```
cd ./spotidnldr/spotidnldr
```
Now check that there is a file named env_setup.py, open it in any file editor you want and paste the key you obtain by Following [these steps](https://github.com/raprocks/spotidnldr/blob/master/README.md#getting-youtube-api-keys-) in the placeholder for youtube api key.

Then assuming you have python3 and pip installed and in you Environment Path, Run the Following Command:
```
pip install .
```

* This installs the required packages from Pypi repo.
  * spotipy - The python wrapper for Spotify's Web API.
  * requests - The HTTP library used to get data from Youtube.
  * youtube-dl - The awesome masterpiece to get audio files.
  * ffmpeg-python - The ffmpeg wrapper for python
  * eyeD3 - The Meta-Data Writer
  * Click - The module which converts the package to a CLI app.


You will probably need the root user permissions if you are on a linux system or Mac. Just add **sudo** at the begining of the command and it should work without any issues.

Next, You need to set some Environment Variables on your system because you don't want to type gibberish in everytime you run the program.

**But**, This gibberish helps you contact the Youtube API to get data about the Songs you want to Download.

#### Getting the API key:-
###### Getting Youtube API keys:-
1. Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard). If you are on your phone please enable the Desktop Mode it will help you a Lot.
2. Make a new project and Name it anything you want.
3. Click on *Enable API's and Services*.
4. Find and click on **Youtube Data API v3** and Enable it.
5. On the left side click on *Credentials*.
6. On Top of the page Click on *Create Credentials* and then on *API key*.
7. You will get another AlphaNumeric key, save this. 

#### Setting the Environment Variables or The API keys for the program:-
###### **Using the python script**
1. There is already a python script named env_setup.py in the files. Just open it using any file editor of your choice and paste the keys you obtained earlier in the specific place and you are good to go.
2. All the file does is set the variable at each start of the program.

### now all you need after this is FFMPEG.
##### For Windows.
1. Get FFMPEG from [here](https://www.ffmpeg.org/download.html)
2. Make a new folder named ffmpeg somewhere and install or extract the downloaded zip to it.
3. Add FFMPEG to system path by following this guide [here](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho).
4. Now you have enables access of FFMPEG from python. 
##### For Linux.
1. Follow this guide [here](https://www.tecmint.com/install-ffmpeg-in-linux). 
2. Done.✌️👌

### Usage
* Just run the program by doing.
```bash
spoti
```
Anywhere!
* Then paste the link of spotify Song, Playlist, Album or Artist.(Nicely rhymes)
* Access help for program by doing ``` spoti --help ```.

# Credits
* ME(obviously) - did everything on my phone.Not kidding.its Hard.
* All the respective devs of pypi packages. All Gawds 🙏🙏.
* @SwapnilSoni1999 
* Termux.

### To Do List
- [x] Make this into a cli application using Click.
- [ ] try to complete your suggestions and squash the bugs.
- [ ] make a interface.
Leave a Star if you think i deserve it 😉. Also Checkout [F8L](https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz?si=O6FR6i9UT1WMpG7bYEBMpg) on spotify.
# Thanks
###### ~ Rohit.
