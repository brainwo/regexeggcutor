import sqlite3

con = sqlite3.connect("userdata.db")

cur: sqlite3.Cursor = con.cursor()
cur.execute("CREATE TABLE user(id, last_activity)")

cur.close()
con.close()
