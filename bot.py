import game, loader
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def exe_cmd(command):
    result = game.game.run(command, 1)#ctx.author.id)
    new_text = ""
    for text in result:
        new_text += " " + text
    return new_text

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('👋 Hello! am PyRPG!.')

@bot.command()
async def look(ctx):
    await ctx.send(exe_cmd("look"))

@bot.command()
async def go(ctx, location: str):
    await ctx.send(exe_cmd("go " + location))

@bot.command()
async def inv(ctx):
    await ctx.send(exe_cmd("inventory"))

@bot.command()
async def fight(ctx, enemy:str):
    await ctx.send(exe_cmd("fight " + enemy))

@bot.command()
async def attack(ctx):
    await ctx.send(exe_cmd("attack"))

@bot.command()
async def defend(ctx):
    await ctx.send(exe_cmd("defend"))

@bot.command()
async def run(ctx):
    await ctx.send(exe_cmd("run"))

@bot.command()
async def kill(ctx):
    await ctx.send(exe_cmd("kill"))

@bot.command()
async def spare(ctx):
    await ctx.send(exe_cmd("spare"))


bot.run(TOKEN)
