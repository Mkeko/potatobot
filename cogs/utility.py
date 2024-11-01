# This project is licensed under the terms of the GPL v3.0 license. Copyright 2024 Cyteon

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from utils import Checks

class Utility(commands.Cog, name="⚡ Utility"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_group(
        name="convert",
        description="Commands to convert stuff",
        usage="convert <subcommand>"
    )
    @commands.check(Checks.is_not_blacklisted)
    @commands.check(Checks.command_not_disabled)
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def convert(self, context: Context) -> None:
        prefix = await self.bot.get_prefix(context)

        cmds = "\n".join([f"{prefix}convert {cmd.name} - {cmd.description}" for cmd in self.convert.walk_commands()])

        embed = discord.Embed(
            title=f"Help: Convert", description="List of available commands:", color=0xBEBEFE
        )
        embed.add_field(
            name="Commands", value=f"```{cmds}```", inline=False
        )

        await context.send(embed=embed)

    @convert.command(
        name="mb-gb",
        aliases=["mbgb", "mb-to-gb", "mb2gb"],
        description="Convert megabytes to gigabytes",
    )
    @commands.check(Checks.is_not_blacklisted)
    @commands.check(Checks.command_not_disabled)
    async def convert_mb_gb(self, context: Context, mb: float, binary: bool = True) -> None:
        if binary:
            gb = mb / 1024
        else:
            gb = mb / 1000

        await context.send(f"{mb}MB is equal to {gb}GB")

    @convert.command(
        name="gb-mb",
        aliases=["gbmb", "gb-to-mb", "gb2mb"],
        description="Convert gigabytes to megabytes",
    )
    @commands.check(Checks.is_not_blacklisted)
    @commands.check(Checks.command_not_disabled)
    async def convert_gb_mb(self, context: Context, gb: float, binary: bool = True) -> None:
        if binary:
            mb = gb * 1024
        else:
            mb = gb * 1000

        await context.send(f"{gb}GB is equal to {mb}MB")

    @convert.command(
        name="gb-tb",
        aliases=["gbtb", "gb-to-tb", "gb2tb"],
        description="Convert gigabytes to terabytes",
    )
    @commands.check(Checks.is_not_blacklisted)
    @commands.check(Checks.command_not_disabled)
    async def convert_gb_tb(self, context: Context, gb: float, binary: bool = True) -> None:
        if binary:
            tb = gb / 1024
        else:
            tb = gb / 1000

        await context.send(f"{gb}GB is equal to {tb}TB")

    @convert.command(
        name="tb-gb",
        aliases=["tbg", "tb-to-gb", "tb2gb"],
        description="Convert terabytes to gigabytes",
    )
    @commands.check(Checks.is_not_blacklisted)
    @commands.check(Checks.command_not_disabled)
    async def convert_tb_gb(self, context: Context, tb: float, binary: bool = True) -> None:
        if binary:
            gb = tb * 1024
        else:
            gb = tb * 1000

        await context.send(f"{tb}TB is equal to {gb}GB")

async def setup(bot) -> None:
    await bot.add_cog(Utility(bot))
