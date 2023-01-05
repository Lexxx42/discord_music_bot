"""This module is for user's handles."""
import logging
import discord

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
        channel = message.channel.id
        print(channel)
        # await channel.connect()


@client.command(name='join', aliases=['summon'])  # CREATING COMMAND "JOIN" WITH ALIAS SUMMON
async def _join(ctx, *,
                channel: discord.VoiceChannel = None):  # TAKING ARGUMENT CHANNEL SO PPL CAN MAKE THE BOT JOIN A VOICE CHANNEL THAT THEY ARE NOT IN
    """Joins a voice channel."""

    destination = channel if channel else ctx.author.voice.channel  # CHOOSING THE DESTINATION, MIGHT BE THE REQUESTED ONE, BUT IF NOT THEN WE PICK AUTHORS VOICE CHANNEL

    if ctx.voice_client:  # CHECKING IF THE BOT IS PLAYING SOMETHING
        await ctx.voice_state.voice.move_to(
            destination)  # IF THE BOT IS PLAYING WE JUST MOVE THE BOT TO THE DESTINATION
        return

    await destination.connect()  # CONNECTING TO DESTINATION
    await ctx.send(f"Succesfully joined the voice channel: {destination.name} ({destination.id}).")
