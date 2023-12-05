import discord
from discord.ext import commands

import button_paginator as pg

bot = commands.Bot(intents = discord.Intents.all(), command_prefix=",")


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")


@bot.command()
async def page(ctx: commands.Context):
    embeds = [
        "This is a text",
        discord.Embed(
            title = "Embed - 1"
        ),
        discord.Embed(
            title = "Embed - 2"
        ),
        discord.Embed(
            title = "Embed - 3"
        ),
        discord.Embed(
            title = "Embed - 4"
        )
    ]
    paginator = pg.Paginator(bot, embeds, ctx)
    # paginator.default_pagination()
    paginator.add_button("prev", emoji = "◀")
    paginator.add_button("goto")
    paginator.add_button("lock", emoji = "❎", style = discord.ButtonStyle.red)
    paginator.add_button("next", emoji = "▶")
    await paginator.start()


bot.run("ODMyODk5Mjc5MDQyMzc5Nzc2.G7rE34.JUJtbpQYZsUl0eEMvj2iJuThr3YLRT_vDVmvlA")