# Interchat
This bot connects multiple channels from multiple servers to a kind of "Interchat", which basically if I send a message in a server I can see it from any other server where the bot is and is configured. Only json is used (to save the channel IDs) and the own functions of discord.py
![Preview](https://media.discordapp.net/attachments/765988053943844884/766151770941423616/unknown.png)

# Setup
To be able to use it you must install the requirements that are in the file `requirements.txt` with `pip install -U -r requirements.txt` (If you are in windows you need to have Pip in environment variables)

Configure the `Settings.py` file. Example:
```py
# Settings for Interchat | Check README.md file for help

  
token =  'Your bot token here'
prefix =  '!'

cogs =  ['events','interchat']
```
If you want to hide the token in the .env file:
* Create the file `.env`
* Put in there this:
```
token=here your token
```

**Interchat channel**
For the moment to set the channel you need to put manually the channel id in `servers.json`  file in `data`  folder after start the bot


#### © BayGamerYT 2020