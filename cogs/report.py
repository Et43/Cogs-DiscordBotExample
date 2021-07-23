from discord.ext import commands
import discord
from cogs.manager import databaseManager

class reportCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="report")
    async def report(self, ctx, member: discord.Member, *, reason: str):
        logsChannel = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        await ctx.send(logsChannel)
        channel = ctx.guild.get_channel(logsChannel)

        await ctx.message.delete()
        await ctx.send(f"**{member}** has been reported for: `{reason}`")
        botMessage = await channel.send(f"**{member}** has been reported")
        await botMessage.add_reaction("❌")
        await self.bot.on_reaction_add()
        



def setup(bot):
    bot.add_cog(reportCommand(bot))