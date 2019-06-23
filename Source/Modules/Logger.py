import json
import datetime

def Log (_Text):
    # _Text = '[{}] : (Info) -> Something has happened now!'
    Text = _Text.format (str (datetime.datetime.now ()))
    # Text = '[2019-06-09 13:46:42.668877] : (Info) -> Something has happened now!'

    with open ('Bot.json', 'r') as BotFile:
        Data = json.loads (BotFile.read ())

    Path = f'Logs/Log-{Data['Build']}.txt'

    with open (Path, 'a') as LogFile:
        LogFile.write (Text)
