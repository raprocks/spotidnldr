import urllib.request
import os
from pathlib import Path

def dl_jpg(url, file_path, file_name):
    name = file_name
    #print(url, file_path, name)
    if "/" in name:
        file_name = name.replace("/","|")
    elif "\\" in name:
        file_name = name.replace("\\", "")
    else:
        pass
        
    full_path = Path(os.path.join(file_path,str(file_name + '.jpg')))
    urllib.request.urlretrieve(url, full_path)
    return full_path

if __name__=="__main__":
    url = input('Enter image URL to download: ')
    file_name = input('Enter file name to save as: ')
    if "images" not in os.listdir():
        os.mkdir(Path("images"))
    dl_jpg(url, file_path=Path("images"), file_name=file_name)
