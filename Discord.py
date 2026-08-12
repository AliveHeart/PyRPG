from TokenAPI import Discord_Token
import game, loader
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv(Discord_Token)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('👋 Hello! am PyRPG!.')

@bot.command()
async def look(ctx):
    result = game.game.run("look", ctx.author.id)
    new_text = ""
    for text in result:
        new_text += " " + text
    await ctx.send(new_text)


bot.run(TOKEN)
