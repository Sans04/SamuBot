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
        role = discord.utils.find(lambda r: r.name == "NEW", msg.server.roles)
        role1 = discord.utils.find(lambda r: r.name == "Moderator", msg.server.roles)
        await client.remove_roles(user, role1)
        await client.add_roles(user, role)
        await client.send_message(chat, "Now you are NEW")


    if message.content.startswith('?uptime'):
        await client.send_message(message.channel, "`Ich bin schon {0} Stunde/n und {1} Minuten online auf {2}. `".format(hour, minutes, message.server))


    if message.content.lower().startswith("?role"):
        botmsg = await client.send_message(message.channel, "You want to be NEW?")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author






@client.event
async def on_message(message):
    if message.content.startswith('?join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Kein Voice channel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('?quit'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin zur zeit nicht connected.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))





@client.event
async def on_member_join(member):
    serverchannel = member.server.default_channel
    msg = "Willkommen {0} auf {1}".format(member.mention, member.server.name)
    await client.send_message(serverchannel, msg)


@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "Bye Bye {0}".format(member.mention)
    await client.send_message(serverchannel, msg)


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
