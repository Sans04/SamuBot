import discord
import asyncio


client = discord.Client()
DEIN_USERNAME = "deine_user_id"


minutes = 0
hour = 0



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
            asyncio.sleep(4)
            await client.send_message(message.channel, "NICHT" + "<:yay:450746929702371328>")
 
    if message.content.startswith('?uptime'):
        await client.send_message(message.channel, "`Ich bin schon {0} stunde/n und {1} minuten online auf {2}. `".format(hour, minutes, message.server))

    if message.content.lower().startswith('?embed'):
        embed = discord.Embed(
            title="Hallo World",
            color=0xe67e22,
            description="guten tag welt adjkhfg iadsfgjkadsh gjkahdfbg adfg\n"
                        "yhuasdghasd\n"
                        "guten\n"
                        "tag"
        )
        embed.set_author(
            name="Bobo",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg",
            url="http://grewoss.com/"
        )
        embed.add_field(
            name="Title 2",
            value="Description 2\n"
                  "fgasdfujhkasfdgk adfg da\n"
                  "asdgufhadsfjgkhads\n"
                  "afsdgadifghahdioufg\n",
            inline=False
        )
        embed.add_field(
            name="haladfgad",
            value="asdgasdfg",
            inline=False
        )
        embed.add_field(
            name="asdggasdfgadfhg",
            value="adfiohgjadfi giuhadf gadjkfhg2222",
            inline=False
        )
        embed.set_footer(
            text="Ein bot von mir",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg"
        )
        embed.set_thumbnail(
            url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg"
        )

        await client.send_message(message.channel, embed=embed)
        
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
