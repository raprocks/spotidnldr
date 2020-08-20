from ytmusicapi import YTMusic


def youtube_search(q,return_indices, filters="songs"):
    res = YTMusic().search(query=q,filter=filters)
    x = ["https://youtube.com/"+video["videoId"] for video in res]
    #print(x[:return_indices])
    return x[:return_indices]

if __name__=="__main__":
    print("this is not the main program use spoti --help")
