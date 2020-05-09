from __future__ import unicode_literals
import youtube_dl

class YDL():
    _opts = {'format':'bestaudio', 'forcefilename':True, "quiet":True}
    def __init__(self, opts=_opts):
        self.ydl=youtube_dl.YoutubeDL(opts)
    def downloader(self,youtube_url):
        self.ydl.download(youtube_url)

#YDL(opts=opts).downloader(["https://youtu.be/FM7MFYoylVs"])

def download_yout(url, file_name):
    opts = {'format':'251', 'outtmpl':f"{file_name}.%(ext)s", "quiet":True}
    YDL(opts=opts).downloader(url)
    return f"{file_name}.webm"


if __name__=="__main__":
    download(["PT2_F-1esPk"], "hens")