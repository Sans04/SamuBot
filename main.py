import discord
import asyncio


client = discord.Client()
DEIN_USERNAME = "deine_user_id"



@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await client.change_presence(game=discord.Game(name="Sans"))


@client.event
async def on_message(message):
    if message.content.lower().startswith('?test'):
        await client.send_message(message.channel, "Test bestanden")
    if message.content.lower().startswith('hi'):
        await client.send_message(message.channel, "heyy")
    

    if message.author.name == "alex-botxd":
        if message.content.lower().startswith("witz des tages"):
            await client.add_reaction(message, "👍")
            await client.send_message(message.channel, "LUSTIG")
            asyncio.sleep(2)
            await client.send_message(message.channel, "NICHT" + ":yay:")

        


client.run('NDA3OTU0MzU2NjAwODMyMDAx.De7jRQ.vix8RqmAlnPCME1PTbcnp3fg1E0')
