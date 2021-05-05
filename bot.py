from dotenv import load_dotenv
import discord, os, time
from discord import FFmpegPCMAudio

from discord.ext import commands as discord_commands
from discord.ext.commands import CommandInvokeError
if __name__ == "__main__":
    load_dotenv()
    intents = discord.Intents.all()
    client = discord_commands.Bot(os.getenv('DISCORD_PREFIX'), guild_subscriptions=True, intents=intents, self_bot=False)
    token = os.getenv('DISCORD_TOKEN')
    index = 0
    client.remove_command('help')
    @client.listen('on_message')
    async def on_message(message):
        msg: str = message.content
        if msg.startswith(os.getenv('DISCORD_PREFIX')):
            # grab the user who sent the command
            user=message.author
            channel=user.voice.channel
            # only play music if user is in a voice channel
            if channel!= None:
                # grab user's voice channel
                # create StreamPlayer
                voice = await channel.connect()
                source = FFmpegPCMAudio(executable="./ffmpeg.exe", source='./campana.mp3')
                player = voice.play(source)
                time.sleep(5)
                voice.disconnect()
    client.run(token)