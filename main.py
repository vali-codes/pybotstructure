import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title= "Bot Ping",
        description= f'Ping: {round(client.latency * 1000)}ms',
        color= discord.Color.blue()
    )
    await ctx.send(embed=embed)

client.run(os.environ.get('TOKEN'))


