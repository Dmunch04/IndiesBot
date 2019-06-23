# Discord Imports
import discord
from discord.ext import commands

import json
from DavesLogger import Logs

import Setup
from Modules import Logger

class Bot (commands.Bot):
    def __init__ (self):
        with open ('Config.json', 'r') as Config:
            self.Data = json.loads (Config.read ())

        self.Status = self.Data['Status'].format (self.Data['Prefix'], str (self.Data['Users']))

        super ().__init__ (command_prefix = self.Data['Prefix'])

    @self.event
    async def on_ready (self):
        await self.change_presence (game = discord.Game (name = self.Status))

        Logs.Server ('The bot has been booted!')

        Log.Log ('[{}] : (Bot Ready) -> The bot is now ready!')

    async def LoadCogs (self, _Folder, _Cogs, _IsCommands = True):
        for Cog in _Cogs:
            Cog = '{0}.{1}Command' if _IsCommands else '{0}.{1}'
            Cog = Cog.format (_Folder, Cog)

            try:
                self.load_extension (Cog)

            except Exception as Error:
                ErrorMsg = '{0} cannot be loaded. Error: {0}'.format (Cog, Error)
                Logs.Error (ErrorMsg)

    # Depricated
    def Log (self, _Type, _Log):
        Message = '[{}] : ' + f'({str (_Type)}) -> {str (_Log)}'

        Logger.Log (Message)

    async def Run (self):
        with open ('Bot.json', 'r') as BotFile:
            Data = json.loads (BotFile.read ())

        Data['Build'] = str (int (Data['Build']) + 1)

        with open ('Bot.json', 'w') as BotFile:
            BotFile.write (json.dumps (Data))

        Setup.Setup ()
        Log.Log ('[{}] : (Bot Run) -> The bots run function was called!')

        self.Data['Users'] = str (self.get_server (self.Data['ServerID']).member_count)

        with open ('Config.json', 'w') as Config:
            Config.write (json.dumps (self.Data))

        self.remove_command ('help')
        self.Client.load_extension ('Events')

        await self.LoadCogs (self.Data['CommandsFolder'], self.Data['Commands'], True)
        await self.LoadCogs (self.Data['ModulesFolder'], self.Data['Modules'], False)

        self.run (self.Data['Token'])

if __name__ == '__main__':
    Client = Bot ()

    await Client.Run ()
