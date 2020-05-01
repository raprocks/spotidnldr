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


You will probably need the root user permissions if you are on a linux system or Mac. Just add **sudo** at the begining of the command and it should work without any issues.

Next, You need to set some Environment Variables on your system because you don't want to type gibberish in everytime you run the program.

**But**, This gibberish helps you contact the Spotify and Youtube API to get data about the Songs you want to Download, like the Meta-Data of the Song.

#### Getting the API keys
###### Spotify API keys:-
1. Go to [Spotify Developers Dashboard](https://developer.spotify.com/dashboard/)
2. Log In using your Spotify Account
3. Click on **CREATE A CLIENT ID**
4. Fill in The Information it asks for and check **I Don't Know** under *What Are You Building*.
5. Now you will see a client ID just copy it and save it somewhere for now.
6. Also, there is a *Show Client Secret* option just click on it and it will give you another AlphaNumeric key save this one too.
7. Now Click on the edit settings button and scroll down to see **Redirect URI's** section. Just add ```"https://google.com/"``` without the quotes in the textbox below it and click on add. Scroll further below and click on save.
8. Done!!
###### Getting Youtube API keys:-
1. Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard). If you are on your phone please enable the Desktop Mode it will help you a Lot.
2. Make a new project and Name it anything you want.
3. Click on *Enable API's and Services*.
4. Find and click on **Youtube Data API v3** and Enable it.
5. On the left side click on *Credentials*.
6. On Top of the page Click on *Create Credentials* and then on *API key*.
7. You will get another AlphaNumeric key, save this too. 

#### Setting the Environment Variables or The API keys for the program
###### Using the python script.**(RECCOMENDED)**
1. There is already a python script named env_setup.py in the files. Just open it using any file editor of your choice and paste the keys you obtained earlier in the specific place and you are good to go.
2. All the file does is set the variable at each start of the program.

##### **For Linux and MacOs Users** Using .bashrc
The .bashrc is a shell script that is run everytime bash is started. It has certain commands written in it by the user or by the system itself that are necessary for the startup or for the requirements of the user.
* It is placed in the HOME directory of the system. 
* If there is no such file it is totally okay for you to make one. Just dont write any unknown commands in it.
* Keep in mind that it is executed when bash starts so if you write some commands now and dont restart it, you won't see any effects.
* To see the effects eithout restarting the terminal do

```bash
source .bashrc
```

* This will run the .bashrc file and you will see the effects right there on the terminal.
###### What is its use to us for this program and how can we use it to set environment variables
To set a certain environment variable we use the export command
```bash
export <environment_var_name>="value_for_var"
```
Obviously dont put the "<" & ">".
And put the value in single or double quotes as the value should always be string.
  * For our program we need some variable namely:-
      * SPOTIPY_CLIENT_ID
      * SPOTIPY_CLIENT_SECRET
      * SPOTIPY_REDIRECT_URI
      * SPOTIFY_USER_ID
      * YOUTUBE_API_KEY
  * Now to set the values of them we use the above command one by one on these variables as follows:-
```bash
export SPOTIPY_CLIENT_ID="<your client id that you first copied>"
export SPOTIPY_CLIENT_SECRET="<your client secret that you second copied>"
export SPOTIPY_REDIRECT_URI="https://google.com"
export SPOTIFY_USER_ID="your spotify user id>"
export YOUTUBE_API_KEY="<the api key you obtained from google api dashboard>"
```
you just have to copy and paste these commands in your .bashrc file replacing the placeholders denoted by **< & >**.

You can get your Spotify User Id by visiting this [link](https://www.spotify.com/in/account/overview/). 
   * Note: Here Spotify User Id means your username.

#### **For Windows Users** please follow the guide [Here](https://www.computerhope.com/issues/ch000549.htm).
You can also set the variables using the ```set or setx(more permanent)``` commands.
The syntax is ```set <variable_name>="value_as_string"```. (This does it for a session.)
Or if you want to permanently set the variables then do ```setx -m <variable_name>="value_as_string"```.
Obviously the guide above gives you a gui but its quite fun typing commands in cmd and flex on your newly learn commands😆.

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
* Just run the python script ```spot.py``` by doing
```bash
python spot.py
```
 In the working directory
* Then paste the link of spotify Song, Playlist, Album or Artist.(Nicely rhymes)

# Credits
* ME(obviously) - did everything on my phone.Not kidding.its Hard.
* All the respective devs of pypi packages
* Termux.

### To Do List
- [x] Make this into a cli application using Click.
- [ ] try to complete your suggestions and squash the bugs.
- [ ] make a interface
Leave a Star if you think i deserve it 😉. Also Checkout [F8L](https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz?si=O6FR6i9UT1WMpG7bYEBMpg) on spotify.
# Thanks
###### ~ Rohit.
