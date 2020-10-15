from discord.ext import commands
import Settings
import discord
import funcs
import json

def get_servers():
    with open('data/servers.json', 'r', encoding='utf-8') as f:
        return json.load(f)

bot = commands.Bot(command_prefix=Settings.prefix)

@bot.event
async def on_ready():
    print(f'Bot ready - {bot.user}')

    for guild in bot.guilds:
        await funcs.store_guild(guild)

    for cog in Settings.cogs:
        bot.load_extension(f'cogs.{cog}')


if __name__ == "__main__":
    
    bot.run(Settings.token)