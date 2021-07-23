from discord.ext import commands

class sayCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="say")
    async def say(self,ctx, *, message: str):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(sayCommand(bot))