import discord
import time
import asyncio
from datetime import datetime
import time
from discord.ext import tasks, commands
from tinydb import TinyDB, Query
import re




class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def logchannel(self, ctx, channel: discord.TextChannel):
        db = TinyDB('db/moderation/logchannel.json')
        db.insert({'guild_id': ctx.guild.id, 'channel_id': channel.id})
        embed = discord.Embed(title="__Moderation__", colour=0xdfe884, timestamp=datetime.utcnow())
        embed.add_field(name="__Type__", value="**Log channel configuration**")
        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
        embed.add_field(name="__Channel__", value=f"-{channel.mention}")
        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        msg = await ctx.message.channel.send(embed=embed)
        await msg.delete(delay=15)
        await channel.send(embed=embed)
        await ctx.message.delete()

    @logchannel.error
    async def log(self, ctx, error):

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


            await msg4.delete(delay=5)
        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def ban(self, ctx, member:discord.Member, *reason):
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't ban a moderator!")
            await msg1.delete(delay=5)
            await ctx.message.delete()
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                    for i in lig:
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed = discord.Embed(title="__Moderation__", colour=0xff0000, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Ban**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed)
                    embed = discord.Embed(title="__Moderation__", colour=0xff0000, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Ban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.ban(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                if len(lig) == 0:
                    embed = discord.Embed(title="__Moderation__", colour=0xff0000, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Ban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.ban(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't ban this user!")
                await msg5.delete(delay=5)

    @ban.error
    async def _ban(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def tempban(self, ctx, member: discord.Member, timestamp, *reason):
        timestr = timestamp
        regex = "^(?:(?P<months>\d)mo)?(?:(?P<weeks>\d{1,2})w)?(?:(?P<days>\d{1,2})d)?(?:(?P<hours>\d{1,4})h)?(?:(?P<minutes>\d{1,5})m)?$"
        match = re.search(regex, timestr)
        months = match.group('months')
        weeks = match.group('weeks')
        days = match.group('days')
        hours = match.group('hours')
        minutes = match.group('minutes')
        if months!= None:
            months_s = int(months) * 2629800
        if weeks != None:
            week_s = int(weeks) * 604800
        if days != None:
            days_s = int(days) * 86400
        if hours != None:
            hours_s = int(hours) * 3600
        if minutes != None:
            minutes_s = int(minutes) * 60
        if months == None:
            months_s = 0
        if weeks == None:
           week_s = 0
        if days == None:
            days_s = 0
        if hours == None:
            hours_s = 0
        if minutes == None:
            minutes_s = 0
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't ban a moderator!")
            await msg1.delete(delay=5)
            await ctx.message.delete()
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                    for i in lig:
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed = discord.Embed(title="__Moderation__", colour=0xcf3a3a, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Tempban**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed)
                    embed = discord.Embed(title="__Moderation__", colour=0xcf3a3a, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Tempban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.ban(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                    await asyncio.sleep(months_s + week_s + days_s + hours_s + minutes_s)
                    await ctx.guild.unban(member)

                if len(lig) == 0:
                    embed = discord.Embed(title="__Moderation__", colour=0xcf3a3a, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Tempban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.ban(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                    await asyncio.sleep(months_s + week_s + days_s + hours_s + minutes_s)
                    await ctx.guild.unban(member)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't ban this user!")
                await msg5.delete(delay=5)

    @tempban.error
    async def _tempban(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def unban(self, ctx, member, *reason):
        try:
            user = self.bot.get_user(int(member))
            await ctx.message.delete()
            if int(member) != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                    for i in lig:
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed = discord.Embed(title="__Moderation__", colour=0x3acf8c, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Unban**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed)
                    embed = discord.Embed(title="__Moderation__", colour=0x3acf8c, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Unban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.unban(user)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                if len(lig) == 0:
                    embed = discord.Embed(title="__Moderation__", colour=0x3acf8c, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Unban**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.unban(user)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't use this command like this!")
                await msg5.delete(delay=5)
        except TypeError as error:
            await ctx.channel.send("You need to type a real id of a user!")
    @unban.error
    async def _unban(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing requirement!')
            await msg1.delete(delay=5)
        if isinstance(error, commands.MissingRole):
            msg = await ctx.send('<:stop:587970807909842944> Ops! you can not use that command!')
            await msg.delete(delay=5)
        if isinstance(error, commands.BadArgument):
            msg2 = await ctx.send(
                '<:stop:587970807909842944> Something is wrong, try again, are you sure that user is banned?!')
            await msg2.delete(delay=5)

        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def tempmute(self, ctx, member: discord.Member, timestamp, *reason):
        timestr = timestamp
        regex = "^(?:(?P<months>\d)mo)?(?:(?P<weeks>\d{1,2})w)?(?:(?P<days>\d{1,2})d)?(?:(?P<hours>\d{1,4})h)?(?:(?P<minutes>\d{1,5})m)?$"
        match = re.search(regex, timestr)
        months = match.group('months')
        weeks = match.group('weeks')
        days = match.group('days')
        hours = match.group('hours')
        minutes = match.group('minutes')
        if months != None:
            months_s = int(months) * 2629800
        if weeks != None:
            week_s = int(weeks) * 604800
        if days != None:
            days_s = int(days) * 86400
        if hours != None:
            hours_s = int(hours) * 3600
        if minutes != None:
            minutes_s = int(minutes) * 60
        if months == None:
            months_s = 0
        if weeks == None:
            week_s = 0
        if days == None:
            days_s = 0
        if hours == None:
            hours_s = 0
        if minutes == None:
            minutes_s = 0
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't mute a moderator!")
            await msg1.delete(delay=5)
            await ctx.message.delete()
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                        for i in lig:
                            role = discord.utils.get(ctx.guild.roles, name="Muted")
                            await member.add_roles(role)
                            global channel1
                            channel_id1 = i['channel_id']
                            channel1 = self.bot.get_channel(int(channel_id1))
                            embed = discord.Embed(title="__Moderation__", colour=0xe8aa00, timestamp=datetime.utcnow())
                            embed.add_field(name="__Type__", value="**Tempmute**")
                            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                            embed.add_field(name="__Member__", value=f"-{member.mention}")
                            embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                            embed.add_field(name="__Log channel__",
                                            value=f"-{channel1.mention}")
                            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            await channel1.send(embed=embed)
                        embed = discord.Embed(title="__Moderation__", colour=0xe8aa00, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Tempmute**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        msg = await ctx.message.channel.send(embed=embed)
                        await ctx.message.delete()
                        await msg.delete(delay=15)
                        await asyncio.sleep(months_s + week_s + days_s + hours_s + minutes_s)
                        await member.remove_roles(role)

                if len(lig) == 0:
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    await member.add_roles(role)
                    embed = discord.Embed(title="__Moderation__", colour=0xe8aa00, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Tempmute**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Timestamp__", value=f"-{timestamp}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                    await asyncio.sleep(months_s + week_s + days_s + hours_s + minutes_s)
                    await member.remove_roles(role)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't mute this user!")
                await msg5.delete(delay=5)

    @tempmute.error
    async def _tempmute(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *reason):
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't unmute a moderator!")
            await msg1.delete(delay=5)
            await ctx.message.delete()
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                    for i in lig:
                        role = discord.utils.get(ctx.guild.roles, name="Muted")
                        await member.remove_roles(role)
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed = discord.Embed(title="__Moderation__", colour=0x74e800, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Unmute**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed)
                    embed = discord.Embed(title="__Moderation__", colour=0x74e800, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Unmute**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                if len(lig) == 0:
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    await member.remove_roles(role)
                    embed = discord.Embed(title="__Moderation__", colour=0x74e800, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Unmute**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't unmute this user!")
                await msg5.delete(delay=5)

    @ban.error
    async def _unmute(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, *reason):
        if member.guild_permissions.administrator:
            msg1 = await ctx.message.channel.send("🚫, you can't kick a moderator!")
            await msg1.delete(delay=5)
            await ctx.message.delete()
        if member.guild_permissions.administrator == False:
            if member.id != ctx.message.author.id or member.id != self.bot.user.id:
                db = TinyDB('db/moderation/logchannel.json')
                Log = Query()
                lig = db.search(Log.guild_id == ctx.guild.id)
                if len(lig) != 0:
                    for i in lig:
                        global channel1
                        channel_id1 = i['channel_id']
                        channel1 = self.bot.get_channel(int(channel_id1))
                        embed = discord.Embed(title="__Moderation__", colour=0xff2929, timestamp=datetime.utcnow())
                        embed.add_field(name="__Type__", value="**Kick**")
                        embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                        embed.add_field(name="__Member__", value=f"-{member.mention}")
                        embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                        embed.add_field(name="__Log channel__",
                                        value=f"-{channel1.mention}")
                        embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                        embed.set_thumbnail(url=ctx.guild.icon_url)
                        await channel1.send(embed=embed)
                    embed = discord.Embed(title="__Moderation__", colour=0xff2929, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Kick**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.kick(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
                if len(lig) == 0:
                    embed = discord.Embed(title="__Moderation__", colour=0xff2929, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Kick**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Member__", value=f"-{member.mention}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    msg = await ctx.message.channel.send(embed=embed)
                    await ctx.guild.kick(member)
                    await ctx.message.delete()
                    await msg.delete(delay=15)
            if member.id == ctx.message.author.id or member.id == self.bot.user.id:
                msg5 = await ctx.message.channel.send("🚫, you can't kick this user!")
                await msg5.delete(delay=5)

    @kick.error
    async def _kick(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, *reason):
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        db = TinyDB('db/moderation/logchannel.json')
        Log = Query()
        lig = db.search(Log.guild_id == ctx.guild.id)
        if len(lig) != 0:
            for i in lig:
                global channel1
                channel_id1 = i['channel_id']
                channel1 = self.bot.get_channel(int(channel_id1))
                embed = discord.Embed(title="__Moderation__", colour=0xc421ac, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Lock**")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"-{channel1.mention}")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                await channel1.send(embed=embed)
            embed = discord.Embed(title="__Moderation__", colour=0xc421ac, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Lock**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"-{channel1.mention}")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.message.channel.set_permissions(role,
                                                      send_messages=False)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.delete()
            await msg.delete(delay=15)
        if len(lig) == 0:
            embed = discord.Embed(title="__Moderation__", colour=0xc421ac, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Lock**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.channel.set_permissions(role,
                                                      send_messages=False)
            await ctx.message.delete()
            await msg.delete(delay=15)
    @lock.error
    async def _lock(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(manage_channels=True)

    async def unlock(self, ctx, *reason):
        role = discord.utils.get(ctx.guild.roles, name='@everyone')
        db = TinyDB('db/moderation/logchannel.json')
        Log = Query()
        lig = db.search(Log.guild_id == ctx.guild.id)
        if len(lig) != 0:
            for i in lig:
                global channel1
                channel_id1 = i['channel_id']
                channel1 = self.bot.get_channel(int(channel_id1))
                embed = discord.Embed(title="__Moderation__", colour=0x4d8c3f, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Unlock**")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"-{channel1.mention}")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                await channel1.send(embed=embed)
            embed = discord.Embed(title="__Moderation__", colour=0x4d8c3f, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Unlock**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"-{channel1.mention}")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.message.channel.set_permissions(role,
                                                      overwrite=None)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.delete()
            await msg.delete(delay=15)
        if len(lig) == 0:
            embed = discord.Embed(title="__Moderation__", colour=0x4d8c3f, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Unlock**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.channel.set_permissions(role,
                                                      overwrite=None)
            await ctx.message.delete()
            await msg.delete(delay=15)

    @unlock.error
    async def _unlock(self, ctx, error):

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


        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number:int, *reason):
        mgs = []  # Empty list to put all the messages in the log
        number = int(number)  # Converting the amount of messages to delete to an integer
        async for x in ctx.message.channel.history(limit=number):
            mgs.append(x)

        db = TinyDB('db/moderation/logchannel.json')
        Log = Query()
        lig = db.search(Log.guild_id == ctx.guild.id)
        if len(lig) != 0:
            for i in lig:
                global channel1
                channel_id1 = i['channel_id']
                channel1 = self.bot.get_channel(int(channel_id1))
                embed = discord.Embed(title="__Moderation__", colour=0x4842f5, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Purge**")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"-{channel1.mention}")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                await channel1.send(embed=embed)
            embed = discord.Embed(title="__Moderation__", colour=0x4842f5, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Purge**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"-{channel1.mention}")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.message.channel.delete_messages(mgs)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.delete()
            await msg.delete(delay=15)
        if len(lig) == 0:
            embed = discord.Embed(title="__Moderation__", colour=0x4842f5, timestamp=datetime.utcnow())
            embed.add_field(name="__Type__", value="**Purge**")
            embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
            embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
            embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
            embed.add_field(name="__Log channel__",
                            value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
            embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            msg = await ctx.message.channel.send(embed=embed)
            await ctx.message.channel.delete_messages(mgs)
            await ctx.message.delete()
            await msg.delete(delay=15)

    @clear.error
    async def _clear(self, ctx, error):

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



        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, time, *reason):
        if int(time) == 0:
            db = TinyDB('db/moderation/logchannel.json')
            Log = Query()
            lig = db.search(Log.guild_id == ctx.guild.id)
            if len(lig) != 0:
                for i in lig:
                    channel_id1 = i['channel_id']
                    channel1 = self.bot.get_channel(int(channel_id1))
                    embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Slowmode**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                    embed.add_field(name="__Delay__", value=f"-Off")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    await channel1.send(embed=embed)
                embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Slowmode**")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Delay__", value=f"-Off")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"-{channel1.mention}")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg = await ctx.message.send(embed=embed)
                await ctx.message.channel.edit(slowmode_delay=0)
                await ctx.message.delete()
                await msg.delete(delay=15)
            if len(lig) == 0:
                embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Slowmode **")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Delay__", value=f"-Off")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg = await ctx.message.channel.send(embed=embed)
                await ctx.message.channel.edit(slowmode_delay=0)
                await ctx.message.delete()
                await msg.delete(delay=15)
        if int(time) != 0 and int(time) < 21600:
            db = TinyDB('db/moderation/logchannel.json')
            Log = Query()
            lig = db.search(Log.guild_id == ctx.guild.id)
            if len(lig) != 0:
                for i in lig:
                    channel_id1 = i['channel_id']
                    channel1 = self.bot.get_channel(int(channel_id1))
                    embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                    embed.add_field(name="__Type__", value="**Slowmode**")
                    embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                    embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                    embed.add_field(name="__Delay__", value=f"-{time}")
                    embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                    embed.add_field(name="__Log channel__",
                                    value=f"-{channel1.mention}")
                    embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                    embed.set_thumbnail(url=ctx.guild.icon_url)
                    await channel1.send(embed=embed)
                embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Slowmode**")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Delay__", value=f"- {time}")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"-{channel1.mention}")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg = await ctx.message.send(embed=embed)
                await ctx.message.channel.edit(slowmode_delay=int(time))
                await ctx.message.delete()
                await msg.delete(delay=15)
            if len(lig) == 0:
                embed = discord.Embed(title="__Moderation__", colour=0xd1f542, timestamp=datetime.utcnow())
                embed.add_field(name="__Type__", value="**Slowmode **")
                embed.add_field(name="__Moderator__", value=f"-{ctx.message.author.mention}")
                embed.add_field(name="__Channel__", value=f"-{ctx.message.channel.mention}")
                embed.add_field(name="__Delay__", value=f"-{time}")
                embed.add_field(name="__Reason__", value=f"-{' '.join(reason)}")
                embed.add_field(name="__Log channel__",
                                value=f"To setup the log channel do ?logchannel [channel mention] or just type ?help to know more about it.")
                embed.set_footer(text="?help for help", icon_url=self.bot.user.avatar_url)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                msg = await ctx.message.channel.send(embed=embed)
                await ctx.message.channel.edit(slowmode_delay=int(time))
                await ctx.message.delete()
                await msg.delete(delay=15)

    @slowmode.error
    async def _slowmode(self, ctx, error):

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

        if isinstance(error, commands.CommandOnCooldown):
            msg9 = 'This command is ratelimited, please try again in {:.2f}seconds'.format(error.retry_after)
            msg6 = await ctx.send(msg9)
            await msg6.delete(delay=5)
        if isinstance(error, commands.MissingPermissions):
            msg1 = await ctx.send('<:stop:587970807909842944> Missing permission!')
            await msg1.delete(delay=5)
def setup(bot):
    bot.add_cog(Moderation(bot))
