# Discord Imports
import discord
from discord.ext import commands

import json
import asyncio
from DavesLogger import Logs

import Setup
from Modules import Logger

with open ('Config.json', 'r') as Config:
    Data = json.loads (Config.read ())

Token = Data['Token']
Client = commands.Bot (command_prefix = Data['Prefix'])

@Client.event
async def on_ready ():
    await Client.change_presence (game = discord.Game (name = Data['Status'].format (Data['Prefix'], str (Data['Users']))))

    Logs.Server ('The bot has been booted!')

if __name__ == '__main__':
    with open ('Bot.json', 'r') as BotFile:
        Data = json.loads (BotFile.read ())

    Data['Build'] = str (int (Data['Build']) + 1)

    with open ('Bot.json', 'w') as BotFile:
        BotFile.write (json.dumps (Data))

    Setup.Setup ()

    Data['Users'] = str (Client.get_server (Data['ServerID']).member_count)

    with open ('Config.json', 'w') as Config:
        Config.write (json.dumps (Data))

    Client.remove_command ('help')
    Client.load_extension ('Events')

    for Command in Data['Commands']:
        Command = '{0}.{1}Command'.format (Data['CommandsFolder'], Command)

        try:
            Client.load_extension (Command)

        except Exception as Error:
            ErrorMsg = '{0} cannot be loaded. Error: {0}'.format (Command, Error)
            Logs.Error (ErrorMsg)

    for Module in Data['Modules']:
        Module = '{0}.{1}'.format (Data['ModulesFolder'], Module)

        try:
            Client.load_extension (Module)

        except Exception as Error:
            ErrorMsg = '{0} cannot be loaded. Error: {0}'.format (Module, Error)
            Logs.Error (ErrorMsg)

    Client.run (Token)
