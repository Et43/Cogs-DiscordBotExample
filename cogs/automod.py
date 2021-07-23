from discord.ext import commands
from cogs.manager import databaseManager
import sqlite3
import discord

class autmodCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        channel = self.bot.get_channel(message.channel.id)
        if message.author.id == 732620620092669952:
            pass
        else:
            try:
                words = databaseManager.sql.getallswearwords(message.guild.id)
                checker = message.content.split(" ")
                for i in checker:
                    if i in words:
                        await message.delete()
                        embed=discord.Embed(title="Automod", color=0xff0000)
                        embed.add_field(name="Warned", value=message.author.id, inline=False)
                        await message.channel.send(embed=embed)
                    else:
                        pass
            except sqlite3.OperationalError as err:
                print(err)

    
    @commands.command(name="addword")
    async def addword(self, ctx, *, word:str):
        serId = ctx.guild.id
        await ctx.message.delete()
        databaseManager.sql.addSwearWords(serId, word)
        embed=discord.Embed(title="Server Swear Words", color=0xff0000)
        embed.add_field(name="Added Swear Words:", value=word, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name="listwords")
    async def listwords(self, ctx):
        swearWords = databaseManager.sql.getallswearwords(ctx.guild.id)
        await ctx.message.delete()
        embed=discord.Embed(title="Server Swear Words", color=0xff0000)
        embed.add_field(name="Swear Words:", value=swearWords, inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name="delword")
    async def delword(self, ctx, *, word:str):
        serId = ctx.guild.id
        await ctx.message.delete()
        try:
            databaseManager.sql.removeSwearWords(serId, word)
            embed=discord.Embed(title="Server Swear Words", color=0xff0000)
            embed.add_field(name="Added Swear Words:", value=word, inline=False)
            await ctx.send(embed=embed)
        except sqlite3.OperationalError as err:
            embed=discord.Embed(title="SQL ERROR!", color=0xff0000)
            embed.add_field(name="Error", value=err, inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(autmodCommand(bot))