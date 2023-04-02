from databases import Database
from Config import DB_URL
import sqlite3 as sq

con = sq.connect(DB_URL)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER NOT NULL, text text NOT NULL);")
con.close()

database = Database(DB_URL)

