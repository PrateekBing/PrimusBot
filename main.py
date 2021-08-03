import discord
import os
import requests
import json
from sys import argv
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+ " -" + json_data[0]['a']
    return(quote)

guild_ids = [849555538102583316]
#, create_permission(699945276156280893, SlashCommandPermissionType.USER, False)
@slash.slash(name="motivate", description="Shows a motivational quote", guild_ids = guild_ids)
async def on_motivate_command(ctx):
    await ctx.send(content=get_quote())

@slash.permission(permissions=[create_permission(732224469543944242, SlashCommandPermissionType.USER, False)])
@slash.slash(name="shutdown", description="Shuts down", guild_ids = guild_ids)
async def on_motivate_command(ctx):
	await ctx.send(content="Shutting down")
	await client.close()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$motivate'):
        quote = get_quote()
        await message.channel.send(quote)

token = os.environ.get('TOKEN')
client.run(token)
