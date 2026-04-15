import json
import discord

# todo
# get all clan member names
# replace all current clan member names in link list


async def get_link_list(ctx):
    with open('Queen_Spy/data/data_link_'+ctx.guild.name+'.json') as f:
        link_data = json.load(f)
    msg1 = '**All links between discord and brawlhalla**\n'
    msg2 = ''
    for num, user in enumerate(link_data, 1):
        if num <= 25:
            msg1 += '**{}**:\n **brawlhala_id**: {} **brawlhalla_name**: {}\n **discord_id**: {} **discord_name**: {}\n\n'.format(
                str(num), user['brawlhalla_id'], user['brawlhalla_name'], user['discord_id'], user['discord_name'])
        else:
            msg2 += '**' + str(num) + '**: \n**brawlhalla_id**: ' + \
                user['brawlhalla_id'] + ', **brawlhalla_name**: ' + \
                user['brawlhalla_name'] + '\n**discord_id**: ' + \
                user['discord_id'] + ', **discord_name**: ' + \
                user['discord_name'] + '\n\n'
    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return msg_list


async def get_not_linked_brawlhalla_list(ctx):
    with open('Queen_Spy/data/data_clan_'+ ctx.guild.name +'.json') as f:
        clan_data = json.load(f)
    with open('Queen_Spy/data/data_link_'+ctx.guild.name+'.json') as f:
        link_data = json.load(f)

    new_brawlhalla_ids = []
    new_brawlhalla_names = []
    for member in clan_data['clan']:
        new_id = True
        for link in link_data:
            if str(link['brawlhalla_id']) == str(member['brawlhalla_id']):
                new_id = False
        if new_id == True:
            new_brawlhalla_ids.append(str(member['brawlhalla_id']))
            new_brawlhalla_names.append(str(member['name']))

    msg1 = "**The following people are in the in-game clan, but aren't linked yet\n**"
    msg2 = ""
    num = 1
    for (id, name) in zip(new_brawlhalla_ids, new_brawlhalla_names):
        if num <= 25:
            msg1 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        else:
            msg2 += str(num) + '. **brawlhalla_id**: ' + id + \
                ', **brawlhalla_name**: ' + name + '\n'
        num += 1

    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_not_linked_discord_list(ctx):
    with open('Queen_Spy/data/data_discord_'+ctx.guild.name+'.json') as f:
        data_discord = json.load(f)
    with open('Queen_Spy/data/data_link_'+ctx.guild.name+'.json') as f:
        link_data = json.load(f)

    new_discord_ids = []
    new_discord_names = []
    for account in data_discord:
        new_id = True
        for link in link_data:
            if str(link['discord_id']) == str(account['id']):
                new_id = False
        if new_id == True:
            new_discord_ids.append(str(account['id']))
            new_discord_names.append(str(account['name']))

    msg1 = "**The following people have the role in discord, but aren't linked yet\n**"
    msg2 = ""
    num = 1
    for (id, name) in zip(new_discord_ids, new_discord_names):
        if num <= 25:
            msg1 += str(num) + '. **discord_id**: ' + id + \
                ', **discord_name**: ' + name + '\n'
        else:
            msg2 += str(num) + '. **discord_id**: ' + id + \
                ', **discord_name**: ' + name + '\n'
        num += 1

    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)


async def get_left_players(ctx):
    with open('Queen_Spy/data/data_link_'+ctx.guild.name+'.json') as f:
        link_data = json.load(f)
    with open('Queen_Spy/data/data_clan_'+ctx.guild.name+'.json') as f:
        clan_data = json.load(f)

    msg = "**The following accounts are linked, but aren't in the clan anymore**\n"
    num = 1
    for link in link_data:
        entry_exists = False
        for member in clan_data['clan']:
            if str(link['brawlhalla_id']) == str(member['brawlhalla_id']):
                entry_exists = True
        if entry_exists == False:
            msg += str(num) + '. **brawlhalla_id**: ' + \
                link["brawlhalla_id"] + ', **brawlhalla_name**: ' + \
                link['brawlhalla_name'] + '\n'
            num += 1

    return msg
