from discord.ext import commands
import discord

import config

bot = commands.Bot(command_prefix=config.prefix)
bot.remove_command("help")

async def _can_run(cmd, ctx):
    try:
        return await cmd.can_run(ctx)
    except:
        return False

@bot.event
async def on_ready():
    print(f"{bot.user} is ready!")

@bot.command()
@commands.is_owner()
async def poweroff(ctx):
    """Turns off the bot"""
    await ctx.send("Bye")
    await bot.logout()

@bot.command(name="help")
async def _help(ctx, *, command_name: str=None):
    """A little help always comes handy"""
    if command_name:
        command = bot.get_command(command_name)
        if not command:
            return await ctx.send("No such command!")
        return await ctx.send(f"```\n{ctx.prefix}{command.name} {command.signature}\n\n{command.help or 'Missing description'}```")
    description = []
    for name, cog in bot.cogs.items():
        entries = [" - ".join([cmd.name, cmd.short_doc or "Missing description"]) for cmd in cog.get_commands() if await _can_run(cmd, ctx) and not cmd.hidden]
        if entries:
            description.append(f"**{name}**:")
            description.append("• " + "\n• ".join(entries))
    await ctx.send(embed=discord.Embed(description="\n".join(description), color=ctx.me.color))

if __name__ == "__main__":
    bot.run(config.token)
