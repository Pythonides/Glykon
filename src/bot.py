import logging
import os

from disnake import Intents
from disnake.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
TOKEN = os.getenv("TOKEN")

# Logger config
logger = logging.getLogger("disnake")
logger.setLevel(logging.DEBUG)

# Handler config
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s || %(levelname)s || %(name)s || %(message)s",
        "%b %d %Y %I:%M:%S %p",
    )
)
logger.addHandler(handler)


class Glykon(Bot):
    """Bots class"""

    def __init__(self):
        super().__init__(
            command_prefix="changeme",
            case_insensitive=True,
            help_command=None,  # type: ignore
            intents=Intents.all(),
        )

    def load_cogs(self) -> None:
        """Load cogs from the src/cogs directory"""
        for file in os.listdir("./src/cogs"):
            if file.startswith("_"):
                continue
            if not file.endswith(".py"):
                self.load_extension(f"src.cogs.{file}")
            self.load_extension(f"src.cogs.{file[:-3]}")

    async def on_ready(self) -> None:
        """On bot ready"""
        logger.info(
            f"""
            ───── ⋆⋅☆⋅⋆ ─────
            WELCOME TO {self.user.display_name}
                ⤷ Servers 💿: {len(self.guilds)}
                ⤷ Users 👥: {len(self.users)}
                ⤷ Cogs ⚙️: {len(self.cogs)}
            ───── ⋆⋅☆⋅⋆ ─────
            Status: Ready 🟢
            """
        )

    def run(self) -> None:
        """Run the bot"""
        self.load_cogs()
        super().run(TOKEN, reconnect=True)
