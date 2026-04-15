import json


async def get_discord_list(ctx):
    with open('Queen_Spy/data/data_discord_'+ctx.guild.name+'.json') as f:
        discord_data = json.load(f)

    num = 1
    msg1 = '**All discord members with the clan member role**' + '\n'
    msg2 = ''
    for player in discord_data:
        if num <= 25:
            msg1 += str(num) + '. **discord_id**: ' + \
                str(player['id']) + ', **discord_name**: ' + \
                player['name'] + '\n'
        else:
            msg2 += str(num) + '. **discord_id**: ' + \
                str(player['id']) + ', **discord_name**: ' + \
                player['name'] + '\n'
        num += 1
    msg_list = []
    msg_list.append(msg1)
    msg_list.append(msg2)
    return(msg_list)
