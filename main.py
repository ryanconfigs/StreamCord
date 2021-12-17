import discord
import requests
import os 
import sys
import json

from discord.ext import commands, tasks

with open('Settings.json') as f:
	load = json.load(f)

token = load.get('token')
prefix = load.get('prefix')

client = commands.Bot(command_prefix=prefix, self_bot=True)

@client.event
async def on_connect():
	os.system('title Github.com/3kv <3')
	print(f'''
	Name : {client.user}
	ID : {client.id}
	Prefix : {prefix}

	Github.com/3kv <3
	''')

@client.command()
async def streaming(ctx, *, message):

	await ctx.message.delete()
	
	await client.change_presence(activity=discord.Streaming(name=message, url='https://twitch.tv/omgbeete'))

@client.command()
async def playing(ctx, *, message):
	
	await ctx.message.delete()
	
	await client.change_presence(activity=discord.Game(name=message))


@client.command()
async def listening(ctx, *, message):
	
	await ctx.message.delete()
	
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))


@client.command()
async def watch(ctx, *, message):
	
	await ctx.message.delete()
	
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))

if __name__ == '__main__':
	try:
		client.run(token, bot=False)
	except:
		print('Invalid token!')
		os.system('pause>nul')