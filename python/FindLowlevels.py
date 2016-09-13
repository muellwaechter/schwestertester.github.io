import requests


payload = {
}

headers = {
'Accept': 'application/json,text/plain, */*',
'Accept-encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.8',
'Connection': 'keep-alive',
'Host': 'www.younow.com',
'Referer': 'https://www.younow.com/explore/',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36',
}

def get_users(start):
    url = "https://www.younow.com/php/api/younow/trendingUsers/locale=ww/numberOfRecords=50/startFrom=%s" % start
    response = requests.get(url, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json()['trending_users']
    return data

def streams_total():
    url = "https://www.younow.com/php/api/younow/trendingUsers/locale=ww/numberOfRecords=50/startFrom=1000000"
    response = requests.get(url, data=payload, headers=headers)
    response.raise_for_status()
    data = response.json()['total']
    return data

g = streams_total()
print "Streamers online:", g


for counter in range(0,g+40,50):
    f = get_users(counter)
    for i in f:
        level = float(i['userlevel'])
        if level <= float(3):
            print "https://www.younow.com/" + i['profile']




#picture "https://ynassets.younow.com/broadcastdynamic/live/"broadcastID"/"broadcastID".jpg"



#u'{"errorCode":0,"trending_users":
#
#   {"userId":"29914243","viewers":"2","likes":"0","tags":["singing"],"broadcastId":"124766904","username":"seannbradley_73419","userlevel":"3.0417"
#    ,"profile":"seannbradley_73419","locale":"en","shares":"0","fans":"1","totalFans":4,"position":0,"views":3},
#m
#    {"userId":"29842513","viewers":"2","likes":"0","tags":["musical.ly"],"broadcastId":"124766186","username":"LilyThomson_12983","userlevel":"3.1339","profile":"LilyThomson_12983","locale":"en","shares":"0","fans":"1","totalFans":6,"position":0,"views":23}
#]
#,"total":793}'
