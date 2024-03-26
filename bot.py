# This example requires the 'message_content' intent.

import discord
import bot_config as conf

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return 

    if "$shania" in message.content.lower():
        await message.channel.send("Let's Go Girls")
        return

    if "$impress" in message.content.lower():
        await message.channel.send("That don't impress me much")
        return

client.run(conf.secret_token)
