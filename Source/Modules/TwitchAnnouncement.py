import discord

import json
import asyncio

from Helpers import EmbedHelper as Embed

class TwitchAnnouncement:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Message = str (self.Data['Messages']['TwitchAnnouncement'])
            self.Channel = str (self.Data['AnnouncementsChannel'])
            self.StreamSleep = int (self.Data['StreamSleep'])

            self.TwitchID = self.Data['TwitchID']
            self.TwitchChannel = self.Data['MakeIndiesTwitchID']
            self.TwitchLink = self.Data['Socials']['Twitch']
            self.URL = f'https://api.twitch.tv/kraken/streams/{self.TwitchChannel}'

        self.CurrentStreamID = None
        self.CurrentStreamName = ''

        self.Client.loop.create_task (self.WatchStream ())

    # There'll be a delay from when you start the stream, to the bot sees it and sends
    # an announcement about it. This delay is max 30 seconds
    async def WatchStream (self):
        await self.Client.wait_until_ready ()

        while not self.Client.is_closed ():
            # Check if the channel is streaming
            IsLive = self.CheckStream ()

            if IsLive and not self.CurrentStreamID:
                await SendAnnouncement (self, self.TwitchLink, self.CurrentStreamName)

            await asyncio.sleep (self.StreamSleep)

    async def CheckStream (self):
        Request = urllib.request.Request (self.URL)
        Request.add_header ('client-id', self.TwitchID)
        Response = urllib.request.urlopen (Request)
        Content = Response.read ()
        Data = json.loads (Content)

        IsLive = Data['stream']

        if IsLive:
            self.CurrentStreamID = IsLive['_id']
            # -- This is the game the stream is playing --
            #self.CurrentStreamName = IsLive['game']
            # -- This is the stream's title --
            self.CurrentStreamName = IsLive['channel']['status']

            return True

        CurrentStreamID = None

        return False

    async def SendAnnouncement (self, _Topic, _URL):
        Message = self.Message.format (
            # This might not work
            '@everyone',
            # But these to should work
            str (_Topic),
            str (_URL)
        )

        Channel = discord.utils.get (self.Client.get_all_channels (), server__name = 'Make Indies', name = self.Channel)

        Embed.Embed (_Client, 'Make Indies - Stream', Message, discord.Color.blue (), _Channel)

def setup (_Client):
    _Client.add_cog (TwitchAnnouncement (_Client))
