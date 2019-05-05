import discord
import asyncio
import random
from discord.ext.commands import Bot

Client = Bot('!')


client = discord.Client()
DEIN_NAME_ID= "DEINE_USER_ID"

xy = ['Staubsaugersuppe', 'Warum gibt es so wenig Frauenfußball. ||Ganz einfach: Frauen zu finden, die freiwillig das gleiche Kostüm anziehen, ist schwierig.||', 'Fragt die Ehefrau ihren Gatten: Was magst du mehr, meinen wunderschönen Körper oder meine überragende Intelligenz? Er, nach kurzer Überlegung: Eher deinen Sinn für Humor.']
az = ['||fett||', '||gay||', '||ein Ehrenmann||']



@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await client.change_presence(game=discord.Game(name="Bierpong"))


@client.event
async def on_message(message):
    if message.content.lower().startswith('rülps'):
        await client.send_message(message.channel, "```SCHULZ```")
    if message.content.lower().startswith('joke'):
        await client.send_message(message.channel, random.choice(xy))
    if message.content.lower().startswith('blaul ist'):
        await client.send_message(message.channel, random.choice(az))
    if message.content.lower().startswith('blöd'):
        await client.send_message(message.channel, "```Miese Prise```")
    if message.content.lower().startswith('schade'):
        await client.send_message(message.channel, "```Miese Prise```")
  
    if message.content.lower().startswith("jawoll"):
        await client.send_message(message.channel, "```JAWOLL```")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "```LOLL```")
        await client.add_reaction(message, "🍺")
        
    if message.content.lower().startswith("!vote"):
        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")
        await asyncio.sleep(8)
        await client.add_reaction(message, "🔥")
        await client.add_reaction(message, "🍻")
        await client.add_reaction(message, "💤")
        

    
    



    
    if message.content.startswith('info'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
 
            userembed = discord.Embed(
                title="Benutzername:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="🕵️"
            )
            userembed.add_field(
                name="Server Beitrittsdatum:",
                value=userjoinedat
            )
            userembed.add_field(
                name="Discord Beitrittsdatum:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Discriminator:",
                value=user.discriminator
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )
 
            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Ich konnte den Trinker nicht finden.")
        except:
            await client.send_message(message.channel, "Sorry Error")
        finally:
            pass
 
 




client.run('NDc4OTkyMzk2MDMwNDQzNTMw.DlSy6w.FL8E2wzGT8B7pypiKujTqPuRyJw')
