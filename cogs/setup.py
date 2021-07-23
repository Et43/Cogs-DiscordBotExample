from cogs.manager import databaseManager
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
import sqlite3

class setupCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Handles the setup for the sql database
    @has_permissions(administrator=True) 
    @commands.command(name="setup")
    async def setup(self,ctx):
        if databaseManager.sql.validateServerTable(serverName = ctx.guild.id):
            await ctx.send("Server already registered!")
        else:
            serverName = ctx.guild.name 
            serverID = ctx.guild.id
            author = ctx.author.id
            
            # Check if the user wqho typed is the author
            def check(message):
                if message.author == author:
                    return True
                else:
                    return False

            # Cancer :`)
            await ctx.send("Please enter the **Member** / **Defualt** Role ID [ Example: `693110627492692089` ]")
            memberRole = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
            
            await ctx.send("Please enter the **Welcome** / **General** Channel ID [ Exmaple: `699332812477693952` ]")
            welcomeChannel = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
            
            await ctx.send("Please enter the **Logs** Channel ID [ Exmaple: `699332812477693952` ]")
            logsChannel = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
            
            await ctx.send("Please enter the **Muted** / **Punished** Role ID [ Example: `693110627492692089` ]")
            mutedRole = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author)
            

            try:
                databaseManager.sql.createSwearWordsTable(serverID)
                databaseManager.sql.createWarningsTable(serverID)
                databaseManager.sql.create(serverID)
                databaseManager.sql.addValue(serverID, memberRole.content, welcomeChannel.content, logsChannel.content, mutedRole.content)
                await ctx.send("Finished Setup :white_check_mark:")
                await ctx.send(databaseManager.sql.getTableForServer(serverID))
            except sqlite3.Error as er:
                # Error Handling
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{current_time} | {er}")
                await ctx.send(f"**Error**: {er}:negative_squared_cross_mark:")


    # Get the value for a certain attrabute
    @has_permissions(administrator=True)
    @commands.command(name="get")
    async def get(self,ctx,query):
        serverName = ctx.guild.id
        try: 
            await ctx.send(databaseManager.sql.getAttributeFromServer(serverName, query)[0])
        except sqlite3.Error as er:
            # Error Handling
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"{current_time} | {er}")
            await ctx.send(f"**Error**: {er} dom naai hoe poes dom is jy:negative_squared_cross_mark:")
    
    @has_permissions(administrator=True)
    @commands.command(name="check")
    async def check(self, ctx):
        if databaseManager.sql.validateServerTable(serverName = ctx.guild.id):
            await ctx.send("Server is registered :white_check_mark:")
        else:
            await ctx.send("Server is not found please run `!setup` :negative_squared_cross_mark:")


def setup(bot):
    bot.add_cog(setupCommand(bot))