import os

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def cheat(ctx: commands.Context):
    LIST = "\n".join(str(f'{c:<16} {desc}') for (c, desc) in [
        ('# CHARACTERS', ''),
        ('[^ABC] [ABC]', '(negated) character set'),
        ('[A-Z]', 'range'),
        ('\\W \\w', '(not) word'),
        ('\\D \\d', '(not) digit'),
        ('\\S \\s', '(not) whitespace'),
        ('.', 'any single character'),
        ('# QUANTIFIERS', ''),
        ('*', 'zero or more'),
        ('+', 'one or more'),
        ('?', 'zero or one'),
        ('{n, m}', 'n to m'),
        ('# ANCHORS', ''),
        ('^', 'beginning'),
        ('$', 'end'),
        ('\\B \\b', '(not) word boundary'),
        ('# GROUP', ''),
        ('(?:ABC) (ABC)', '(non-)capturing group'),
        ('(?<name>ABC)', 'named capturing group'),
        ('\\1', 'numeric reference'),
        ('# LOOKAROUND', ''),
        ('(?=ABC)', 'positive lookahead'),
        ('(?!ABC)', 'negative lookahead'),
        ('(?<=ABC)', 'positive lookbehind'),
        ('(?<!ABC)', 'negative lookbehind'),
        ('# ESCAPE', ''),
        ('\\+', 'reversed character'),
        ('\\000', 'octal'),
        ('\\xFF', 'hexadecimal'),
        ('\\u{FFFF} \\uFFFF', '(extended) unicode'),
        ('\\cI', 'control character'),
        ('\\v \\t', '(vertical) tab'),
        ('\\n', 'line feed'),
        ('\\f', 'form feed'),
        ('\\r', 'carriage return'),
        ('\\0', 'null'),
    ])

    EMBED = discord.Embed(
        title='RegEx Cheatsheet',
        description=f'```yaml\n{LIST}```'
    ).set_footer(text='Adapted from regexr.com')

    await ctx.send(f'{ctx.author.id}')

    await ctx.send(embed=EMBED)

token = os.environ['BOT_TOKEN']
bot.run(token)
