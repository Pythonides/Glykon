"""
    Main bot file
"""
import os
from disnake import Intents
from disnake.ext.commands import Bot

from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
TOKEN = os.getenv("TOKEN")


class Glykon(Bot):
    """
    Bots class
    """
    def __init__(self):
        super().__init__(
            command_prefix="changeme",
            case_insensitive=True,
            help_command=None,  # type: ignore
            intents=Intents.all(),
        )

    def loadCogs(self) -> None:
        for file in os.listdir("./src/cogs"):
            if file.startswith("_"):
                continue
            if not file.endswith("py"):
                self.load_extension(f"src.cogs.{file}")
            self.load_extension(f"src.cogs.{file[:-3]}")

    async def on_ready(self) -> None:
        print(
            f"""
            ───── ⋆⋅☆⋅⋆ ─────
            WELCOME TO {self.user.display_name}
            ⤷ Servers 💿: {len(self.guilds)}
            ⤷ Users 👥: {len(self.users)}
            ⤷ Cogs ⚙️: {len(self.cogs)}
            ───── ⋆⋅☆⋅⋆ ─────
                🟢 Ready 🟢
            """
        )

    def run(self) -> None:
        self.loadCogs()
        super().run(TOKEN, reconnect=True)
