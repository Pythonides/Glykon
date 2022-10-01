import os
from src import Glykon

if __name__ == "__main__":
    if ".env" not in os.listdir():

        print("⇒ Running configurations")

        token = input("🔴 paste your bot's token 🔴:")
        with open(".env", "x") as f:
            f.write(f"TOKEN='{token}'")

    Glykon().run()
