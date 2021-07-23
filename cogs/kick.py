from discord.ext import commands
from cogs.manager import databaseManager
from discord.ext.commands import has_permissions, MissingPermissions
import discord

class kickCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @has_permissions(administrator=True)
    @commands.command(name="kick")
    async def kickUser(self,ctx, member: discord.Member, *, reason: str):
        channelId = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        mutedlId = databaseManager.sql.getSpecific(ctx.guild.id, 3)
        channel = member.guild.get_channel(channelId)
        embed=discord.Embed(title="User >> Kicked", color=0xec3818)
        embed.set_thumbnail(url="https://i.imgur.com/SskLshZ.png")
        embed.add_field(name="Author: ", value=ctx.author.name, inline=True)
        embed.add_field(name="Target: ", value=member.name, inline=False)
        embed.add_field(name="Reason:", value=reason, inline=True)
        embed.set_footer(text=f"{ctx.author.id}")
        await ctx.message.delete()
        await channel.send(embed=embed)
        await member.kick(reason=reason)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(kickCommand(bot))