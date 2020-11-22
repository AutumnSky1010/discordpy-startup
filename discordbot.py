import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content==('こんばんは'):
        await message.channel.send('こんばんは!!')

client.run(token)
