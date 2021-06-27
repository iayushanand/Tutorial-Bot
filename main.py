from attr import __description__
import discord,random,DiscordUtils,datetime,asyncio,json
from discord import client
from discord.ext import commands, tasks
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from datetime import datetime

with open('config.json','rb') as f:
    data =  json.load(f)

    token=data["TOKEN"]
    prefix=data["PREFIX"]



intents=discord.Intents.all()
intents.members=True
intents.presences=True

client=commands.Bot(command_prefix=prefix,intents=intents)
tracker = DiscordUtils.InviteTracker(client)

@client.event
async def on_ready():
    print(f'{client.user.name} is now Online')
    logs.start()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f'in {len(client.guilds)}servers with {len(client.users)} memebers!'))



@client.event
async def on_member_join(member):
    inviter = await tracker.fetch_inviter(member)
    channel= client.get_channel(826387689472917515)
    wel = Image.open('red.jpg')
    asset=member.avatar_url_as(size=128)
    data=BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.resize((128,128))
    wel.paste(pfp,(18,118))

    name = f'Name: {member.name}#{member.discriminator}'
    server=f'Welcome to {member.guild.name}'
    memid=f'Id: {member.id}'
    invite=f'Invited by: {inviter}'
    accc=f'Acc Date: {member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}'
    mc=f'We are now {member.guild.member_count} members Strong!'

    font1 = ImageFont.truetype('font.otf',48)
    font2 = ImageFont.truetype('font.otf',24)

    draw = ImageDraw.Draw(wel)
    draw.text((168,97), server, (255,255,255), font=font1)
    draw.text((168,148), name, (255,255,255), font=font2)
    draw.text((168,173), memid, (255,255,255), font=font2)
    draw.text((168,196), invite, (255,255,255), font=font2)
    draw.text((168,222), accc, (255,255,255), font=font2)
    draw.text((168,246), mc, (255,255,255), font=font2)



    wel.save('wel.png')
    await channel.send(f'{member.mention}')
    await channel.send(file=discord.File('wel.png'))


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@client.command()
@commands.has_permissions(manage_nicknames=True)
async def setnick(self, ctx, member:discord.Member,*,nick=None):
    old_nick = member.display_name

    await member.edit(nick=nick)

    new_nick = member.display_name

    await ctx.send(f'Changed nick from *{old_nick}* to *{new_nick}*')
    
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(self,ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

    embed=discord.Embed(title=f'🔒 Locked',description=f'Reason: {reason}')

    await channel.send(embed=embed)

@commands.command()
@commands.has_permissions(manage_channels=True)
async def unlock(self,ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed=discord.Embed(title=f'🔓 Unlocked',description=f'Reason: {reason}')
    await channel.send(embed=embed)









# 837215080411168768
# <a:hey:853159656246476810>


# 798887148509593600 : Rules
# 826387689472917515 : Chat





# @client.event
# async def on_member_join(member):
#     channel = client.get_channel(837215080411168768)

#     em=discord.Embed(
#         title=f'Welcome',
#         description=f'{member.mention} Joined {member.guild.name}',
#         color=discord.Color.random(),
#         timestamp=datetime.utcnow()
#         ).add_field(
#         name=f'<a:hey:853159656246476810> Rules',
#         value=f'<#798887148509593600>'
#         ).add_field(
#         name=f'<a:hey:853159656246476810> Chat',
#         value='<#826387689472917515>'
#         ).add_field(
#         name=f'Total members',
#         value=f'{member.guild.member_count}'
#         ).set_footer(text=f'{member.name} just joined')

#     await channel.send(embed=em)


message = 0



# @client.event
# async def on_message(msg):
#     global message
#     message+=1

#     await client.process_commands(msg)









# @client.command(aliases=['av'])
# async def avatar(ctx,member:discord.Member):
#     if not member:
#         member=ctx.author

#     icon=member.avatar_url

#     em=discord.Embed(
#         ).set_image(
#         url=icon).set_author(
#         name=f'{member.name}#{member.discriminator}',
#         icon_url=icon)

#     await ctx.send(embed=em)










@client.command(aliases=['av'])
async def avatar(ctx,member:discord.Member=None):
    if not member:
        member=ctx.author

    icon=member.avatar_url
    em=discord.Embed(title='Avatar',color=0x123456,
        timestamp=datetime.utcnow()).set_author(
        name=f'{member.name}#{member.discriminator}',icon_url=icon).set_image(
        url=icon)

    await ctx.send(embed=em)



@client.command(aliases=['sm'])
async def slowmode(ctx,sec:int=None,channel:discord.TextChannel=None):
    if not sec:
        sec=0
    if not channel:
        channel=ctx.channel

    await channel.edit(slowmode_delay=sec)

    await channel.send(f'This channel is now on **{sec}s** slowmode')





# from random import *

# @client.command(aliases=['cd'])
# async def countdown(ctx,time:int=None):
#     if not time:
#         msg=await ctx.send('Please enter seconds between 0-60')

#         def check(message):
#             return message.author==ctx.author and message.channel==ctx.channel
#         try:
#             msg1 = await client.wait_for('message',check=check,timeout=10.0)
#         except asyncio.TimeoutError:
#             return await ctx.send("**Timeout!** Please try again later")

#         else:
#             time=int(msg1.content)

#     else:
#         pass

#     if time<0 or time>60:
#         await ctx.send('Limit of 0-60s exceeded!')

#     else:
#         await ctx.send(f'{time}s')






from random import *

@client.command(aliases=['cd'])
async def countdown(ctx,time:int=None):
    if not time:
        await ctx.send('Enter time between 0-60s')

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        try:
            msg1 = await client.wait_for('message',check=check,timeout=10)

        except asyncio.TimeoutError:
            return await ctx.send('**Timeout!** Limit of 10s exceeded')

        else:
            time=int(msg1.content)

    if time<0 or time>60:
        await ctx.send('Time must be between 0-60 seconds')

    else:
        msg2=await ctx.send(f'{time}s')
        while time>0:
            time-=1
            await asyncio.sleep(1)
            await msg2.edit(content=f'{time}s')

        await ctx.send(f'{ctx.author.mention} Countdown Completed!')









# @client.command(aliases=['em'])
# async def embed(ctx,color=ffffff):
#     print(color)
#     msg=await ctx.send('Please provide your message with 60s')

#     def check(message):
#         return message.author==ctx.author and message.channel==ctx.channel
#     try:
#         msg1 = await client.wait_for('message',check=check,timeout=60)

#     except asyncio.TimeoutError:
#         await msg.delete()
#         await ctx.send('Timeout!',delete_after=5.0)

#     else:
#         msag=msg1.content

#     em=discord.Embed(timestamp=datetime.utcnow(),
#         color=color).set_author(
#         name=f'{ctx.author.name}#{ctx.author.discriminator}',
#         icon_url=f'{ctx.author.avatar_url}').add_field(name=' ',
#         value=f'{msag}')

#     await msg.delete()
#     await ctx.send(embed=em)



























































































# @client.event
# async def on_member_update(before,after):
#     role = before.guild.get_role(808896036395286528)

#     if role not in before.roles:
#         if role in after.roles:
#             channel = client.get_channel(826387689472917515)

#             em=discord.Embed(
#                 color=0xff00de,
#                 timestamp=datetime.utcnow()
#             ).add_field(
#                 name='Boost Incoming!',
#                 value=f'Thanks for boosting {after.mention}'
#             ).set_footer(text=f'We have now {str(after.guild.premium_subscription_count)} boost')
    
#             await channel.send(embed=em)




@tasks.loop(seconds=60)
async def logs():
    global message
    with open('logs/msg.txt','a') as f:
        try:
            f.write(f'{datetime.utcnow()} : {message}\n')
            message = 0
        except Exception as e:
            message = 0
            print(e)


client.run(token)