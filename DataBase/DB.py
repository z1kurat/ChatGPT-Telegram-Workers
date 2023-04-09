from Configs.GPT_Setting import MAX_SAVE_MESSAGE_HISTORY

from SetupBot.Setup import pool


async def read_message_history(user_id):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f'SELECT PR_ROLE, CONTENT '
                              f'FROM MessageHistory{user_id};')

            results = await cur.fetchall()
            return [{"role": result[0], "content": result[1]} for result in results]

    pool.close()
    await pool.wait_closed()


async def save_message_history(user_id, role, content):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO MessageHistory%s (PR_ROLE, CONTENT) "
                              "VALUES (%s, %s);", (user_id, role, content))
    await conn.commit()

    pool.close()
    await pool.wait_closed()


async def del_old_message(user_id):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"SELECT count(*) FROM MessageHistory{user_id};")
            result = (await cur.fetchone())[0]

            if result > MAX_SAVE_MESSAGE_HISTORY:
                await cur.execute(f"DELETE FROM MessageHistory{user_id} WHERE ID < "
                                  f"(SELECT MAX(ID) - {result - MAX_SAVE_MESSAGE_HISTORY} FROM "
                                  f"(SELECT ID FROM MessageHistory{user_id}) AS subQuery);")
    await conn.commit()

    pool.close()
    await pool.wait_closed()


async def del_all_message(user_id):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"TRUNCATE TABLE MessageHistory{user_id};")
    await conn.commit()

    pool.close()
    await pool.wait_closed()


async def create_if_not_exists_message_history(user_id):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(f"CREATE TABLE IF NOT EXISTS MessageHistory{user_id} ("
                              f"ID INT PRIMARY KEY AUTO_INCREMENT,"
                              f"PR_ROLE VARCHAR(128),"
                              f"CONTENT VARCHAR(4096));")
    await conn.commit()

    pool.close()
    await pool.wait_closed()
