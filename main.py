# merge github and release

import random
from commands.command_link_remove import remove_link
from commands.command_waitinglist_list import get_waitinglist_list
import discord
import os
from modules.keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import has_permissions
from commands.command_clan_list import get_clan_list
from commands.command_discord_list import get_discord_list
from commands.command_link_list import get_link_list
from commands.command_clan_update import update_clan_data
from commands.command_discord_update import update_discord_data
from commands.command_status import get_status
from commands.command_link_add import add_link
from commands.command_link_update import update_links
from modules.assign import assign_all
from modules.env import env_variable


# VARIABLES
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['qs', 'Qs'], intents=intents)
embed_color = 0x790eab

# ⬇️ STATUS COMMANDS ⬇️
# ⬇️ STATUS COMMANDS ⬇️
# ⬇️ STATUS COMMANDS ⬇️


@bot.command(
    name='status',
    aliases=['tatus', 'st', 's'],
    description=
    'Shows new discord members, new clan members and if people left the clan')
async def status(ctx):
    # get and send status (maybe seperate this so no dependency in file)
    await get_status(ctx, embed_color)


# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️
# ⬇️ DISCORD COMMANDS ⬇️


@has_permissions(ban_members=True)
@bot.command(name='lsdi',
             aliases=['lsdc'],
             description='Show all clan members in discord')
async def show_all_discord_members(ctx):
    # update clan data
    await ctx.send(await update_discord_data(ctx))

    # get discord list
    msg_list = await get_discord_list(ctx)

    # send discord list
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)


# ⬇️ CLAN COMMANDS ⬇️
# ⬇️ CLAN COMMANDS ⬇️ **
# ⬇️ CLAN COMMANDS ⬇️


@has_permissions(ban_members=True)
@bot.command(name='lscl', description='Show all ingame clan members')
async def show_all_clan_members(ctx):
    # update clan data
    await ctx.channel.send(update_clan_data(ctx))

    # get clan list
    msg_list = await get_clan_list(ctx)

    # send clan list
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    await ctx.channel.send(embed=embed2)


@bot.command(name='upcl', description='Manually updates clan data')
async def qsupcl(ctx):
    await ctx.channel.send(update_clan_data(ctx))


# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️
# ⬇️ LINKING COMMANDS ⬇️


@has_permissions(ban_members=True)
@bot.command(name='rmli', description='Remove a discord-brawlhalla link')
async def rmli(ctx, brawlhalla_id):
    # remove link from link list
    await remove_link(brawlhalla_id, bot, ctx)


@rmli.error
async def missing_question(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'format your message like the following\n`qsrmli brawlhalla_id`')


@bot.command(name='lsli', description='Show All Links')
@has_permissions(ban_members=True)
async def list_link(ctx):
    # update link list
    embed_name_changes = update_links(ctx, embed_color)

    # get link list
    msg_list = await get_link_list(ctx)

    # send link list
    embed1 = discord.Embed(description=msg_list[0], color=embed_color)
    embed2 = discord.Embed(description=msg_list[1], color=embed_color)
    await ctx.channel.send(embed=embed1)
    try:
        await ctx.channel.send(embed=embed2)
    except:
        print('less than 26 entries')

    # send name changes
    await ctx.channel.send(embed=embed_name_changes)


@has_permissions(ban_members=True)
@bot.command(
    name='adli',
    aliases=['addli', 'ali'],
    description='Create a link between a discord and brawlhalla account')
async def qsadli(ctx, brawlhalla_id, discord_id):
    # adds a link to link list
    await add_link(bot, ctx, brawlhalla_id, discord_id, embed_color)


@qsadli.error
async def missing_question(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            'format your message like the following\n`qsadli brawlhalla_id discord_id`'
        )


@bot.command(name='upli',
             description='manually updates all old brawlhalla names in links')
async def upli(ctx):
    await ctx.channel.send(embed=update_links(ctx, embed_color))


# ⬇️ WAITING LIST COMAMNDS ⬇️
# ⬇️ WAITING LIST COMAMNDS ⬇️
# ⬇️ WAITING LIST COMAMNDS ⬇️


@has_permissions(ban_members=True)
@bot.command(name='lswa', description='Shows Waiting List')
async def get_waiting_list(ctx):
    # delete command message
    await ctx.message.delete()
    # get and send waiting list
    await ctx.channel.send(embed=await get_waitinglist_list(ctx=ctx))


# ⬇️ OTHER COMMANDS ⬇️
# ⬇️ OTHER COMMANDS ⬇️
# ⬇️ OTHER COMMANDS ⬇️

@has_permissions(ban_members=True)
@bot.command(name='assignall')
async def assignall(ctx, role_name):
  await assign_all(ctx, role_name)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    log_channel = bot.get_channel(973594560368373820)
    await log_channel.send("I'm back online!")


@bot.command(name='say')
async def say(ctx, arg):
    await ctx.message.delete()
    await ctx.channel.send(arg)


@bot.command(name='meme')
async def meme(ctx):
    memes = [
        'https://media.discordapp.net/attachments/973594560368373820/991113816299548753/unknown.png',
        'https://cdn.discordapp.com/attachments/973594560368373820/991114373366034512/unknown.png',
        'https://media.discordapp.net/attachments/973594560368373820/991115406716719144/unknown.png?width=589&height=670',
        'https://cdn.discordapp.com/attachments/973594560368373820/991116025158443019/unknown.png'
    ]
    meme = memes[random.randint(0, len(memes) - 1)]
    await ctx.channel.send(meme)


@bot.command(name='doc',
             aliases=['docs'],
             description="Send you to the GitHub page")
async def doc(ctx):
    await ctx.channel.send(
        'Queen Spy Documentation -> https://github.com/CrossyChainsaw/Queen-Spy'
    )



def run_queen_spy():
    bot.run(env_variable("QUEEN_SPY_BOT_TOKEN"))
