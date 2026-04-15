import json
import discord

# todo
# get link list data
# get clan member data
# in link list replace clan member name with clan member data names

def update_links(ctx, embed_color):
  # get link list
  with open('Queen_Spy/data/data_link_'+ctx.guild.name+'.json') as f1:
    link_data = json.load(f1)
  # get clan list
  with open('Queen_Spy/data/data_clan_'+ctx.guild.name+'.json') as f2:
    clan_data = json.load(f2)

  embed = discord.Embed(title='Name Changes', description='', color=embed_color)
  
  link_data_new = []  
  # in link list replace clan member name with clan member data names
  for account in link_data:
    for clan_member in clan_data['clan']:
      if str(account['brawlhalla_id']) == str(clan_member['brawlhalla_id']):
        if account['brawlhalla_name'] != clan_member['name']:
          embed.description += '**old_name**: ' + account['brawlhalla_name']+'\n'
          embed.description += '**new_name**: ' + clan_member['name'] + '\n'
          embed.description += '\n'
          account['brawlhalla_name'] = clan_member['name']
        break
  link_data_new = link_data
  # overwrite old data with new data
  with open('Queen_Spy/data/data_link_' + ctx.guild.name + '.json', 'w') as f:
    json.dump(link_data_new, f)
  # check if embed is empty
  if len(embed.description) == 0:
    embed.description += 'there were no new name changes'
  return embed
    
  