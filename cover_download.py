import urllib.request

def dl_jpg(url, file_path, file_name):
    name = file_name
    print(url, path, name)
    if "/" in name:
        file_name = name.replace("/\\\\","Λ" )
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)


if __name__=="__main__":
    url = input('Enter image URL to download: ')
    file_name = input('Enter file name to save as: ')
    dl_jpg(url, 'images/', file_name)
