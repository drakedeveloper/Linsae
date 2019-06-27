import discord
import time
import asyncio
from datetime import datetime
import time
from discord.ext import tasks, commands
from tinydb import TinyDB, Query

class Warninggsystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def warn(self, ctx, member: discord.Member, *reason):
        await ctx.message.delete()
        db1 = TinyDB('db/moderation/warn.json')
        db = TinyDB('db/moderation/logchannel.json')
        Log = Query()
        Warn = Query()
        li = db1.search(Warn.member_id == member.id)
        lig = db.search(Log.guild_id == ctx.guild.id)
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't warn a moderator!")
            await msg1.delete(delay=5)
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                if len(li) > 1:
                    await ctx.guild.ban(member)
                    if len(lig) != 0:
                        for i in lig:
                            global channel
                            channel_id = i['channel_id']
                            channel = self.bot.get_channel(int(channel_id))
                            embed = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                            embed.add_field(name="__Type__", value="**Temp ban**")
                            embed.add_field(name="__Moderator__", value=f"-{self.bot.user.mention}")
                            embed.add_field(name="__Member__", value=f"-{member.mention}")
                            embed.add_field(name="__Reason__", value=f"-Reached 3 warnings: {' '.join(reason)}")
                            embed.add_field(name="__Log channel__",
                                            value=f"-{channel.mention}")
                            embed.add_field(name="__Time stamp__", value="2 hours")
                            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            await channel.send(embed=embed)
                        embed = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Temp ban**")
                        embed.add_field(name="__Moderator__", value=f"-{self.bot.user.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-Reached 3 warnings: {' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel.mention}")
                        embed.add_field(name="__Time stamp__", value="2 hours")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        msg = await ctx.message.channel.send(embed=embed)
                        await msg.delete(delay=15)
                        db1.remove(Warn.member_id == member.id)
                        await asyncio.sleep(7200)
                        await ctx.guild.unban(member)
                    if len(lig) == 0:
                        embed = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Temp ban**")
                        embed.add_field(name="__Moderator__", value=f"-{self.bot.user.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-Reached 3 warnings: {' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                        embed.add_field(name="__Time stamp__", value="2 hours")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        msg = await ctx.message.channel.send(embed=embed)
                        await msg.delete(delay=15)
                        db1.remove(Warn.member_id == member.id)
                        await asyncio.sleep(7200)
                        await ctx.guild.unban(member)
                elif len(li) < 3:

                    db1.insert({'member_id': member.id, 'guild_id': ctx.guild.id, 'reason': reason,
                            'moderator': f"{ctx.message.author.name}#{ctx.message.author.discriminator}"})
                li1 = db1.search(Warn.member_id == member.id)
                if len(lig) == 0:
                    embed = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Warn**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Warnings__", value=f"-{len(li1)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await msg.delete(delay=15)
                if len(lig) != 0:
                    for i in lig:
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed1 = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                        embed1.add_field(name="__Type__", value="**Warn**")
                        embed1.add_field(name="__Moderator__", value=f"{ctx.message.author.mention}")
                        embed1.add_field(name="__Member__", value=f"{member.mention}")
                        embed1.add_field(name="__Reason__", value=f"{' '.join(reason)}")
                        embed1.add_field(name="__Warnings__", value=f"{len(li1)}")
                        embed1.add_field(name="__Log channel__",
                                         value=f"{channel1.mention}")
                        embed1.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed1.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed1)
                    embed = discord.Embed(title="__Moderation__", colour=0xe89384, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Warn**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Warnings__", value=f"-{len(li1)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await msg.delete(delay=15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't warn this user!")
                await msg5.delete(delay=5)


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def dewarn(self, ctx, member: discord.Member, *reason):
        db1 = TinyDB('db/moderation/warn.json')
        db = TinyDB('db/moderation/logchannel.json')
        Log = Query()
        Warn = Query()
        li = db1.search(Warn.member_id == member.id)
        lig = db.search(Log.guild_id == ctx.guild.id)
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't dewarn a moderator!")
            await msg1.delete(delay=5)

        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                if len(li) == 0:
                    await ctx.message.channel.send("🚫, This member already has 0 warnings!")
                if len(li) != 0:
                    if len(lig) != 0:
                        for i in lig:
                            global channel1
                            channel_id1 = i['channel_id']
                            channel1 = self.bot.get_channel(int(channel_id1))
                            embed = discord.Embed(title="__Moderation__", colour=0xb7e884, timestamp=datetime.utcnow())
                            embed.add_field(name="__Type__", value="**Dewarn**")
                            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                            embed.add_field(name="__Member__", value=f"-{member.mention}")
                            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                            embed.add_field(name="__Warnings__", value=f"-{len(li)}")
                            embed.add_field(name="__Log channel__",
                                            value=f"-{channel1.mention}")
                            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            await channel1.send(embed=embed)
                        embed = discord.Embed(title="__Moderation__", colour=0xb7e884, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Dewarn**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Warnings__", value=f"-{len(li)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        msg = await ctx.message.channel.send(embed=embed)
                        db1.remove(Warn.member_id == member.id)
                        await ctx.message.delete()
                        await msg.delete(15)
                    if len(lig) == 0:
                        embed = discord.Embed(title="__Moderation__", colour=0xb7e884, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Dewarn**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Warnings__", value=f"-{len(li)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        msg = await ctx.message.channel.send(embed=embed)
                        db1.remove(Warn.member_id == member.id)
                        await ctx.message.delete()
                        await msg.delete(15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't dewarn this user!")
                await msg5.delete(delay=5)

    @commands.command()
    async def warnings(self, ctx, member: discord.Member = None):
        db1 = TinyDB('db/moderation/warn.json')
        if member != None:
            Warn = Query()
            li = db1.search(Warn.member_id == member.id)
            if len(li) == 0:
                msg = await ctx.channel.send(f"{member.mention}, has no warnings! all clear sir.")
                await msg.delete(delay=5)
            if len(li) == 1:
                for i in li:
                    embed = discord.Embed(title="__Warnings__", description=f"Those are {member} warnings.",
                                          colour=0xedd500, timestamp=datetime.utcnow())
                    embed.add_field(name="Only one warning", value=f"""Moderator : {i['moderator']}
    Reason: {i['reason']}
    """)
                    embed.add_field(name="__Notice__", value="To remove all the warnings do ?dewarn @member")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg1 = await ctx.channel.send(embed=embed)
                    await msg1.delete(delay=15)

            if len(li) > 1:
                embed = discord.Embed(title="__Warnings__", description=f"Those are {member} warnings.",
                                      colour=0xedd500,
                                      timestamp=datetime.utcnow())
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg2 = await ctx.channel.send(embed=embed)
                await msg2.delete(delay=30)

                for i in li:
                    embed1 = discord.Embed(title="Warning", description=f"""Moderator : {i['moderator']}
    Reason: {i['reason']}
    """, colour=0xedd500, timestamp=datetime.utcnow())
                    embed1.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed1.set_thumbnail(url=ctx.guild.icon_url)
                    msg3 = await ctx.channel.send(embed=embed1)
                    await msg3.delete(delay=30)
        if member == None:
            Warn = Query()
            li = db1.search(Warn.member_id == ctx.message.author.id)
            if len(li) == 0:
                msg = await ctx.channel.send(f"You have no warnings! all clear sir.")
                await msg.delete(delay=5)
            if len(li) == 1:
                for i in li:
                    embed = discord.Embed(title="__Warnings__", description=f"Those are {ctx.message.author} warnings.",
                                          colour=0xedd500, timestamp=datetime.utcnow())
                    embed.add_field(name="Only one warning", value=f"""Moderator : {i['moderator']}
    Reason: {i['reason']}
    """)
                    embed.add_field(name="__Notice__", value="To remove all the warnings do ?dewarn @member")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg1 = await ctx.channel.send(embed=embed)
                    await msg1.delete(delay=15)

            if len(li) > 1:
                embed = discord.Embed(title="__Warnings__", description=f"Those are {ctx.message.author} warnings.",
                                      colour=0xedd500,
                                      timestamp=datetime.utcnow())
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg2 = await ctx.channel.send(embed=embed)
                await msg2.delete(delay=30)

                for i in li:
                    embed1 = discord.Embed(title="Warning", description=f"""Moderator : {i['moderator']}
    Reason: {i['reason']}
    """, colour=0xedd500, timestamp=datetime.utcnow())
                    embed1.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed1.set_thumbnail(url=ctx.guild.icon_url)
                    msg3 = await ctx.channel.send(embed=embed1)
                    await msg3.delete(delay=30)




    @warn.error
    async def _warn(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing requirement!')
            await msg1.delete(delay=5)
        if isinstance(error, commands.MissingRole):
            msg = await ctx.send('<:stop:587970807909842944> Ops! you can not use that command!')
            await msg.delete(delay=5)
        if isinstance(error, commands.BadArgument):
            msg2 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg2.delete(delay=5)

        if isinstance(error, commands.CommandInvokeError):
            msg4 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg4.delete(delay=5)
        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @dewarn.error
    async def _dewarn(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing requirement!')
            await msg1.delete(delay=5)
        if isinstance(error, commands.MissingRole):
            msg = await ctx.send('<:stop:587970807909842944> Ops! you can not use that command!')
            await msg.delete(delay=5)
        if isinstance(error, commands.BadArgument):
            msg2 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg2.delete(delay=5)

        if isinstance(error, commands.CommandInvokeError):
            msg4 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg4.delete(delay=5)
        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @warnings.error
    async def _warnings(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing requirement!')
            await msg1.delete(delay=5)
        if isinstance(error, commands.MissingRole):
            msg = await ctx.send('<:stop:587970807909842944> Ops! you can not use that command!')
            await msg.delete(delay=5)
        if isinstance(error, commands.BadArgument):
            msg2 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg2.delete(delay=5)

        if isinstance(error, commands.CommandInvokeError):
            msg4 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again!')
            await msg4.delete(delay=5)
        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)
def setup(bot):
    bot.add_cog(Warninggsystem(bot))