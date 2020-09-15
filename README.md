![spotidnldr - The Spotify Song Downloader](https://github.com/raprocks/spotidnldr/blob/master/cover.jpg)
# Spotidnldr
### What is it?
A terminal based application written in Python3, which helps you download songs in MP3 format, with meta-data like artist information and album-arts just like on Spotify.

### Installation

#### Requirements
* Python3.6 or above
* ffmpeg (in PATH)

#### Installing Using pip

To install the latest **Release** just do
```sh
pip install spotidnldr
```

#### Installing from source repo
1. Clone the repo first (using git clone or downloading and extracting the zip)
```sh
git clone https://github.com/raprocks/spotidnldr
```
OR
download zip
```sh
wget https://github.com/raprocks/spotidnldr/archive/master.zip
```
unzip it
```sh
unzip master.zip
```

2. Change Working directory to the project root and do
```sh
pip install .
```
###### This installs the required packages from Pypi repo.
  * spotipy - The python wrapper for Spotify's Web API.
  * requests - The HTTP library used to get data from Youtube.
  * youtube-dl - The awesome masterpiece to get audio files.
  * ffmpeg-python - The ffmpeg wrapper for python
  * eyeD3 - The Meta-Data Writer
  * Click - The module which converts the package to a CLI app.
  * ytmusicapi - the module which retrives youtube links of songs.

      You will probably need the root user permissions if you are on a linux system or Mac. Just add **sudo** at the begining of the command and it should work without any issues.


3. Done.

#### Installing in Termux
```bash                                                                 curl https://raw.githubusercontent.com/raprocks/spotidnldr/master/termux_setup.sh >> "termux_setup.sh" && sh termux_setup.sh
```
This script above will setup spotidnldr for your device on termux, making the songs folder, setting up the environment and setting up permissions.

### Installing FFMPEG.
##### For Windows.
1. Get FFMPEG from [here](https://www.ffmpeg.org/download.html)
2. Make a new folder named ffmpeg somewhere and install or extract the downloaded zip to it.
3. Add FFMPEG to system path by following this guide [here](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho).
4. Now you have enables access of FFMPEG from python.
##### For Linux.
1. Follow this guide [here](https://www.tecmint.com/install-ffmpeg-in-linux).
2. Done.

### Usage
#### Environment Variables
* SPOTIFY_DOWNLOAD_PATH
  This default Path for download. This is where all songs will be saved  if you do not provide a value to the -o flag. If not set the songs will be downloaded in the Current Folder('./').

* Just run the program by doing.
    ```sh
    spoti download [url]
    ```
    Anywhere!
* Access help for program by doing `spoti download --help`.
* Usage: spoti download [OPTIONS] URL

  Downloads Songs from URL.

  URL must be a valid spotify link of a song, album or a playlist.

Options:
  -v, --verbose      flag for verbosity, usage of this flag gives more
                     output use this for sending or finding errors.

  -o, --output PATH  provide a output path for the song explicitly.
                     [default: ./]

  --version          Show the version and exit.
  --help             Show this message and exit.

# Credits
* ME(obviously) - did everything on my phone. Not kidding, it's Hard.
* All the respective devs of pypi packages. All Gawds.
* [Swapnil Soni](@SwapnilSoni1999) sir for making me do this(?).
* @AyamDobhal sir for fixing readme.
* @Sharvil234 sir for hard testing.
* Termux.

### To Do List
- [x] Make this into a cli application using Click.
- [ ] try to complete your suggestions and squash the bugs.
- [ ] make a web interface.
* Leave a Star if you think I deserve it. Also Checkout [F8L](https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz?si=O6FR6i9UT1WMpG7bYEBMpg) on spotify.
# Thanks
###### > ~ Rohit.
