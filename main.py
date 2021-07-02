#import modules
import discord
from dscord.ext import commands

# input token, prefix and extensions
token='bot_token'
prefix='prefix
ext=['cogs.embed']

# create a client
client=commands.Bot(command_prefix=prefix)

#load extensions
for e in ext:
    client.load_extension(e)

# run client
client.run(token)
