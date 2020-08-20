import discord
from discord.ext import commands
from __main__ import send_cmd_help


class Animal:
    """Animal commands."""

    def __init__(self, bot):
        self.bot = bot
        self.session = self.bot.http.session

    @commands.command()
    async def cats(self):
        """Shows a cat"""
        search = "https://api.thecatapi.com/v1/images/search"
        try:
            async with self.session.get(search) as r:
                result = await r.json()
            await self.bot.say(result['url'])
        except:
            await self.bot.say("Couldnt Get An Image")

    @commands.command()
    async def pugs(self):
        """Shows a pug"""
        search = "https://dog.ceo/api/breeds/image/random"
        try:
            async with self.session.get(search) as r:
                result = await r.json()
            await self.bot.say(result['pug'])
        except:
            await self.bot.say("Could Not Get An Image")

def setup(bot):
    n = Animal(bot)
    bot.add_cog(n)
