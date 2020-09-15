pkg update
pkg upgrade -y
#set storage permissions
echo "Please allow to provide access to internal storage"
termux-setup-storage
#get packages
echo "Installing needed packages for Termux ...."
pkg install -y ffmpeg python git
pkg update && pkg upgrade
if [ -d "$HOME/spotidnldr" ]; then
	rm -rf $HOME/spotidnldr
fi
#make bin if not present
#if [ ! -d "$HOME/bin" ]; then
#	mkdir "$HOME/bin"
#fi

#touch $HOME/bin/termux-url-opener
# get gist, put it in termux url opener and set it as executable
#curl 'https://raw.githubusercontent.com/raprocks/spotidnldr/master/gist' > "$HOME/bin/termux-url-opener"

#chmod +x $HOME/bin/termux-url-opener
#make a directory to store songs into
if [ ! -d "/storage/emulated/0/Songs" ]; then
    echo "Making Songs Directory in Internal Memory where songs will be saved"
	mkdir "/storage/emulated/0/Songs"
fi

#get spotidnldr
echo "Getting Spotidnldr"
pip install --upgrade spotidnldr
# git clone https://github.com/raprocks/spotidnldr.git $HOME/spotidnldr

# traverse into directory
# cd $HOME/spotidnldr

# pip install .

echo "Setting environment variables and adding to bashrc/zshrc"
echo 'export SPOTIFY_DOWNLOAD_PATH="/storage/emulated/0/Songs/"' >> $HOME/.bashrc
echo 'export SPOTIFY_DOWNLOAD_PATH="/storage/emulated/0/Songs/"' >> $HOME/.zshrc

echo "the Songs will be downloaded to the folder named Songs in Internal Memory  ```spoti --help```"

exit 0
