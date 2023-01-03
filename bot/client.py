"""This module is for creating client for the bot."""
import discord
import logging

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)
