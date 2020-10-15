from discord.ext import commands
import funcs

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        r = await funcs.store_guild(guild)
        if r == None:
            print(f'Failed to store config for a guild')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        r = await funcs.delete_guild(guild)
        if r == None:
            print(f'Failed to delete config for a guild')


def setup(bot):
    bot.add_cog(Events(bot))