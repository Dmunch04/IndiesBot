import json
import datetime

def Setup ():
    with open ('Bot.json', 'r') as BotFile:
        Data = json.loads (BotFile.read ())

    Path = f'Logs/Log-{Data['Build']}.txt'

    with open (Path, 'w+') as LogFile:
        LogFile.write (f'Bot started at: {str (datetime.datetime.now ())}')
        LogFile.write (f'Build: {str (Data['Build'])}')
        LogFile.write (f'Version: {str (Data['Version'])}')
        LogFile.write ('------------------------------------------')
        LogFile.write ('Events:')
