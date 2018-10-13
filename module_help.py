#!/usr/bin/env python3.5
import asyncio
import discord
import json
import random
import time

from discord.ext import commands
from pixie_function import *

import config as cfg

class Help:

    def __init__(self, bot):
        self.bot = bot

    def __unload(self):
        pass

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """Help message generator."""
        listmodules = readData('main')
        serverlistmodules = readData('server', ctx.message.author.server.id)
        if ctx.message.author == self.bot.user:
            return
        # botmaster help command
        if ctx.message.author.id == '258418027844993024':
            embed = discord.Embed(description=':gear: Botmaster Commands list :', colour=0x7289da, timestamp=datetime.datetime.utcnow())
            embed.add_field(name='!load', value='Load bot modules.', inline=False)
            embed.add_field(name='!unload', value='Unload bot modules.', inline=False)
            embed.add_field(name='!reload', value='Reload given bot modules or all.', inline=False)
            embed.add_field(name='!checkmodule', value='Check modules parsing.', inline=False)
            embed.add_field(name='!quit', value='Close connexion and stop bot instance.', inline=False)
            await self.bot.send_message(ctx.message.channel, embed=embed)
        # server admin help command
        if ctx.message.author.id == ctx.message.author.server.owner.id:
            embed = discord.Embed(description=':gear: Admin Commands list :', colour=0x7289da, timestamp=datetime.datetime.utcnow())
            embed.add_field(name='!enable', value='Enable bot module for your server.', inline=False)
            embed.add_field(name='!disable', value='Disable bot module for your server.', inline=False)
            embed.add_field(name='!config', value='Edit bot modules configuration.', inline=False)
            embed.add_field(name='!checkconfig', value='Check modules configuration.', inline=False)
            await self.bot.send_message(ctx.message.channel, embed=embed)
        # admin/mod help command
        # regular help command
        embed = discord.Embed(description=':gear: Commands list :', colour=0x7289da, timestamp=datetime.datetime.utcnow())
        if (listmodules["help"]["last"] == "loaded" and serverlistmodules["help"]["last"] == "enabled"):
            embed.add_field(name='!help', value='Affiche ce message.', inline=False)
        if (listmodules["misc"]["last"] == "loaded" and serverlistmodules["misc"]["last"] == "enabled"):
            embed.add_field(name='!flip', value='Pile ou face.', inline=False)
            embed.add_field(name='!ping', value='Pong !', inline=False)
            embed.add_field(name='!rand', value='Random sur base du nombre donné.', inline=False)
            embed.add_field(name='!roll', value='Je lance un dé à 6 faces.', inline=False)
        if (listmodules["jokes"]["last"] == "loaded" and serverlistmodules["jokes"]["last"] == "enabled"):
            embed.add_field(name='!joke', value='Je raconte une blague.', inline=False)
        if (listmodules["poll"]["last"] == "loaded" and serverlistmodules["poll"]["last"] == "enabled"):
            embed.add_field(name='!poll', value='Sondage express.', inline=False)
        await self.bot.send_message(ctx.message.channel, embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))