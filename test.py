import discord
from discord.ext import commands

token = 'TOKEN HERE'


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f"logged in as {client.user}")


@client.command(name='test')
async def test(ctx):
    await ctx.send("command test")


client.run(token)