from discord.ext import commands
import asyncio
import discord
from cogs.manager import databaseManager

class banCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ban")
    async def ban(self,ctx, member: discord.Member, *, reason: str):
        author = ctx.author.name
        authorID = ctx.author.id 
        target = member.name
        channelId = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        channel = member.guild.get_channel(channelId)

        embed=discord.Embed(title="Punishment >> Banned", color=0xff0000)
        embed.add_field(name="Author", value=author, inline=True)
        embed.add_field(name="User", value=target, inline=False)
        embed.add_field(name="Reason", value=reason, inline=True)
        embed.set_footer(text=authorID)
        await ctx.message.delete()
        await channel.send(embed=embed)
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

    @commands.command(name="unban")
    async def unban(self,ctx, *, member):
        author = ctx.author.name
        authorID = ctx.author.id 
        channelId = databaseManager.sql.getSpecific(ctx.guild.id, 2)
        channel = ctx.guild.get_channel(channelId)
        bannedUsers = await ctx.guild.bans()
        memberName, memberDisc = member.split('#')
        unbanned = False
        for bans in bannedUsers:
            user = bans.user 

            if (user.name, user.discriminator) == (memberName, memberDisc):
                await ctx.guild.unban(user)
                unbanned = True
                embed=discord.Embed(title="Punishment >> Unbanned", color=0xff0000)
                embed.add_field(name="Author", value=author, inline=True)
                embed.add_field(name="User", value=member, inline=False)
                embed.set_footer(text=authorID)
                await ctx.message.delete()
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

        if unbanned == True:
            pass
        else:
            embed=discord.Embed(title="Error >> User Not Found", color=0xff0000)
            embed.add_field(name="User", value=member, inline=False)
            embed.set_footer(text=authorID)
            await ctx.message.delete()
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(banCommand(bot))