import discord
import asyncio
from datetime import datetime
# importing essentials

bot=discord.Bot(activity=discord.Activity(type=discord.ActivityType.watching,name="Ayu's Subscribers"))
# declaring bot

@bot.event # creating on_ready event
async def on_ready():
    print(f"{bot.user.name} Logged In!")


@bot.command(guild_ids=[798880389904203797],name="ping",description="""Return Bot's Latency""") #normal ping cmd, make sure to add your guild ids...
async def ping(ctx):
    await ctx.respond(f"**Pong!**\nLatency: {round(bot.latency*1000)}ms",ephemeral=True)

@bot.command(guild_ids=[798880389904203797],description="""Creates a new ticket""") # creating <new> command, use it by writing /new <reason>, I will tell you the use of reason later! make sure u have application.commands scope turned on while inviting the bot
async def new(ctx,reason):
    await ctx.respond("Hold up! working on your request",ephemeral=True)
    categ=discord.utils.get(ctx.guild.categories,name="OPENED TICKETS") # selecting the category(by its name)
    for ch in categ.channels: # using for loop to go through all channels in that category
        if ch.topic==str(ctx.author.id): # checking if author already have a ticket in there, as we added their id as topic
            return await ch.send(f"{ctx.author.mention}! You already have a ticket here!") # if they have ticket, then mentioning them
    r1=ctx.guild.get_role(798881589055717376)
    overwrite={
        ctx.guild.default_role:discord.PermissionOverwrite(read_messages=False),
        ctx.me:discord.PermissionOverwrite(read_messages=True),
        ctx.author:discord.PermissionOverwrite(read_messages=True),
        r1:discord.PermissionOverwrite(read_messages=True)
        } #creating overwrites/permission for channel
    channel=await categ.create_text_channel(name=f"{ctx.author.name}-{ctx.author.discriminator}",overwrites=overwrite,topic=f"{ctx.author.id}") # creating the channel/ticket
    em=discord.Embed(title="New Ticket Created!",
                        description=f"Ticket created by {ctx.author.mention}",
                        timestamp=datetime.utcnow(),
                        color=discord.Color.random())

    await asyncio.sleep(3)

    await ctx.respond(f"{channel.mention} click to go to ticket",ephemeral=True)
    await channel.send(embed=em)


# running the bot
bot.run("TOKEN")
