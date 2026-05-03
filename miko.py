import asyncio
import logging
from pyrogram import Client
from config import APP_ID, API_HASH, BOT_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    app = Client(
        "miko_bot",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="plugins"),
    )

    logger.info("Starting Miko Bot...")
    async with app:
        me = await app.get_me()
        logger.info(f"Bot started as @{me.username} ({me.id})")
        await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
