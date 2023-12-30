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
            description="✨ Zephyr is a Discord bot created for the Capital Gaming server",
            color=discord.Color.blurple()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))