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

        choices = ['https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif', 'https://media.giphy.com/media/5eyhBKLvYhafu/giphy.gif', 'https://i.imgur.com/Ltmb8aa.gif', 'https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=hug.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Hug(bot)
    bot.add_cog(n)
