import os
import random
import discord
from discord.ext import commands, tasks


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'splashes.txt'), encoding='utf-8') as s:
    splashes = [line.strip() for line in s.readlines() if line.strip()]


class Activity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_status.start()

    @tasks.loop(hours=1)
    async def update_status(self):
        try:
            splash = random.choice(splashes)
            await self.bot.change_presence(activity=discord.Game(name=splash))
            print(f"Updated activity: {splash}")
        except Exception as e:
            print(f"An error occurred when updating the activity: {e}")

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()


def setup(bot: commands.Bot):
    bot.add_cog(Activity(bot))
