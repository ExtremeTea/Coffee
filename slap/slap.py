from discord.ext import commands
import random
import discord

class slap:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def slap(self, context, member: discord.Member):
        """Slap everyone!"""
        author = context.message.author.mention
        mention = member.mention

        slap = "**{0} got slapped by {1}!**"

        choices = ['https://media.giphy.com/media/8R8htEk0IgAlq/giphy.gif', 'https://media.giphy.com/media/rFfmUWVMOyKVG/giphy.gif', 'https://media.giphy.com/media/ellxlkgbPTiM0/giphy.gif', 'https://media.giphy.com/media/3lBOIbP9ghX2/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=slap.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = slap(bot)
    bot.add_cog(n)
