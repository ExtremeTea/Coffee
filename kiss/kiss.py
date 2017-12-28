from discord.ext import commands
import random
import discord

class Kiss:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kiss(self, context, member: discord.Member):
        """Kiss Someone"""
        author = context.message.author.mention
        mention = member.mention

        kiss = "**{0} gave {1} a smooch**"

        choices = ['https://media.giphy.com/media/BaEE3QOfm2rf2/giphy.gif', 'https://media.giphy.com/media/R5y0BdnOL010c/giphy.gif', 'https://media.giphy.com/media/izQncAc6OnIUo/giphy.gif', 'https://media.giphy.com/media/hnNyVPIXgLdle/giphy.gif', 'https://media.giphy.com/media/OSq9souL3j5zW/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Kiss(bot)
    bot.add_cog(n)
