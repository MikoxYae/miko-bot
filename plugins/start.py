import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database import add_user, total_users_count
from config import get_start_pic, START_MSG, OWNER_ID


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client: Client, message: Message):
    user = message.from_user
    await add_user(user.id)

    me = await client.get_me()
    text = START_MSG.format(
        first=user.first_name,
        last=user.last_name or "",
        username=f"@{user.username}" if user.username else "N/A",
        mention=user.mention,
        id=user.id,
        bot_name=me.first_name,
        bot_username=f"@{me.username}",
    )

    pic = get_start_pic()

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👨‍💻 Owner", url=f"https://t.me/{OWNER_ID}"),
                InlineKeyboardButton("🔔 Updates", url="https://t.me/Anythingbutnew56"),
            ],
        ]
    )

    if pic:
        await message.reply_photo(
            photo=pic,
            caption=text,
            reply_markup=buttons,
        )
    else:
        await message.reply_text(text, reply_markup=buttons)


@Client.on_message(filters.command("users") & filters.user(OWNER_ID))
async def users_count(client: Client, message: Message):
    count = await total_users_count()
    await message.reply_text(f"📊 Total users in database: **{count}**")
