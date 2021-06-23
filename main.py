
import discord
from discord.ext import commands
import datetime
import asyncio
from asyncio.tasks import sleep
import random
from discord import embeds
from discord import client
from discord.colour import Color

bot = commands.Bot(command_prefix = ",")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command()
@commands.has_role("Owner")
async def gstart(ctx, mins : int, *, prize: str):
    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins)

    embed.add_field(name="Ends At:", value=f"{end} UTC")
    #embed.set_footer(text="Ends {mins} minutes from now!")

    my_msg = await ctx.send(embed = embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")

bot.run("#")