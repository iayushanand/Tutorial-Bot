@client.command()
@commands.has_permissions(manage_nicknames=True)
async def setnick(ctx, member:discord.Member,*,nick=None):
    old_nick = member.display_name

    await member.edit(nick=nick)

    new_nick = member.display_name

    await ctx.send(f'Changed nick from *{old_nick}* to *{new_nick}*')
    
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

    embed=discord.Embed(title=f'🔒 Locked',description=f'Reason: {reason}')

    await channel.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed=discord.Embed(title=f'🔓 Unlocked',description=f'Reason: {reason}')
    await channel.send(embed=embed)
