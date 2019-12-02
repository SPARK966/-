import discord
import os
from discord import channel

cilent = discord.Client()

@cilent.event
async def on_ready():
    print(cilent.user.id)
    print("실행완료")
    game = discord.Game("24시간 자판기 프리미엄.com")
    await cilent.change_presence(status=discord.Status.online, activity=game)


@cilent.event
async def on_message(message):

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)






access_token = os.environ["BOT TOKEN"]
cilent.run(access_token)
