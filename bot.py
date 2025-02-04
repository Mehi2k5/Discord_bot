import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

thank_you = ["thank you", "thanks", "tysm", "tks"]
GG = ["you are welcome", "nothing", "my pleasure"]
Hello = ["hello", "Hello", "lô"]
sad_word = ["sad", "depressing", "tired", "unhappy", "miserable" ]
rickroll = ["rickroll","Rickroll"]

starter_encouragements = [
  "Hang in there",
  "you are a great person/bot"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
 print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg= message.content

  if msg.startswith('inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_word):
    await message.channel.send(random.choice(starter_encouragements))

  if msg.startswith('yo'):
    await message.channel.send('yo')

  if any(word in msg for word in thank_you):
    await message.channel.send(random.choice(GG))

  if any(word in msg for word in Hello):
    await message.channel.send('lô con c')
  
  if any(word in msg for word in rickroll ):
    await message.channel.send('Never gonna give you up, Never gonna let you down, Never gonna run around and desert you')

keep_alive()
client.run(os.getenv('GG'))
