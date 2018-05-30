import discord
import asyncio


client = discord.Client()
testmsgid = None
testmsguser = None


@client.event
async def on_ready():
    print(client.user.name)
    print("========")
    await client.change_presence(game=discord.Game(name="music"))


@client.event
async def on_message(message):
    if message.content.lower().startswith("hi"):
        await client.send_message(message.channel, "heyy")

    if message.content.startswith('?uptime'):
        await client.send_message(message.channel, "`Ich bin schon {0} Stunde/n und {1} Minuten online auf {2}. `".format(hour, minutes, message.server))


    if message.content.lower().startswith("?Abstimmung"):
        botmsg = await client.send_message(message.channel, "Ok")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author





async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

client.loop.create_task(tutorial_uptime())




client.run('NDA3OTU0MzU2NjAwODMyMDAx.De7jRQ.vix8RqmAlnPCME1PTbcnp3fg1E0')
