import discord
import time
import asyncio
from datetime import datetime
import time
from discord.ext import tasks, commands
from tinydb import TinyDB, Query
import re



class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        msg = await ctx.channel.send("🤚 i'm gonna send you a dm with the commands! make sure that your dms are open!")
        await msg.delete(delay=5)
        embed1 = discord.Embed(title='__Help__', description=f"""Hello, {ctx.message.author.mention}, to get help react either with:
🇲: to get help about moderation commands.
🇹: to get help about the ticket system.""", colour=0x5bff14, timestamp=datetime.utcnow())
        embed1.add_field(name="**Prefix**", value="The bot's prefix is ?")
        embed1.set_thumbnail(url=self.bot.user.avatar_url)
        embed1.set_footer(text="Made by Ɗrake#7418", icon_url=self.bot.user.avatar_url)
        msg = await ctx.message.author.send(embed=embed1)
        await msg.add_reaction("🇲")
        await msg.add_reaction("🇹")
        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '🇲' or str(reaction.emoji) == '🇹' and reaction.message == msg


        reaction, user = await self.bot.wait_for('reaction_add', check=check)
        if str(reaction.emoji) == '🇲':
            embed =discord.Embed(title='__Moderation__', description=f"""Those are the commands of moderation""", colour=0x5bff14, timestamp=datetime.utcnow())
            embed.add_field(name="**Logchannel**", value="This command is used to to specify the log channel for the bot and it's necessary use it on this format: ?logchannel [mention channel], example: ?logchannel #linsae-logs")
            embed.add_field(name="**Ban**", value="This command is used to ban members without a timestamp and you can use it on this format: ?ban [member] [optional reason], example; ?ban @Ɗrake#7418 toxic")
            embed.add_field(name="**Tempban**",
                            value="This command is used to ban members temporarily and you can use it on this format: ?ban [member] [timestamp] [optional reason], ?tempban @Ɗrake#7418 1mo2w1d2h3m toxic, notice mo for monthn w for week, d for day, h for hour and m four minutes and you can choose to specify some of them or not, example: ?tempban @Ɗrake#7418 1h toxic")
            embed.add_field(name="**Unban**",
                            value="This command is used to unban members without a timestamp and you can use it on this format: ?unban [member_id] [optional reason], example; ?unban @168704474066452481 reason")
            embed.add_field(name="**Kick**",
                            value="This command is used to kick members and you can use it on this format: ?kick [member] [optional reason], example; ?kick @Ɗrake#7418 toxic")
            embed.add_field(name="**Warn**",
                            value="This command is used to warn members and you can use it on this format: ?warn [member] [optional reason], example; ?warn @Ɗrake#7418 toxic, Notice: 3 warnings = tempban for 2 hours")
            embed.add_field(name="**Dewarn**",
                            value="This command is used to remove the warns from specifique member and you can use it on this format: ?dewarn [member] [optional reason], example; ?dewarn @Ɗrake#7418 acting good.")
            embed.add_field(name="**Warnings**",
                            value="This command is used to get the member warnings and you can use it on this format: ?warnings [member], example; ?warnings @Ɗrake#7418, Notice: if member is not defined then it return the message author warnings.")
            embed.add_field(name="**Tempmute**",
                            value="This command is used to mute members temporarily and you can use it on this format: ?tempmute [member] [timestamp] [optional reason], ?tempmute @Ɗrake#7418 1mo2w1d2h3m toxic, notice mo for monthn w for week, d for day, h for hour and m four minutes and you can choose to specify some of them or not, example: ?tempmute @Ɗrake#7418 1h toxic")
            embed.add_field(name="**Unmute**",
                            value="This command is used to unmute members without a timestamp and you can use it on this format: ?unmute [member] [optional reason], example; ?unmute @Ɗrake#7418 reason")
            embed.add_field(name="**Lock**",
                            value="This command is used to lock the channel and you can use it on this format: ?lock .")
            embed.add_field(name="**Unlock**",
                            value="This command is used to unlock the channel and you can use it on this format: ?unlock ")
            embed.add_field(name="**Clear**",
                            value="This command is used to an ammout of messages from a  channel and you can use it on this format: ?clear [ammount of messages], example: ?clear 10 .")
            embed.add_field(name="**Slowmode**",
                            value="This command is used to set slowmode for a  channel and you can use it on this format: ?slowmode [delay per seconds], example: ?slowmode 10, Notice: to stop the slowmode write: ?slowmode 0.")
            embed.add_field(name="**Ticket system**",
                            value="if you wanna get help about the ticket system just type help in any chat and react with 🇹.")
            embed1.add_field(name="Info", value="This command is used to get information about the bot and its creator.")
            embed1.add_field(name="Server", value="This command is used to get information about the server.")
            embed.set_footer(text="Made by Ɗrake#7418", icon_url=self.bot.user.avatar_url)
            await ctx.message.author.send(embed=embed)
        if str(reaction.emoji) == '🇹':
            embed = discord.Embed(title='__Ticket system__', description=f"""Those are the commands of ticket system""",
                                  colour=0x5bff14, timestamp=datetime.utcnow())
            embed1.add_field(name="**Ticketconfig**", value="This command is a must before beginning to use the ticket system, it allows you to setup the channels and roles and category for the ticket system, Notice: never change the role name or names of categories and channel created by the bot.")
            embed.add_field(name="**Support**", value="This command is used to open a ticket and works only on ticket-request channel and you can use it on this format: ?support.")
            embed.add_field(name="**Conversation**", value="This command is used to retrieve conversation history from a ticket and you can use it on this format: ?conversation [conversation_id(you can find within the ticket channel name)], example: ?conversation 10, Notice: please wait some time before using this command when you already finished a ticket..")

            embed.set_footer(text="Made by Ɗrake#7418", icon_url=self.bot.user.avatar_url)
            await ctx.message.author.send(embed=embed)
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="**Info**", color=0x7a42f4, timestamp=datetime.utcnow())
        embed.add_field(name="Dawg",
                        value="This bot is developped by Ɗrake#7418 using python, he's 16 years old and from tunisia ,if you want to get help about the command juste type ?help in any chat")
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def server(self, ctx):
        name = ctx.guild.name
        region = ctx.guild.region
        t_channels = ctx.guild.text_channels
        v_channels = ctx.guild.voice_channels
        channels = ctx.guild.categories
        member = ctx.guild.member_count
        owner = ctx.guild.owner
        c_time = ctx.guild.created_at

        embed = discord.Embed(title=f"{name} Info :", timestamp=datetime.utcnow(), color=0xe842f4)
        embed.add_field(name="Name", value=name)
        embed.add_field(name="Region", value=region)
        embed.add_field(name="Owner", value=owner)
        embed.add_field(name="Categories", value=len(channels))
        embed.add_field(name="Text channels", value=len(t_channels))
        embed.add_field(name="Voice channels", value=len(v_channels))
        embed.add_field(name="Members", value=member)
        embed.add_field(name="Invite link", value="https://discord.gg/QSgUG5D")
        embed.add_field(name="Created at", value=c_time)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(icon_url=self.bot.user.avatar_url, text="Made by Ɗrake#7418")
        await ctx.send(embed=embed)

    @help.error
    async def _help(self, ctx, error):

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

    @info.error
    async def _info(self, ctx, error):

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

    @server.error
    async def _server(self, ctx, error):

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
    bot.add_cog(Info(bot))