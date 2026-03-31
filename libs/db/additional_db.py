import sqlite3
from .statisticDb import GameDB

class EnemyDefeated(GameDB): # include bar graph
    def __init__(self):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        self.initialize_tables()

        self.columns = ['skeleton', 'goblin', 'mushroom', 'big_mushroom', 'flying_eye', 'minotaur', 'golem', 'widow']
        self.table_name = 'species_defeated'

        # self.cur.execute(f"""INSERT OR IGNORE INTO {self.table_name} (id, {self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]}, {self.columns[5]}, {self.columns[6]}, {self.columns[7]})
        #                      VALUES (1, 1, 0, 0, 0, 0, 0, 0, 0)
        #                 """)
        # self.con.commit()

    def update(self, a, b, c, d, e, f, g, h):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]}, {self.columns[5]}, {self.columns[6]}, {self.columns[7]})
                                   VALUES ({a}, {b}, {c}, {d}, {e}, {f}, {g}, {h})""")
        self.con.commit()
        print(f"({a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}) -> Data inserted into {self.table_name}")

class PointUsage(GameDB): # Bar graph
    def __init__(self):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        self.initialize_tables()

        self.columns = ['health', 'power', 'critical', 'stamina', 'stamina_regen']
        self.table_name = 'point_usage_statistic'

        # self.cur.execute(f"""INSERT OR IGNORE INTO {self.table_name} (id, {self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]})
        #                      VALUES (1, 1, 0, 0, 0, 0)
        #                 """)
        # self.con.commit()

    def update(self, a, b, c, d, e):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}, {self.columns[3]}, {self.columns[4]})
                                   VALUES ({a}, {b}, {c}, {d}, {e})""")
        self.con.commit()
        print(f"({a}, {b}, {c}, {d}, {e}) -> Data inserted into {self.table_name}")

class InGameTimeStamp(GameDB): # include Histogram for ( points & health )
    def __init__(self):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        self.initialize_tables()

        self.columns = ['health', 'points', 'time_stamp']
        self.table_name = 'in_game_ts'

        # self.cur.execute(f"""INSERT OR IGNORE INTO {self.table_name} (id, {self.columns[0]}, {self.columns[1]}, {self.columns[2]})
        #                      VALUES (1, 1, 0, 0)
        #                 """)
        # self.con.commit()

    def update(self, a, b, c):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]})
                                   VALUES ({a}, {b}, {c})""")
        self.con.commit()
        print(f"({a}, {b}, {c}) -> Data inserted into {self.table_name}")