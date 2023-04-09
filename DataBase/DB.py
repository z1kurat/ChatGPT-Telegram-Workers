from Configs.GPT_Setting import MAX_SAVE_MESSAGE_HISTORY

import aiomysql

from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB


async def get_pool():
    pool = await aiomysql.create_pool(host=HOST,
                                      port=PORT,
                                      user=USER,
                                      password=PASSWORD,
                                      db=NAME_DB,
                                      maxsize=10)

    return pool


async def read_message_history(user_id):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f'SELECT PR_ROLE, CONTENT '
                              f'FROM MessageHistory{user_id};')

            results = await cur.fetchall()
            return [{"role": result[0], "content": result[1]} for result in results]


async def save_message_history(user_id, role, content):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO MessageHistory%s (PR_ROLE, CONTENT) "
                              "VALUES (%s, %s);", (user_id, role, content))
        await conn.commit()


async def del_old_message(user_id):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"SELECT count(*) FROM MessageHistory{user_id};")
            result = (await cur.fetchone())[0]

            if result > MAX_SAVE_MESSAGE_HISTORY:
                await cur.execute(f"DELETE FROM MessageHistory{user_id} WHERE ID < "
                                  f"(SELECT MAX(ID) - {MAX_SAVE_MESSAGE_HISTORY} FROM "
                                  f"(SELECT ID FROM MessageHistory{user_id}) AS subQuery);")
        await conn.commit()


async def del_all_message(user_id):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"TRUNCATE TABLE MessageHistory{user_id};")
        await conn.commit()


async def create_if_not_exists_message_history(user_id):
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"CREATE TABLE IF NOT EXISTS MessageHistory{user_id} ("
                              f"ID INT PRIMARY KEY AUTO_INCREMENT,"
                              f"PR_ROLE VARCHAR(128),"
                              f"CONTENT VARCHAR(4096));")
        await conn.commit()
