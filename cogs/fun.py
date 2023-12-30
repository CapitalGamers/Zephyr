import random

import discord

from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        

    @app_commands.command(name="roll", description="Rolls a random number")
    @app_commands.describe(max="The maximum number to roll", min="The minimum number to roll")
    async def roll(self, ctx: discord.Interaction, max: int = 100, min: int = 1):
        if max < min:
            embed = discord.Embed(
                title="Error",
                description="The maximum number cannot be less than the minimum number!",
                color=discord.Color.red()
            )
            await ctx.response.send_message(embed=embed)
            return
        elif max == min:
            embed = discord.Embed(
                title="Error",
                description="The maximum number cannot be equal to the minimum number!",
                color=discord.Color.red()
            )
            await ctx.response.send_message(embed=embed)
            return
        elif max > 1000000:
            embed = discord.Embed(
                title="Error",
                description="The maximum number cannot be greater than 1,000,000!",
                color=discord.Color.red()
            )
            await ctx.response.send_message(embed=embed)
            return
        elif min < 1:
            embed = discord.Embed(
                title="Error",
                description="The minimum number cannot be less than 1!",
                color=discord.Color.red()
            )
            await ctx.response.send_message(embed=embed)
            return
        else:
            embed = discord.Embed(
                title="Roll",
                description=f"You rolled a {random.randint(min, max)} out of a number between {min} and {max}!",
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Use /help to see a list of commands")
            await ctx.response.send_message(embed=embed)


    @app_commands.command(name="coinflip", description="Flips a coin")
    async def coinflip(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="Coinflip",
            description=f"You flipped a {random.choice(['heads', 'tails'])}!",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


    @app_commands.command(name="8ball", description="Ask the magic 8ball a question")
    @app_commands.describe(question="The question to ask the 8ball")
    async def eightball(self, ctx: discord.Interaction, question: str):
        embed = discord.Embed(
            title="8ball",
            description=f"Question: {question}\nAnswer: {random.choice(['Yes', 'No', 'Maybe'])}",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


    @app_commands.command(name="say", description="Make the bot say something")
    @app_commands.describe(message="The message to say")
    async def say(self, ctx: discord.Interaction, message: str):
        await ctx.response.send_message(message)


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))