import os, json, discord
from dotenv import load_dotenv
from prefix import get_prefix, set_prefix 
from spells import print_spell

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
default_prefix = "&"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_guild_join(guild):
    set_prefix(guild.id, "&")

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f"Hi, my prefix is {get_prefix(guild.id)}")
            break

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    prefix = get_prefix(message.guild.id)
    if message.content.startswith(prefix + "ping"):
        await message.channel.send("Pong!")

    elif message.content.startswith(prefix + "prefix "):
        set_prefix(message.guild.id, message.content[len(prefix + "prefix "):])
        await message.channel.send(f"Prefix set to {get_prefix(message.guild.id)}")

    elif message.content.startswith(prefix + "prefix"):
        await message.channel.send(f"My prefix is {prefix}")

    elif message.content.startswith(prefix + "spell "):
        search_term = message.content[len(prefix + "spell "):]
        matches = []
        for file in os.scandir('data/spells'):
            with open(file, "r") as f:
                spells = json.load(f)
                for spell in spells["spell"]:
                    if search_term.lower() == spell["name"][0:len(search_term)].lower():
                        matches.append(spell)
        if len(matches) > 1:
            pass
        else:
            await message.channel.send(embed=print_spell(matches[0]))
client.run(TOKEN)