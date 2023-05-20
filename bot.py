import discord
from discord.ext import commands

import asyncpg
from config import *

import time


bot = commands.Bot(
    command_prefix=".",
    intents=discord.Intents.all(),
)


bot.db = None


async def setup_db() -> asyncpg.Connection:
    bot.db = await asyncpg.connect(dsn=postgres)
    await bot.db.execute(
        """
        CREATE TABLE IF NOT EXISTS afk(
            user_id BIGINT,
            reason TEXT,
            afk_time BIGINT
        )
    """
    )  # user_id, reason, afk_time


@bot.event
async def on_ready():
    print("Bot Logged in!")
    await setup_db()


@bot.command(name="afk")
async def afk(ctx: commands.Context, reason: str = None):
    user_id = ctx.author.id
    reason = reason or "AFK"
    afk_time = int(time.time())
    res = await bot.db.fetch("SELECT afk_time FROM afk WHERE user_id = $1", user_id)
    if len(res) != 0:
        return await ctx.reply("You are already afk")
    await bot.db.execute(
        "INSERT INTO afk VALUES($1, $2, $3)", user_id, reason, afk_time
    )
    await ctx.reply("I set your afk!")


@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot:
        return
    user = msg.author
    res = await bot.db.fetch("SELECT afk_time FROM afk WHERE user_id = $1", user.id)
    if len(res) != 0:
        await bot.db.execute("DELETE FROM afk WHERE user_id = $1", user.id)
        await msg.reply("Welcome back! I removed your afk.")
        return
    if msg.mentions:
        for mention in msg.mentions:
            res = await bot.db.fetch(
                "SELECT afk_time, reason FROM afk WHERE user_id = $1", mention.id
            )
            if len(res) != 0:
                afk_time = res[0].get("afk_time")
                reason = res[0].get("reason")
                await msg.reply(
                    f"`{mention.display_name}` is AFK: {reason} (<t:{afk_time}:R>)"
                )
                break

    await bot.process_commands(msg)


bot.run(token=token)
