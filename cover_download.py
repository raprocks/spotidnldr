import urllib.request
import os
from pathlib import Path

def dl_jpg(url, file_path, file_name):
    name = file_name
    print(url, file_path, name)
    while True:
        if "/" in name:
            file_name = name.replace("/","|")
        elif "\\" in name:
        
    full_path = Path(file_path + file_name + '.jpg')
    print(full_path)
    urllib.request.urlretrieve(url, full_path)


if __name__=="__main__":
    url = input('Enter image URL to download: ')
    file_name = input('Enter file name to save as: ')
    if "images" not in os.listdir():
        os.mkdir("./images")
    dl_jpg(url, file_path='./images/', file_name=file_name)
