from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB

from Configs.GPT_Setting import MAX_SAVE_MESSAGE_HISTORY

import aiomysql

import json


async def set_sql_connect():
    return await aiomysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DB)


async def read_message_history(user_id, db):
    async with db.cursor() as cur:
        await cur.execute(f'SELECT message '
                          f'FROM MessageHistory{user_id} '
                          f'WHERE ID_USER = {user_id};')

        results = await cur.fetchall()
        return [json.loads(result[0]) for result in results]


async def save_message_history(user_id, text, db):
    async with db.cursor() as cur:
        await cur.execute(f"INSERT INTO MessageHistory{user_id} (ID_USER, message)"
                          f"VALUES ({user_id}, {str(text)});")
    await db.commit()


async def del_old_message(user_id, db):
    async with db.cursor() as cur:
        await cur.execute(f"SELECT count(*) FROM MessageHistory{user_id};")
        result = (await cur.fetchone())[0]

        if result > MAX_SAVE_MESSAGE_HISTORY:
            await cur.execute(f"DELETE TOP (2) FROM MessageHistory{user_id}")
    await db.commit()


async def create_if_not_exists_message_history(user_id, db):
    async with db.cursor() as cur:
        await cur.execute(f"CREATE TABLE IF NOT EXISTS MessageHistory{user_id} ("
                          f"ID INT PRIMARY KEY AUTO_INCREMENT,"
                          f"ID_USER INT NOT NULL,"
                          f"message VARCHAR(1024));")
    await db.commit()
