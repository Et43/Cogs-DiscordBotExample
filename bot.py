import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

loaders = ["cogs.say", "cogs.report", "cogs.me", "cogs.setup", "cogs.kick", "cogs.ban", "cogs.mute", "cogs.automod", "cogs.warn"]

@bot.event
async def on_ready():
    print(f"""
   
 AWE MASEKIND

 Bot Id: {bot.user.id}
 Bot Name: {bot.user.name}
 Bot Latency: {bot.latency}
    
    """)

def meCheck(yes):
    if yes == 730692546392621076:
        return True
    else:
        return False

@bot.command(name="reload")
async def reload(ctx, *, string):
    if meCheck(ctx.author.id):
        bot.reload_extension(f"cogs.{string}")
        await ctx.send("Reloaded: " + f"cogs.{string}")
    else:
        await ctx.send("Missing Permission")

@bot.command(name="reloadall")
async def reloadall(ctx):
    if meCheck(ctx.author.id):
        for i in range(len(loaders)): 
            bot.reload_extension(loaders[i])
            await ctx.send("Reloaded: " + loaders[i])
    else:
        await ctx.send("Missing Permission")

@bot.command(name="update")
async def update(ctx, name: str):  
    if meCheck(ctx.author.id):
        bot.load_extension(f"cogs.{name}")
        await ctx.send(f"Added: cogs.{name}")
        if f"cogs.{name}" in loaders:
            pass
        else:
            loaders.append(f"cogs.{name}")

    else:
        await ctx.send("Missing Permission ") 

def loadExtensions(): 
    for i in range(len(loaders)): 
        bot.load_extension(loaders[i])
        print("[+] Loaded " + loaders[i] + " extension")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"**Error**: {error}")
    raise error

if __name__ == "__main__":
    loadExtensions()
    bot.run("ur token here")