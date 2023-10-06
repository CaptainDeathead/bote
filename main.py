from keep_alive import keep_alive
import discord
import os 
from discord.ext import commands
import random
import discord
import random
from discord import FFmpegPCMAudio

import chess
import engine
import utils
import asyncio
import flask
from threading import Thread
import requests
import json
import datetime
import pytz
import wavelink
import math
from random import randint
from replit import db
import re
import youtube_dl
import json
import asyncio
import matplotlib.pyplot as plt

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)
 

@bot.event

async def on_ready():
    game = discord.Game("Sex With Hitler 2077")
    await bot.change_presence(status=discord.Status.online, activity=game)
  
    try:

      synced = await bot.tree.sync()
      print(f"Synced {len(synced)} command(s)")

    except Exception as e:

      print(e)
    bot.loop.create_task(node_connect())

#first version release version 1.0 


@bot.tree.command(name="goodbye")
async def goodbye(interaction: discord.Interaction):
  await interaction.response.send_message("Goodbye! I hope you have a great rest of your day!")

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message("Hello! How are you today! 🙂")

@bot.tree.command(name="who-creator")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("My creator is Osama Bin Collection he also goes by Ruxless and Big Booty Latinas")

#update 1.1 release.
#added 3 slash commands

@bot.tree.command(name="vote-for")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("You should vote for the Osama Bin Collection and Slotho101 coalition the MLU or the mindoor liberal union for a reliable, strong and fair future.")

@bot.tree.command(name="how-are-you")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("Im doing great today, thanks for asking. How are things with you?")

@bot.tree.command(name="kill-yourself")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("I appriciate this message, thank you for telling me to keep myself safe, this means alot!")

# update 1.2 release.
#added 5 slash commands

@bot.tree.command(name="september")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("September 11 attacks. September 11 attacks, also called 9/11 attacks, series of airline hijackings and suicide attacks committed in 2001 by 19 militants associated with the Islamic extremist group al-Qaeda against targets in the United States, the deadliest terrorist attacks on American soil in U.S. history.")

@bot.tree.command(name="who-helped-in-project")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("While working on this bot, I was helped by Yesn't and CaptainDeathead to fix bugs and make the first realease.")

@bot.tree.command(name="asian-parent")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("YOU FALIURE, COUSIN JIMMY IS ONLY 3 AND HE BETTER THEN YOU. HE HAVE DOCTORATE YOU HAVENT GOTTEN A+++++. YOU STUUUUPID. YOU DUMB. YOU WASTE OF AIR FALIURE.")

@bot.tree.command(name="current-version")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("This bot is currently on version 1.15 as of 7/9/23.")

@bot.tree.command(name="did-epstein-kill-himself")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("Jeffery epstein did not kill himself.")

#update 1.3 release.
#added 3 slash commands

@bot.tree.command(name="sponser")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("This bot is proudly sponsered by Raid Shadow Legends. Raid shadow legends is a free MMO RPG game free on the apple app store and google play store available on all phones. You can claim up to 15000 gold if you sign up using my creator code BigBootyLatinas to gain a head start and beat your opponents.")

@bot.tree.command(name="countries-of-the-world")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("https://youtu.be/x88Z5txBc7w?si=q_F4He5AdN_C-KSZ")

#update 1.3.1 patch
#spelling mistake

@bot.tree.command(name="best-country")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("The best country in the world is The United Kingdom of Great Britain and Northern Ireland")

@bot.tree.command(name="god-save-our")
async def god(interaction: discord.Interaction):
  await interaction.response.send_message("gracious King. Long live our noble King. God save the King.Send him victorious, Happy and glorious, Long to reign over us, God save the King. Thy choicest gifts in store. On him be pleased to pour, Long may he reign. May he defend our laws, And ever give us cause, To sing with heart and voice, God save the King.")

@bot.tree.command(name="who-is-the-best-kitty")
async def god(interaction: discord.Interaction):
  await interaction.response.send_message("TONY is the goodest kitty around. TONY is life.")


#update 1.11.1
#god save the king

@bot.tree.command(name="god-save-the-king")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("God save our gracious King. Long live our noble King. God save the King.Send him victorious, Happy and glorious, Long to reign over us, God save the King. Thy choicest gifts in store. On him be pleased to pour, Long may he reign. May he defend our laws, And ever give us cause, To sing with heart and voice, God save the King.")



#update 1.4 release
#added former british colonies command


# A list of former British colonies and their colonial names
former_british_colonies = {
    'united States': 'british america',
    'canada': 'british north america',
    'australia': 'the commonwealth of australia',
    'new zealand': 'auckland island',
    'india': 'british raj',
    'pakistan': 'british india',
    'bangladesh': 'east bengal',
    'nigeria': 'nigerian protectorate',
    'kenya': 'british east africa',
    'ghana': 'gold coast',
  'sudan': 'anglo-egyptian sudan',
  'lesotho': 'basutoland',
  'botswana': 'botswana',
  'brunei': 'british borneo',
  'uganda': ' british east africa',
  'egypt': 'british egypt',
  'belize': 'british honduras',
  'malaysia': 'british malaya',
  'somalia': 'british somaliland',
  'togo': 'british togoland',
  'sri lanka': 'ceylon',
  'israel': 'palestine protectorate',
  'zambia': 'northern rhodesia',
  'zimbabwe': 'southern rhodesia',
  'wa': 'the swan river colony',
  'western australia': 'the swan river colony',
  'tanzania': 'tanganyika territory',
  'usa': 'the thirteen colonies',
  'singapore': 'the straits settlements',
  'borneo': 'straits settlements',
  'new south wales': 'the colony of new south wales',
  'nsw': 'the colony of new south wales',
  'kiribati': 'gilbert and Ellice Islands',
  'tuvalu': 'gilbert and Ellice Islands',
  'jordan': 'emirate of Transjordan',
  'gambia': 'the colony and protectorate of gambia'
}

#update 1.5 release
#https://uptimerobot.com/dashboard?ref=website-header#mainDashboard
#https://discord-bot-main.lachlanorourke.repl.co
#keep alive framework added
#always on added

#update 1.7
# quiz added
# update 1.7.1
# Quiz fixed

@bot.tree.command(name="quiz")
async def quiz(interaction: discord.Interaction):
  questions_and_answers = {
  "what is the capital of the uk": "london",
  "what is the name of the current US president": "joe biden",
  "what is the chemical formula for water": "h2O",
  "what year did ww2 start": "1939",
  "where was the nuclear bomb originally intended to be dropped on": "germany",
  "who was the prime minister after boris johnson": "liz truss",
  "who shat his pants at an engadine mc donalds in 1997": "scott morrison",
  "which company owns minecraft": ["mojang", "microsoft"],
  "which video game has 3 main protaganists that go by the name of micheal de santa, trevor phillps and franklin clinton": ["gta 5", "gta v"],
  "which home alone 2 background character turned us president got arrested": "trump",
  "What american state is known for incest?": "alabama",
  "what is the kool kids klub also known as": "kkk",
  "which company sent pinkertons to raid a youtubers house because they got magic the gathering cards early": "hazbro",
  "which game on Steam has a similar name to sum in space": "cum in space",
  "what happened to the jar in 1 guy one 1 jar": "it broke",
  "what game was release by a german chancellor that is in the collection called the furer bundle": "sex with hitler",
  "whats your favourite sex position": "missionary",
  "what do you do in the evenings": ["wank", "drink yourself to sleep", "hurt yourself"],
  "whos the best adult movie star": "johnny sins",
  "what does Rascam do on the holidays": "his sister",
  "have you done your homework": ["yes","no",],
      
  }

  question, answers = random.choice(list(questions_and_answers.items()))

  await interaction.response.send_message(question)

  #user_answer = await bot.wait_for("message", check=lambda message: message.author == interaction.user)
  #made it so any user can answer, this may be removed though
  user_answer = await bot.wait_for("message")

  if isinstance(answers, str):
    if user_answer.content.lower() == answers.lower():
        await interaction.channel.send("correct!")
    else:
        await interaction.channel.send(f"{user_answer.content} is incorrect. The correct answer is: {answers}")
  elif isinstance(answers, list):
    if user_answer.content.lower() in map(str.lower, answers):
        await interaction.channel.send("correct!")
    else:
      correct_answers = ", ".join(answers)
      await interaction.channel.send(f"{user_answer.content} is incorrect. The correct answers are: {correct_answers}")

  else:
    await interaction.channel.send("Error has occured")



#update 1.6
#more commands added
#financial tips moved to random selection

@bot.tree.command(name="never-back-down-never-what")
async def creator(interaction: discord.Interaction):
  await interaction.response.send_message("never give up")


#update 1.8
#different type of commands available
#more finacial tips added
# financial tips moved to random 

@bot.command()
async def examplecommand(ctx):
  await ctx.send("This is an alternative legacy command")



#update 1.9 
#adding a fun facts section

@bot.tree.command(name="facts")
async def quiz(interaction: discord.Interaction):
  facts = [
          "did you know that the population of the earth is about 8 billion people?",
    "The world's deepest point is the Mariana Trench, which is over 11 kilometers deep.",
    "The sun is about 149.6 million kilometers from Earth.",
    "The human brain contains about 100 billion neurons.",
    "The average person blinks about 15 times per minute.",
  'who invented math and why did they add number',
    'is there life after death',
    'who decided whats right or wrong',
    'what is a god',
    'what age should people stop dreaming',
    'how do we know were real',
    'what series of decisions led up to this exact point',
  'why do we exist',
  'what is the meaning of life',
  'do our human accomplishments have a long-term, universal significance, or when the world ends, do we all end with it, including what we’ve achieved',
  'if you punch yourself and it hurts, are you wear or are you strong',
  'if you took a ship and replaced all of its parts until none of the original parts are intact anymore, is it the same ship or a completely different ship',
  'what shape is your field of vision',
  'isn’t good health just a slower rate at which to die',
  'What do they call french kissing in France',
    'every year, over 8 million people die from hunger',
    'there are more slaves to day that at any other point in history',
    '1 in 3 women will experience physical or sexual violence in their lifetime',
    'over 1 million childeren die from malaria every year',
    'the world is facing a biodiversity crisis with millions of species of plants and animals risking extinction',
    'The longest place name in the world is Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu, which is a hill in New Zealand. It translates to The summit where Tamatea, the man with the big knees, who slid, climbed up and swallowed the mountains, known as the land of the wind, played his flute to his loved one.',
    'The world oldest peice of chewing gum is 9,000 years old and found in a cave in swede,',
    'The largest snowflake ever recorded was 15 inches wide and 8 inches thick. it was found in montana usa in 1887',
    "The Earl of Sandwich, John Montagu, who lived in the 1700s, reportedly invented the sandwich so he wouldn’t have to leave his gambling table to eat.",
    "The Four Corners is the only spot in the US where you can stand in four states at once: Utah, Colorado, Arizona and New Mexico.",
    "parts of Canada are south of Detroit",
    "Bats are the only mammal that can actually fly.",
    "Wombats are the only animal whose poop is cube-shaped. This is due to how its intestines form the feces. The animals then stack the cubes to mark their territory.",
    "For comparison, an elephant's heart weighs around 30 pounds. And a human heart? A mere 10 ounces.",
      
    
    
    
             ]
             
  fact = random.choice(facts)
  await interaction.response.send_message(fact)
  def setup(bot: commands.Bot):
    bot.add_command(FactCommand())

#update 1.10
#making finacial tips a random selection of tips

@bot.tree.command(name="financial-tips")
async def quiz(interaction: discord.Interaction):
  tips = [ "you will never prove a flat earther wrong because they will just say nu-uh and keep lying like a 5 year-old todler",
          "people saying they wouldnt eat any human no matter the circumstances are stupid because they clearly have never eaten pussy.",
          "if 9/11 was an inside job then why didnt they get all the planes to hit their intended target",
          "if incest is normal in alabama then what would being with a girl whose not related to you be called?",
          "Lady Bugs are known to eat their own larvae to ensure the survival of the other larvae.",
          "Just one frog has enough lethal poison in its skin to kill 10 to 15 people",
          "The golden poison dart frog (Phyllobates terribilis) is the size of a paperclip, adorable, and can kill you with a single touch",
          "would it be considered incest if you were sperated at birth by adoption and coinsidentally met up at a coffee shop in cincinatti and began a relationship, get engaged and at the wedding your adoptive birth parents remember eachother and then tell you the truth about the person youve grown to love and care about.",
          "is it gay to sleep with a trans girl even if your drunk and got trick into going home with her but you low-key like it and keep her number.",
          "sex is like the stock market you start slow and keep getting more and more invested until your all in",
          "When you get a pay rise, the natural thing to do is direct all that increased disposable income towards upgrading your lifestyle.And while you should definitely reward yourself for your hard work, resist the urge to direct all that increased income to lifestyle.Mainly because if you establish that constant upgrade habit when you’re young, you’ll tend to keep going with that same habit when you get older. We’ve all heard stories from when the mining boom ended here in Perth of people who were making $300K a year, lost their job and somehow had zero savings to fall back on while they looked for a new one. And when they did get a new one, it was a lower-paying job that couldn’t support the lifestyle they were used to. Not fun. If you get in the habit now of only making small lifestyle upgrades with each increase in income,you’ll be setting yourself up beautifully for later in life." ,
          "In your late teens and early twenties, it’s easier to save if you understand exactly what you are saving for. For most people in this age cohort, holidays, cars and house deposits are the main saving goals.Having those goals means your saving has a purpose and will make it easier to build that saving habit. Write down a number to target, rename the account to reflect your goal, and make sure to celebrate the achievement when you get there.",
          "Just like buying a house, investing is a good idea but only at the right time for you. To get a proper return out of investing, you need to lock your cash away for a minimum of 5 years.  But if you really want to leverage the true power of investing (compound interest), 10+ years is a better time commitment.  I generally advise that people don’t invest cash until:They have bought a home or saved up enough for a 20 percent deposit, They have built a decent offset balance, They have set a trajectory for paying off their debt at a decent pace",
          "I define ‘good debt’ as acceptable, unavoidable debt – things like a HECS debt, home loan or investment loan. All these debts deliver some level of long-term return: education or capital growth.Bad debt, on the other hand, usually sees you paying interest on things you might want, but don’t necessarily need. Almost all kinds of personal loans (credit cards, store cards, Afterpay, and most car loans) fall in this category If you’re going to commit to a bad form of debt, commit only if you truly need the thing, have no other choice, and where possible, can pay it off relatively quickly.",
          'No matter how much or how little you are paid, you may find it difficult to get ahead if you spend more than you earn. Prudent cuts to your spending can result in big savings.',
          'A budget will show where your money is going.  Depending on when you are paid, you may decide on a weekly, fortnightly or monthly budget. You need a budget regardless of how much you earn a year.',
          'Credit card debt can be a big obstacle to improving your finances.',
          'If you want to boost your savings, you can set aside a minimum of five to 10% of your salary for savings.',
          'If you contribute to super and a savings account, and you still have some spare money, then you may want to consider putting it into other investments.',
                



          
             ]
  
  
             
  tips = random.choice(tips)
  await interaction.response.send_message(tips)
  def setup(bot: commands.Bot):
    bot.add_command(FactCommand())

#update 1.10.1
  #added more finacial tips
  #added more fun facts

  #update 1.10.2
  #added framework for plazma.live added currently not functional
  #added more fun facts

#update 1.11
#new bots merged into one 
#bots include plasma.bot to be merged
#plazma bot now included in main segment

def calculate(equation):
    equation = equation.replace(" ", "")
    equation = equation.replace("x", "*")
    equation = equation.replace("^", "**")
    equation = equation.replace("÷", "/")
    equation = equation.replace("π", str(math.pi))
    equation = equation.replace("e", str(math.e))
    equation = equation.replace("sin", "math.sin")
    equation = equation.replace("cos", "math.cos")
    equation = equation.replace("tan", "math.tan")
    equation = equation.replace("asin", "math.asin")
    equation = equation.replace("acos", "math.acos")
    equation = equation.replace("atan", "math.atan")
    equation = equation.replace("sinh", "math.sinh")
    equation = equation.replace("cosh", "math.cosh")
    equation = equation.replace("tanh", "math.tanh")
    equation = equation.replace("asinh", "math.asinh")
    equation = equation.replace("acosh", "math.acosh")
    equation = equation.replace("atanh", "math.atanh")
    equation = equation.replace("log", "math.log")
    equation = equation.replace("log10", "math.log10")
    equation = equation.replace("log2", "math.log2")
    equation = equation.replace("sqrt", "math.sqrt")
    equation = equation.replace("exp", "math.exp")
    equation = equation.replace("floor", "math.floor")
    equation = equation.replace("ceil", "math.ceil")
    equation = equation.replace("abs", "math.fabs")
    equation = equation.replace("factorial", "math.factorial")
    equation = equation.replace("gcd", "math.gcd")
    equation = equation.replace("pi", str(math.pi))
    equation = equation.replace("e", str(math.e))
    equation = equation.replace("√", "math.sqrt")
    equation = equation.replace("∛", "math.pow")
    equation = equation.replace("∜", "math.pow")
    equation = equation.replace("∞", "math.inf")
    equation = equation.replace("∑", "math.fsum")
    equation = equation.replace("∏", "math.prod")
    equation = equation.replace("∫", "math.trunc")

    try:
        return eval(equation)
    except Exception as e:
        return "Error: " + str(e)

@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    try:
        channel = str(message.channel.name)
    except AttributeError:
        channel = str(message.channel)
    user_message = str(message.content)

    print(f"Message {user_message} by {username} on {channel}")

    user_message = user_message.lower()
    if message.author == bot.user:
        return
    if user_message == "hello":
        await message.channel.send("Hello!")

    elif user_message == "ping":
        await message.channel.send("pong")
    elif user_message == "pong":
        await message.channel.send("ping")
    elif user_message == "crazy":
      await message.channel.send("Crazy!? I was crazy once! They Locked me in a room. A rubber room.A rubber room with rats. And rats make me crazy!")#henlo josh a: e, what do you, oh, rats! Crazy!? I was crazy once!
    elif "cat" in user_message:
      await message.channel.send("MEOW 🐱")
    elif "Kitty" in user_message:
      await message.channel.send("MEOW 🐱")
    elif "everyone" in user_message:
      await message.channel.send("shut the fuck up")
    elif "kys" in user_message:
      await message.channel.send("shut the fuck up you fat peice of shit")
    elif "dog" in user_message:
      await message.channel.send("Cats are better then dogs MEOW 🐱")
    elif "uwu" in user_message:
      await message.channel.send("kys")
    elif "yej" in user_message:
      await message.channel.send("speak english you dumb fuck")
    elif "disablist" in user_message:
      await message.channel.send("don't do that, use /vote-for for better results.")
    elif "jewish" in user_message:
      await message.channel.send("Jews? Don't remind me.")
    elif "keep yourself safe" in user_message:
      await message.channel.send("everyone knows you mean kill yourself cut the bullshit")
    elif "jews" in user_message:
      await message.channel.send("Jews? I was a jew once. They locked me in a room. A concrete room. A concrete room with gas. And gas kills jews.")
    elif "communist" in user_message:
      await message.channel.send("Communist? I was a communist once. They locked me in a camp. A gulag camp. A gulag camp with Stalin. And Stalin made me communist.")
    elif user_message == "e":
      await message.channel.send("e")
    elif user_message == "a":
      await message.channel.send("asshole")
    elif user_message == "nu uh":
      await message.channel.send("The fuck you mean Nu Uh")
    elif user_message == "fuck":
      await message.channel.send("WATCH YOUR TONE YOU UNGREATFUL SON OF A BITCH")
    elif user_message == "shit":
      await message.channel.send("WE DONT SWEAR IN THIS HOUSEHOLD FUCKFACE.")
    elif user_message == "election":
      await message.channel.send("You should vote for the MLU, the Mindoor Liberal Union for a fairer and democratic future")
    elif user_message == "vote":
      await message.channel.send("You should vote for the MLU, the Mindoor Liberal Union for a fairer and democratic future")
    elif user_message == "give":
      await message.channel.send("We're no strangers to love. You know the rules and so do I (do I). A full commitment's what I'm thinking of. You wouldn't get this from any other guy. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. And if you ask me how I'm feeling. Don't tell me you're too blind to see. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (to say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you!")
    elif user_message == "never":
      await message.channel.send("We're no strangers to love. You know the rules and so do I (do I). A full commitment's what I'm thinking of. You wouldn't get this from any other guy. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. And if you ask me how I'm feeling. Don't tell me you're too blind to see. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (to say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you!")
    elif user_message == "up":
      await message.channel.send("We're no strangers to love. You know the rules and so do I (do I). A full commitment's what I'm thinking of. You wouldn't get this from any other guy. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. And if you ask me how I'm feeling. Don't tell me you're too blind to see. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. We've known each other for so long. Your heart's been aching, but you're too shy to say it (to say it). Inside, we both know what's been going on (going on). We know the game and we're gonna play it. I just wanna tell you how I'm feeling. Gotta make you understand. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you. Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. Never gonna make you cry. Never gonna say goodbye. Never gonna tell a lie and hurt you!")
 

    elif "crazy_gen " in user_message:
        term = user_message.split()[1]
        await message.channel.send(crazy(term))

  
        #while True:
        #    await message.channel.send("UwU")
    # Check if the message contains the name of a former British colony
    elif message.content in former_british_colonies:
        # Get the colonial name of the country
        colonial_name = former_british_colonies[message.content.lower()]

        # Reply with the colonial name
        await message.reply(f'The colonial name of {message.content} is {colonial_name}')
    elif user_message == "help":
        view = Help()
        await message.reply("Click a button to get started!", view=view)

    elif "c++" in user_message:
        user_message = user_message.replace("c++ ", "")
        user_message = user_message.replace("c++", "")
        user_message = user_message.replace("```", "")
        user_message = user_message.replace("“", '"')
        user_message = user_message.replace("”", '"')
        user_message = user_message.replace("‘", "'")
        user_message = user_message.replace("’", "'")

        with open("code.cpp", "w") as file:
            file.write(user_message)
        await message.channel.send("Compiling...")
        await bot.change_presence(
            activity=discord.Game(name="Compiling..."),
            status=discord.Status.dnd)
        response = utils.compile_cpp()
        response = f"`Plazma C++ Code Compilation:`\n```{response}```"
        try:
            await message.channel.send(response)
        except discord.errors.HTTPException:
            with open("output.txt", "w") as file:
                file.write(response)
            await message.channel.send(file=discord.File("output.txt"))
        await bot.change_presence(activity=discord.Game(name="Sex With Hitler 2077"),
                                     status=discord.Status.online)

    elif "calculate" in user_message:
        user_message = user_message.replace("calculate ", "")
        await message.channel.send(str(calculate(user_message)))

    elif "python" in user_message:
        user_message = user_message.replace("python ", "")
        user_message = user_message.replace("python", "")
        user_message = user_message.replace("“", '"')
        user_message = user_message.replace("”", '"')
        user_message = user_message.replace("‘", "'")
        user_message = user_message.replace("’", "'")

        with open("code.py", "w") as file:
            file.write(user_message)
        await message.channel.send("Compiling...")
        try:
            await bot.change_presence(
                activity=discord.Game(name="Compiling..."),
                status=discord.Status.dnd)
            response = utils.compile_python()
        except Exception as e:
            response = str(e)
        response = f"`Plazma Python Code Compilation:`\n```{response}```"
        try:
            await message.channel.send(response)
        except discord.errors.HTTPException:
            with open("output.txt", "w") as file:
                file.write(response)
            await message.channel.send(file=discord.File("output.txt"))
        await bot.change_presence(activity=discord.Game(name="Sex With Hitler 2077"),
                                     status=discord.Status.online)

    elif "tts" in user_message:
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None and "file" not in user_message:
            user_message = user_message.replace("tts ", "")
            utils.speak(user_message)
            channel = voice_channel.name

            await message.channel.send(f"Playing *{user_message}* in {channel}"
                                       )

            vc = await voice_channel.connect()

            source = discord.FFmpegOpusAudio("voice.mp3")

            vc.play(source)

            while vc.is_playing():
                await asyncio.sleep(1)

            vc.stop()
            await vc.disconnect()
        elif voice_channel != None and "file" in user_message:
            user_message = user_message.replace("tts", "")
            user_message = user_message.replace("file", "")
            user_message = user_message.replace(" ", "")
            file = open(user_message)
            contents = ""
            for line in file:
                contents += line
            try:
                utils.speak(contents)
            except RecursionError:
                utils.speak("File too long.")
            channel = voice_channel.name

            await message.channel.send(f"Playing {user_message} in {channel}")

            vc = await voice_channel.connect()

            source = discord.FFmpegOpusAudio("voice.mp3")

            vc.play(source)

            while vc.is_playing():
                await asyncio.sleep(1)

            vc.stop()
            await vc.disconnect()
        else:
            await message.channel.send(f"{username} is not in a voice channel."
                                       )
            
    # plazma search engine
    elif "search" in user_message.lower():
        await message.channel.send("Searching...")
        user_message = user_message.replace("search ", "")
        response = requests.get(f"https://plazma-search-server.captaindeathead.repl.co/search?q={user_message}")
        if response.status_code == 200:
            # titles and links in json response
            titles = []
            links = []
            images = []

            for i in range(len(response.json()["links"])):
                if "imgurl" in response.json()["links"][i]:
                    continue
                try:
                    if titles[i] == None:
                        titleResponse = requests.get(f"https://plazma-search-server.captaindeathead.repl.co/getTitle?url={response.json()['links'][i]}")
                        if titleResponse.status_code == 200:
                            titles[i] = titleResponse.json()["title"]
                    titles.append(response.json())
                except IndexError:
                    titles.append("No title found.")
                    titleResponse = requests.get(f"https://plazma-search-server.captaindeathead.repl.co/getTitle?url={response.json()['links'][i]}")
                    if titleResponse.status_code == 200:
                        titles[i] = titleResponse.json()
                try:
                    links.append(response.json()["links"][i])
                except IndexError:
                    links.append("No link found.")

            # create embed
            embed = discord.Embed(title=f"Search results for {user_message}", color=0x00ff00)
            for i in range(len(titles)):
                embed.add_field(name=titles[i], value=links[i], inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Error: Search engine is down or a network error occured.")

    # check if the message includes "number_guess" and a mention
    elif "number_guess" in user_message and message.mentions:
        number = random.randint(1, 10)
        await message.channel.send(
            f"Guess a number between 1 and 10, {username}!")
        guess = await bot.wait_for(
            "message", check=lambda message: message.author == message.author)
        if int(guess.content) == number:
            await message.channel.send(f"Correct, {username}!")
        else:
            await message.channel.send(
                f"Wrong, {username}! The number was {number}.")
        await message.channel.send(f"Thanks for playing, {username}!")
        # ping the mentioned user to guess the number
        await message.channel.send(
            f"{message.mentions[0].mention} guess a number between 1 and 10!")
        number = random.randint(1, 10)
        # wait for the mentioned user to guess the number
        guess1 = await bot.wait_for(
            "message",
            check=lambda message: message.author == message.mentions)
        if int(guess1.content) == number:
            await message.channel.send(
                f"Correct, {message.mentions[0].mention}!")
        else:
            await message.channel.send(
                f"Wrong, {message.mentions[0].mention}! The number was {number}."
            )
        await message.channel.send(
            f"Thanks for playing, {message.mentions[0].mention}!")

    elif "chess" in user_message:
        channel = message.channel
        if message.mentions:
            board = chess.Board()
            black = message.mentions[0]
            white = message.author
            await message.channel.send(
                f"{black.mention} is black and {white.mention} is white.")
            await message.channel.send(f"{white.mention} starts.")
            # draw the letters
            readable_board = (
                "  a  b  c  d  e  f  g  h\n8 " + board.unicode()[0:16] + "7 " +
                board.unicode()[16:32] + "6 " + board.unicode()[32:48] + "5 " +
                board.unicode()[48:64] + "4 " + board.unicode()[64:80] + "3 " +
                board.unicode()[80:96] + "2 " + board.unicode()[96:112] +
                "1 " + board.unicode()[112:128])
            await message.channel.send(f"```{readable_board}```")
            while not board.is_game_over():
                if board.turn == chess.WHITE:
                    await message.channel.send(
                        f"{white.mention} select a piece to move. (exit to cancel move)"
                    )
                    piece = await bot.wait_for(
                        "message",
                        check=lambda message: message.author == white and
                        message.channel == channel,
                    )
                    if piece.content == "exit":
                        await message.channel.send("Move cancelled.")
                        break
                    else:
                        await message.channel.send(
                            f"{white.mention} select a square to move to. (exit to cancel move)"
                        )
                        square = await bot.wait_for(
                            "message",
                            check=lambda message: message.author == white and
                            message.channel == channel,
                        )
                        if square.content == "exit":
                            await message.channel.send("Move cancelled.")
                            continue
                        else:
                            try:
                                board.push_san(
                                    f"{piece.content}{square.content}")
                            except ValueError:
                                await message.channel.send(
                                    "That is not a valid move.")
                            # draw the letters
                            readable_board = ("  a  b  c  d  e  f  g  h\n8 " +
                                              board.unicode()[0:16] + "7 " +
                                              board.unicode()[16:32] + "6 " +
                                              board.unicode()[32:48] + "5 " +
                                              board.unicode()[48:64] + "4 " +
                                              board.unicode()[64:80] + "3 " +
                                              board.unicode()[80:96] + "2 " +
                                              board.unicode()[96:112] + "1 " +
                                              board.unicode()[112:128])
                            await message.channel.send(
                                f"```{readable_board}```")
                else:
                    await message.channel.send(
                        f"{black.mention} select a piece to move. (exit to cancel move)"
                    )
                    piece = await bot.wait_for(
                        "message",
                        check=lambda message: message.author == black and
                        message.channel == channel,
                    )
                    if piece.content == "exit":
                        await message.channel.send("Move cancelled.")
                        break
                    else:
                        await message.channel.send(
                            f"{black.mention} select a square to move to. (exit to cancel move)"
                        )
                        square = await bot.wait_for(
                            "message",
                            check=lambda message: message.author == black and
                            message.channel == channel,
                        )
                        if square.content == "exit":
                            await message.channel.send("Move cancelled.")
                            continue
                        else:
                            try:
                                board.push_san(
                                    f"{piece.content}{square.content}")
                            except ValueError:
                                await message.channel.send(
                                    "That is not a valid move.")
                            # draw the letters
                            readable_board = ("  a  b  c  d  e  f  g  h\n8 " +
                                              board.unicode()[0:16] + "7 " +
                                              board.unicode()[16:32] + "6 " +
                                              board.unicode()[32:48] + "5 " +
                                              board.unicode()[48:64] + "4 " +
                                              board.unicode()[64:80] + "3 " +
                                              board.unicode()[80:96] + "2 " +
                                              board.unicode()[96:112] + "1 " +
                                              board.unicode()[112:128])
                            await message.channel.send(
                                f"```{readable_board}```")

        else:
            depth = 3
            board = chess.Board()
            moves_played = 0
            white = "Plazma Chess Engine"
            black = message.author
            await message.channel.send(f"{message.author.mention} is black.")
            await message.channel.send(f"Plazma Chess Engine is white.")
            await message.channel.send(f"{message.author.mention} starts.")
            await message.channel.send(
                f"Please enter a depth for the engine to search to (2 - 5 is recommended). (exit to cancel game)"
            )
            depth = await bot.wait_for(
                "message",
                check=lambda message: message.author == black and message.
                channel == channel,
            )
            # draw the letters
            readable_board = (
                "  a  b  c  d  e  f  g  h\n8 " + board.unicode()[0:16] + "7 " +
                board.unicode()[16:32] + "6 " + board.unicode()[32:48] + "5 " +
                board.unicode()[48:64] + "4 " + board.unicode()[64:80] + "3 " +
                board.unicode()[80:96] + "2 " + board.unicode()[96:112] +
                "1 " + board.unicode()[112:128])
            await message.channel.send(f"```{readable_board}```")
            while not board.is_game_over():
                if board.turn == chess.WHITE:
                    await message.channel.send(
                        f"Plazma Chess Engine is thinking...")
                    engine_move, moves_played = engine.process(
                        board, "black", moves_played, int(depth.content))
                    print(engine_move)
                    board.push(engine_move)
                    # draw the letters
                    readable_board = ("  a  b  c  d  e  f  g  h\n8 " +
                                      board.unicode()[0:16] + "7 " +
                                      board.unicode()[16:32] + "6 " +
                                      board.unicode()[32:48] + "5 " +
                                      board.unicode()[48:64] + "4 " +
                                      board.unicode()[64:80] + "3 " +
                                      board.unicode()[80:96] + "2 " +
                                      board.unicode()[96:112] + "1 " +
                                      board.unicode()[112:128])
                    await message.channel.send(f"```{readable_board}```")
                else:
                    await message.channel.send(
                        f"{message.author.mention} select a piece to move. (exit to cancel move)"
                    )
                    piece = await bot.wait_for(
                        "message",
                        check=lambda message: message.author == black and
                        message.channel == channel,
                    )
                    if piece.content == "exit":
                        await message.channel.send("Move cancelled.")
                        break
                    else:
                        await message.channel.send(
                            f"{message.author.mention} select a square to move to. (exit to cancel move)"
                        )
                        square = await bot.wait_for(
                            "message",
                            check=lambda message: message.author == black and
                            message.channel == channel,
                        )
                        if square.content == "exit":
                            await message.channel.send("Move cancelled.")
                            continue
                        else:
                            try:
                                board.push_san(
                                    f"{piece.content}{square.content}")
                            except ValueError:
                                await message.channel.send(
                                    "That is not a valid move.")
                            # draw the letters
                            readable_board = ("  a  b  c  d  e  f  g  h\n8 " +
                                              board.unicode()[0:16] + "7 " +
                                              board.unicode()[16:32] + "6 " +
                                              board.unicode()[32:48] + "5 " +
                                              board.unicode()[48:64] + "4 " +
                                              board.unicode()[64:80] + "3 " +
                                              board.unicode()[80:96] + "2 " +
                                              board.unicode()[96:112] + "1 " +
                                              board.unicode()[112:128])
                            await message.channel.send(
                                f"```{readable_board}```")

            if board.is_checkmate():
                await message.channel.send(f"Checkmate! {board.turn} wins!")
            elif board.is_stalemate():
                await message.channel.send("Stalemate!")
            elif board.is_insufficient_material():
                await message.channel.send("Draw!")
            elif board.is_seventyfive_moves():
                await message.channel.send("Draw!")
            elif board.is_fivefold_repetition():
                await message.channel.send("Draw!")
            else:
                await message.channel.send("Draw!")

    elif "menu" in user_message:
        view = Menu()
        await message.reply("Click a button to get started!", view=view)
    await bot.process_commands(message)


class Menu(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Children", style=discord.ButtonStyle.blurple)
    async def children(self, interaction: discord.Interaction,
                       button: discord.ui.Button):
        embed = discord.Embed(
            title="Children",
            description="Children are people under the age of 18.",
            color=discord.Color.random(),
        )
        embed.add_field(
            name="Children",
            value="Children are people under the age of 18.",
            inline=False,
        )
        embed.add_field(
            name="Not Children",
            value="Not Children are people over the age of 18.",
            inline=False,
        )
        embed.set_footer(text="Plazma")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Not Children", style=discord.ButtonStyle.blurple)
    async def not_children(self, interaction: discord.Interaction,
                           button: discord.ui.Button):
        embed = discord.Embed(
            title="Not Children",
            description="Not Children are people over the age of 18.",
            color=discord.Color.random(),
        )
        embed.add_field(
            name="Children",
            value="Children are people under the age of 18.",
            inline=False,
        )
        embed.add_field(
            name="Not Children",
            value="Not Children are people over the age of 18.",
            inline=False,
        )
        embed.set_footer(text="Plazma")
        await interaction.response.send_message(embed=embed, ephemeral=True)


class Help(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Commands", style=discord.ButtonStyle.blurple)
    async def commands(self, interaction: discord.Interaction,
                       button: discord.ui.Button):
        embed = discord.Embed(
            title="Plazma Commands:",
            description=(
                "`help` - Shows this message.\n"
                "`ping` - Pong!\n"
                "`pong` - Ping!\n"
                "`e` - e\n"
                "`tts` - Text to speech.\n"
                "`number_guess` - Guess a number between 1 and 10.\n"
                "`chess` - Play chess against Plazma or another user.\n"
                "`c++` - Compile C++ code.\n"
                "`python` - Compile Python code."),
            color=discord.Color.random(),
        )
        embed.set_footer(text="Plazma")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="C++ Compilation Guide",
                       style=discord.ButtonStyle.blurple)
    async def cpp(self, interaction: discord.Interaction,
                  button: discord.ui.Button):
        embed = discord.Embed(
            title="C++ Compilation Guide",
            description=
            ("To compile C++ code, type 'c++ ' followed by your code.\n\n"
             "You can also use code blocks after the 'c++ ' keyword to make your code look nicer.\n\n"
             " - If you use code blocks, make sure to type 'c++' after the '```' followed by a new line to add syntax highlighting.\n\n"
             "Once you have typed your code, I will compile it and send the output.\n\n"
             "I will also prompt you for input if your program requires it. "
             "If you want to cancel the input prompt, but continue the program, type 'exit'.\n\n"
             "Otherwise, type your input and I will send the output."),
            color=discord.Color.random(),
        )
        embed.set_footer(text="Plazma C++ Compilation Guide")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Python Compilation Guide",
                       style=discord.ButtonStyle.blurple)
    async def python(self, interaction: discord.Interaction,
                     button: discord.ui.Button):
        embed = discord.Embed(
            title="Python Compilation Guide",
            description=
            ("To compile Python code, type 'python ' followed by your code.\n\n"
             "You can also use code blocks after the 'python ' keyword to make your code look nicer.\n\n"
             " - If you use code blocks, make sure to type 'python' after the '```' followed by a new line to add syntax highlighting.\n\n"
             "Once you have typed your code, I will compile it and send the output.\n\n"
             "I will also prompt you for input if your program requires it.\n\n"
             "If you want to cancel the input prompt, but continue the program, type 'exit'.\n\n"
             "Otherwise, type your input and I will send the output."),
            color=discord.Color.random(),
        )
        embed.set_footer(text="Plazma Python Compilation Guide")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Chess Guide", style=discord.ButtonStyle.blurple)
    async def chess(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
        embed = discord.Embed(
            title="Chess Guide",
            description=
            ("VS Plazma:\n\n"
             " - I will prompt you for a depth for the engine to search to. 2 - 5 is recommended.\n\n"
             " - Once you have entered a depth, I will start the game.\n\n"
             " - To make a move, type the piece you want to move, followed by the square you want to move to.\n\n"
             " - For example, if you want to move the pawn at e2 to e4, type 'e2' then when I prompt you, type 'e4'.\n\n"
             " - I will then make a move, and you will make a move, and so on.\n\n"
             " - If you want to cancel a move, type 'exit'.\n\n"
             " - If you want to cancel the game, type 'exit' when I prompt you to select a piece to move.\n\n"
             "VS Another User:\n\n"
             " - Mention the user you want to play against.\n\n"
             " - I will then prompt you for a piece to move, and a square to move to.\n\n"
             " - If you want to cancel a move, type 'exit'.\n\n"
             " - If you want to cancel the game, type 'exit' when I prompt you to select a piece to move.\n\n"
             " - The other player will then make a move, and you will make a move, and so on."
             ),
            color=discord.Color.random(),
        )
        embed.set_footer(text="Plazma Chess Guide")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="About", style=discord.ButtonStyle.blurple)
    async def about(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
        embed = discord.Embed(
            title="About Plazma",
            description="Plazma is a Discord bot made by CaptainDeathead and Osama Bin collection. helped by Yesnt",
            color=discord.Color.random(),
        )
        embed.set_footer(text="Plazma")
        await interaction.response.send_message(embed=embed, ephemeral=True)


#soundboard command
class sndmen(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Megalovania", style=discord.ButtonStyle.blurple)
    async def megalovania(self, interaction: discord.Interaction,
                       button: discord.ui.Button):
      user = interaction.user
      user_message = interaction.message   # bruh, why are you adding this, isnt it in your bot
      voice_channel = user.voice.channel #e
      channel = None
      if voice_channel is not None:
          # File playback code block
          await interaction.send(f"Playing soundboard item in {voice_channel.name}")
          vc = await voice_channel.connect()
          source = discord.FFmpegOpusAudio("megalovania.wav")
          vc.play(source)
      else:
          await interaction.send("You are not in a voice channel.")

@bot.tree.command(name="soundboard")
async def soundboard(interaction: discord.Interaction):
    view = sndmen()
    await interaction.response.send_message("Yej", view=view)


#added magic 8 ball command 
# added roast command

PFuture = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "**E!**", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
ROptions = ["If you were spice, you'd be flour", "There's no one in this world like you. Or at least I hope so", "I'd like to roast you, but it looks like your genetics already did", "I didn't hear you. I'm busy ignoring an annoying person", "You should photoshop your life with better decisions.", "You look like a before picture.", "I'd like to roast you, but i'm too busy judging your choices", "The only way you could get laid is if you crawled up a chicken's ass and waited.", "Your face is so oily that I'm suprised America hasn't invaded yet", "You're not good looking enough to be a model, but you're not smart enough to be anything else", "Did you forget to wipe or is that your natural scent?", "Sorry. I'm on the toilet and I can only deal with one shit at a time", "It's a parent's job to raise their children right. So looking at you, it's no wonder your dad quit after just one day.", "You might just be why the middle finger was invented in the first place", "You do realise we are just tolerating you, right?", "If I had a dollar every time you shut up, I would give it back as a thank you", "It's impossible to underestimate you", "You're the reason gene pools need lifeguards", "You're like the gray sprinkle on a rainbow cupcake", "Have you ever tried not being an idiot", "You're the human version of athlete's foot: annoying and hard to get rid of", "You were so happy about getting negitive for covid... we didn't have the heart to tell you it was actually an IQ test", "We were going to roast you, but burning trash is apparently an environmental hazard", "Everyone has a purpose in life, and your's is to become an organ donor", "You can be anything you want, except good looking", "Don't feel bad, don't feel blue, Frankenstein was ugly too", "I'm the type of person to laugh at mistakes, so sorry if I laughed at your face"]

@bot.tree.command(name="8ball")
async def ball(interaction: discord.Interaction, *, question: str):
  await interaction.response.send_message()
  predict53 = random.choice(PFuture)
  await interaction.response.send_message(predict53)

@bot.tree.command(name="roast")
async def suscrystals(interaction: discord.Interaction, *, target: discord.User):
    await interaction.response.send_message(f"**Fronk bot roasted {target.mention}**")
    predict53 = random.choice(ROptions)
    await interaction.channel.send(predict53)



#update 1.12
#added a code that tells time to be added later
#reminders bot that reminds you of things
#more commands added

@bot.tree.command(name="time")
async def time(interaction: discord.Interaction):
    auzTime = pytz.timezone('Australia/Perth')
    # niceAuzTime converts to 12 hour time with AM/PM
    niceAuzTime = datetime.datetime.now(auzTime).strftime('%I:%M %p')
    await interaction.response.send_message(f"The time is {niceAuzTime} in Western Australia")

@bot.tree.command(name="remind")
async def remind(interaction: discord.Interaction, *, reminder: str, mins: str, author: discord.User):
    await interaction.response.send_message(f"Reminder set for {mins} mins from now")
    await asyncio.sleep(int(mins)*60)
    await interaction.channel.send(f"Reminder for {author.mention}: {reminder}")



#added urban dictionary
async def get_definition(word, count):
  url = f"http://api.urbandictionary.com/v0/define?term={word}"
  response = requests.get(url)
  data = response.json()
  if not data['list']:
    return f"No definition found for {word}"
  else:
    return data['list'][count]['definition']

@bot.tree.command(name="urbandictionary")
async def urban(interaction: discord.Interaction, word: str, count: int = 1):
  definition = await get_definition(word, count - 1)
  await interaction.response.send_message(f"The definition of {word} is {definition}")

#update 1.12.1 
#moving slash commands to same area

#update 1.13
#music functionality
#added calculator
#added where i hid a 39 year old women i killed in 2016 and left her body to rot and decompose at the bottom of the river thames

@bot.tree.command(name='music')
async def songinfo(ctx):
  if not ctx.voice_client:
    return await ctx.send("You are not playing any music.")
  elif not getattr(ctx.author.voice, "channel", None):
    return await ctx.send("Join a voice channel first.")
  else:
    vc: wavelink.Player = ctx.voice_client

  if not vc.is_playing():
    return await ctx.send("There is no music playing at the moment.")

  em = discord.Embed(title=f"Now playing: {vc.current.title}",
                     description=f"Artist: {vc.current.author}")
  em.add_field(name="Duration",
               value=str(datetime.timedelta(milliseconds=vc.current.length)))
  em.add_field(name="Extra Info",
               value=f"Song URL: [Click here]({vc.current.uri})")
  await ctx.send(embed=em)


@bot.command()
async def gen(ctx, *, msg):
  data = query({"inputs": msg})
  generated_text = data[0]['generated_text']
  await ctx.send(generated_text)


@bot.command()
async def volume(ctx, volume: int):
  if not ctx.voice_client:
    return await ctx.send("Ur not playing any music :bruh:")
  elif not getattr(ctx.author.voice, "channel", None):
    return await ctx.send("Join a voice channel first")
  else:
    vc: wavelink.Player = ctx.voice_client
  if volume < 0:
    return await ctx.send("That's way too low")
  await ctx.send(f"The volume was set to *{volume}%*")
  return await vc.set_volume(volume)

#update 1.14
#added commands

#custom join message
@bot.event
async def on_member_join(member):
  for channel in member.guild.channels:
    if channel.name == 'general':
      await channel.send(f"Welcome to Hell on earth, {member.mention}!")
      return
    if channel.name == 'general-communism': #general communism is not general
      await channel.send(f"Welcome to the most amzing country ever, {member.mention}!")
      return


#update 1.15 upgraded to new version of python
#added banning and kicking capabilities 
#stole voting

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await member.send("You have been kicked from the server for "+reason)
    await member.kick(reason=reason)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No Reason Provided"):
    await ctx.send(member.name + " has been from banned the server for "+reason)
    await member.ban(reason=reason)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('>>')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member.name,member_disc):

            await ctx.uild.unban(user)
            await ctx.send(member.name +" has been unbanned!")
            return

    await ctx.send(member+"was not found!")

#stole fronk bot 1 


@bot.tree.command(name='snipe')
async def snipe(ctx):
  if snipe_message_content == None:
    await ctx.send("kys you fat peice of shit")
  else:
    em = discord.Embed(colour=(discord.Colour.random()),
                       description=f"{snipe_message_content}")
    em.set_footer(text=f"Requested by {ctx.author}.")
    em.set_author(name=f"Sniped the message by {snipe_message_author}")
    await ctx.send(embed=em)


@bot.command()
async def avatar(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author

  memberAvatar = user.avatar.url
  await ctx.send(memberAvatar)


class VotingDropdown(discord.ui.Select):

    def __init__(self, user_uwu):
        options = []
        print("user_uwu:", user_uwu)
        for candidate_id in user_uwu:
            candidate_username = candidate_id_to_name[candidate_id]
            options.append(discord.SelectOption(label=candidate_username))
        super().__init__(placeholder="Who do you vote for?",
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        with open("hasvoted.json", 'r') as file:
          men = json.load(file)
        if user_id in men:
          return await interaction.response.send_message("You have already voted", ephemeral=True)
        with open('votes.json', 'r') as file:
            votes = json.load(file)
        await interaction.response.send_message(
            f"You voted for {self.values[0]}!", ephemeral=True)
        candidate_username = self.values[0]
        candidate_id = next((cid
                             for cid, uname in candidate_id_to_name.items()
                             if uname == candidate_username), None)
        candidate_id = str(candidate_id)
        if candidate_id not in votes:
            votes[candidate_id] = 0
        votes[candidate_id] += 1
        with open('votes.json', 'w') as file:
            json.dump(votes, file)
        men.append(user_id)
        with open("hasvoted.json", 'w') as file:
          json.dump(men, file)
 

class VotingView(discord.ui.View):

    def __init__(self, user_uwu):
        super().__init__()
        self.add_item(VotingDropdown(user_uwu))


@bot.tree.command(name="vote")
async def vote(interaction: discord.Interaction):
    user_id = interaction.user.id
    with open("hasvoted.json", 'r') as file:
      men = json.load(file)
    if user_id in men:
      return await interaction.response.send_message("You have already voted", ephemeral=True)
    with open('cand.json', 'r') as file:
        user_owo = json.load(file)
    candidate_id_to_name.clear()
    for furry in user_owo:
        option = await bot.fetch_user(furry)
        candidate_id_to_name[furry] = option.name
        print(f"Mapping: {furry} -> {option.name}")
    print("candidate_id_to_name:", candidate_id_to_name)
    await interaction.response.send_message("Click the dropdown to vote",
                                            view=VotingView(
                                                candidate_id_to_name.keys()),
                                            ephemeral=True)

@bot.tree.command(name="better-vote")
async def vote(interaction: discord.Interaction):
    user_id = interaction.user.id
    with open("hasvoted.json", 'r') as file:
      men = json.load(file)
    if user_id in men:
      return await interaction.response.send_message("You have already voted", ephemeral=True)
    with open('cand.json', 'r') as file:
        user_owo = json.load(file)
    candidate_id_to_name.clear()
    for furry in user_owo:
        option = await bot.fetch_user(furry)
        candidate_id_to_name[furry] = option.name
        print(f"Mapping: {furry} -> {option.name}")
    print("candidate_id_to_name:", candidate_id_to_name)
    await interaction.response.send_message("Click the dropdown to vote",
                                            view=VotingView(
                                                candidate_id_to_name.keys()),
                                            ephemeral=True)

@bot.command()
async def poll(ctx, *, question):
    options = question.split("|")
    question = options[0]
    del options[0]
    if len(options) <= 1:
        await ctx.send('You need more than one option to make a poll!')
        return
    if len(options) > 10:
        await ctx.send('You cannot make a poll for more than 10 things!')
        return
    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']
    else:
        reactions = [
            '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'
        ]
    description = []
    for i, option in enumerate(options):
        description += '\n {} {}'.format(reactions[i], option)
    embed = discord.Embed(title=question, description=''.join(description))
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)
    await ctx.message.delete()


@bot.command()
async def check_reactions(ctx, message_link: str):
    try:
        with open('link.json', 'r') as file:
            message_list = json.load(file)
        message_link = message_list[0]
        message_id = int(message_link.split('/')[-1])
        channel = bot.get_channel(ctx.channel.id)
        message = await channel.fetch_message(message_id)

        reactions = message.reactions
        reaction_info = []

        for reaction in reactions:
            async for user in reaction.users():
                reaction_info.append(f"{reaction.emoji} - {user.name}")

        if reaction_info:
            await ctx.send("\n".join(reaction_info))
        else:
            await ctx.send("No reactions found for the specified message.")

    except Exception as e:
        await ctx.send(f"Error: {e}")

@commands.is_owner()
@bot.command()
async def config_election(ctx):
    em = discord.Embed(
        title="Run for Server Admin",
        description=
        "Are you interested in becoming the admin for the server? Just react 🎂 to this message",
        color=discord.Color.green()  # You can set a color for the embed
    )
    msg = await ctx.send(embed=em)
    await msg.add_reaction("🎂")
    message_link = f"https://discord.com/channels/{ctx.guild.id}/{msg.channel.id}/{msg.id}"
    data = [message_link]
    with open('link.json', 'w') as file:
        json.dump(data, file)

@commands.is_owner()
@bot.command()
async def start_election(ctx):
    try:
        with open('link.json', 'r') as file:
            message_list = json.load(file)
        message_link = message_list[0]
        message_id = int(message_link.split('/')[-1])
        channel = bot.get_channel(ctx.channel.id)
        message = await channel.fetch_message(message_id)

        reactions = message.reactions
        user_ids = []
        sniffuwu = []
        with open('hasvoted.json', 'w') as file:
          json.dump(sniffuwu, file)

        for reaction in reactions:
            async for user in reaction.users():
                user_ids.append(user.id)

        if user_ids:
            if 1091708065985876128 in user_ids:
                user_ids.remove(1091708065985876128)
            votes = {}
            with open("votes.json", 'w') as file:
                json.dump(votes, file)
            with open('cand.json', 'w') as file:
                json.dump(user_ids, file)
            with open('cand.json', 'r') as file:
                user_uwu = json.load(file)
            em = discord.Embed(title="Vote for the Server Admin",
                               color=discord.Color.blue(),
                               description="Vote by using /vote")
            for user in user_uwu:
                em.add_field(name=f"<@{user}>", value="Candidate")
            await ctx.send(embed=em)
        else:
            await ctx.send("No reactions found for the specified message.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@commands.is_owner()
@bot.command()
async def eval_election(ctx):
    with open("votes.json", 'r') as file:
        votes = json.load(file)
    em = discord.Embed(title="Election Results",
                       color=discord.Color.orange(),
                       description="The results are displayed below")
    for candidate, vote_count in votes.items():
        candidate = int(candidate)
        candidate = await bot.fetch_user(candidate)
        candidate = candidate.name
        em.add_field(name=candidate,
                     value=f"Votes: {vote_count}",
                     inline=False)
    maxkey = max(votes, key=votes.get)
    maxkeyname = await bot.fetch_user(maxkey)
    maxkeyname = maxkeyname.name
    em.add_field(name=f"That means the chancellor is {maxkeyname}",
                 value="The chancellor role has been applied")
    with open("chancellor.json", 'r') as file:
      prevchancellor = json.load(file)
    role = discord.utils.get(ctx.guild.roles, name="Chancellor")
    if prevchancellor:
      anime = int(prevchancellor)
      member = ctx.guild.get_member(anime)
      await member.remove_roles(role)
    user_id = int(maxkey)
    member = ctx.guild.get_member(user_id)
    await member.add_roles(role)
    prevchancellor = user_id
    with open("chancellor.json", "w") as file:
      json.dump(prevchancellor, file)
    await ctx.send(embed=em)

@bot.command()
async def current_results(ctx):
    with open("votes.json", 'r') as file:
        votes = json.load(file)
    x = []
    y = []
    for candidate, vote_count in votes.items():
      candidate = int(candidate)
      candidate = await bot.fetch_user(candidate)
      candidate = candidate.name
      x.append(candidate)
      y.append(vote_count)
    plt.bar(x, y, color='Orange')
    plt.xlabel('Candidates')
    plt.ylabel('Votes')
    plt.title('Election Results (Current)')
    plt.savefig('graph.png')
    await ctx.send(file=discord.File('graph.png'))

#pirated carl-bot

def to_keycap(c):
    return '\N{KEYCAP TEN}' if c == 10 else str(c) + '\u20e3'


class Polls:
    """Poll voting system."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def quickpoll(self, ctx, *, questions_and_choices: str):
        """
        delimit questions and answers by either | or , 
        supports up to 10 choices
        """
        if "|" in questions_and_choices:
            delimiter = "|"
        elif "," in questions_and_choices:
            delimiter = ","
        else:
            delimiter = None
        if delimiter is not None:
            questions_and_choices = questions_and_choices.split(delimiter)
        else:
            questions_and_choices = shlex.split(questions_and_choices)

        if len(questions_and_choices) < 3:
            return await ctx.send('Need at least 1 question with 2 choices.')
        elif len(questions_and_choices) > 11:
            return await ctx.send('You can only have up to 10 choices.')

        perms = ctx.channel.permissions_for(ctx.guild.me)
        if not (perms.read_message_history or perms.add_reactions):
            return await ctx.send('Need Read Message History and Add Reactions permissions.')

        question = questions_and_choices[0]
        choices = [(to_keycap(e), v)
                   for e, v in enumerate(questions_and_choices[1:], 1)]

        try:
            await ctx.message.delete()
        except:
            pass

        fmt = '{0} asks: {1}\n\n{2}'
        answer = '\n'.join('%s: %s' % t for t in choices)
        poll = await ctx.send(fmt.format(ctx.message.author, question.replace("@", "@\u200b"), answer.replace("@", "@\u200b")))
        for emoji, _ in choices:
            await poll.add_reaction(emoji)

    @commands.command(no_pm=True)
    async def poll(self, ctx, *, question: str):
        """
        Quick and easy yes/no poll, for multiple answers, see !quickpoll
        """
        msg = await ctx.send("**{}** asks: {}".format(ctx.message.author, question.replace("@", "@\u200b")))
        try:
            await ctx.message.delete()
        except:
            pass
        if ctx.guild.id == 207943928018632705:
            # Essential :sexthumb:
            yes_thumb = discord.utils.get(
                ctx.guild.emojis, id=287711899943043072)
            no_thumb = discord.utils.get(
                ctx.guild.emojis, id=291798048009486336)
        else:
            yes_thumb = "👍"
            no_thumb = "👎"
        await msg.add_reaction(yes_thumb)
        await msg.add_reaction(no_thumb)

    @commands.command()
    async def strawpoll(self, ctx, *, question_and_choices: str=None):
        """
        Usage: !strawpoll my question | answer a | answer b | answer c\nAt least two answers required.
        """
        if question_and_choices is None:
            return await ctx.send("Usage: !strawpoll my question | answer a | answer b | answer c\nAt least two answers required.")
        if "|" in question_and_choices:
            delimiter = "|"
        else:
            delimiter = ","
        question_and_choices = question_and_choices.split(delimiter)
        if len(question_and_choices) == 1:
            return await ctx.send("Not enough choices supplied")
        elif len(question_and_choices) >= 31:
            return await ctx.send("Too many choices")
        question, *choices = question_and_choices
        choices = [x.lstrip() for x in choices]
        print(choices)
        header = {"Content-Type": "application/json"}
        payload = {
            "title": question,
            "options": choices,
            "multi": False
        }
        print(payload)
        async with self.bot.session.post("https://www.strawpoll.me/api/v2/polls", headers=header, json=payload) as r:
            data = await r.json()
        print(data)
        id = data["id"]
        await ctx.send(f"http://www.strawpoll.me/{id}")


def setup(bot):
    bot.add_cog(Polls(bot))

def get_definition(word, count):
  url = f"http://api.urbandictionary.com/v0/define?term={word}"
  response = requests.get(url)
  data = response.json()
  if not data['list']:
    return f"No definition found for {word}"
  else:
    return data['list'][count]['definition']

def crazy(triangle):
  biangle = get_definition(triangle, 0)
  biangle = biangle.replace("[", "")
  biangle = biangle.replace("]", '')
  hexangle = biangle.split()
  noangle = random.choice(hexangle)
  quadrangle = random.choice(hexangle)
  pentangle = f"""
  {triangle}?
  I was a {triangle} once.
  They locked me in a room.
  A {quadrangle} room.
  A {quadrangle} room with {noangle}.
  And {noangle} makes me {triangle}.
  {triangle}?
  """
  return pentangle
  
def rgbToAnsi(r, g, b, text):
  return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

@bot.tree.command(name="rgbtest")
async def rgbtest(interaction: discord.Interaction):
  await interaction.response.send_message(rgbToAnsi(108, 35, 217, "Hello"))
  
keep_alive()  
bot.run(os.getenv("TOKEN"))
#Copyright (c) 2023 Something231, CaptainDeathead, LachlanORourke 