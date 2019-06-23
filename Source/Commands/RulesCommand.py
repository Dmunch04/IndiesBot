import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Rules:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Message = Data['Messages']['Rules']

    @commands.command (pass_context = True)
    async def rules (self, ctx):
        Channel = ctx.message.channel

        await Embed.RulesEmbed (
            self.Client,
            'Make Indies - Rules',
            self.Message,
            discord.Color.black (),
            Channel
        )

    @commands.command (pass_context = True)
    async def rule (self, ctx, _RuleNumber : int):
        Channel = ctx.message.channel

        try:
            Rule = self.Message[int (_RuleNumber) - 1]

        except:
            await Embed.Embed (
                self.Client,
                'Rule Number Out Of Index',
                f'The rule number is out of index: {_RuleNumber}!',
                discord.Color.red (),
                Channel
            )

            return None

        await Embed.Embed (
            self.Client,
            f'Make Indies - Rule {str (_RuleNumber)}',
            f'{Rule}',
            discord.Color.black (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Rules (_Client))
