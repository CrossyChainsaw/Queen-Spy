import discord
import json
from Queen_Spy.classes.DiscordAccount import DiscordAccount


async def update_discord_data(ctx):
    if ctx.guild.name == "Dair":
      clan_member_role_name = '💧 Dair 💧'
    elif ctx.guild.name == "Skyward":
      clan_member_role_name = 'Clan Member'
    elif ctx.guild.name == "🌸Blossom🌸":
      clan_member_role_name = "Blossom"
    elif ctx.guild.name == "Pandation":
      clan_member_role_name = "Pandation"
    guild = ctx.guild
    msg = ''
    num = 1
    discord_member_names = []
    discord_member_ids = []
    discord_accounts = []
    role = discord.utils.get(ctx.message.guild.roles, name=clan_member_role_name)
    for member in guild.members:
        if role in member.roles:
            msg += str(num) + '. ' + member.name + '\n'
            discord_member_ids.append(member.id)
            discord_member_names.append(member.name)
            num += 1
        if role in member.roles:
            account = DiscordAccount(member.id, member.name)
            discord_accounts.append(account.__dict__)
    with open('Queen_Spy/data/data_discord_' + ctx.guild.name + '.json', 'w') as f:
        json_string = json.dump(discord_accounts, f)
    msg = '*Updated ' + ctx.guild.name + 'discord data*'
    return msg
