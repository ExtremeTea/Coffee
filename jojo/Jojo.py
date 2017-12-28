from discord.ext import commands
import random
import discord

class hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, context, member: discord.Member):
        """hug someone!"""
        author = context.message.author.mention
        mention = member.mention

        hug = "**{0} got hugged by {1}!**"

        choices = ['http://i.imgur.com/10VrpFZ.gif', 'http://i.imgur.com/x0u35IU.gif', 'http://i.imgur.com/0gTbTNR.gif', 'http://i.imgur.com/hlLCiAt.gif', 'http://i.imgur.com/sAANBDj.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=hug.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = hug(bot)
    bot.add_cog(n)
