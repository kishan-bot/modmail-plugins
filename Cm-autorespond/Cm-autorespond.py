import discord
from discord.ext import commands


class ClashMasterAutoReplyHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id == 633338364661334036:
            if "help" in message.content.lower():
                await message.channel.send(f"if you need help than you can contact <@661738241959002122>")

        if message.channel.id == 633338364661334036:
            if "clashmaster" in message.content.lower():
                await message.channel.send(f"clash master is discord server for coc recruitments")

def setup(bot):
    bot.add_cog(ClashMasterAutoReplyHelp(bot))
