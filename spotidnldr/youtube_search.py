from ytmusicapi import YTMusic


def youtube_search(q, return_indices, filters="songs", recurse_count=0):
    if recurse_count == 1:
        try:
            q = q[:q.rindex('-')]
        except:
            pass
    elif recurse_count == 2:
        try:
            q = q[:q.rindex('(')]
        except:
            pass

    res = YTMusic().search(query=q, filter=filters)
    if filters == 'songs':
        x = ["https://music.youtube.com/watch?v="+video["videoId"] for video in res]
    elif filters == 'videos':
        x = ["https://youtu.be/" + video["videoId"] for video in res]
    titles = [each['title'] for each in res]
    passed = False
    count = 0
    total = len(titles[0])
    for each in q.replace(' ', ''):
        if each in titles[0]:
            count += 1
        elif each not in titles[0]:
            count += 0

    if (count/total)>0.8:
        passed = True
    else:
        passed = False
    if passed:
        return x[:return_indices]

    elif not passed:
        filters = 'videos'
        x = youtube_search(q, return_indices=return_indices, filters=filters, recurse_count=recurse_count+1)
    return x[:return_indices]
# https://youtu.be/o1RducJbUdc
# https://music.youtube.com/watch?v=8_Cw99SiHvc&feature=share
if __name__ == "__main__":
    print("this is not the main program use spoti --help")
