import discord

import json

# --- Embeds ---
async def Embed (_Client, _Title, _Content, _Color, _Channel):
    Embed = discord.Embed (title = _Title, description = _Content, color = _Color)

    await _Client.send_message (_Channel, embed = Embed)

async def LinkEmbed (_Client, _Title, _Content, _Link, _Color, _Channel):
    Embed = discord.Embed (title = _Title, url = _Link, description = _Content, color = _Color)

    await _Client.send_message (_Channel, embed = Embed)

async def CommandsEmbed (_Client, _Title, _Description, _Commands, _Color, _Channel):
    # Title = Make Indies - Commands
    # Description = Here's all the Make Indies bot's commands
    Embed = discord.Embed (title = _Title, description = _Description, color= _Color)

    for Command in _Commands:
        Embed.add_field (name = Command, value = _Commands[Command], inline = False)

    await _Client.send_message (_Channel, embed = Embed)

async def RulesEmbed (_Client, _Title, _Rules, _Color, _Channel):
    RulesString = ''
    Index = 1
    for Rule in _Rules:
        RulesString += f'{str (Index)}. {str (Rule)}\n'

    Embed = discord.Embed (title = _Title, description = RulesString, color = _Color)

    await _Client.send_message (_Channel, embed = Embed)
