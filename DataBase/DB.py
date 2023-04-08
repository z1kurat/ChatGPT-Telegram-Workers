from Configs.DB_PARAMETERS import HOST
from Configs.DB_PARAMETERS import USER
from Configs.DB_PARAMETERS import PORT
from Configs.DB_PARAMETERS import PASSWORD
from Configs.DB_PARAMETERS import NAME_DB

import aiomysql


async def set_sql_connect():
    return await aiomysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=NAME_DB)


async def read_message_history(user_id, db):
    results = await db.fetch_all('SELECT text '
                                 'FROM messages '
                                 'WHERE telegram_id = :telegram_id ',
                                 values={'telegram_id': user_id})

    return [next(result.values()) for result in results]


async def save_message_history(user_id, text, db):
    await db.execute(f"INSERT INTO messages(telegram_id, text) "
                     f"VALUES (:telegram_id, :text)", values={'telegram_id': user_id, 'text': text})


async def create_if_not_exists_message_history(user_id, db):
    await db.execute(f"CREATE TABLE IF NOT EXISTS MessageHistory{user_id} (:"
                     f"ID INT PRIMARY KEY AUTO_INCREMENT,"
                     f"ID_USER INT,"
                     f"message VARCHAR(255),"
                     f"FOREIGN KEY (ID_USER) REFERENCES User(ID));")
