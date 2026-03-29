import sqlite3

class GameDB:
    def __init__(self):
        self.con = sqlite3.connect("libs/db/histories.db")
        self.cur = self.con.cursor()

        self.columns = 'game_statistic'
        self.table_name = ['a', 'b', 'c']

        self.initialize_tables()
    
    def update(self, a, b, c):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}) VALUES ('{a}', {int(b)}, {float(c)})""")
        self.con.commit()
        print(f"({a}, {b}, {c}) -> Data inserted into {self.table_name}")

    def remove_cell(self, column_ , to_delete):
        try:
            self.cur.execute(f"""DELETE FROM {self.table_name} WHERE {column_} = '{to_delete}'""")
            self.con.commit()
            print("Cell deleted")
        except sqlite3.OperationalError:
            print("Error while removing selected cell")

    def get_data_at_column(self, this_):
        try:
            if this_ not in self.columns:
                raise sqlite3.OperationalError
            res = self.con.execute(f"""SELECT {this_.lower()} FROM {self.table_name}""")
            this_ = res.fetchall()
            return this_
        except sqlite3.OperationalError:
            print(f"{this_} not in database column")

    def get_data(self):
        res = self.cur.execute(f"""SELECT * FROM {self.table_name}""")
        this_ = res.fetchall()
        return this_
    
    def get_id(self, id_):
        res = self.cur.execute(f"""SELECT * FROM {self.table_name} WHERE id = {id_}""")
        this_ = res.fetchall()
        return this_
    
    def get_last_row(self):
        res = self.cur.execute(f"""SELECT * FROM {self.table_name} ORDER BY id DESC LIMIT 1""")
        this_ = res.fetchall()
        return this_

    def reset_db(self):
        try:
            res = self.cur.execute(f"""DELETE FROM {self.table_name}""")
            self.con.commit()
            print(f"Database cleare -> {self.get_data()}")
        except sqlite3.OperationalError:
            print("Error while cleaning database")

    def initialize_tables(self):
        b = ['health', 'power', 'critical', 'stamina', 'stamina_regen', 'accumulative_points']
        c = ['skeleton', 'goblin', 'mushroom', 'big_mushroom', 'flying_eye']
        d = ['health', 'points', 'time_stamp']

        self.cur.execute(f"CREATE TABLE if not exists player_statistic (id INTEGER PRIMARY KEY, {b[0]}, {b[1]}, {b[2]}, {b[3]}, {b[4]}, {b[5]})")
        self.cur.execute(f"CREATE TABLE if not exists point_usage_statistic (id INTEGER PRIMARY KEY, {b[0]}, {b[1]}, {b[2]}, {b[3]}, {b[4]})")
        self.cur.execute(f"CREATE TABLE if not exists species_defeated (id INTEGER PRIMARY KEY, {c[0]}, {c[1]}, {c[2]}, {c[3]}, {c[4]})")
        self.cur.execute(f"CREATE TABLE if not exists in_game_ts (id INTEGER PRIMARY KEY, {d[0]}, {d[1]}, {d[2]})")

        # print('Statistic database initialized . . .')
        # print('Player statistic database initialized . . .')