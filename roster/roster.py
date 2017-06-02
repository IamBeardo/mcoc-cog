import discord
from discord.ext import commands

class roster:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stujdföklafdsölkjdsfaöklafdskölff!"""

        #Your code will go here
        await self.bot.say("I can do everyting!")


    @commands.command()
    async def punch(self, user : discord.Member):
        """PUNCH"""

        await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")



def setup(bot):
    bot.add_cog(roster(bot))
