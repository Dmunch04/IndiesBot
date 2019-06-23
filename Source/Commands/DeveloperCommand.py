import discord
from discord.ext import commands

import os
import json
import shutil

from Helpers import EmbedHelper as Embed

class CMD_Developer:
    def __init__ (self, Client):
        self.Client = Client

        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

        self.Path = self.Data['UserPath']

    @commands.command (pass_context = True)
    @commands.has_role ('MOD')
    async def userfiles (self, ctx):
        Server = ctx.message.server
        Channel = ctx.message.channel

        # Empty all user folders here
        shutil.rmtree (self.Path)

        for Member in Server.members:
            Name = Member.name
            Tag = Member.discriminator
            ID = Member.id
            IsBot = Member.bot
            Roles = Member.roles
            JoinTime = Member.joined_at

            UserData = {
                'Name': Name,
                'Tag': Tag,
                'ID': ID,
                'IsBot': IsBot,
                'Roles': Roles,
                'JoinTime': JoinTime,
                'Karma': 0,
                'Warnings': 0,
                'Activity': 0,
                'Level': 0,
                'XP': 0
            }

            Path = self.Path + f'{Name}#{Tag}/'

            # Create a user folder here, with: {Name}#{Tag}
            if not os.path.exists (Path):
                os.makedirs (Path)

            # And then create a User.json file inside that
            # folder, containing the users info
            Path += 'UserFile.json'

            with open (Path, 'w+') as UserFile:
                UserFile.write (json.dumps (UserData))

    @commands.command (pass_context = True)
    @commands.has_role ('MOD')
    async def clear (self, ctx):
        shutil.rmtree (self.Path)

    @commands.command (pass_context = True)
    @commands.has_role ('MOD')
    async def userfile (self, ctx, _Member : discord.Member):
        Name = _Member.name
        Tag = _Member.tag
        ID = _Member.id
        IsBot = _Member.bot
        Roles = _Member.roles
        JoinTime = _Member.joined_at

        UserData = {
            'Name': Name,
            'Tag': Tag,
            'ID': ID,
            'IsBot': IsBot,
            'Roles': Roles,
            'JoinTime': JoinTime,
            'Karma': 0,
            'Warnings': 0,
            'Activity': 0,
            'Level': 0,
            'XP': 0
        }

        Path = self.Path + f'{Name}#{Tag}/'

        if is.path.exists (Path):
            shutil.rmtree (Path)

        # Create a user folder here, with: {Name}#{Tag}
        if not os.path.exists (Path):
            os.makedirs (Path)

        # And then create a User.json file inside that
        # folder, containing the users info
        Path += 'UserFile.json'

        with open (Path, 'w+') as UserFile:
            UserFile.write (json.dumps (UserData))

def setup (_Client):
    _Client.add_cog (CMD_Developer (_Client))
