import discord
from Queen_Spy.commands.command_link_list import get_not_linked_brawlhalla_list, get_not_linked_discord_list, get_left_players
from Queen_Spy.commands.command_clan_update import update_clan_data
from Queen_Spy.commands.command_discord_update import update_discord_data

async def get_status(ctx, embed_color):
    # send loading message
    msg_loading_data = await ctx.send('_Loading Data..._')

    # update all data
    await update_discord_data(ctx)
    update_clan_data(ctx)

    # setup all embeds and their corresponding information
    msg_list2 = await get_not_linked_brawlhalla_list(ctx)
    embed_not_linked_brawlhalla_list_first = discord.Embed(
        description=msg_list2[0], color=embed_color)
    embed_not_linked_brawlhalla_list_last = discord.Embed(
        description=msg_list2[1], color=embed_color)

    msg_list3 = await get_not_linked_discord_list(ctx)
    embed_not_linked_discord_list_first = discord.Embed(
        description=msg_list3[0], color=embed_color)
    embed_not_linked_discord_list_last = discord.Embed(
        description=msg_list3[1], color=embed_color)

    msg_left_players = await get_left_players(ctx)
    embed_left_players = discord.Embed(description=msg_left_players,
                                       color=embed_color)

    # send embeds
    # send not linked brawlhalla accounts
    await ctx.channel.send(embed=embed_not_linked_brawlhalla_list_first)
    try:
        await ctx.channel.send(embed=embed_not_linked_brawlhalla_list_last)
    except:
        print('less than 26 entries')

    # send not linked discord accounts
    await ctx.channel.send(embed=embed_not_linked_discord_list_first)
    try:
        await ctx.channel.send(embed=embed_not_linked_discord_list_last)
    except:
        print('less than 26 entries')

    # send all players who left the clan
    await ctx.send(embed=embed_left_players)

    # delete loading message
    await msg_loading_data.delete()