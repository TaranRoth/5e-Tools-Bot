import discord

def print_spell(spell):
    schools = {
        "C" : "conjuration",
        "A" : "abjuration",
        "T" : "transmutation",
        "D" : "divination",
        "E" : "enchantment",
        "V" : "evocation",
        "I" : "illusion",
        "N" : "necromancy"
    }
    level = spell["level"]
    school = schools[spell["school"]]
    if level == 0:
        type_str = school.title() + " cantrip"
    elif level == 1:
        type_str = "1st level " + school
    elif level == 2:
        type_str = "2nd level " + school
    elif level == 3:
        type_str = "3rd level " + school
    else:
        type_str = f"{level}th level " + school
    description = f"""
Book: {spell["source"]}
Type: {type_str}
Description: {spell["entries"][0]}
At Higher Levels: {spell["entries"][1]}
""" 
    return discord.Embed(title=spell["name"], description=description)