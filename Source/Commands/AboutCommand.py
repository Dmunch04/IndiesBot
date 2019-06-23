import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_About:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Message = Data['Messages']['About']

    @commands.command (pass_context = True)
    async def about (self, ctx):
        Channel = ctx.message.channel

        await Embed.Embed (
            self.Client,
            'Make Indies - About',
            f'{self.Message}',
            discord.Color.black (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_About (_Client))
