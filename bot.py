import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

# Set up intents
intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

thank_you = ["thank you", "thanks", "tysm", "tks"]
GG = ["you are welcome", "nothing", "my pleasure"]
Hello = ["hello", "Hello", "lô"]
sad_word = ["sad", "depressing", "tired", "unhappy", "miserable"]
rickroll = ["rickroll", "Rickroll"]

starter_encouragements = [
    "Hang in there",
    "You are a great person/bot"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()  # Convert message to lowercase to make it case-insensitive

    if msg.startswith('inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif any(word in msg for word in sad_word):
        await message.channel.send(random.choice(starter_encouragements))

    elif msg.startswith('yo'):
        await message.channel.send('yo')

    elif any(word in msg for word in thank_you):
        await message.channel.send(random.choice(GG))

    elif any(word in msg for word in Hello):
        await message.channel.send('lô con c')

    elif any(word in msg for word in rickroll):
        await message.channel.send('Never gonna give you up, Never gonna let you down, Never gonna run around and desert you')

# Keep the bot alive on Replit
keep_alive()

# Run the bot
TOKEN = os.getenv('GG')
if TOKEN:
    client.run(TOKEN)
else:
    print("Error: Bot token not found. Make sure to set the GG environment variable.")
