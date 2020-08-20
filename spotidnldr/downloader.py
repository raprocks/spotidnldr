from __future__ import unicode_literals
from pytube import YouTube
import os

class YDL():
    def __init__(self, vid_link):
        self.ydl = YouTube(vid_link)
        self.best_audio = (self.ydl
                           .streams
                           .filter(only_audio=True)
                           .order_by("abr")
                           .last()
                           )
    def downloader(self, filename):
        outfile = self.best_audio.download(output_path='./.temp', filename=filename)
        return outfile

if __name__=="__main__":
    pass
