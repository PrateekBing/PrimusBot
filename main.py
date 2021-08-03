import discord
import os
import requests
import json
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+ " -" + json_data[0]['a']
  return(quote)




@client.event
async def on_ready():
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
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

token = os.environ.get('TOKEN')
client.run(token)