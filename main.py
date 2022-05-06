import asyncio

import discord
import os
from lib import Mailer

token = os.environ['DISCORD_TOKEN']

mailer = Mailer()
# mailer.send("plz\na\nb")
import platform

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import discord



client = discord.Client()
def parse_deal(embed):
    title = embed.title
    url = embed.url
    details = {}
    for field in embed.fields:
        print(field)
        if field.name == 'Promo Codes' and field.value != 'None':
            details['Promo Code'] = field.value

    return title, url, details



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message):
    if message.channel.name == 'amazon-freebies':
        if not message.embeds: return
        title, url, details = parse_deal(message.embeds[0])

        embed = message.embeds[0]
        # output = [embed.title, embed.url]
        print(embed.title)

        mailer.send(title)
        mailer.send(url)
        detailed = ""
        for key, value in details.items():
            detailed += f"{key}: {value}\n"
        mailer.send(detailed)

client.run(token)
