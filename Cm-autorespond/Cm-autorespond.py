import discord
from discord.ext import commands


class ClashMasterAutoReplyHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.channel.id == 711520959361974272:
            if "help" in message.content.lower():
                await message.channel.send(f"if you need help than you can contact <@661738241959002122>")

        if message.channel.id == 711520959361974272:
            if "clashmaster" in message.content.lower():
                await message.channel.send(f"clash master is discord server for coc recruitments")
        if message.channel.id == 711520959361974272:
            if "clan" in message.content.lower():
                await message.channel.send(f"{message.author.mention}! if you need clan than u can bla bla")
        if message.channel.id == 711520959361974272:
            if "mod" in message.content.lower():
                await message.channel.send(f"{message.author.mention}! You can learn Moderation commands here https://dyno.gg/commands#/Moderator")
        if message.channel.id == 711520959361974272:
            if "sell" in message.content.lower():
                await message.delete()
                await message.channel.send(f"{message.author.mention}! If you are trying to sell coc account than i remind you it's against TOS if send this again you will get banned from server") 
def setup(bot):
    bot.add_cog(ClashMasterAutoReplyHelp(bot))
