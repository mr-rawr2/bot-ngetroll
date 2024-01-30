import discord
from discord.ext import commands
from projec import gen_pass, sampah_organik, sampah_anorganik
import random,os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} use $for command')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def password(ctx):
    await ctx.send('berikut password untukmu')
    await ctx.send(gen_pass())

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times = 10, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def command(ctx):
    """meme"""
    await ctx.send('the command is: on_ready, hello, password, joined, repeat(text), _bot, meme_random, command and alwyas using $ for command')

@bot.command()
async def bye(ctx):
    """bye"""
    await ctx.send('have a good day')

@bot.command()
async def meme(ctx):
    gambar = random.choice(os.listdir('images'))
    with open(f'images/{gambar}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def animals(ctx):
    hewan = random.choice(os.listdir('animalia'))
    with open(f'animalia/{hewan}', 'rb') as f:
        pic = discord.File(f)

    await ctx.send(file=pic)

@bot.command()
async def organik(ctx):
    sampah = ""
    for i in sampah_organik:
        i = i+'\n'
        sampah += i
        await ctx.send('berikut  daftar sampah organik')
        await ctx.send(sampah)

@bot.command()
async def anorganik(ctx):
    sampah2 = ""
    for i in sampah_anorganik:
        i = i+'\n'
        sampah2 += i
        await ctx.send('berikut  daftar sampah anorganik')
        await ctx.send(sampah2)



bot.run("MTE5NDI2NTA0ODQ3OTE3MDY2MQ.GE0smJ.Fzfaz2VEw0X7W3yhUSHfWeckXOCOKD6lw-_R5Q")

