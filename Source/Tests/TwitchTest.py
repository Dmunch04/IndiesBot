import json
import urllib
import requests

def IsLive (_Channel, _ClientID = None):
    if _ClientID:
        #URL = f'https://api.twitch.tv/kraken/streams/{_Channel}?client_id={_ClientID}'
        #URL = f'https://api.twitch.tv/kraken/users?login={_Channel}'
        #URL = f'https://api.twitch.tv/kraken/streams?client_id={_ClientID}&channel={_Channel}'
        #URL = f'https://api.twitch.tv/{_Channel}/streams?client_id={_ClientID}&user_login={_Channel}'
        #URL = f'https://api.twitch.tv/helix/streams?user_id={_Channel}?client-id={_ClientID}'
        URL = f'https://api.twitch.tv/helix/users?login=niackz?client-id={_ClientID} '
        print (URL)

        HTML = requests.get (URL)
        Streaming = json.loads (HTML.content)

        return Streaming['stream'] is not None

    else:
        URL = f'https://api.twitch.tv/kraken/streams/{_Channel}'
        ID = -1

        print (URL)

        Response = urllib.request.urlopen (URL)
        HTML = Response.read ()
        Data = json.loads (HTML)

        ID = Data.get ('stream', -1)
        if ID is not -1:
            ID = ID.get ('_id', -1)

        return (int (ID))

def Test (_Channel, _ClientID):
    #URL = f'https://api.twitch.tv/helix/users?login={_Channel}'
    #URL = 'https://api.twitch.tv/helix/streams?first=20'
    URL = f'https://api.twitch.tv/kraken/streams/125080945'
    print (URL)

    Request = urllib.request.Request (URL)
    Request.add_header ('client-id', _ClientID)
    Response = urllib.request.urlopen (Request)
    Content = Response.read ()
    Data = json.loads (Content)

    print (Data)
    Object = Data['data'][0]
    print (Object)

    #return Data

# REMOVE THE IDS!!!!
#Result = IsLive ('Quitoooo', '1bkmon5ekz8p9umnhm7o7mgc037vgy')
Result = Test ('makeindies' ,'1bkmon5ekz8p9umnhm7o7mgc037vgy')
print (Result)
