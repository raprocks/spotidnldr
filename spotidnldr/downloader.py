import os
import pathlib
from pytube import YouTube
from spotidnldr.progress_bar import download_progress_bar


class YDL:
    def __init__(self, vid_link):
        self.ydl = YouTube(vid_link)
        self.ydl.register_on_progress_callback(download_progress_bar)
        self.best_audio = (
            self.ydl.streams.filter(only_audio=True).order_by("abr").last()
        )

    def downloader(self, filename):
        outfile = self.best_audio.download(
            output_path=pathlib.Path("./.temp"), filename=filename
        )
        return outfile


if __name__ == "__main__":
    pass
