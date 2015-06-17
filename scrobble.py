import urllib.request
import urllib.parse
import json

my_api_key = "829b12779f358d0af117bef698aaa7e2"

url = "http://ws.audioscrobbler.com/2.0/?"

params = urllib.parse.urlencode(
    {'method': 'user.getRecentTracks', 'user': 'nickedes', 'format': 'json', 'page': 1,
     'api_key': my_api_key})

site = urllib.request.urlopen(url+params)

str_response = site.readall().decode('utf-8')
obj = json.loads(str_response)
print({1:obj})
totalPages = obj['recenttracks']['@attr']['totalPages']

all_data = {}
all_data[1] = obj
for page in range(2, int(totalPages)):
    params = urllib.parse.urlencode(
        {'method': 'user.getRecentTracks', 'user': 'nickedes', 'format': 'json', 'page': page,
         'api_key': my_api_key})
    site = urllib.request.urlopen(url+params)
    str_response = site.readall().decode('utf-8')
    all_data[page] = json.loads(str_response)
    print({page: all_data[page]})
