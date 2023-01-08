"""This module is for creating client for the bot."""
import discord
import logging
from discord.ext import commands
from .TOKEN import TOKEN
from .youtube import Music

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Discord music bot',
    intents=intents,
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.event  # dm_only() ???
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        print(message)
        if "channel=<DMChannel" in message:
            # message.content.startswith('https://www.youtube.'):
            await message.channel.send('Hello!')
            logging.info("sent message: %s", message.content)


async def main():
    async with bot:
        await bot.add_cog(Music(bot))
        await bot.start(TOKEN)
