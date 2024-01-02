import os
import sys
import aiohttp

import discord
from discord.ext import commands

# For hot reloading
from cogwatch import watch

from config import Config as cfg

import dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))


intents = discord.Intents.all()


class Zephyr(commands.Bot):
    def __init__(self):

        super().__init__(
            command_prefix=cfg.PREFIX,
            intents=intents,
            allowed_mentions=discord.AllowedMentions(everyone=False),
        )


    async def setup_hook(self):

        cogs = [
            'fun',
            'info',
            'moderation',
            'utility'
        ]

        for cog in cogs:
            await self.load_extension(f'cogs.{cog}')
            print(f'\n+ Loaded {cog}')

        await self.load_extension("jishaku")
        print("\n+ Loaded jishaku\n")

        self.aiohttp_session = aiohttp.ClientSession()

    @watch(path='cogs', preload=True)
    async def on_ready(self):
        print("\n________________________________________________")
        print(f"\n{bot.user} is ready!")
        print(f"Zephyr v{cfg.VERSION}")
        print(f"\nUsing Discord.py {discord.__version__} on Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        print(f"\nRunning on {sys.platform.title()}\n")
        print("________________________________________________\n\n")

        await self.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="you struggle to use me"))


bot = Zephyr()

bot.run(token)
