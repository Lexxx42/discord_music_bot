"""This module is for user's handles."""
import logging
from .. import client


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    logging.info(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://www.youtube.'):
        await message.channel.send('Hello!')
        logging.info("sent message: %s", message.content)
