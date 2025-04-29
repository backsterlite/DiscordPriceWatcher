from discord.ext import commands

from services.coingecko_service import CoinGeckoService


class Price(commands.Cog):
    """
    Price command to fetch the price of a given symbol.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def price(self, ctx, symbol: str):
        """
        Command !price SYMBOL
        Currently just a placeholder for response.
        """
        price = CoinGeckoService.get_price(symbol)
        if price is not None:
            await ctx.send(f"The current price of {symbol.upper()} is ${price:.2f}.")
        else:
            await ctx.send(f"Could not fetch the price for {symbol.upper()}. Please try again later.")
        
        
async def setup(bot):
    """
    Load the Price cog.
    """
    await bot.add_cog(Price(bot))
    
    