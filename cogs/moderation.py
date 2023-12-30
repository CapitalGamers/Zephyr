import discord

from discord import app_commands
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def send_incomplete_command_message(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="Incomplete Command",
            description="This command is undergoing development.",
            color=discord.Color.red()
        )
        embed.set_footer(text="Use /help to see a list of commands")
        await ctx.response.send_message(embed=embed)

    @app_commands.command(name="ban", description="Ban a member")
    async def ban(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="unban", description="Unban a member")
    async def unban(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="kick", description="Kick a member")
    async def kick(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="timeout_add", description="Timeout a member")
    async def timeout_add(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="timeout_remove", description="Remove a timeout from a member")
    async def timeout_remove(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="mute", description="Mute a member")
    async def mute(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="unmute", description="Unmute a member")
    async def unmute(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="purge", description="Purge messages")
    async def purge(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="lock", description="Lock a channel")
    async def lock(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)

    @app_commands.command(name="unlock", description="Unlock a channel")
    async def unlock(self, ctx: discord.Interaction):
        await self.send_incomplete_command_message(ctx)


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))