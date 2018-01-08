from discord.ext import commands
import random
import discord

class jojo:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def jojo(self, context, member: discord.Member):
        """Give someone Jojo love!"""
        author = context.message.author.mention
        mention = member.mention

        jojo = "**{0} got a reference by {1}!**"

        choices = ['https://i.imgur.com/XJhnSv5.gif', 'https://i.imgur.com/3xhoZg8.gif', 'https://i.imgur.com/D7SqDBP.gif', 'https://i.imgur.com/dUAc1jw.gif', 'https://i.imgur.com/W7OsiYW.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=jojo.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = jojo(bot)
    bot.add_cog(n)
