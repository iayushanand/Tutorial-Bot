import discord, datetime, asyncio
from discord.ext import commands
from datetime import datetime

class Embed(commands.Cog):
	"""docstring for Embed"""
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener
	async def on_ready():
		print('Embed.py loaded!')

	@commands.command(aliases=['em'])
	async def embed(self,ctx,*,msg=None):
		if not msg:
			await ctx.send('Enter message withing 30s')

			def check(message):
				return message.author == ctx.author and message.channel == ctx.channel

			try:
				mes=await self.client.wait_for('message',check=check,timeout=30.0)
			except asyncio.TimeoutError:
				await ctx.send('Timeout! Please be quicker next time.')
			else:
				msg=mes.content

		em=discord.Embed(
			description=f'{msg}',
			timestamp=datetime.utcnow(),
			color=discord.Color.random()).set_author(
			name=f'{ctx.author.name}#{ctx.author.discriminator}',
			icon_url=f'{ctx.author.avatar_url}')

		await ctx.send(embed=em)

def setup(client):
	client.add_cog(Embed(client))
