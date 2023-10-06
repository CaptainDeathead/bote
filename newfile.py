

import discord

from discord.ext import commands

 

# define your bot's token here

token = 'your_bot_token'

 

# create an instance of the bot

bot = commands.bot(command_prefix='!')

 

# define a simple command

@bot.command(name='hello')

async def hello(ctx):

    await ctx.send('hello, world!')

 

# event handler for when the bot is ready

@bot.event

async def on_ready():

    print(f'logged in as {bot.user.name}')

 

# run the bot

if __name__ == '__main__':

    try:

        bot.run(token)

    except exception as e:

        print(f'an error occurred while running the bot: {e}')

