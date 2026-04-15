import json


async def get_clan_list(ctx):
    with open('Queen_Spy/data/data_clan_'+ctx.guild.name+'.json') as f:
        clan_data = json.load(f)

    num = 1
    msg1 = '**All clan members ingame**\n'
    msg2 = ''
    for player in clan_data['clan']:
        if num <= 25:
            msg1 += str(num) + '. **brawlhalla_id**: ' + \
                str(player['brawlhalla_id']) + ', **brawlhalla_name**: ' + \
                player['name'] + '\n'
        else:
            msg2 += str(num) + '. **brawlhalla_id**: ' + \
                str(player['brawlhalla_id']) + ', **brawlhalla_name**: ' + \
                player['name'] + '\n'
        num += 1
    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)
