from discord.ext import commands
import discord

import config

bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

if __name__ == "__main__":
    bot.run(config.token)
