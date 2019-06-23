import discord
from discord.ext import commands

import json

from Helpers import EmbedHelper as Embed

class CMD_Support:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

    @commands.command (pass_context = True)
    async def support (self, ctx, *_Description):
        Server = ctx.message.server
        Sender = ctx.message.author

        Description = ' '.join (_Description)
        ChannelNumber = str (self.Data['SupportIndex'])

        DefaultPermission = discord.PermissionOverwrite (read_messages = False, send_messages = False)
        ViewPermission = discord.PermissionOverwrite (read_messages = True, send_messages = True)

        SupportRole = discord.utils.get (Server.roles, name = self.Data['SupportRole'])

        self.Client.create_channel (
            Server,
            f'support-{ChannelNumber}',
            (Server.default_role, DefaultPermission),
            (Sender, ViewPermission),
            (SupportRole, ViewPermission),
            type = discord.ChannelType.text
        )

        self.Data['SupportIndex'] = str (int (self.Data['SupportIndex']) + 1)

        with open ('Config.json', 'w') as Config:
            Config.write (json.dumps (Data))

    @commands.command (pass_context = True)
    async def close (self, ctx):
        Channel = ''

        if Channel.name.startswith ('support-'):
            self.Client.delete_channel (Channel)

def setup (_Client):
    _Client.add_cog (CMD_Support (_Client))
