import discord, requests
from discord.ext import commands
from bs4 import BeautifulSoup
from xkcd import comic
from astropic import astropic


rss_url = 'https://manga4life.com/rss/Onepunch-Man.xml'
res = requests.get(rss_url)
soup = BeautifulSoup(res.text, features="xml")

title = soup.item.title.text
link = soup.item.link.text
image_url = soup.image.url.text

token = '[BOT TOKEN HERE]'


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)



@client.event
async def on_ready():
    print(f"logged in as {client.user}")




@client.command(name='test')
async def test(ctx):
    await ctx.send(content="test")




@client.command(name='pic')
async def pic(ctx):
    picture = discord.File("images/aglet.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://images/aglet.png")
    await ctx.send("AGLET", file=picture, embed=embed)



@client.command(name="chapter")
async def chap(ctx):
    embed = discord.Embed(
        title=title,
        url=link,
        color= discord.Colour.fuchsia(),
        description="it's punchin' time"
    )
    embed.set_thumbnail(url=image_url)
    #embed.set_author(name="Yusuke Murata")
    await ctx.send(embed=embed)



@client.command(name="here")
async def there(ctx):
    channels = discord.abc.GuildChannel.name
    print(channels)



@client.command(name="xkcd")
async def xkcd(ctx, extras=None):
    title = comic(extras)
    if title.startswith("Issue number #"):
        await ctx.send(title)
        return
    picture=discord.File("images/xkcd.jpg")
    await ctx.send(title, file=picture)



@client.command(name="astropic")
async def astropix(ctx, extras="today"):
    explan = astropic(extras)
    embed = discord.Embed(description=explan)

    if explan.startswith("This day did not have an astropic."):
        await ctx.send(embed=embed)
        return

    picture = discord.File("images/astropic.jpg")
    await ctx.send(file=picture, embed=embed)



client.run(token)