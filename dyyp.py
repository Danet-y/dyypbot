import discord
from discord.ext import commands
from discord.ext.commands import Bot
from googletrans import Translator
import asyncio
import random
import datetime
import youtube_dl
bot = commands.Bot('dyp.', description='Dyyyyp')
nukeron = 'on'
token = '--'
YTDL_OPTS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }
#####################################
@bot.event 
async def on_ready():
    """On ready event!"""
    print("Logged in as " + str(bot.user))
    print("User ID: " + str(bot.user.id))
    print("Ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="🧨Danet🧨(6dnt)"))
#####################################
#####################################


#######################################################################################
#######################################################################################
#######################################################################################

@bot.command()
async def helpy(ctx):
    embed = discord.Embed(title=f"Dyyp Help",color=0xFF5733)
    embed.add_field(name="clear:",value = f'', inline=False)
    embed.add_field(name="Clear msg with amount", value = f'clear Number' ,inline=False)

    embed.add_field(name="txt:", value = f'', inline=False)
    embed.add_field(name="Crete Channel with amount", value = f'txt Name Number' , inline=False)

    embed.add_field(name="catg:",value = f'', inline=False)
    embed.add_field(name="Crete Catgory with amount",value = f'catg Name' , inline=False)

    embed.add_field(name="============", value = f'', inline=False)

    embed.add_field(name="avatar:", value = f'', inline=False)
    embed.add_field(name="Avatar of Users", value = f'avatar @user' , inline=False)

    embed.add_field(name="userinfo:",value = f'', inline=False)
    embed.add_field(name="Info About User",value = f'userinfo @user' , inline=False)

    embed.add_field(name="anon:", value = f'', inline=False)
    embed.add_field(name="Message Anonymouse to someone",value = f'anon @user message' , inline=False)

    embed.add_field(name="translate:", value = f'', inline=False)
    embed.add_field(name="Translate message",value = f'translate lang message' , inline=False)

    embed.add_field(name="=============",value = f'', inline=False)

    embed.add_field(name="dyn_del:", value = f'', inline=False)
    embed.add_field(name="Delete All Channel [!]Nuke",value = f'dyn_del' , inline=False)

    embed.add_field(name="dyn_spam:", value = f'', inline=False)
    embed.add_field(name="Spam a Msg in Channel [!]Nuke",value = f'dyn_spam Msg Number' , inline=False)

    ##embed.add_field(name="dyn_nukemsg:",value = f'', inline=False)
    ##embed.add_field(name="Clear all msg in channel [!]Nuke", value = f'dyn_nukemsg' ,inline=False)

    embed.add_field(name="=============",value = f'',  inline=False)

    embed.add_field(name="giveaway:", value = f'', inline=False)
    embed.add_field(name="Giveaway",value = f'giveaway C_id Prize Time' , inline=False)

    embed.add_field(name="reroll:", value = f'', inline=False)
    embed.add_field(name="reroll giveaway",value = f'reroll C_id Msg_id', inline=False)
    
    embed.set_footer(text="Dyyp Bot")
    await ctx.send(embed=embed)
#######################################################################################
#######################################################################################
#######################################################################################

##FUN:
@bot.command()
async def slap(ctx, user: discord.Member=None):
    if user is None:
        message = "I don't wanna slap you!"
    else:
        message = "{} was slapped by {}! *ouch*".format(ctx.author.mention,
                                                        user.mention)
    await ctx.send(message)


#######################################################################################
#######################################################################################
#######################################################################################

##Clear
@bot.command(pass_context=True)
async def clear(ctx, number : int):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:        
        try:
            await ctx.channel.purge(limit=number+1)
            await ctx.send(f"`Successfully cleared {str(number)} messages from this channel`")
        except:
            await ctx.send("`I don't have permission to delete messages.`") 
    else:
        await ctx.send("`You don't have permission to delete messages.`")


##addchannel
@bot.command()
 
async def txt(ctx, *, name=None):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        if name == None:
            await ctx.send('Sorry, but you have to insert a name. Try again, but do it like this: `>create [channel name]`')
        else:
            x = name.split()
        if len(x)!=2:
                await ctx.send('Sorry , plz insert name of channel and number of them')
        nam = x[0]
        num = int(x[1])
        for i in range(num):
            await guild.create_text_channel(nam)
        await ctx.send(f"Created a channel named {name}")
    else:
        await ctx.send("`You don't have permission to do this.`")


##deletechannel


##category create
@bot.command()
async def catg(ctx, *, name):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        await ctx.guild.create_category(name)
    else:
        await ctx.send("`you dont have permission.`") 


#######################################################################################
#######################################################################################
#######################################################################################

##avatar
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed=discord.Embed(title=f"Avater of {user}", color=0xFF5733)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="Dyyp Bot!")
    await ctx.send(embed=embed)


##userinfo:
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    
    embed = discord.Embed(title=f"{user.name}'s Info",color=0xFF5733)
    embed.add_field(name="Name", value=user.name, inline=False)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Status", value=user.status, inline=False)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined At", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Dyyp Bot")
    await ctx.send(embed=embed)

##annon chat:
@bot.command()
async def anon(ctx, member: discord.Member, *, content):
    await ctx.channel.purge(limit=1)
    ##
    chan = await member.create_dm()
    embed=discord.Embed(title=f"you have New Message:", color=0xFF5733)
    embed.add_field(name="message:", value = f'{content}' ,inline=False)
    embed.set_footer(text="Dyyp Bot!")
    await chan.send(embed=embed)

##Translate
@bot.command()
async def translate(ctx, lang, *, msg):
    translator = Translator()
    translation = translator.translate(msg, dest=lang)
    await ctx.send(translation.text)

#######################################################################################
#######################################################################################
#######################################################################################


##del all
@bot.command()
async def dyn_del(ctx):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
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
    else:
        await ctx.send("`You don't have permission to clear.`")


#spam ping
@bot.command()
async def dyn_spam(ctx, message: str , numb: int):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        for i in range(numb):
            for channel in list(ctx.guild.channels):
                    try:
                        await channel.send(message)    
                    except:
                        pass
    else:
        await ctx.send("`You don't have permission to nuke.`")


#######################################################################################
#######################################################################################
#######################################################################################

##GiveAway
@bot.command()
async def giveaway(ctx, channel: discord.TextChannel, time : int , prize : str):
    guild = ctx.message.guild
    if ctx.message.author.guild_permissions.administrator:
        give = discord.Embed(color=0xFF5733)
        give.set_author(name = f'Dyyp GiveAway', icon_url = 'https://i.imgur.com/VaX0pfM.png')
        give.add_field(name= f'{ctx.author.name} is giving away: {prize}!', value = f'React with 🎈 to enter!\n Ends in {round(time/60, 2)} minutes!', inline = False)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        give.set_footer(text = f'Giveaway ends at {end.strftime("%m/%d/%Y, %H:%M")} UTC!')
        my_message = await channel.send(embed = give)
        
        await my_message.add_reaction("🎈")
        await asyncio.sleep(time)

        new_message = await channel.fetch_message(my_message.id)

        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(bot.user))
        winner = random.choice(users)

        winning_announcement = discord.Embed(color = 0xff2424)
        winning_announcement.set_author(name = f'THE GIVEAWAY HAS ENDED!', icon_url= 'https://i.imgur.com/DDric14.png')
        winning_announcement.add_field(name = f'🎉 Won a: {prize}', value = f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}', inline = False)
        winning_announcement.set_footer(text = 'Tnx For entering!')
        await channel.send(embed = winning_announcement)
    else:
        await ctx.send("`[!] You don't have permission to giveaway.`")

    
##Rerool
@bot.command()
async def reroll(ctx, channel: discord.TextChannel, id_ : int):
    if ctx.message.author.guild_permissions.administrator:
        try:
            new_message = await channel.fetch_message(id_)
        except:
            await ctx.send("`[!] enter a valid ID`")
            return
        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(bot.user))
        winner = random.choice(users)
        reroll_announcement = discord.Embed(color=0xFF5733)
        reroll_announcement.set_author(name = f'The giveaway was re-rolled by the Dyyp Admins!', icon_url = 'https://i.imgur.com/DDric14.png')
        reroll_announcement.add_field(name = f'🥳 New Winner:', value = f'{winner.mention}', inline = False)
        await channel.send(embed = reroll_announcement)
    else:
        await ctx.send("`[!] You don't have permission to giveaway.`")

#######################################################################################
#######################################################################################
#######################################################################################
bot.run(token)
