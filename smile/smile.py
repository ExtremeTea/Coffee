from discord.ext import commands
import random
import discord

class smile:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def smile(self, context, member: discord.Self):
        """smile for everyone!"""
        author = context.message.author.
        mention = member.

        smile = "**Smiled**"

        choices = ['https://media.giphy.com/media/8R8htEk0IgAlq/giphy.gif', 'https://media.giphy.com/media/rFfmUWVMOyKVG/giphy.gif', 'https://media.giphy.com/media/ellxlkgbPTiM0/giphy.gif', 'https://media.giphy.com/media/3lBOIbP9ghX2/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=smile.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = smile(bot)
    bot.add_cog(n)
