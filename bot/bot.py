import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='', intents=discord.Intents.all())

cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")


for root, _, files in os.walk(cogs_dir):
    module_base = os.path.relpath(root, cogs_dir).replace(os.sep, '.')

    for file in files:
        if file.endswith('.py') and not file.startswith('__'):
            cog_name = file[:-3]  # Remove .py extension
            cog_path = f'bot.cogs.{module_base}.{cog_name}' if module_base != '.' else f'bot.cogs.{cog_name}'
            bot.load_extension(cog_path)


def run(token):
    bot.run(token)
