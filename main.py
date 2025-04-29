import os
import asyncio
from dotenv import load_dotenv
from bot import bot, load_extensions

load_dotenv()
DS_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not DS_TOKEN:
    print("❌ DISCORD_BOT_TOKEN not found in .env file.")
    exit(1)

async def main():
    await load_extensions()
    await bot.start(DS_TOKEN)


# Bot entry point
# This is the main entry point for the bot. It loads the necessary extensions and starts the bot.
if __name__ == "__main__":
    
    asyncio.run(main())