![spotidnldr - The Spotify Song Downloader](https://github.com/raprocks/spotidnldr/blob/master/cover.jpg)
# Spotidnldr
### What is it?
A terminal based application written in Python3, which helps you download songs in MP3 format, with meta-data like artist information and album-arts just like on Spotify.
### Installation
### For Termux on Android
I made this whole thing in termux only, So I should give back to it. 
So to install in termux just copy below command, paste it and press enter.
```bash
curl https://raw.githubusercontent.com/raprocks/spotidnldr/master/termux_setup.sh >> "term.sh" && bash term.sh
```
You are good to go now.
#### Getting the Files
* For Linux
  * Just clone the git repo using 
    * ```bash
      git clone https://github.com/raprocks/spotidnldr.git spotidnldr
      ```

  * Then change your working directory to the newly made folder named spotidnldr 
    * ```bash
      cd ./spotidnldr
      ```
  * When you are in ```./spotidnldr``` folder and assuming you have python3 and pip installed and in you Environment Path, Run the Following Command:
      * ```bash
         pip install .
        ```
* for windows
	* just download the zip of the repo and unzip it.
	* just double click on ```setup.py```
	* Done!
###### This installs the required packages from Pypi repo.
  * spotipy - The python wrapper for Spotify's Web API.
  * requests - The HTTP library used to get data from Youtube.
  * youtube-dl - The awesome masterpiece to get audio files.
  * ffmpeg-python - The ffmpeg wrapper for python
  * eyeD3 - The Meta-Data Writer
  * Click - The module which converts the package to a CLI app.
  * ytmusicapi - the module which retrives youtube links of songs.

You will probably need the root user permissions if you are on a linux system or Mac. Just add **sudo** at the begining of the command and it should work without any issues.

### now all you need after this is FFMPEG.
##### For Windows.
1. Get FFMPEG from [here](https://www.ffmpeg.org/download.html)
2. Make a new folder named ffmpeg somewhere and install or extract the downloaded zip to it.
3. Add FFMPEG to system path by following this guide [here](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho).
4. Now you have enables access of FFMPEG from python. 
##### For Linux.
1. Follow this guide [here](https://www.tecmint.com/install-ffmpeg-in-linux). 
2. Done.

### Usage
* Just run the program by doing.
```bash
spoti
```
Anywhere!
* Then paste the link of spotify Song, Playlist, Album or Artist.(Nicely rhymes)
* Access help for program by doing ``` spoti --help ```.

# Credits
* ME(obviously) - did everything on my phone. Not kidding, it's Hard.
* All the respective devs of pypi packages. All Gawds.
* @SwapnilSoni1999 sir for making me do this(?).
* @AyamDobhal sir for fixing readme.
* @Sharvil234 sir for hard testing.
* Termux.

### To Do List
- [x] Make this into a cli application using Click.
- [ ] try to complete your suggestions and squash the bugs.
- [ ] make a interface.
* Leave a Star if you think I deserve it. Also Checkout [F8L](https://open.spotify.com/artist/6LkOho0r5aIaYkMtjWYDAz?si=O6FR6i9UT1WMpG7bYEBMpg) on spotify.
# Thanks
###### > ~ Rohit.
