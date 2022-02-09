import discord
import os
import LolChess

# instantiate LolChess class from LolChess.py
igname = "rudyr"
elo = LolChess.LolChessPage(igname)

client = discord.Client()

@client.event
async def on_ready():

  game = discord.Game("with your feelings ✨")
  await client.change_presence(status=discord.Status.idle, activity=game)

  print(f"{client.user} is now online!")

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith(f"!r elo"):

    current_elo = elo.send_elo()

    print(current_elo) ### for testing

    await msg.channel.send(current_elo)

  if msg.content.startswith(f"!r help"):

    await msg.channel.send("try using these commands:\n```!r help\n!r elo```")

client.run(os.getenv('TOKEN'))