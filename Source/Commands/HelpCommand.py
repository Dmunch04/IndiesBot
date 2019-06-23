import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Help:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Message = Data['Messages']['Help']
            self.Commands = Data['Messages']['Commands']
            self.Prefix = Data['Prefix']

    @commands.command (pass_context = True)
    async def help (self, ctx):
        Channel = ctx.message.channel

        await Embed.Embed (
            self.Client,
            'Make Indies - Help',
            f'{self.Message}',
            discord.Color.black (),
            Channel
        )

    @commands.command (pass_context = True)
    async def commands (self, ctx):
        Channel = ctx.message.channel

        """
        Commands = []
        for Command in self.Commands:
            Commands.append (Command.format (self.Data['Prefix']))

        await Embed.RulesEmbed (
            self.Client,
            'Make Indies - Commands',
            Commands,
            discord.Color.black (),
            Channel
        )
        """

        Commands = {}
        for Command in self.Commands:
            Command = Command.format (self.Data['Prefix'])
            Commands[Command] = self.Commands[Command]

        await Embed.RulesEmbed (
            self.Client,
            'Make Indies - Commands',
            'Here\'s all the Make Indies bot\'s commands'
            Commands,
            discord.Color.black (),
            Channel
        )

    @commands.command (pass_context = True)
    async def command (self, ctx, _Command):
        Channel = ctx.message.channel

        if not _Command.lower () in self.Commands:
            await Embed.Embed (
                self.Client,
                'Unkown Command',
                f'Could not find the command: {_Command}!',
                discord.Color.red (),
                Channel
            )

            return None

        Commands = list (self.Commands)
        Index = Commands.index (_Command.lower ())
        Command = Commands[Index]

        await Embed.Embed (
            self.Client,
            f'Commands - {_Command}',
            f'Use: {Command.format (self.Prefix)}\nDescription:{self.Commands[Command]}',
            discord.Color.black (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Help (_Client))
