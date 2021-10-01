import discord
from discord.ext import commands
from discord.utils import get
import random
import time

bot_token = "NzY1MjIyMzgwNTYwOTczODQ2.X4Rq4A.qYjcrysfMVuKXIY9OsqJnq17PYU"

words = []
client = commands.Bot(command_prefix="!")

with open("common_words.txt", "r") as words_file:

    for line in words_file:
        words.append(line.strip())


@client.event
async def on_ready():
    print("Online")


@client.event
async def on_message(message):
    silence_role = discord.utils.get(message.author.guild.roles, name="gay")  # trash, the backup Admin role 

    with open("phrase.txt", "r") as phrase_file:
        phrase = phrase_file.read()
        

    if phrase in message.content.lower().split() and str(message.author) != "Silencer#3457":

        time_muted = random.randint(900, 3601)

        await message.channel.send(f"{message.author} has been silenced! The word was \"{phrase.capitalize()}.\" You've been muted for {time_muted//60} minutes.")
        await message.author.add_roles(silence_role)

        with open("phrase.txt", "w") as phrase_file:
            phrase_file.write(words[random.randint(1, 108)])

        time.sleep(time_muted)
        await message.author.remove_roles(silence_role)
 

client.run(bot_token)
