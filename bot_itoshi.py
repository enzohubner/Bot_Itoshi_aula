import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} esta Online!')

@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send("Hello World!!{ }".format(message.author))
    
client.run("MTE0MDc4MjEzNzYxNjg5NjAzMA.GbeA7O.HPFlG-2flvEmnz9EXjPllWrRjrBIUTq3iJzMRk")