import discord
from discord.ext import commands

import google.generativeai as genai


bot = commands.Bot(command_prefix = ">", intents = discord.Intents.all())

genai.configure(api_key="your-api-key")

model = genai.GenerativeModel('gemini-pro',
	safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
	]
	)


@bot.event
async def on_ready():
	print(f"Logged in as: {bot.user.name}!")


@bot.command(name = "askai")
async def askai(ctx: commands.Context, *, prompt: str):
	response = model.generate_content(prompt)

	await ctx.reply(response.text)

bot.run("discord-bot-token")
