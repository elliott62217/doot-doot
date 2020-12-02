#dood doot bot by ElliottRF

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print ("Ready when you are")
    print ("I am running on " + bot.user.name)
    print ("With The ID: " + str(bot.user.id))
    

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send(":ping_pong: ping!!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def inf(ctx, user: discord.Member):
    await ctx.send("The username is: {}".format(user.name))
    await ctx.send("The users ID is: {}".format(user.id))
    await ctx.send("The users status is: {}".format(user.status))
    await ctx.send("The users highest role is: {}".format(user.top_role))
    await ctx.send("The user joined at: {}".format(user.joined_at))


@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    await ctx.send("The avatar url is {}".format(user.avatar_url))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    info = discord.Embed(title="USER INFO", color=0x00ff00)
    info.set_footer(text="pubg>fortnite")
    info.set_author(name="doot doot")
    info.add_field(name="The username is: ", value=format(user.name), inline=True)
    info.add_field(name="The users ID is: ", value=format(user.id), inline=True)
    info.add_field(name="The users status is: ", value=format(user.status), inline=True)
    info.add_field(name="The users highest role is: ", value=format(user.top_role), inline=True)
    info.add_field(name="The user joined at: ", value=format(user.joined_at), inline=True)
    await ctx.send(embed=info)

@bot.command(pass_context=True)
async def lmfao(ctx):
    await ctx.send("LMFAOOOO "+ctx.message.author.mention+" :joy: :sunglasses: :ok_hand::skin-tone-1: :fire: ")

@bot.command(pass_context=True)
async def serverinfo(ctx):
    info = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    info.set_author(name="doot doot")
    info.add_field(name="Name: ", value=(ctx.message.server.name), inline=True)
    info.add_field(name="ID: ", value=(ctx.message.server.id), inline=True)
    info.add_field(name="Roles: ", value=len(ctx.message.server.roles), inline=True)
    info.add_field(name="Members: ", value=len(ctx.message.server.members))
    await ctx.send(embed=info)

    


@bot.command(pass_context=True)
async def commands(ctx):
    await ctx.send("Command List:")
    await ctx.send("#info")
    await ctx.send("#inf")
    await ctx.send("#avatar (@)")
    await ctx.send("#lmfao")

@bot.command(pass_context=True)
async def esketit(ctx):
    await ctx.send("ESKKETITT :fire: :ok_hand: :skin-tone-1: :sunglasses:")
    await ctx.send("http://i0.kym-cdn.com/entries/icons/original/000/024/776/maxresdefault.jpg")


bot.run("x")
