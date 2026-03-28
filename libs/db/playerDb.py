import sqlite3
from .statisticDb import GameDB

class PlayerStats(GameDB):
    def __init__(self):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        self.initialize_tables()

        self.columns = ['health', 'power', 'critical', 'stamina', 'stamina_regen', 'accumulative_points']
        self.table_name = 'player_statistic'

        self.cur.execute(f"""INSERT OR IGNORE INTO {self.table_name} (id, {self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]}, {self.columns[5]})
                             VALUES (1, 70, 4, 0.05, 100, 1, 0)
                        """)
        self.con.commit()
    
    def update(self, a, b, c, d, e, f):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]}, {self.columns[5]})
                                   VALUES ({a}, {b}, {c}, {d}, {e}, {f})""")
        self.con.commit()
        print(f"({a}, {b}, {c}, {d}, {e}, {f}) -> Data inserted into {self.table_name}")

    def get_points(self):
        tmp_ = self.get_current_stat()[-1]
        return tmp_

    def get_current_stat(self):
        tmp_ = self.get_last_row()[0]
        return tmp_

    # def create_initial_initial(self):

# a = PlayerStats(['health', 'power', 'critical', 'stamina', 'stamina_regen', 'accumulative_points'], 'player_statistic')
# a.update(10, 10, 10, 10, 10, 10)
# print(a.get_last_row())