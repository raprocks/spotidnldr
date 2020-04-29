import requests
import os
import json

class youtube:
    def __init__(self):
        self.api_key = os.environ['YOUTUBE_API_KEY']
        self.base = "https://www.googleapis.com/youtube/v3"#https://www.googleapis.com/youtube/v3/search?part=snippet&q=Retrovision-tommorowland%202019&prettyPrint=true&key=
    def _url(self, endpoint):
        return self.base + "/" + str(endpoint)
    def search(self, query, order, limit, return_indices):
        self.parameters={"part":"snippet", "q":str(query),"order":str(order),"maxResults":int(limit),"type":"video","videoCategoryId":"10", "key":self.api_key}
        request_url = str(self._url("search"))
        self.obje = requests.get(request_url, params=self.parameters)
        print(self.obje)
        self.search_results=self.obje.json()["items"]
        _res = []
        for x in self.search_results:
            _res.append(x["id"]["videoId"])
        print(_res[:return_indices])
        return [_res[:return_indices]]


if __name__=="__main__":
    resp = youtube().search(query="Home (feat. Bonn) - Martin Garrix, Bonn", order="relevance", limit=10)
    print(resp)