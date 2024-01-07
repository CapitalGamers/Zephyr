import discord

from discord import app_commands
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leave", description="Leave the server")
    async def leave(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="Incomplete Command",
            description="This command is undergoing development.",
            color=discord.Color.red(),
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))
