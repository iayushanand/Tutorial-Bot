@client.event
async def on_member_join(member):
    channel = client.get_channel(837215080411168768)

    em=discord.Embed(
        title=f'Welcome',
        description=f'{member.mention} Joined {member.guild.name}',
        color=discord.Color.random(),
        timestamp=datetime.utcnow()
        ).add_field(
        name=f':hey: Rules',
        value=f'<#798887148509593600>'
        ).add_field(
        name=f':hey: Chat',
        value='<#826387689472917515>'
        ).add_field(
        name=f'Total members',
        value=f'{member.guild.member_count}'
        ).set_footer(text=f'{member.name} just joined')

    await channel.send(embed=em)
