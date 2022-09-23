import discord

token = 'TOKEN HERE'


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f"logged in as {client    .user}")

@client.event
async def on_message(message):
    print(client.get_channel(id))
    print(f"message sent by {message.author}: {message.content}")
    if message.author == client.user:
        return
    else:
        await message.channel.send("hi, this is a test message!")

client.run(token)