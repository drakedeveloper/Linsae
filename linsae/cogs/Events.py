import discord
import time
import asyncio
from datetime import datetime
import time
from discord.ext import tasks, commands
from tinydb import TinyDB, Query
import re




class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        role = await guild.create_role(name="Muted", colour=discord.Colour.dark_grey())
        for channel in guild.channels:
            await channel.set_permissions(role, send_messages = False)

        await asyncio.sleep(delay=5)
        for member in guild.members:
            if member.guild_permissions.administrator and member.id != self.bot.user.id:
                join_message = discord.Embed(title="__**Linsae!**__",
                                             description=f"**Hello, {member.mention}, This is me linsae and in order for me to work you need to do some configuration, sooo let's get started!**",
                                             colour=0x4298f4, timestamp=datetime.utcnow())
                join_message.add_field(name="__Knowledge__",
                                       value=f"""**First of all, {member.mention} let me introduce my self:
    - My name as you know is Linsae and i'm glad to meet you.
    - My developer is Ɗrake#7418 and if you need any help with bots or something feel free to contact him!
    - My birthday is 6/25/2019.**""")
                join_message.add_field(name="__Configuration__", value=""" Alright so i'm a support bot that helps moderators and make their lifes easier, so what do i do ?
    .If a member needs help with something he can just type ***?support*** in a specific channel that i will menion later.
    .i have many moderator commands like ban, warn, kick, mute and more....
    --> Now in order to do all that the i need to config somethings in the server and don't worry i won't do harm to it!i will just create some channels and roles and ask you things but for that to work you need to type ***?ticketconfig*** in any channel  and i will give you instructions!""")
                join_message.set_footer(
                    text="For more help just try to read this embed again or contact the developer!",
                    icon_url=self.bot.user.avatar_url)
                join_message.set_author(name=self.bot.user)
                join_message.set_thumbnail(url=guild.icon_url)
                await member.send(embed=join_message)
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel) == "ticket-request":
            if message.content != "?support":
                await message.delete()
        if message.content == "nigga" or  message.content == "nigger" or message.content == "nigro":
            await message.delete()
            await message.channel.send("You can't say that!")
def setup(bot):
    bot.add_cog(Events(bot))