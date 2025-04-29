from discord.ext import commands


class OnReady(commands.Cog):
    """
    Event handler for when the bot is ready.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        Called when the bot is ready.
        """
        print(f"✅ Bot is ready. Logged in as {self.bot.user} (ID: {self.bot.user.id})")
        

async def setup(bot):
    """
    Load the OnReady cog.
    """
    await bot.add_cog(OnReady(bot))