import motor.motor_asyncio
from config import DB_URI, DB_NAME

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
db = client[DB_NAME]

users_col = db["users"]


async def add_user(user_id: int):
    if not await is_user_exist(user_id):
        await users_col.insert_one({"user_id": user_id})


async def is_user_exist(user_id: int) -> bool:
    user = await users_col.find_one({"user_id": user_id})
    return bool(user)


async def get_all_users():
    return users_col.find({})


async def total_users_count() -> int:
    return await users_col.count_documents({})


async def delete_user(user_id: int):
    await users_col.delete_many({"user_id": user_id})
