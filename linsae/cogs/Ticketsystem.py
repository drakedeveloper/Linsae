import discord
import time
import asyncio
from datetime import datetime
import time
from discord.ext import tasks, commands
from tinydb import TinyDB, Query


async def is_support(ctx):
    return str(ctx.channel) == "ticket-request"

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ticketconfig(self, ctx):
        await ctx.message.delete()
        ctx_channel = ctx.channel
        guild = ctx.message.guild
        config_message = discord.Embed(title="__**Configuration**__",
                                       description="**Configuration gonna start right now! but in order to do that we need a little confirmation and you can do that by just clicking on the risen hand!**",
                                       colour=0xf44141, timestamp=datetime.utcnow())
        config_message.add_field(name="__Notice__", value="""**This is what the command gonna do:**
                                                          1.Create a category for the tickets.
                                                          2.Create ticket request channel.
                                                          3.Create necessary role for ticket request.(make sure my role is above (everyone role))""")
        config_message.set_footer(text="For more help just type ?help in any channel", icon_url=self.bot.user.avatar_url)
        config_message.set_author(name=self.bot.user, url=self.bot.user.avatar_url)
        config_message.set_thumbnail(url=ctx.guild.icon_url)
        msg_c = await ctx_channel.send(embed=config_message)
        await msg_c.delete(delay=60)
        emoji = "✋"
        await msg_c.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == emoji

        try:
            global channel
            reaction, user = await self.bot.wait_for('reaction_add', check=check)
            await msg_c.delete()
            role = await guild.create_role(name="Ticket on")
            category = await guild.create_category_channel(name="Tickets", reason="Linsae Configuration")
            overwrites = {
                role: discord.PermissionOverwrite(send_messages=False, read_messages=True)
            }
            channel = await guild.create_text_channel(name="ticket-request", category=category, overwrites=overwrites)
            config_message1 = discord.Embed(title="__**Configuration**__",
                                            description="**Configuration is one step to be over.**",
                                            colour=0xf48f42, timestamp=datetime.utcnow())
            config_message1.add_field(name="__Role giving__",
                                      value="""The last thing you need to do is to write the role that you wanna assign the tickets to and you can do that only by just typing the role's name right after this message, **be careful! uppercase is case sensitive, means per example  support is not the same as Support**""")
            config_message1.set_footer(text="For more help just type ?help in any channel",
                                       icon_url=self.bot.user.avatar_url)
            config_message1.set_author(name=self.bot.user, url=self.bot.user.avatar_url)
            config_message1.set_thumbnail(url=ctx.guild.icon_url)
            msg_c1 = await ctx_channel.send(embed=config_message1)
            await msg_c1.delete(delay=60)

            def check1(m):
                return m.channel == ctx_channel and m.author == ctx.author

            msg = await self.bot.wait_for('message', check=check1)
            msg_c1 = await ctx_channel.send(embed=config_message1)
            await msg_c1.delete()

            done = discord.Embed(title="__**Configuration**__",
                                 description="**Configuration is over and there are no further steps for you to do!**",
                                 colour=0x41f441, timestamp=datetime.utcnow())
            done.add_field(name="__Commands__",
                           value="""**Now you only need to know the commands and you can do that by typing ?help.**""")
            done.set_footer(text="For more help just type ?help in any channel", icon_url=self.bot.user.avatar_url)
            done.set_author(name=self.bot.user, url=self.bot.user.avatar_url)
            done.set_thumbnail(url=ctx.guild.icon_url)
            msg_done1 = await ctx_channel.send(embed=done)
            await msg_done1.delete(delay=15)
            db = TinyDB('db/tickets/ticketroles.json')
            db.insert({'role': f'{msg.content}', 'guild_id': guild.id})

        except asyncio.TimeoutError:
            error = await ctx_channel.send('```Something went wrong, try again please!```')
            await error.delete(delay=5)


    @commands.command()
    @commands.check(is_support)
    async def support(self, ctx, *reason):
        await ctx.message.delete(delay=0)
        db = TinyDB('db/tickets/requests.json')
        User = Query()
        count = db.count(User.guild_id == ctx.guild.id)
        db.insert({'request-owner': f'{ctx.message.author}', 'guild_id': ctx.guild.id, 'count': count})
        for category in ctx.guild.categories:
            if category.name == "Tickets":
                db = TinyDB('db/tickets/ticketroles.json')
                Role = Query()
                li = db.search(Role.guild_id == ctx.guild.id)
                for i in li:
                    role = i['role']
                    role1 = discord.utils.get(ctx.guild.roles, name=str(role))
                    role2 = discord.utils.get(ctx.guild.roles, name="Ticket on")
                    every = discord.utils.get(ctx.guild.roles, name="@everyone")
                    overwrites = {
                        role1: discord.PermissionOverwrite(send_messages=True, read_messages=True),
                        ctx.message.author: discord.PermissionOverwrite(send_messages=False, read_messages=True),
                        every: discord.PermissionOverwrite(send_messages=False, read_messages=False)

                    }
                    try:
                        rch = await ctx.message.guild.create_text_channel(name=f'request-{count}',
                                                                          overwrites=overwrites, category=category)
                        await ctx.message.author.add_roles(role2)
                        embed = discord.Embed(title="Ticket",
                                              description=f"**{ctx.message.author.mention}, your ticket has been accepted please wait until someone of the staff team opens it.**",
                                              colour=0xf44e42, timestamp=datetime.utcnow())
                        embed.add_field(name="__Notice__",
                                        value="**Any trolling will lead to unexpected consequences!**")
                        embed.add_field(name="__Closing or Opening ticket__",
                                        value="**If you wanna close the ticket just click on the chain lock 🔒 and to open it click on unlock 🔓.**")
                        embed.set_footer(icon_url=self.bot.user.avatar_url, text="?help for more help.")
                        msg = await rch.send(embed=embed)
                        emoji = "🔒"
                        emoji1 = "🔓"
                        await msg.add_reaction(emoji)
                        await msg.add_reaction(emoji1)
                        await asyncio.sleep(1)

                        def check(reaction, user):
                            for m in role1.members:
                                return user == m and str(reaction.emoji) == emoji or str(reaction.emoji) == emoji1

                        reaction, user = await self.bot.wait_for('reaction_add', check=check)
                        if str(reaction.emoji) == emoji:
                            embed2 = discord.Embed(title="__Closing__",
                                                   description="**Channel will be deleted in 5 seconds 🛑.**",
                                                   timestamp=datetime.utcnow(), colour=0xe88a84)
                            embed2.set_footer(icon_url=self.bot.user.avatar_url, text="?help for more help.")
                            await rch.send(embed=embed2)
                            await msg.delete(delay=0)
                            await asyncio.sleep(delay=5)
                            await ctx.message.author.remove_roles(role2)
                            await rch.delete()
                        if str(reaction.emoji) == emoji1:
                            await rch.set_permissions(ctx.message.author, send_messages=True, read_messages=True)
                            await msg.delete(delay=0)
                            embed3 = discord.Embed(title="__Open__",
                                                   description=f"**Channel is now open you can explain your issue to {user.mention}.**",
                                                   timestamp=datetime.utcnow(), colour=0x9ee884)
                            embed3.add_field(name=f"__{role}__",
                                             value=f"**{user.mention} You can close the ticket after talking with {ctx.message.author.mention} by reacting with {emoji}.**")
                            msg1 = await rch.send(embed=embed3)
                            await msg1.add_reaction(emoji)

                            def check2(reaction, user):
                                for m in role1.members:
                                    return user == m and str(reaction.emoji) == emoji

                            reaction, user = await self.bot.wait_for('reaction_add', check=check2)
                            embed4 = discord.Embed(title="__Closing__",
                                                   description=f"**Ticket has been closed, now please choose to delete the channel ⛔ or save this conversation 📰 **",
                                                   timestamp=datetime.utcnow(), colour=0x9ee884)
                            msg2 = await rch.send(embed=embed4)
                            await msg2.add_reaction("⛔")
                            await msg2.add_reaction("📰")
                            await msg1.delete()

                            def check3(reaction, user):
                                for m in role1.members:
                                    return user == m and str(reaction.emoji) == "⛔" or str(reaction.emoji) == '📰'

                            reaction, user = await self.bot.wait_for('reaction_add', check=check3)
                            if str(reaction.emoji) == "⛔":
                                embed5 = discord.Embed(title="__Closing__",
                                                       description="**Channel will be deleted in 5 seconds 🛑.**",
                                                       timestamp=datetime.utcnow(), colour=0xe88a84)
                                embed5.set_footer(icon_url=self.bot.user.avatar_url, text="?help for more help.")
                                await rch.send(embed=embed5)
                                await msg2.delete(delay=0)
                                await asyncio.sleep(delay=5)
                                await ctx.message.author.remove_roles(role2)
                                await rch.delete()
                            if str(reaction.emoji) == '📰':
                                messages = await rch.history(limit=None).flatten()
                                await asyncio.sleep(delay=5)
                                f = open(f'conversations/conversation-{count}-{ctx.guild.id}.txt', 'w',
                                         encoding="utf-8")
                                writ = f.write(f"---Conversation {count}---\n")
                                messages.reverse()
                                for m in messages:
                                    if m.author != self.bot.user:
                                        db1 = TinyDB('db/tickets/conversation.json')
                                        db1.insert(
                                            {'request-owner': f'{ctx.message.author}', 'guild_id': ctx.guild.id,
                                             'conversation': m.content, "conversation-headname": m.author.name,
                                             "conversation-headdisc": m.author.discriminator, 'count': count})
                                        write = f.write(f"{m.author.name}#{m.author.discriminator} : {m.content}\n")
                                msg3 = await rch.send("Saving...")
                                await msg3.delete()
                                embed5 = discord.Embed(title="__Saving__",
                                                       description="**This conversation has been saved and in order to see the conversation write ?conversation {conversation id number(you see it on the ticket channel)}, Example: ?conversation 10, this command will send you a dm with the full conservation. Now the channel is gonna be deleted after 15 seconds.**",
                                                       timestamp=datetime.utcnow(), colour=0xe88a84)
                                embed5.add_field(name="__Notice__",
                                                 value="Only an admin can use this command and please wait at least 3 minutes before you use ?conversation command.")
                                embed5.set_footer(icon_url=self.bot.user.avatar_url, text="?help for more help.")
                                await rch.send(embed=embed5)
                                await asyncio.sleep(30)
                                await ctx.message.author.remove_roles(role2)
                                await rch.delete()
                    except AttributeError as error:
                        print(error)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def conversation(self, ctx, id: int):
        msg = await ctx.message.channel.send("**I will send you a private message in 10 seconds**")
        await asyncio.sleep(10)
        f = open(f'conversations/conversation-{id}-{ctx.guild.id}.txt', 'rb')
        embed = discord.Embed(title=f"Conversation {id}",
                              description=f"""**This is conversation number {id} history, i will send a file which contains all the messages between the users. **""",
                              colour=0x42f4ce, timestamp=datetime.utcnow())
        embed.add_field(name="__Notice__",
                        value="The file is a text file so open it with block note or something that reades .txt and it's not a malware.")
        embed.set_footer(icon_url=self.bot.user.avatar_url, text="Makde by Ɗrake#7418")
        file = discord.File(f, filename=f"Conversation {id}.txt")
        await ctx.message.author.send(embed=embed)
        await ctx.message.author.send(file=file)
        await ctx.message.delete()
        await msg.delete(delay=15)
    @ticketconfig.error
    async def ticket_config(self, ctx, error):
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

    @support.error
    async def _support(self, ctx, error):
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

    @conversation.error
    async def _conversations(self, ctx, error):
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
    bot.add_cog(Tickets(bot))