#pkg update
#pkg upgrade -y
#set storage permissions
echo "Please allow to provide access to internal storage"
termux-setup-storage
#get packages
echo "Installing needed packages for Termux ...."
pkg install -y ffmpeg python git micro
#make bin if not present
if [ ! -d "$HOME/bin" ]; then
	mkdir "$HOME/bin"
fi
# get gist, put it in termux url opener and set it as executable
curl 'https://raw.githubusercontent.com/raprocks/spotidnldr/master/gist' > "$HOME/bin/termux-url-opener.sh"
chmod +x termux-url-opener.sh
#make a directory to store songs into
if [ ! -d "/storage/emulated/0/Songs" ]; then
	mkdir "/storage/emulated/0/Songs"
fi

#get spotidnldr
echo "Getting Spotidnldr"
git clone https://github.com/raprocks/spotidnldr.git $HOME/spotidnldr
# traverse into directory
cd spotidnldr
#opening api key setup script to edit
micro env_setup.py

echo " You are good to go now just share your spotify link to termux from spotify and the song will be downloaded to the folder named Songs in Internal Memory"

exit 0