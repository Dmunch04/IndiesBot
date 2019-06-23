import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Server:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Link = Data['Invite']

    @commands.command (pass_context = True)
    async def invite (self, ctx):
        Channel = ctx.message.channel

        await Embed.Embed (
            self.Client,
            f'Make Indies - Invite Link {str (_RuleNumber)}',
            f'Link:\n<{str (self.Link)}>',
            discord.Color.purple (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Rules (_Client))
