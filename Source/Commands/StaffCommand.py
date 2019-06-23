import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Staff:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Moderator = Data['ModeratorRole']
            self.Muted = Data['MutedRole']

    @commands.command (pass_context = True)
    async def warn (self, ctx, _User : discord.User, *_Reason = ['']):
        Channel = ctx.message.channel

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        Reason = ' '.join (_Reason)

        await Embed.Embed (
            self.Client,
            'Make Indies - Warn',
            f'{_User.name} has now been warned by {Sender.mention}, for: {Reason}!',
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def mute (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Sender = ctx.message.author

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        Role = discord.utils.get (Server.roles, name = self.Muted)

        await self.Client.add_roles (_User, Role)

        await Embed.Embed (
            self.Client,
            'Make Indies - Mute',
            f'{_User.name} has now been muted by {Sender.mention}!',
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def unmute (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Sender = ctx.message.author

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        Role = discord.utils.get (Server.roles, name = self.Muted)

        await self.Client.remove_roles (_User, Role)

        await Embed.Embed (
            self.Client,
            'Make Indies - Unmute',
            f'{_User.name} has now been unmuted by {Sender.mention}!',
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def kick (self, ctx, _User : discord.User):
        Channel = ctx.message.channel
        Sender = ctx.message.channel

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        self.Client.kick (_User)

        await Embed.Embed (
            self.Client,
            'Make Indies - Kick',
            f'{_User.name} has now been kicked by {Sender.mention}!',
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def ban (self, ctx, _User : discord.User):
        Channel = ctx.message.channel
        Sender = ctx.message.author

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        await self.Client.ban (_User, 0)

        await Embed.Embed (
            self.Client,
            'Make Indies - Ban',
            f'{_User.name} has now been banned by {Sender.mention}!',
            discord.Color.purple (),
            Channel
        )

    @commands.command (pass_context = True)
    async def unban (self, ctx, _User : discord.User):
        Server = ctx.message.server
        Channel = ctx.message.channel
        Sender = ctx.message.author

        # The command sender is not a moderator
        if role.CheckRole (Sender, self.Moderator) == False:
            await Embed.Embed (
                self.Client,
                'Make Indies - Permission Error',
                'You don\'t have the required permissions to perform this command!',
                discord.Color.red (),
                Channel
            )

            return None

        await self.Client.unban (Server, _User)

        await Embed.Embed (
            self.Client,
            'Make Indies - Unban',
            f'{_User.name} has now been unbanned by {Sender.mention}!',
            discord.Color.purple (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Staff (_Client))
