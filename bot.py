# This example requires the 'message_content' intent.

import discord
import bot_config as conf

intents = discord.Intents.default()
intents.message_content = True
