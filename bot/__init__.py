import discord
from discord.ext import commands





intents = discord.Intents.default()
intents.message_content = True  # Allow reading message content

bot  = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    """
    Load all extensions (cogs) for the bot.
    """

    await bot.load_extension("bot.commands.price")
    await bot.load_extension("bot.events.on_ready")
