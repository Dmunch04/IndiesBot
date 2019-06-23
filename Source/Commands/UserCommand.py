import discord
from discord.ext import commands

import os
import json

from Helpers import EmbedHelper as Embed

class CMD_User:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

        self.Path = self.Data['UserPath']

    @commands.command (pass_context = True)
    async def thanks (self, ctx, _Member : discord.Member):
        Channel = ctx.message.channel

        Name = _Member.name
        Tag = _Member.discriminator

        Path = self.Path + f'{Name}#{Tag}/'

        if os.path.exists (Path):
            Path += 'UserFile.json'

            with open (Path, 'r') as UserFile:
                Data = json.loads (UserFile.read ())

            Data['Karma'] = str (int (Data['Karma']) + 1)

            with open (Path, 'w') as UserFile:
                UserFile.write (json.dumps (Data))

def setup (_Client):
    _Client.add_cog (CMD_User (_Client))
