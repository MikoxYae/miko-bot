import motor.motor_asyncio
from datetime import datetime, timezone, timedelta
from config import DB_URI, DB_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
db = client[DB_NAME]

users_col = db["users"]

IST = timezone(timedelta(hours=5, minutes=30))


def get_today_ist() -> str:
    return datetime.now(IST).strftime("%Y-%m-%d")


async def add_user(user_id: int):
    if not await is_user_exist(user_id):
        await users_col.insert_one({
            "user_id": user_id,
            "pic_index": 0,
            "last_date": get_today_ist(),
        })


async def is_user_exist(user_id: int) -> bool:
    user = await users_col.find_one({"user_id": user_id})
    return bool(user)


async def get_next_pic_index(user_id: int, total_pics: int) -> int:
    today = get_today_ist()
    user = await users_col.find_one({"user_id": user_id})

    if not user:
        await users_col.insert_one({
            "user_id": user_id,
            "pic_index": 1 % total_pics,
            "last_date": today,
        })
        return 0

    last_date = user.get("last_date", "")
    pic_index = user.get("pic_index", 0)

    if last_date != today:
        pic_index = 0

    next_index = (pic_index + 1) % total_pics

    await users_col.update_one(
        {"user_id": user_id},
        {"$set": {"pic_index": next_index, "last_date": today}},
    )

    return pic_index


async def get_all_users():
    return users_col.find({})


async def total_users_count() -> int:
    return await users_col.count_documents({})


async def delete_user(user_id: int):
    await users_col.delete_many({"user_id": user_id})
