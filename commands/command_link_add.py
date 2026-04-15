import json
import discord
from Queen_Spy.classes.User import User

h = 'hello time'
g = 'swagg moment'

async def add_link(bot, ctx, brawlhalla_id, discord_id, embed_color):
    # first check if the entry already exists
    with open('./data/data_link_' + ctx.guild.name + '.json') as data:
        link_data = json.load(data)
    new_entry = True
    for user in link_data:
      if len(str(brawlhalla_id)) > 3:
        if str(user['brawlhalla_id']) == str(brawlhalla_id):
            await ctx.send('brawlhalla_id: ' + brawlhalla_id +
                           ' has already been linked')
            new_entry = False
            break
      else:
        if str(user['brawlhalla_id'])[0:3:1] == str(brawlhalla_id)[0:3:1]:
            await ctx.send('brawlhalla_id: ' + brawlhalla_id +
                           ' has already been linked, if not try entering the full id')
            new_entry = False
            break
      if len(str(discord_id)) > 3:
        if str(user['discord_id']) == str(discord_id):
            await ctx.send('discord_id: ' + discord_id +
                           ' has already been linked')
            new_entry = False
            break
      else:
        if str(user['discord_id'])[0:3:1] == str(discord_id)[0:3:1]:
            await ctx.send('discord_id: ' + discord_id +
                           ' has already been linked, if not try entering the full id')
            new_entry = False
            break

    brawlhalla_name = 'blank'
    discord_name = 'blank'
    short_hand = False

    # check if ids are valid
    if new_entry == True:
        valid_brawlhalla_id = False
        valid_discord_id = False
        # check clan id
        with open('./data/data_clan_' + ctx.guild.name + '.json') as data:
            clan_data = json.load(data)
        for member in clan_data['clan']:
            if str(member['brawlhalla_id']) == str(brawlhalla_id):
                valid_brawlhalla_id = True
                brawlhalla_name = member['name']
        if valid_brawlhalla_id == False:
          for member in clan_data['clan']:
            if str(member['brawlhalla_id'])[0:3:1] == str(brawlhalla_id)[0:3:1]:
                brawlhalla_id = str(member['brawlhalla_id'])
                valid_brawlhalla_id = True
                brawlhalla_name = member['name']
                short_hand = True
        # check dc id
        with open('./data/data_discord_' + ctx.guild.name + '.json') as data:
            discord_data = json.load(data)
        for account in discord_data:
            if str(account['id']) == str(discord_id):
                valid_discord_id = True
                discord_name = account['name']
        if valid_discord_id == False:
          for account in discord_data:
            if str(account['id'])[0:3:1] == str(discord_id)[0:3:1]:
                discord_id = str(account['id'])
                valid_discord_id = True
                discord_name = account['name']
                short_hand = True

    # if entry ids are valid, add it
    if ((valid_brawlhalla_id == True) and (valid_discord_id == True)
            and (new_entry == True)):
        if short_hand == True:
          await ctx.send("I couldn't find the exact id's but I found the following id's. If these are wrong try writing out the full id's")
        else:
          await ctx.send('Are you sure you want to add the following link?,')
        await ctx.send(
            embed=discord.Embed(description='**brawlhalla_id**: ' +
                                brawlhalla_id + '\n**brawlhalla_name**: ' +
                                brawlhalla_name + '\n**discord_id**: ' +
                                discord_id + '\n**discord_name**: ' +
                                discord_name,
                                color=embed_color))
        await ctx.send('Send `y` to confirm or `n` to cancel.')
        msg = await bot.wait_for('message', check=check)
        if msg.content == 'y':
            user = User(brawlhalla_id, brawlhalla_name, discord_id,
                        discord_name)
            users = []
            users = link_data
            users.append(user.__dict__)
            with open('./data/data_link_' + ctx.guild.name + '.json', 'w') as f:
                some_data = json.dump(users, f)

            embed = discord.Embed(
                description='**Added Following Link**\n**brawlhalla_id**: ' +
                brawlhalla_id + '\n**brawlhalla_name**: ' + brawlhalla_name +
                '\n**discord_id**: ' + discord_id + '\n**discord_name**: ' +
                discord_name,
                color=embed_color)
            await ctx.send(embed=embed)
        elif msg.content == 'n':
            await ctx.send('*Process Canceled*')
        else:
            await ctx.send('Invalid answer, process canceled')
    else:
        await ctx.send(
            "There was an error while trying to make the link. One of the following ids doesn't exist\n`discord_id: "
            + discord_id + '`\n`brawlhalla_id: ' + brawlhalla_id + '`')

def check(author):
  def inner_check(message):
    return message.author == author and message.content == "Hello"
  return inner_check