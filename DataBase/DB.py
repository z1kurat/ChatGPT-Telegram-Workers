from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB

import aiomysql


async def set_sql_connect():
    return await aiomysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DB)


async def read(user_id, db):
    results = await db.fetch_all('SELECT text '
                           'FROM messages '
                           'WHERE telegram_id = :telegram_id ',
                           values={'telegram_id': user_id})

    return [next(result.values()) for result in results]
