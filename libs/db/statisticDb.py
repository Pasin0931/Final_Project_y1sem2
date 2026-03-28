import sqlite3

class gameDB:
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

    def clean_db(self):
        try:
            res = self.cur.execute(f"""DELETE FROM {self.table_name}""")
            self.con.commit()
            print(f"Database cleare -> {self.get_data()}")
        except sqlite3.OperationalError:
            print("Error while cleaning database")

    def initialize_tables(self):
        a = ['a', 'b', 'c']
        b = ['health', 'power', 'critical', 'stamina', 'stamina_regen', 'accumulative_points']

        self.cur.execute(f"CREATE TABLE if not exists game_statistic (id INTEGER PRIMARY KEY, {a[0]}, {a[1]}, {a[2]})")
        self.cur.execute(f"CREATE TABLE if not exists player_statistic (id INTEGER PRIMARY KEY, {b[0]}, {b[1]}, {b[2]}, {b[3]}, {b[4]}, {b[5]})")

        # print('Statistic database initialized . . .')
        # print('Player statistic database initialized . . .')