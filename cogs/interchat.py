from discord.ext import commands
import discord
import main

class Interchat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True:
            return

        if message.channel.id == main.get_servers()[str(message.guild.id)]['channel']:

            embed = discord.Embed(
                description = message.content,
                timestamp = message.created_at,
                color = 0x303136
            )
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_footer(text=f'{message.guild.name} {len(message.guild.members)} members', icon_url=message.guild.icon_url)

            await message.delete()

            for g in self.bot.guilds:

                if main.get_servers()[str(g.id)]['channel'] != 1:

                    channel = self.bot.get_channel(main.get_servers()[str(g.id)]['channel'])
                    try:
                        await channel.send(embed=embed)
                    except Exception as e:
                        print(f'Failed to send embed in {g.id}: {e}')

def setup(bot):
    bot.add_cog(Interchat(bot))