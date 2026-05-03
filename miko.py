import asyncio
import logging
import importlib
import os
from pathlib import Path
from pyrogram import Client
from config import APP_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def load_plugins(app: Client):
    plugins_path = Path("plugins")
    for file in sorted(plugins_path.glob("*.py")):
        module_name = f"plugins.{file.stem}"
        if file.stem == "__init__":
            continue
        try:
            importlib.import_module(module_name)
            logger.info(f"Loaded plugin: {module_name}")
        except Exception as e:
            logger.error(f"Failed to load plugin {module_name}: {e}")


async def main():
    app = Client(
        "miko_bot",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
    )

    load_plugins(app)

    logger.info("Starting Miko Bot...")
    async with app:
        me = await app.get_me()
        logger.info(f"Bot started as @{me.username} ({me.id})")
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
