from discord.ext import commands
import random
import discord

class Cry:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cry(self, context, member: discord.Member):
        """Cry now"""
        author = context.message.author.mention
        mention = member.mention

        cry = "**{0} starting cry because {1}*" 

        choices = ['https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif', 'https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif', 'http://media1.giphy.com/media/oAW9QPkQwJqJq/giphy.gif', 'https://media.giphy.com/media/xQVq9Wv61jlSw/giphy.gif', 'https://78.media.tumblr.com/2878ee0ff1de9034a8b96e77915771ea/tumblr_opqkpsFVyG1scqbpuo1_500.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=cry.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Cry(bot)
    bot.add_cog(n)
