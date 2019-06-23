# Discord Imports
from discord.ext import commands

import json

# Module Imports
from Modules import FileHandler as Filing
from Modules import RoleCheck as Role
from Modules import Logger as Log
from Helpers import EmbedHelper as Embed

class Events:
    def __init__ (self, Client):
        self.Client = Client

    async def on_message (self, _Message):
        Server = _Message.server
        Channel = _Message.channel
        Sender = _Message.author

        if Sender.bot:
            return

    async def on_member_join (self, _Member):
        Role = discord.utils.get (_Member.server.roles, name = 'Indie')

        await self.Client.add_roles (_Member, Role)

        with open ('Config.json', 'r') as Config:
            Data = json.loads (Config.read ())

        Data['Users'] = str (int (Data['Users']) + 1)

        with open ('Config.json', 'w') as Config:
            Config.write (json.dumps (Data))

        Status = Data['Status'].format (Data['Prefix'], str (Data['Users']))
        self.Client.change_presence (game = discord.Game (name = Status))

        Filing.AddMember (_Member)

        await Embed.Embed (
            self.Client,
            f'Welcome, {_Member.name}!',
            Data['Messages']['Welcome'],
            discord.Color.blue (),
            _Member
        )

        Log.Log ('[{}] : (Member Join) -> A new member has joined: ' + _Member.name)
        Log.Log ('[{}] : (Member Count) -> +1, Total: ' + str (Data['Users']))

    async def on_member_leave (self, _Member):
        with open ('Config.json', 'r') as Config:
            Data = json.loads (Config.read ())

        Data['Users'] = str (int (Data['Users']) - 1)

        with open ('Config.json', 'w') as Config:
            Config.write (json.dumps (Data))

        Status = Data['Status'].format (Data['Prefix'], str (Data['Users']))
        self.Client.change_presence (game = discord.Game (name = Status))

        Filing.RemoveMember (_Member)

        Log.Log ('[{}] : (Member Join) -> A member has left: ' + _Member.name)
        Log.Log ('[{}] : (Member Count) -> -1, Total: ' + str (Data['Users']))

    async def on_member_update (self, _Before, _After):
        Filing.UpdateMember (_Before, _After)

    async def on_server_update (self, _Before, _After):
        Filing.UpdateServer (_Before, _After)

def setup (_Client):
    _Client.add_cog (Events (_Client))
