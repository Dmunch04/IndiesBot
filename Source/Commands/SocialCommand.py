import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Socials:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Patreon = Data['Socials']['Patreon']
            self.Twitch = Data['Socials']['Twitch']
            self.Twitter = Data['Socials']['Twitter']
            self.Instagram = Data['Socials']['Instagram']

    @commands.command (pass_context = True)
    async def patreon (self, ctx):
        Channel = ctx.message.channel

        """
        await Embed.Embed (
            self.Client,
            'Make Indies - Patreon',
            f'Here\'s the link to Make Indies Patreon page:\n{self.Patreon}',
            discord.Color.purple (),
            Channel
        )
        """

        await Embed.LinkEmbed (
            self.Client,
            'Make Indies - Patreon',
            'Here\'s the link to Make Indies Patreon page',
            self.Patreon,
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def twitch (self, ctx):
        Channel = ctx.message.channel

        """
        await Embed.Embed (
            self.Client,
            'Make Indies - Twitch',
            f'Here\'s the link to Make Indies Twitch channel:\n{self.Twitch}',
            discord.Color.purple (),
            Channel
        )
        """

        await Embed.LinkEmbed (
            self.Client,
            'Make Indies - Twitch',
            'Here\'s the link to Make Indies Twitch channel',
            self.Twitch,
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def twitter (self, ctx):
        Channel = ctx.message.channel

        """
        await Embed.Embed (
            self.Client,
            'Make Indies - Twitter',
            f'Here\'s the link to Make Indies Twitter account:\n{self.Twitter}',
            discord.Color.purple (),
            Channel
        )
        """

        await Embed.LinkEmbed (
            self.Client,
            'Make Indies - Twitter',
            'Here\'s the link to Make Indies Twitter page',
            self.Twitter,
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def instagram (self, ctx):
        Channel = ctx.message.channel

        """
        await Embed.Embed (
            self.Client,
            'Make Indies - Instagram',
            f'Here\'s the link to Make Indies Instagram account:\n{self.Instagram}',
            discord.Color.purple (),
            Channel
        )
        """

        await Embed.LinkEmbed (
            self.Client,
            'Make Indies - Instagram',
            'Here\'s the link to Make Indies Instagram page',
            self.Instagram,
            discord.Color.purple (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Socials (_Client))
