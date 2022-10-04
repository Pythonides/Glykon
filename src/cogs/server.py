import disnake
from disnake.ext import commands

from src.bot import Glykon


class Server(commands.Cog):
    """Server Cog"""

    def __init__(self, bot: Glykon):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Ping command"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command(
        name="server", aliases=["info", "serverinfo", "guild", "guildinfo"]
    )
    async def server_info(self, ctx: commands.Context) -> None:
        """Get info about the server"""
        guild = ctx.guild
        embed = disnake.Embed(
            title=guild.name,
            description=f"Owner: {guild.owner.mention}",
            color=0x00FF00,
        )
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(
            name="Created at", value=f"<t:{int(guild.created_at.timestamp())}:R>"
        )
        embed.add_field(name="Members", value=guild.member_count)
        embed.add_field(name="Roles", value=len(guild.roles))
        embed.add_field(name="Channels", value=len(guild.channels))
        embed.add_field(name="Emojis", value=len(guild.emojis))
        embed.add_field(name="Boosts", value=guild.premium_subscription_count)
        embed.add_field(name="Boost level", value=guild.premium_tier)
        embed.add_field(name="Verification level", value=guild.verification_level)

        val = ": [✅] \n".join(guild.features).replace("_", " ").lower()
        fixed_val = f"""```yml\n{val}: [✅]\n```"""

        embed.add_field(name="Features", value=fixed_val, inline=False)
        await ctx.send(embed=embed)


def setup(bot: Glykon) -> None:
    """Load the Server cog"""
    bot.add_cog(Server(bot))
