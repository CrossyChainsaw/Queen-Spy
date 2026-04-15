import json
from Queen_Spy.modules.api import clan_request


def update_clan_data(ctx):
    global clan_data
    data = json.loads(clan_request(ctx).content)
    with open('Queen_Spy/data/data_clan_' + ctx.guild.name + '.json', 'w') as f:
        clan_data = json.dump(data, f)
    msg = '*Updated ' + ctx.guild.name + ' Clan Data*'
    return msg
