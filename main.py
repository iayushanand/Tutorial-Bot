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
