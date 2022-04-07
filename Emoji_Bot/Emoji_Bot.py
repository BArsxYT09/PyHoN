import discord
from discord.activity import Game
from discord.ext import commands
from discord.ext.commands import bot
from discord.flags import Intents


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix= "", intents=intents)

@Bot.event
async def on_ready():
    print("BANE")

@Bot.command()
async def YardımEtBot(msg):
    await msg.send("Kullanabilceğin Komutlar : ")
    await msg.send("aglamak")
    await msg.send("pepedans")
    await msg.send("otuzbir")
    await msg.send("öpücük")
    await msg.send("supra")
    await msg.send("Fbı")
    await msg.send("np")
    await msg.send("bruh")
    await msg.send("amogus")
    await msg.send("lol")
    await msg.send("like")
    await msg.send("dislike")
    await msg.send("nazarboncuğu")
    await msg.send("tr")
    await msg.send("us")
    await msg.send("ukraynaya_destek_ol")
    await msg.send("savaşbitsin , #SAVAŞBİTSİNARTIK(SBA)")
    await msg.send("bluuscren")
    await msg.send("UnoTers")


@Bot.command()
async def aglamak(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/877129505863516160.png?size=64")
@Bot.command()
async def pepedans(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/880906167562416248.gif?size=64")
@Bot.command()
async def otuzbir(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/853947691860230164.gif?size=64")
@Bot.command()
async def öpücük(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/842050273740455967.png?size=64")
@Bot.command()
async def supra(ctx):
    await ctx.send("https://tenor.com/view/supra-gif-22160855")
@Bot.command()
async def Fbı(ctx):
    await ctx.send("https://tenor.com/view/fbi-fbiopenup-carlwhitman-gif-19586039")
@Bot.command()
async def np(ctx):
    await ctx.send("https://tenor.com/view/np-nope-check-boxes-gif-7864220")
@Bot.command()
async def bruh(ctx):
    await ctx.send("https://tenor.com/view/monkey-bruh-weak-sick-gif-16818912")
@Bot.command()
async def amogus(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/764770867661242379.png?size=64 ")
@Bot.command()
async def lol(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/754413401610125352.png?size=64 ")
@Bot.command()
async def like(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/638921289305948180.png?size=64 ")
@Bot.command()
async def dislike(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/638921287892336690.png?size=64 ")
@Bot.command()
async def nazarboncuğu(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/754413405984784525.png?size=64 ")
@Bot.command()
async def tr(ctx):
    await ctx.send(":flag_tr:")
@Bot.command()
async def us(ctx):
    await ctx.send(":flag_us:")
@Bot.command()
async def ukraynaya_destek_ol(ctx):
    await ctx.send(":flag_ua:")
    await ctx.send(":flag_ua:")
    await ctx.send(":flag_ua:")
@Bot.command()
async def savaşbitsin(ctx):
    await ctx.send(":flag_ru:")
    await ctx.send(":skull_crossbones:")
@Bot.command()
async def bluuscren(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/850766598246629436/852901398923575326/220px-Maviekran.gif")
@Bot.command()
async def UnoTers(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/850766598246629436/950435121113206794/uno-yon-degistir-ters-kart.png")
@Bot.command()
async def kombo(msg):
    await msg.send("https://cdn.discordapp.com/emojis/877129505863516160.png?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/880906167562416248.gif?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/853947691860230164.gif?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/842050273740455967.png?size=64")
    await msg.send("https://tenor.com/view/supra-gif-22160855")
    await msg.send("https://tenor.com/view/fbi-fbiopenup-carlwhitman-gif-19586039")
    await msg.send("https://tenor.com/view/np-nope-check-boxes-gif-7864220")
    await msg.send("https://tenor.com/view/monkey-bruh-weak-sick-gif-16818912")
    await msg.send("https://cdn.discordapp.com/emojis/764770867661242379.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/754413401610125352.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/638921289305948180.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/638921287892336690.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/754413405984784525.png?size")
    await msg.send(":flag_ua:")
    await msg.send(":flag_ua:")

Bot.run('ODk1NzM5MTAyMTE5NDczMTYy.YV88Cw.PeF7-dm1DViqsDNcYoGFpRByiMg')