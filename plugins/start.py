from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from database import add_user, total_users_count
from config import START_PICS, START_MSG, OWNER, OWNER_ID


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

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("👨‍💻 Owner", url=f"https://t.me/{OWNER}"),
                InlineKeyboardButton("🔔 Updates", url=f"https://t.me/{OWNER}"),
            ],
        ]
    )

    if START_PICS:
        if len(START_PICS) == 1:
            await message.reply_photo(
                photo=START_PICS[0],
                caption=text,
                reply_markup=buttons,
            )
        else:
            media_group = [
                InputMediaPhoto(media=pic, caption=text if i == 0 else "")
                for i, pic in enumerate(START_PICS)
            ]
            await message.reply_media_group(media=media_group)
            await message.reply_text(text, reply_markup=buttons)
    else:
        await message.reply_text(text, reply_markup=buttons)


@Client.on_message(filters.command("users") & filters.user(OWNER_ID))
async def users_count(client: Client, message: Message):
    count = await total_users_count()
    await message.reply_text(f"📊 Total users in database: **{count}**")
