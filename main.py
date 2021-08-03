import discord
import os
from discord.colour import Color
import requests
import json
import random
from sys import argv
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from discord.ext import commands
from discord_slash.utils.manage_commands import create_option

client = commands.Bot(command_prefix = '.')
slash = SlashCommand(client, sync_commands=True)

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q']+ " -" + json_data[0]['a']
    return(quote)

guild_ids = [871955836396781598, 769060032582516746]
@slash.slash(name="motivate", description="Shows a motivational quote", guild_ids = guild_ids)
async def on_motivate_command(ctx):
    await ctx.defer()
    await ctx.send(content=get_quote())

@slash.slash(name="ping", description="Shows the ping", guild_ids = guild_ids)
async def on_motivate_command(ctx):
    await ctx.send(content=f'{round(client.latency*1000)}ms')

@slash.slash(name="shutdown", description="Shuts down", guild_ids = guild_ids)
async def on_motivate_command(ctx):
	await ctx.send(content="Shutting down")
	await client.close()

responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']

@slash.slash(name="8ball", description="never gonna give you up", options=[
               create_option(
                 name="question",
                 description="The Question tm",
                 option_type=3,
                 required=True
               )
             ], guild_ids = guild_ids)
async def on_motivate_command(ctx, question: str):
    await ctx.defer()
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

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
    print('{0.user}, Indeed.'.format(client))

@client.command()
async def motivate(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['user', 'info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title = member.name, description = member.mention)
    embed.add_field(name="ID", value=member.id, inline=True)
    await ctx.send(embed=embed)

token = os.environ.get('TOKEN')
client.run(token)
