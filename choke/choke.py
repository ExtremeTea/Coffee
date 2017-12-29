from discord.ext import commands
import random
import discord

class choke:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def choke(self, context, member: discord.Member):
        """choke someone!"""
        author = context.message.author.mention
        mention = member.mention

        choke = "**{0} got choked by {1}!**"

        choices = ['https://i.pinimg.com/originals/c8/50/da/c850daccaff312f7aa1c6cb23b62b512.gif', 'https://i.pinimg.com/originals/de/65/28/de6528ed86c887ff598c39b6e97df7e2.gif', 'https://78.media.tumblr.com/79675353fbeeed25969255ec6ee82a0f/tumblr_n94nbhTTM41rb06tgo1_r2_500.gif', 'https://data.whicdn.com/images/107788263/original.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=choke.format(mention, author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = choke(bot)
    bot.add_cog(n)
