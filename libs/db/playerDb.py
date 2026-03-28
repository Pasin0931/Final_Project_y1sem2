import sqlite3
from .statisticDb import gameDB

class PlayerStats(gameDB):
    def __init__(self, columns, table_name):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        super().__init__(columns, table_name)

        self.cur.execute(f"CREATE TABLE if not exists {self.table_name}(id INTEGER PRIMARY KEY, {self.columns[0]} INTEGER, {self.columns[1]} INTEGER, {self.columns[2]} REAL, {self.columns[3]} INTEGER, {self.columns[4]} INTEGER, {self.columns[5]} INTEGER)")

        print('Player stats database initialized . . .')
    
    def update(self, a, b, c, d, e, f):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]}, {self.columns[5]}) VALUES ({a}, {b}, {c}, {d}, {e}, {f})""")
        self.con.commit()
        print(f"({a}, {b}, {c}, {d}, {e}, {f}) -> Data inserted into {self.table_name}")

            