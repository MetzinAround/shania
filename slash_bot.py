import discord
from discord import app_commands 
import bot_config as conf

token = conf.secret_token
guild_id = conf.guild_id

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn"t sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=guild_id)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

#name is the command to use, description shows up in the slash command list
@tree.command(guild = discord.Object(id=guild_id), name = "shania", description="Bup baaaa dudada bup bup") 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Let's go girls...") 

@tree.command(guild = discord.Object(id=guild_id), name = "impress", description="find out if Shania is impressed")
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"That don't impress me much...")

client.run(token)


