#!/usr/bin/env python3.5
import asyncio
import discord

from discord.ext import commands
from pixie_function import *

class Welcome:

    def __init__(self, bot):
        self.bot = bot

    def __unload(self):
        pass

    async def on_member_join(self, member):
        serverlistmodules = readData('server', member.server.id)
        if serverlistmodules["welcome"]["last"] == "enabled":
            fmt = serverlistmodules['welcome']['config']['message']['value']
            channel = str(''.join(filter(str.isdigit, serverlistmodules['welcome']['config']['channel']['value'])))
            member.id = '<@' + member.id + '>'
            await self.bot.send_message(self.bot.get_channel(channel), fmt.format(user=member.id))

    async def on_member_remove(self, member):
        serverlistmodules = readData('server', member.server.id)
        if serverlistmodules["welcome"]["last"] == "enabled":
            fmt = '{user} nous a quitté. :wave:'
            channel = str(''.join(filter(str.isdigit, serverlistmodules['welcome']['config']['channel']['value'])))
            await self.bot.send_message(self.bot.get_channel(channel), fmt.format(user=member.name))

def setup(bot):
    bot.add_cog(Welcome(bot))
