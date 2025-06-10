import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "everyone" in message.content.lower():
        await message.channel.send("何してるんですか！？勇気出して全体メンションしてください！！")
        print(f"Detected 'everyone' from {message.author}: {message.content}")

client.run(TOKEN)
