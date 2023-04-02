from databases import Database
from Config import DB_URL

database = Database(DB_URL)
database.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER NOT NULL, text text NOT NULL);")

