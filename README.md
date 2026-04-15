Holy this documentation sucks please fix this

---

# Queen Spy Documentation 
In short, Queen Spy manages the links between brawlhalla and discord accounts. This helps to see if there are currently people in the discord with the clan role that shouldn't have the clan role.

## Table of Contents
- [Prefix](#prefix)
- [How to use](#how-to-use)
- [List of Commands](#list-of-commands)
  - [Command Logic](#command-logic)
  - [Get Status](#get-status)
  - [Add Link](#add-link)
  - [Remove Link](#remove-link)
  - [Update Links](#update-links)
  - [Update Clan](#update-clan)
  - [Get Link List](#get-link-list)
    - [Get Name Changes](#get-name-changes)
  - [Get Clan List](#get-clan-list)
  - [Get Discord List](#get-discord-list)
  - [Get Waiting List](#get-waiting-list)

# Prefix
Both `qs` and `Qs` work.

# How to use
First run `qstatus`, this gives you the current status of the clan and discord accounts. So what you should be doing is adding links between brawlhalla accounts and discord accounts. By adding links, they get removed from `qstatus`. Your goal is to make `qstatus` output nothing. I'll bring you through an example.

## Examples
Force is a new member to our clan and joined our discord. `qstatus` / `qsstatus` shows us that his brawlhalla account isn't linked yet, also does it show his discord account isn't linked yet.

![image](https://user-images.githubusercontent.com/74303221/176176688-37c51b9b-0500-43c5-aa8c-561c9dd532be.png)

To solve this we add a link between his accounts using the `qsadli` command.

![image](https://user-images.githubusercontent.com/74303221/176177177-31d1869e-b49e-4e74-aec3-26a3ac4f054e.png)

If we run `qstatus` now, you'll see it doesn't point out anyone to us. You can also run `qslsli` to see the link is added to the list of links.

![image](https://user-images.githubusercontent.com/74303221/176177321-a524f02d-794b-4949-9e60-f152ced22285.png)

This means everyone their brawlhalla account and discord account are linked. Now when a linked person leaves the clan and we run `qstatus`, Queen Spy will point out who left.

a player named Emma left the clan, when we run `qstatus`, Queen Spy points out an account that is linked but not in the clan anymore.

![image](https://user-images.githubusercontent.com/74303221/176177804-ee6c8d6f-f617-4ee6-9447-86d72c4f56ed.png)

This means we can remove him from the discord and remove the link.

![image](https://user-images.githubusercontent.com/74303221/176178969-11474ebb-f330-42f0-b2e4-9aa916855257.png)

if we run `qstatus` now, it doesn't point out anything, meaning everything is solved.

![image](https://user-images.githubusercontent.com/74303221/176179196-22e1c435-838a-44b1-b98d-b1e818603757.png)

If it ever shows a `discord_id` but not a `brawlhalla_id` this means someone is in the discord has the `@Clan Member` role who shouldn't have it.

![image](https://user-images.githubusercontent.com/74303221/176179611-b3ba52ea-0fc1-420c-9dec-a58769c1e7c2.png)

To solve this we simply remove `@Clan Member` role from Queen Spy, if we run `qstatus` now its blank again.

# List of commands

## Command Logic
A command consists of 2 letters after each other multiple times.

**Example 1**

`qsadli` stands for 

- qs -> queen spy

- ad -> add

- li -> link

**Example 2**

`qslsdc` stands for

- qs -> queen spy

- ls -> list

- dc -> discord

Multiple commands more than 1 command names. For example `qsali` / `qsadli` / `qsaddli` all do the same thing.

## Get Status
`qsstatus` / `qstatus` gives you the current status of the brawlhalla accounts, discord accounts and links.

## Add Link
`qsadli` / `qsaddli` / `qsali` creates a new link. Keep in mind that you have to provide parameters.

**Example**

`qsadli brawlhalla_id discord_id`

`qsadli 7364605 413070742591373314`

Bot will respond with 

`Are you sure you want to add the following link?`

```py
brawlhalla_id: 7364605
brawlhalla_name: CrossyChainsaw
discord_id: 413070742591373314
discord_name: CrossyChainsaw
```
`Send y to confirm or n to cancel.`

type `y` to confirm and `n` to cancel.

now type `qslsli` to get the list with links. You'll see the new link is added.

**Pro tip: you can type the first 3 numbers instead of the whole ID. So instead of** `qsadli 7364605563 413070742591373314` **you can also type** `qsadli 736 413`

## Remove Link
`qsrmli brawlhalla_id` with this command you can remove an existing link, just like adding a link, it will ask for confirmation. To see all brawlhalla ids of the links use the command `qslsli`.

**Pro tip: you can type the first 4 numbers instead of the whole ID. So instead of** `qsrmli 7364605563 ` **you can also type** `qsrmli 7364`

# Update Links
`qsupli` manually updates all links in the link list. Also does this command point out people who changed their name, see example below.

![image](https://user-images.githubusercontent.com/74303221/188316637-a2fbdbce-5cd3-41a6-b371-cda2792dd6f1.png)

This command runs automatically when running `qslsli`

# Update Clan
`qsupcl` manually updates clan data. This command automatically runs when running `qslscl`

## Get Link List
`qslsli` shows a list of all current links between discord and brawlhalla. (This command automatically runs `qsupli`)

### Get Name Changes
As if right now the command `qslsli` also shows all name changes. Here is an example.

![image](https://user-images.githubusercontent.com/74303221/190578712-3967570f-8fd4-4e84-bc70-2c844a7a24b5.png)

## Get Clan List
`qslscl` return a list of all clan members in game.

## Get Discord List
`qslsdc` / `qslsdi` returns a list of everyone in the discord with the `@Clan Member` role.

## Get Waiting List
`qslsw` / `qslswa` returns a list of everyone in the discord server with the `@Waiting List` role.
