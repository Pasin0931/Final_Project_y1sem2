import sqlite3

class gameDB:
    def __init__(self, columns, table_name):
        self.con = sqlite3.connect("tutorial.db")
        self.cur = self.con.cursor()

        self.columns = columns
        self.table_name = table_name

        self.cur.execute(f"CREATE TABLE if not exists {self.table_name}(id INTEGER PRIMARY KEY, {self.columns[0]}, {self.columns[1]}, {self.columns[2]})")
    
    def insert_data(self, title, year, rating):
        res = self.cur.execute(f"""INSERT INTO {self.table_name} ({self.columns[0]}, {self.columns[1]}, {self.columns[2]}) VALUES ('{title}', {int(year)}, {float(rating)})""")
        self.con.commit()
        print(f"({title}, {year}, {rating}) -> Data inserted into {self.table_name}")

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

    def clean_db(self):
        try:
            res = self.cur.execute(f"""DELETE FROM {self.table_name}""")
            self.con.commit()
            print(f"Database cleare -> {self.get_data()}")
        except sqlite3.OperationalError:
            print("Error while cleaning database")