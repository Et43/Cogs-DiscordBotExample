from discord.ext import commands
import discord
from cogs.manager import databaseManager
from discord.utils import get
import asyncio

class muteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="mute")
    async def mute(self,ctx, member: discord.Member, Mutetime: str, *, reason: str):
        mutedlId = databaseManager.sql.getSpecific(ctx.guild.id, 3)
        role = get(ctx.guild.roles, id=mutedlId)
        author = ctx.author.name
        authorID = ctx.author.id 
        target = member.name
        channelId = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        channel = member.guild.get_channel(channelId)

        def timeCheck(muteTime):
            if "h" in muteTime:
                muteTime = muteTime.replace("h", "")
                muteTime = int(muteTime) * 3600
                return muteTime
            elif "m" in muteTime:
                muteTime = muteTime.replace("m", "")
                muteTime = int(muteTime) * 60
                return muteTime
            elif "d" in muteTime:
                muteTime = muteTime.replace("d", "")
                muteTime = int(muteTime) * 86400
                return muteTime
            elif "s" in muteTime:
                muteTime = muteTime.replace("s", "")
                return muteTime


        embed=discord.Embed(title="Punishment >> Muted", color=0xff0000)
        embed.add_field(name="Author", value=author, inline=True)
        embed.add_field(name="User", value=target, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Time", value=Mutetime, inline=True)
        embed.set_footer(text=authorID)
        await ctx.message.delete()
        await channel.send(embed=embed)
        await member.add_roles(role)
        await ctx.send(embed=embed)
        await asyncio.sleep(int(timeCheck(Mutetime)))
        await member.remove_roles(role)


    @commands.command(name="unmute")
    async def unmute(self,ctx, member: discord.Member):
        mutedlId = databaseManager.sql.getSpecific(ctx.guild.id, 3)
        role = get(ctx.guild.roles, id=mutedlId)
        author = ctx.author.name
        authorID = ctx.author.id 
        target = member.name
        channelId = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        channel = member.guild.get_channel(channelId)

        embed=discord.Embed(title="Punishment >> Unmuted", color=0xff0000)
        embed.add_field(name="Author", value=author, inline=True)
        embed.add_field(name="User", value=target, inline=False)
        embed.set_footer(text=authorID)
        await ctx.message.delete()
        await channel.send(embed=embed)
        await member.remove_roles(role)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(muteCommand(bot))