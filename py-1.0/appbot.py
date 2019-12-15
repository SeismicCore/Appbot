import time
import json
import datetime
import discord
from discord.ext import commands
from datetime import datetime, timedelta
import asyncio
import os
import traceback
import sys
 
allowed_channels = ["CHANNEL_IDS"]
not_aloud_words = ["BAD_WORDS"]
android_blacklisted = ["android","androyd", "Android", "Androyd"]
known_issues = ["kik", "gun flip", "youtuberslife", "dreamleague", "dream league", "snapchat++", "snapchat", "tinder++", "tinder", "btd battles", "baloon tower defense"]
invite_link = ["d.gg", "https://discord.gg", "youtube.com", "twitch.tv", "twitter.com", "instagram.com"]
fake_links = ["https://appvalley.vip", "https://kubadownload.com/news/appvalley", "https://apkpure.com/appvalley-android/com.appslifestyle.appvalley", "https://appvalley-apk.com/appvalley-apk/", "https://www.malavida.com/en/soft/appvalley/android/#gref", "https://www.apkmonk.com/app/com.appslifestyle.appvalley/", "https://appvalleyvip.com/", "https://appvalley.onl", ]
last_claimed_xp = {}
color=discord.Colour
bot = commands.Bot(command_prefix='_')
bot.remove_command('help')
embed_footer = ('AppBot By RevokedCookie - v1.0!')
embed_thumbnail = ('https://cdn.discordapp.com/attachments/544599878257344513/552625604458053633/appbot.logo.png')
agree_channel = ["-agree"]
with open('users.json', 'r') as f:
    users = json.load(f)
 
 
# Events
 
 
@bot.event
async def on_ready():
 for Channel in (bot.get_channel("CHANNEL_ID"), bot.get_channel("CHANNEL_ID")):  
    embed=discord.Embed(title="Connected!", description="AppBot has connected to guild (GUILD_ID), and is ready to go!", color=discord.Colour(0x00ff39))
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(Channel, embed=embed)
    await bot.change_presence(game=discord.Game(name='AppBot now running v1.0!'))
 
           
 
   
 
@bot.event
async def on_member_join(member):
    if member.bot:
        return
    Channel = bot.get_channel("CHANNEL_ID")
    await bot.send_message(Channel, f"Hello {member.mention}, and welcome to the official AppValley server! To gain acsess to our server, Check your DMs for a message from 'Auttaja'. You will need to click the link and compleate the google CaptCHA. Then you will need to go read our <#509015468728909834> as well as our <#517554260355973169>, then, come back here and type `-agree` to agree that you have read, and understand our Rules and FAQ!")
 
    join_leave_logs = discord.utils.get(member.server.channels, name='join-leave-logs')
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Member Joined')
    embed.add_field(name="Member:", value='{} ({})'.format(member.mention, member.id), inline=False)
    embed.add_field(name="Account Created:", value='{}'.format((member.created_at), inline=False))    
    embed.set_thumbnail(url=embed_thumbnail)
    embed.set_footer(text=embed_footer)
    await bot.send_message(join_leave_logs, embed=embed)
   
    if member.id not in users:
        users[member.id] = {
            'experience': 0,
            'level': 0
        }
 
@bot.event
async def on_member_remove(member):
    if member.bot:
        return
    join_leave_logs = discord.utils.get(member.server.channels, name='join-leave-logs')
    embed = discord.Embed(colour = discord.Colour.red())
    embed.set_author(name='Member Left')
    embed.add_field(name="Member:", value='{} ({})'.format(member.mention, member.id), inline=False)
    embed.add_field(name="Roles:", value='{}'.format(', '.join([r.mention for r in member.roles if r.name != '@everyone']), inline=False))  
    embed.set_thumbnail(url=embed_thumbnail)
    embed.set_footer(text=embed_footer)
    await bot.send_message(join_leave_logs, embed=embed)
 
 
 
@bot.event
async def on_message(message):
    #Filters
    if message.author.bot:
        return
    if not message.author.permissions_in(message.channel).administrator:
        if any(word in message.content for word in not_aloud_words):
            await bot.delete_message(message)
            await bot.send_message(message.channel,'{} Please dont use that language on our server!'.format(message.author.mention))
            embed=discord.Embed(title="AppBot Filter", description="{} Please dont use that language on our server!".format(message.author.mention), color=0xff0000)
            embed.set_thumbnail(url=embed_thumbnail)
            embed.set_footer(text=embed_footer)
            await bot.send_message(message.channel, embed=embed)
        if any(word in message.content for word in android_blacklisted):
            await bot.delete_message(message)
            embed=discord.Embed(title="AppBot Filter", description="{} Please read our <#517554260355973169> before asking for support. And no, AppValley isnt, and never will be, on android.".format(message.author.mention), color=0xff0000)
            embed.set_thumbnail(url=embed_thumbnail)
            embed.set_footer(text=embed_footer)
            await bot.send_message(message.channel, embed=embed)
        if any(word in message.content for word in fake_links):
            await bot.delete_message(message)
            embed=discord.Embed(title="AppBot Filter", description=":warning: :warning:{} ***WARNING***! That website is **NOT** the oficial AppValley website, and by installing it you may be putting your device in danger! **NEVER** install AppValley from an outside link or source. The **ONLY** safe place to dowload AppValley is https://app-valley.vip !:warning: :warning:".format(message.author.mention), color=0xff0000)
            embed.set_thumbnail(url=embed_thumbnail)
            embed.set_footer(text=embed_footer)
            await bot.send_message(message.channel, embed=embed)          
     
       
        if message.channel.id == "CHANNEL_ID":
            return  
        if any(word in message.content for word in invite_link):
            await bot.delete_message(message)
            embed=discord.Embed(title="AppBot Filter", description="{} Our server is not advertising friendly! Please only post self promo links in <#522693697041858560>!".format(message.author.mention), color=0xff0000)
            embed.set_thumbnail(url=embed_thumbnail)
            embed.set_footer(text=embed_footer)
            await bot.send_message(message.channel, embed=embed)    
        if any(word in message.content for word in known_issues):
            embed=discord.Embed(title="Known Issue!", description="{} This is a known issue. We have contacted the developer and we are working on a fix! (If you were not asking for support for an application, ignore this message. This feature is still a bit buggy.)".format(message.author.mention), color=0xff0000)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(message.channel, embed=embed)
   #Leveling System
    await bot.process_commands(message)
    if message.author.id in last_claimed_xp and datetime.now() - last_claimed_xp[message.author.id] <= timedelta(seconds=2):
        return
 
    last_claimed_xp[message.author.id] = datetime.now()
 
    with open('users.json',) as u:
        users = json.load(u)    
 
    if message.channel.id in allowed_channels:
 
        if not message.author.id in users:
            users[message.author.id] = {
                'experience': 0,
                'level': 0
            }
 
        users[message.author.id]['experience'] += 23
 
        xp = users[message.author.id]['experience'] #users current xp
        level = users[message.author.id]['level'] #users current level
        lvl_end = int(5/3 * level ** 3  +  55/2  * level ** 2  +  755/6 * level  +  100) #the XP you need to lvl up
           
        with open('users.json', 'w') as f:
                users[message.author.id]['level'] = level
                json.dump(users, f)
 
        if xp >= lvl_end:
            with open('users.json', 'w') as f:
                users[message.author.id]['level'] = int(level + 1)
                json.dump(users, f)
           
            embed=discord.Embed(title="Level Up!", description="{0} has leveled up to level {1}!".format(message.author.mention, level + 1), color=0x00ff39)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(message.channel, embed=embed)
       
#warning system
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = {}
  else:
      report.setdefault("users", {})
   
 
#IGNORE THIS ITS NOT FINISHED
@bot.command(pass_context = True)
async def warn(ctx, member, *, reason = "None Provided"):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        reason = ' '.join(reason)
        for current_user in report['users']:
            if current_user['name'] == user.name:
                current_user['reasons']['text'] = reason
                break
        else:
            report['users'].append({
            'name':user.name,
            'reasons': [reason,]
         })
        with open('reports.json','w+') as f:
            json.dump(report,f)
    else:
        embed=discord.Embed(title="Acsess Denyed!", description="{} You must have the `Manage Messages` permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
@bot.command(pass_context = True)
async def infractions(ctx,user:discord.User):
  if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        for current_user in report['users']:
            if user.name == current_user['name']:
                await client.say(f"{user.name} has receved {len(current_user['reasons'])} warnings. : {','.join(current_user['reasons'])}")
                break
            else:
                await client.say(f"{user.name} has never been reported")  
  else:  
        embed=discord.Embed(title="Acsess Denyed!", description="{} You must have the `Manage Messages` permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
#IGNORE ABOVE CODE
 
 
@bot.event
async def on_message_delete(message):  
    if message.author.bot:
        return
    else:
        message_logs = discord.utils.get(message.server.channels, name='message-logs')
        author = message.author
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name='Deleted Message')
        embed.add_field(name="Author:", value='{} ({})'.format(message.author.mention, author.id))
        embed.add_field(name="Deleted In:", value='{} ({})'.format(message.channel.mention, message.channel.id), inline=False)
        embed.add_field(name="Message ID:", value='{}'.format(message.id))
        embed.add_field(name="Deleted content:", value='{}'.format(message.content), inline=False)        
        embed.set_thumbnail(url=embed_thumbnail)
        embed.set_footer(text=embed_footer)
        await bot.send_message(message_logs, embed=embed)
 
@bot.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        message_logs = discord.utils.get(before.server.channels, name='message-logs')
        author = before.author
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_author(name='Edited Message')
        embed.add_field(name="Author:", value='{} ({})'.format(before.author.mention, author.id))
        embed.add_field(name="Edited In:", value='{} ({})'.format(before.channel.mention, before.channel.id, inline=False))
        embed.add_field(name="Message ID:", value='{}'.format(before.id, inline=False))
        embed.add_field(name="Before:", value='{}'.format(before.content, inline=False))      
        embed.add_field(name='After:', value='{}'.format(after.content, inline=False))
        embed.set_thumbnail(url=embed_thumbnail)
        embed.set_footer(text=embed_footer)
        await bot.send_message(message_logs, embed=embed)
 
 
# Commands
@bot.command(name="notify", pass_context=True)
async def notify(ctx):
            member = ctx.message.author
            role = discord.utils.get(member.server.roles, name='Updates')
            await bot.add_roles(member, role)
            embed=discord.Embed(title="Updates", description="<@{0}> You will now get notified for announcments!".format(member.id, ctx.message.author.mention), color=0x00ff39)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(ctx.message.channel,embed=embed)
         
@bot.command(name="unnotify", pass_context=True)
async def unnotify(ctx):
            member = ctx.message.author
            role = discord.utils.get(member.server.roles, name='Updates')
            await bot.remove_roles(member, role)
            embed=discord.Embed(title="Updates", description="<@{0}> You will no longer get notified for announcments".format(member.id, ctx.message.author.mention), color=0x00ff39)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(ctx.message.channel,embed=embed)
 
 
#Mod Commands
 
 
#kick cmd
@bot.command(name="kick", pass_context=True)
async def kick(ctx, member: discord.Member, *, reason = "None Provided"):
    if ctx.message.author.permissions_in(ctx.message.channel).kick_members:
 
        embed=discord.Embed(title="User Kicked!", description="<@{0}> has sucsessfully been kicked by moderator: {1}!".format(member.id, ctx.message.author.mention), color=0x00ff39)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
       
        await bot.kick(member)
       
        mod_logs = discord.utils.get(ctx.message.server.channels, name='mod-logs')
        embed = discord.Embed(colour = discord.Colour.orange())
        embed.add_field(name='AppBot Mod Logs', value='**{} has been kicked**'.format(member.display_name))
        embed.add_field(name="User:", value="<@{}> ({})".format(member.id, member.id), inline=True)
        embed.add_field(name="Action By:", value="{} ({})".format(ctx.message.author.mention, ctx.message.author.id), inline=True)
        embed.add_field(name="Reason Provided:", value="{}".format(reason), inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(mod_logs, embed=embed)
 
 
    else:
        embed=discord.Embed(title="Acsess Denyed!", description="{} You must have the `Kick Mambers` permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
 
#ban cmd
@bot.command(name="ban", pass_context=True)
async def ban(ctx, member: discord.Member, *, reason = "None Provided"):
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
 
        embed=discord.Embed(title="User Kicked!", description="<@{0}> has sucsessfully been banned by moderator: {1}!".format(member.id, ctx.message.author.mention), color=0x00ff39)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
       
        await bot.ban(member)
       
        mod_logs = discord.utils.get(ctx.message.server.channels, name='mod-logs')
        embed = discord.Embed(colour = discord.Colour.orange())
        embed.add_field(name='AppBot Mod Logs', value='**{} has been banned**'.format(member.display_name))
        embed.add_field(name="User:", value="<@{}> ({})".format(member.id, member.id), inline=True)
        embed.add_field(name="Action By:", value="{} ({})".format(ctx.message.author.mention, ctx.message.author.id), inline=True)
        embed.add_field(name="Reason Provided:", value="{}".format(reason), inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(mod_logs, embed=embed)
 
 
    else:
        embed=discord.Embed(title="Acsess Denyed!", description="{} You must have the `ban Mambers` permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
#Purge CMD
@bot.command(pass_context=True)
async def purge(ctx, amount :int):  
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        messages = await bot.purge_from(ctx.message.channel, limit=amount)
        await bot.delete_messages(messages)
        embed=discord.Embed(title="Chat Purged", description="{0} has purged {1} messages from {2}!".format(ctx.message.author.mention, amount, ctx.message.channel), color=0x00ff39)
        embed.set_thumbnail(url=embed_thumbnail)
        embed.set_footer(text=embed_footer)
        await bot.send_message(ctx.message.channel, embed=embed)  
   
        mod_logs = discord.utils.get(ctx.message.server.channels, name='mod-logs')
        embed = discord.Embed(colour = discord.Colour.green())
        embed.add_field(name='AppBot Mod Logs', value='**{0} messages have been purged from chat!**'.format(amount))
        embed.add_field(name='Channel:', value='{} ({})'.format(ctx.message.channel.mention, ctx.message.channel.id), inline=False)
        embed.add_field(name="Action By:", value="{} ({})".format(ctx.message.author.mention, ctx.message.author.id), inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(mod_logs, embed=embed)
   
    else:
        embed=discord.Embed(title="Permission Denied.", description="{} You must have the `Manage Messages` permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
 
#mute command
@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member, *, reason = "None Provided"):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_roles:
            role = discord.utils.get(member.server.roles, name='AppBot Muted')
            await bot.add_roles(member, role)
            embed=discord.Embed(title="User Muted!", description="<@{0}> has sucsessfully been muted by moderator: {1}!".format(member.id, ctx.message.author.mention), color=0x00ff39)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(ctx.message.channel,embed=embed)
   
            mod_logs = discord.utils.get(ctx.message.server.channels, name='mod-logs')
            embed = discord.Embed(colour = discord.Colour.orange())
            embed.add_field(name='AppBot Mod Logs', value='**{} has been muted**'.format(member.display_name))
            embed.add_field(name="User:", value="<@{}> ({})".format(member.id, member.id), inline=False)
            embed.add_field(name="Action By:", value="{} ({})".format(ctx.message.author.mention, ctx.message.author.id), inline=False)
            embed.add_field(name="Reason Provided:", value="{}".format(reason), inline=False)
            embed.set_footer(text=embed_footer)
            embed.set_thumbnail(url=embed_thumbnail)
            await bot.send_message(mod_logs, embed=embed)
    else:
        embed=discord.Embed(title="Permission Denied.", description="<@{}> You must have the `Manage Roles` permission to run this command!".format(member.id), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel,embed=embed)
 
#unmute command
@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member, *, reason = "None Provided"):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_roles:
        role = discord.utils.get(member.server.roles, name='AppBot Muted')
        await bot.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="<@{0}> has sucsessfully been unmuted by moderator: {1}!".format(member.id, ctx.message.author.mention), color=0x00ff39)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)  
        await bot.send_message(ctx.message.channel, embed=embed)
   
        mod_logs = discord.utils.get(ctx.message.server.channels, name='mod-logs')
        embed = discord.Embed(colour = discord.Colour.green())
        embed.add_field(name='AppBot Mod Logs', value='**{} has been unmuted**'.format(member.display_name))
        embed.add_field(name="User:", value="<@{}> ({})".format(member.id, member.id), inline=False)
        embed.add_field(name="Action By:", value="{} ({})".format(ctx.message.author.mention, ctx.message.author.id), inline=False)
        embed.add_field(name="Reason Provided:", value="{}".format(reason), inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(mod_logs, embed=embed)
   
    else:
        embed=discord.Embed(title="Permission Denied.", description="<@{}> You must have the `Manage Roles` permission to run this command!".format(member.id), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
#Info Commands
 
#help cmd
@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.blue())
 
    embed.set_author(name='AppBot Help Page')
    embed.add_field(name='Informational Commands:', value='----------------------', inline=False)
    embed.add_field(name='help', value='Displays the help message', inline=False)
    embed.add_field(name='ping', value='Displays the bots current command latency ping.', inline=False)
    embed.add_field(name='ching', value='Displays the bot current command latency ping, but for asians. Requested by <@333675525417467904>', inline=False)
    embed.add_field(name='twitter', value="Displays AppValley's offical Twitter page.", inline=False)
    embed.add_field(name='reddit', value="Displays AppValley's official Reddit page", inline=False)
    embed.add_field(name='vipsite', value="Displays the AppValley VIP (builds) website.", inline=False)
    embed.add_field(name='website', value="Displays the AppValley VIP website.", inline=False)
    embed.add_field(name='viphelp', value="Displays where you can find help for AppValley VIP (builds).", inline=False)
    embed.add_field(name='status', value="Displays the revoke status of or applications.", inline=False)
    embed.add_field(name='rules', value='Displays where you can find our servers rules and FAQ.', inline=False)
    embed.add_field(name="lvlhelp", value="Displays info on how the bots leveling system works.", inline=False)
    embed.add_field(name="whatsarevoke", value="This command displays what a revoke is, and how to avoid them.", inline=False)
    embed.add_field(name='Moderation Commands:', value='-------------------', inline=False)
    embed.add_field(name='purge <# of messages>', value='Purges the specified ammount of messages. Requires `Manage Messages` permission.', inline=False)
    embed.add_field(name='kick @member/User ID', value='Kicks a member. Requires `Kick Members` permission.', inline=False)
    embed.add_field(name='ban @member/User ID', value='Bans a member. Requires `Ban Members` permission.', inline=False)
    embed.add_field(name='mute @member/User ID', value='Mutes a member. Reasons and lenth not avalible yet. Requires `Manage Roles` Permission.', inline=False)
    embed.add_field(name='unmute', value='Unmutes a member. Requires `Manage Roles` permission.', inline=False)
    embed.add_field(name="Other Commands", value="--------------", inline=False)
    embed.add_field(name="su, statusupdate", value="A command to update the bots status page remotely. Requiers `Developers ID`.", inline=False)
    embed.add_field(name="level", value="This command displays your level. For info our the leveling system, use command `lvlhelp`.", inline=False)
    embed.add_field(name="suggest", value="Make a suggestion to our server! (will be posted in <#507908076439994388>) NOTE: This is not for bot suggestions!", inline=False)
    embed.add_field(name="feedback", value="Give feedback to the bot's developer! Please use this command to make any suggestions (FOR THE BOT ONlY), or to report something like a spelling error or bug!", inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/507873444738760706/544654015703810068/appvalleynew.png')
    await bot.send_message(author, embed=embed)
 
   
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.blue())
   
   
    embed.set_author(name='AppBot Help Page (2)')
    embed.add_field(name='ModMail (Ticket) Commands', value='---------------------------', inline=False)
    embed.add_field(name='dm', value='NOT A COMMAND - DMing the bot will create a modmail thread', inline=False)
    embed.add_field(name='reply', value='Replys to a modmail thread, must be done in a thread channel, requiers `support` role or above.', inline=False)
    embed.add_field(name='anonreply', value='Replys to a modmail thread anoynomously (says `AppValley team` instead of your name), must be done in a thread channel, requiers `support` role or above.', inline=False)
    embed.add_field(name='close', value="Closes a thread must be done in a thread channel, requiers `support` role or above.", inline=False)
    embed.add_field(name='Need more help?', value='If you didnt find what you were looking for, come join our suport server: https://discord.gg/STs2X3C', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/507873444738760706/544654015703810068/appvalleynew.png')
    await bot.send_message(author, embed=embed)
   
    embed = discord.Embed(colour = discord.Colour.green())
    embed.add_field(name=':white_check_mark:', value='{} Ive sent the message to your DM! Please dont reply as this will create a modmail ticket!'.format(ctx.message.author.mention), inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#lvlhelp cmd
@bot.command(pass_context=True)
async def lvlhelp(ctx):
   
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot Lveling System')
        embed.add_field(name='XP per message', value='You can earn from 10 to 25xp per message! The longer the message, the more XP you will earn!', inline=False)
        embed.add_field(name='XP cooldown', value='You can only earn xp every 30 seconds. This reduces spamming.', inline=False)
        embed.add_field(name="XP to level up", value="We use this equasion for how much xp  you need for each level: 5 * (lvl ^ 2) + 50 * lvl + 100. Replace `lvl` with your current level!")
        embed.add_field(name="Visuals", value="Wanna see a visual of our leveling system? check out these links:")
        embed.add_field(name="Graph:", value="https://cdn.discordapp.com/attachments/507002982391349253/545985734348374016/unknown.png")
        embed.add_field(name="Chart:", value="https://cdn.discordapp.com/attachments/507002982391349253/545986075433369620/unknown.png")
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
#Status cmd
@bot.command(pass_context=True)
async def status(ctx):
   
    with open("status.json") as f:
        data = json.load(f)
   
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot Status Page')
        embed.add_field(name='Overall Status:', value=data["overall_status"], inline=False)
        embed.add_field(name='Revoke Status:', value=data["revoke_status"], inline=False)
        embed.add_field(name='Server Status', value=data["server_status"], inline=False)
        embed.add_field(name='VIP (Builds) Status', value=data["vip_status"], inline=False)
        embed.add_field(name='Bot Status:', value=data["bot_status"], inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
#update status cmd
@bot.command(name="su", pass_context=True)
async def su(ctx, key, *, value):
    if ctx.message.author.id == ("516840368843522073"):
        with open("status.json", "r") as fp:
            data = json.load(fp)
            data[key] = value
        with open("status.json", "w") as fp:
            json.dump(data, fp)
        embed=discord.Embed(title=":white_check_mark:", description="{} has updated the {}!".format(ctx.message.author.mention, key), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
       
        statuschannel = bot.get_channel("552626824186822666")
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot Current Status Page')
        embed.add_field(name='Overall Status:', value=data["overall_status"], inline=False)
        embed.add_field(name='Revoke Status:', value=data["revoke_status"], inline=False)
        embed.add_field(name='Server Status', value=data["server_status"], inline=False)
        embed.add_field(name='VIP (Builds) Status', value=data["vip_status"], inline=False)
        embed.add_field(name='Bot Status:', value=data["bot_status"], inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(statuschannel, embed=embed)
   
    else:
        embed=discord.Embed(title="Permission Denied.", description="{} Only the bot's developer has permission to run this command!".format(ctx.message.author.mention), color=0xff0000)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
 
 
 
@bot.command(pass_context=True)
async def twitter(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='AppValley Twitter', value='Here is the official AppValley twitter page: https://twitter.com/app_valley_vip?lang=en', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
 
#native cmd
@bot.command(pass_context=True)
async def native(ctx):
    await bot.send_message(ctx.message.channel, "Here's how to fix your error: https://cdn.discordapp.com/attachments/507862796592218112/545975797614247954/native.png")
 
#safari cmd
@bot.command(pass_context=True)
async def safari(ctx):
    await bot.send_message(ctx.message.channel, "To fix your error: Visit our website (https://app-valley.vip) on ***SAFARI*** browser. Chrome, firefox, edge, or any other browser cannot be used to install out=r scervice!")
#whatsarevoke cmd
@bot.command(pass_context=True)
async def whatsarevoke(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='Whats A Revoke?', value='What we call a revoke, is something that happens when someone reports a third-party app store to apple and takes away our permissions to use our signed programs. they take away our permissions to allow you to download apps and force anyone to delete any currently downloaded apps; however, revokes can be avoided by purchasing a VIP membership at https://appvalley.builds.io !', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#links command
@bot.command(pass_context=True)
async def website(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='AppValley Website:', value='Here is a link to the AppValley website: https://app-valley.vip', inline=False)
    embed.add_field(name='AppValley Online Webstore:', value='Here is a link to the AppValley Online webstore: https://app.app-valley.vip', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#reddit command
@bot.command(pass_context=True)
async def reddit(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='AppValley Reddit', value='Here is the AppValley official reddit page: https://www.reddit.com/r/appvalley', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#vip command
@bot.command(pass_context=True)
async def vipsite(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='AppValley VIP', value='Here is the AppValley VIP website: https://appvalley.builds.io', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#viphelp cmd
@bot.command(pass_context=True)
async def viphelp(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='Need help with VIP?', value='Go check out the builds.io help page: builds.io/help', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#rules cmd
@bot.command(pass_context=True)
async def rules(ctx):
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='AppValley Server Rules', value='You can view our server rules here: <#509015468728909834> and our servers FAQ here: <#517554260355973169>', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#ping cmd
@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='Pong!')
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    t = await bot.send_message(ctx.message.channel, embed = embed)
 
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
 
    embed2 = embed.add_field(name='Command Latency:', value=':ping_pong:  {}ms'.format(int(ms)))
    await bot.edit_message(t,embed=embed2)
 
#Ching command
#Command requested by IRL friend to be a korean version of 'Ping'
@bot.command(pass_context=True)
async def ching(ctx):
    embed = discord.Embed(colour = discord.Colour.green())
    embed.set_author(name='종!')
    embed.set_footer(text='@ skydaz3 # 1611 님이 요청한 명령')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/507873444738760706/544654015703810068/appvalleynew.png')
    t = await bot.send_message(ctx.message.channel, embed = embed)
 
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
 
    embed2 = embed.add_field(name='명령 대기 시간 :', value='🥢  {}밀리 초'.format(int(ms)))
    await bot.edit_message(t,embed=embed2)
 
#info
@bot.command(pass_context=True)
async def info(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.set_author(name='AppBot Information Page')
    embed.add_field(name='About The Developer', value='Hey there! Im Oreos#0001, and im a moderator for the official AppValley Discord server. After being support for multiple months, then becoming a mod on the server, i started to notice how unorganized the server was. From having four moderation bots, to having extremely cluttered logs, i started to ask questions to the administrators like "what bot should i use for this?", But nobody knew as we had so many bots. This also led to the issue of warning =s having no meaning, as everyone would use a different bot to warn a member! Thats when i said we needed to fix the issue. I came up with the idea of AppBt privately, then shared it among the other staff who all thought it was a great idea. I then started working on AppBot at the beginning of February, at my local library. From then on, ive been working extremely hard and AppBot has grown a ton.', inline=False)
    embed.add_field(name='Continued...', value='From moderation commands, logs etc. to features like `_status` to help our members know when our service is down, AppBot has helped a ton around the server for or staff team, and our members too! And this is only just the beginning. Im very excited to further develop AppBot, and to see where this project will lead me. Thanks for reading! Below is some basic bot information:', inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(author, embed=embed)
 
    embed = discord.Embed(colour = discord.Colour.blue())
    embed.add_field(name='Developer:', value='Oreos#0001', inline=False)
    embed.add_field(name='Commands', value='Currently, the bot has 14 commands. 8 in which all members can use.', inline=False)
    embed.add_field(name='Library', value='Im coding the bot in Discord.py v0.16.1', inline=False)
    embed.add_field(name='Python Version', value='Currently, the bot is writen in CPython 3.6.6', inline=False)
    embed.add_field(name='Update Version', value='Currently, the bot is on update v0.3')
    embed.add_field(name='Support Server', value='Here you can get support for the bot, and see or update log: https://discord.gg/STs2X3C')
    embed.add_field(name='Icon URL', value='https://cdn.discordapp.com/attachments/507873444738760706/544654015703810068/appvalleynew.png')
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(author, embed=embed)
 
    embed = discord.Embed(colour = discord.Colour.green())
    embed.add_field(name=':white_check_mark:', value='{} Ive sent the message to your DM! If you didnt receve the message, make sure you have DMs enabled for `Server Members`!'.format(ctx.message.author.mention), inline=False)
    embed.set_footer(text=embed_footer)
    embed.set_thumbnail(url=embed_thumbnail)
    await bot.send_message(ctx.message.channel, embed=embed)
 
#level commands
#level CMD
@bot.command(pass_context=True)
async def level(ctx):
    with open("users.json") as f:
        data = json.load(f)
    if  data[str(ctx.message.author.id)]["experience"] >= 1000:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name="{}'s Activity:".format(ctx.message.author))
        embed.add_field(name="Level", value="You are currently level {}!".format((data[str(ctx.message.author.id)]["level"])))
        embed.add_field(name="XP", value="You currently have {0:.1f}k XP, and you will level up when you reach {1:.1f}k XP!".format(data[str(ctx.message.author.id)]["experience"] / 1000, int(5/3 * (data[str(ctx.message.author.id)]["level"]) ** 3  +  55/2  * (data[str(ctx.message.author.id)]["level"]) ** 2  +  755/6 * (data[str(ctx.message.author.id)]["level"])  +  100) / 1000))
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
    else:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name="{}'s Activity:".format(ctx.message.author))
        embed.add_field(name="Level", value="You are currently level {}!".format((data[str(ctx.message.author.id)]["level"])))
        embed.add_field(name="XP", value="You currently have {0} XP, and you will level up when you reach {1} XP!".format((data[str(ctx.message.author.id)]["experience"]), int(5/3 * (data[str(ctx.message.author.id)]["level"]) ** 3  +  55/2  * (data[str(ctx.message.author.id)]["level"]) ** 2  +  755/6 * (data[str(ctx.message.author.id)]["level"])  +  100)))
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
       
#Suggestions
@bot.command(name="suggest", pass_context=True)
async def suggest(ctx, *, suggestion):
       
        embed = discord.Embed(colour = discord.Colour.green())
        embed.add_field(name="New Suggestion:", value="'{}'".format(suggestion))
        embed.set_footer(text="Suggestion By: {}".format(ctx.message.author))
        embed.set_thumbnail(url=embed_thumbnail)
        message = await bot.send_message(bot.get_channel("CHANNEL_ID"), embed=embed)
       
        embed=discord.Embed(title="Suggestion Submitted!", description="{0} Your suggestion has sucsessfuly been subimitted to <#507908076439994388>!".format(ctx.message.author.mention), color=0x00ff39)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
        await bot.add_reaction(message, '✅')
        await bot.add_reaction(message, '❌')
#feedback
@bot.command(name="feedback", pass_context=True)
async def feedback(ctx, *, feedback):
       
        embed = discord.Embed(colour = discord.Colour.green())
        embed.add_field(name="New Report:", value="'{}'".format(feedback))
        embed.set_footer(text="Reporting User: {}".format(ctx.message.author))
        await bot.send_message(bot.get_channel("551232129074331678"), embed=embed)
       
        embed=discord.Embed(title="Feedback Submitted!", description="{0} Your feedback has successfully been submitted to Oreos, the bots developer!".format(ctx.message.author.mention), color=0x00ff39)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
#updates
"""I used to keep all of my update logs in here for some reason... it was strange, but did allow me to get the change log 
whenever it was needed"""
#update v0.01
@bot.command(pass_context=True)
async def update01(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
        embed = discord.Embed(colour = discord.Colour.blue())
 
        embed.set_author(name='AppBot version 0.01')
        embed.add_field(name='Features', value='The following features have been added in AppBot version 0.01:', inline=False)
        embed.add_field(name='Embeds', value='All messages are embeded and look great! Includes the AppValley logo!', inline=False)
        embed.add_field(name='Levels', value='now introducing levels! The bot will give up to 5 xp per message. Commands to check your level are expected in v0.02!', inline=False)
        embed.add_field(name='StartLog', value='This feature is mainly for me, but the bot will log when it has started and is ready to be used!', inline=False)
        embed.add_field(name='Moderation', value='For our mods, commands `purge, kick, ban` have been added!', inline=False)
        embed.add_field(name='Information', value='Some information commands have been added for our members! These commands include `help, ping, twitter, reddit,  vip, viphelp, status, rules`! See what these commands do by running the help command!', inline=False)
        embed.add_field(name='Prefix', value="I've changed the prefix of the bot to `_`. This will not be changed in the future!", inline=False)
        embed.add_field(name='Filters', value='I have added some filtered words. The bot will delete your message, and ping you saying not to use that!', inline=False)
        embed.add_field(name='This includes all our new features in v0.01!', value="This includes all our features in v0.01! I hope you enjoy the update! Please ping @Oreos me with any suggestions!", inline=False)
        embed.set_thumbnail(url=embed_thumbnail)      
        embed.set_footer(text=embed_footer)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
#update v0.02
@bot.command(pass_context=True)
async def update02(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 0.02')
        embed.add_field(name='Features', value='The following features have been added in AppBot version 0.02:', inline=False)
        embed.add_field(name='Embeds', value='Yes more embed features! I have added `AppBot developed by Oreos#0001 - <version>` as a footer on all embeded messages, as well as ive made it so **all** of the bots messages are embeded, even mod messages and level ups! [[excludes the weclome message]]')
        embed.add_field(name='Moderation', value='I have added a lot of features for the mmoderatiors this update. First, I have added a mute and unmute command. Keep in mind, there is no time feature yet. That will hopefully come next update. Ive also added an unmutte feature.', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. Ido have many typos in my code, and i have fixed many of them this update. If you spot another, let me know!', inline=False)
        embed.add_field(name='Bug Fixes', value='The following bugs have been pixed in this patch: Staff will not be effected by filters; XP antispam has been fixed, you will only gain XP every 30 seconds; now, filters will work if the word in a sentance, not if its exactly the word filtered;', inline=False)
        embed.add_field(name='Known Issues', value='Our known-issues page has been removed, and now, when a member asks about a known-issue-application, the bot will automatically respond. Basically a filter.', inline=False)
        embed.add_field(name='This includes all our new features in v0.02!', value="This includes all our features in v0.02! I hope you enjoy the update! Please ping @Oreos with any suggestions!", inline=False)
        embed.set_thumbnail(url=embed_thumbnail)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=embed_footer)    
        await bot.send_message(ctx.message.channel, embed=embed)
 
#update v0.03
@bot.command(pass_context=True)
async def update03(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 0.3')
        embed.add_field(name='Features', value='The following features have been added in AppBot version 0.3:', inline=False)
        embed.add_field(name='Update Version', value='First i just wanna start saying, you may have noticed the updates went from v0.02 to v0.3. This is becouse ive relised as much as i work on the bot that v1.0 will come out sooner than expected. At v1.0, the full bot will be mostly finished. Therefore there wont be many updates after that. Anyway, heres the things ive added, Enjoy!', inline=False)
        embed.add_field(name='Logging', value='Ive added AppBot logging! We have mod logs, message logs, an join/leave logs!', inline=False)
        embed.add_field(name='Fake Links', value='This is an adition to our filters. If a member posts an unoficial AppValley install link, the bot will delete the msg and ssend a warning saying tat its not an oficial link.', inline=False)
        embed.add_field(name='Commands', value='Ive only added two command this patch. The first command is `ching`. It the same as `ping` but asian.. <@333675525417467904> requested this, and i delivered... The next command ive added is `info`. This cmmand wil give some basic info about the bot.')
        embed.add_field(name='DM Conformations', value='Ive added confermation messages whenever the bot sends you a response via DM!')
        embed.add_field(name='Bug Fixes', value='Ive fuxed a lot of bugs this patch. A lot of inside stuff you probally didnt even notice :eyes:. This mostly included tags being broken. For example, they looked like <@@everyone> instead of @everyone. Simple errrors in text.', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. I do have many typos in my code, and i have fixed many of them this update. If you spot another, let me know!', inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
#update v0.4
@bot.command(pass_context=True)
async def update04(ctx):
       
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 0.4 changelog')
        embed.add_field(name='Features', value='The following features have been added in AppBot version 0.4:', inline=False)
        embed.add_field(name='Levels', value='Ive made huge changes to levels! Ive added the `level` command, as well as chenged the equasion for XP. Also, if you were level 10 or above for MEE6, your level has ben caried over to AppBot. Otherwise, youll just have to restart. Sorry!', inline=False)
        embed.add_field(name='Fake Links', value='Ive added a bunch more links to the fake links page', inline=False)
        embed.add_field(name='Commands', value='Ive added a few commands. Firs one is `level`. It wil dislay your current level. Im working on more for this command, and may make a small 0.4.5 patch just to update the command. Ive also added `lvlhelp` that displays all the info about our leveling system yu could need. Also, ive added the `su, statusupdate` command. This is a developer-only command, but its usefull for everyone as the status page will be more accurate and will be updated faster! The last cmd i added is `native`. This displays how to install appvaley if your are getting the `Cannot connect to app-valley.vip` error.', inline=False)
        embed.add_field(name='Bug Fixes', value='Ive fuxed a lot of bugs this patch. A lot of inside stuff you probally didnt even notice :eyes:. This mostly included tags being broken. For example, they looked like <@@everyone> instead of @everyone. Simple errrors in text. If you find any more bugs, please report them!', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. I do have many typos in my code, and i have fixed many of them this update. If you spot another, let me know!', inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
 
#Update 0.4.5
@bot.command(pass_context=True)
async def update045(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).ban_members:    
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 0.4.5 changelog')
        embed.add_field(name='Features', value='v0.4.5 is just a quick bot update for levels. Nothing much here. v0.5 coming soon!', inline=False)
        embed.add_field(name='Levels', value='Now the `level` command displays your level, xp, and how much xp you need to level up! If you are verified, staff, or above llevel 10 you goot your levels transfered from mee6!', inline=False)
        embed.add_field(name='Bug Fixes', value='Ive fuxed a lot of bugs this patch. A lot of inside stuff you probally didnt even notice :eyes:. This mostly included tags being broken. For example, they looked like <@@everyone> instead of @everyone. Simple errrors in text. If you find any more bugs, please report them!', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. I do have many typos in my code, and i have fixed many of them this update. If you spot another, let me know!', inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
#Update 0.5
@bot.command(pass_context=True)
async def update05(ctx):
     if ctx.message.author.permissions_in(ctx.message.channel).ban_members:
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 0.5 changelog')
        embed.add_field(name='Features', value='Ive added a bunch of features for this major patch.. i hope you enjoy them!', inline=False)
        embed.add_field(name='Suggestions', value='Now, we has a `suggest` command! You can use this command to suggest things like server suggestions, app suggestions, or anything you can think of! Please no bot suggestions though, use the next new feature for those!', inline=False)
        embed.add_field(name="Feedback", value="The new `feedback` command will send me any feedback, suggestions, or reports you may have!", inline=False)
        embed.add_field(name="Levels", value="Ive made bige changes to levels. Mostly inside stuff. Currently, you can only check your own level. This is changing soon!", inline=False)
        embed.add_field(name="Mod Feature", value="Ive added better logs (with reasons), and fixed a bug requiering you to enter a reason when giving action.", inline=False)
        embed.add_field(name='Bug Fixes', value='Ive fuxed a lot of bugs this patch. A lot of inside stuff you probally didnt even notice :eyes:. Some things were text that didnt look right, and some were more majoe like join logs not working due to a date error. If you find anymore bugs, use the `feedback` command so i can squash them!', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. I do have many typos in my code, and i have fixed many of them this update. If you spot another, let me know through the `feedback` command!', inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
 
       
@bot.command(pass_context=True)
async def changelog(ctx):
       
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='AppBot version 1.0 changelog')
        embed.add_field(name='v1.0', value='Hello everyone! This update is HUGE! Thats right, v1.0 is here, and the bot is now fully stable! Ive worked a ton this patch, but i have to give EXTREAME credit where its due. This update and many others following are only possble thanks to <@359366374411468802> and <@322564797403234306> for their donations twords the bot. They are the reason 1.0 is able to come out so soon, and why i was able to code 5 updates in one. Thanks a ton :heart:', inline=False)
        embed.add_field(name='Hosting', value='This is probally the most exciting thing ive gotten to announce in an update. Thansk to Doc and Dru, the bot is now hosted on a VPS 100% uptime, 24h a day. No more downtime! This was a ton of work, but im so happy i was able to do it for you guys!', inline=False)
        embed.add_field(name='Modmail/tickets', value='Now intorducing: Modmail tickets! Need to contact staff or report a member for any reason? DM the bot! This will create a thread with you and any onine staff members! Check the help page for commands! If you abuse you will be blacklisted! This was a TON of code (3195 lines to be excact) in a library that i was just testing out. It may be buggy and have issues, if it does use the `feedback` cmd. I hope you enjoy this feature!', inline=False)
        embed.add_field(name='Command Changes', value='Some cmd names have been changed. `links` has been changed to `website`, and `vip` has been changed ro `vipsite`', inline=False)
        embed.add_field(name='Bug Fixes', value='Ive fuxed a lot of bugs this patch. Some stll havnt been fixed (such as punishment reasons) but most have. Such as the purge cmd not working, suggestions bugging out and not creating emojis, and more! If you spot another bug, let me know by using the `feedback` command so i can squash it!', inline=False)
        embed.add_field(name='Spelling Errors', value='Well this should be self explaitory. I do have many typos in my code, and i have fixed many of them this update. If you spot another, let me know through the `feedback` command!', inline=False)
        embed.set_footer(text=embed_footer)
        embed.set_thumbnail(url=embed_thumbnail)
        await bot.send_message(ctx.message.channel, embed=embed)
   
                                 
                     
bot.run('TOKEN')
