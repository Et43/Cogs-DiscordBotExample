from discord.ext import commands
import discord
from cogs.manager import databaseManager

class warnCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="warn")
    async def warn(self,ctx, member: discord.Member, *, reason):
        databaseManager.sql.addWarnings(ctx.guild.id, member.id, reason)
        await ctx.send(f"{member.mention} has been warned for {reason}")
    
    @commands.command(name="getwarns")
    async def getwarns(self, ctx, member: discord.Member):
        warns = databaseManager.sql.getallwarnings(ctx.guild.id, member.id)
        warnID = -1
        for i in warns:
            warnID = warnID + 1
            await ctx.send(f"[{warnID}] {i}")

def setup(bot):
    bot.add_cog(warnCommand(bot))