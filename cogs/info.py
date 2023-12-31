import discord

from discord import app_commands
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        

    @app_commands.command(name="about", description="About the Zephyr bot")
    async def about(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="⚡ About Zephyr",
            description="✨ Zephyr is a Discord bot created for the Capital Gaming server. This bot helps us manage things like moderation, info, FAQ, and some fun things.",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


    @app_commands.command(name="help", description="Help with the Zephyr bot")
    async def help(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="❓ Help",
            description="📖 Zephyr is a Discord bot created for the Capital Gaming server",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


    @app_commands.command(name="invite", description="Invite the Zephyr bot")
    async def invite(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="📨 Invite",
            description="📩 Zephyr is a Discord bot created for the Capital Gaming server",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


    @app_commands.command(name="ping", description="Ping the Zephyr bot")
    async def ping(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="🌐 Ping",
            description=f"**Latency:** `{round(self.bot.latency * 1000)}ms`",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
