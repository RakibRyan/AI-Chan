#Ai-chan Discord bot
#Name ideas
#Tinker,bolt,roberto,rust,core,Ava,Myrai,Echo,Enzo,

import discord
import os
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

# bot is live

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


#member events

@client.event 
async def on_member_join(member):
  print(f'{member} has joined the server')

@client.event 
async def on_member_remove(member):
  print(f'{member} has left the server')

@client.event 
async def on_member_ban(member):
  print(f'{member} has been banned from the server')

@client.event 
async def on_member_unban(member):
  print(f'{member} is now unbanned')

@client.event 
async def member_update(member):
  print(f'{member} has updated profile')

# Event commands

@client.command()
async def ping(ctx):
  Latency = round(client.latency * 1000)
  await ctx.send(f'pong! [{Latency} ms]')
  print(f'ping: [{Latency}]ms')


@client.command(aliases=['hi', 'hola'])
async def hello(ctx):
  await ctx.send('hello')
 

# Function commands

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

client.run(os.environ['Discord_Token'])
