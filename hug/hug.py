huggedfrom discord.ext import commands
import random
import discord

class hug:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hug(self, context, member: discord.Member):
        """hug everyone!"""
        author = context.message.author.mention
        mention = member.mention

        hug = "**{0} got hugged by {1}!**"

        choices = ['https://media.giphy.com/media/tX29X2Dx3sAXS/giphy.gif', 'https://media.giphy.com/media/RXGNsyRb1hDJm/giphy.gif', 'https://media.giphy.com/media/exaa8OED1vvq/giphy.gif', 'https://media.giphy.com/media/1iw7RG8JbOmpq/giphy.gif', 'https://media.giphy.com/media/xXRDuvEcMA2JO/giphy.gif', 'https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif', 'https://media1.giphy.com/media/KtWEleZrkvois/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=hug.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = hug(bot)
    bot.add_cog(n)
