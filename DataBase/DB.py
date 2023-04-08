from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB

import aiomysql


async def set_sql_connect(loop):
    return await aiomysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DB, loop=loop)


async def read_message_history(user_id, db):
    async with db.cursor() as cur:
        await cur.execute(f'SELECT message '
                          f'FROM MessageHistory{user_id} '
                          f'WHERE ID_USER = :user_id ',
                          values={'user_id': user_id})

        results = await cur.fetchall()

        return [next(result.values()) for result in results]


async def save_message_history(user_id, text, db):
    cur = await db.cursor()

    await cur.execute(f"INSERT INTO MessageHistory{user_id} "
                      f"VALUES (:ID_USER, :message)", values={'ID_USER': user_id, 'message': text})

    await cur.close()


async def create_if_not_exists_message_history(user_id, db):
    cur = await db.cursor()

    await cur.execute(f"CREATE TABLE IF NOT EXISTS MessageHistory{user_id} ("
                      f"ID INT PRIMARY KEY AUTO_INCREMENT,"
                      f"ID_USER INT NOT NULL,"
                      f"message VARCHAR(1024),"
                      f"FOREIGN KEY (ID_USER) REFERENCES User(ID));")

    await cur.close()
