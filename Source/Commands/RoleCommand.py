import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Roles:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

            self.Roles = Data['Roles']

    @commands.command (pass_context = True)
    async def role (self, ctx, _Role):
        Channel = ctx.message.channel
        Sender = ctx.message.author

        if not _Role.lower () in self.Roles:
            await Embed.Embed (
                self.Client,
                'Unkown Role',
                f'Could not add the role: {_Role}!',
                discord.Color.red (),
                Channel
            )

            return None

        Role = discord.utils.get (Server.roles, name = _Role)

        if role.CheckRole (Sender, Role) == True:
            await self.Client.remove_roles (Sender, Role)

            await Embed.Embed (
                self.Client,
                'Role Removed',
                f'Successfully removed the role, {str (Role)}, from {str (Sender)}',
                discord.Color.green (),
                Channel
            )

            return None

        else:
            await self.Client.add_roles (Sender, Role)

            await Embed.Embed (
                self.Client,
                'Role Added',
                f'Successfully added the role, {str (Role)}, to {str (Sender)}',
                discord.Color.green (),
                Channel
            )

            return None

    @commands.command (pass_context = True)
    async def roles (self, ctx):
        Channel = ctx.message.channel

        await Embed.RulesEmbed (
            self.Client,
            'Make Indies - Roles',
            self.Roles,
            discord.Color.purple (),
            Channel
        )

def setup (_Client):
    _Client.add_cog (CMD_Roles (_Client))
