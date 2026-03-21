import csv
import random
import multiprocessing

class BossNameGennerator:
    mino = []
    golem = []
    widow = []

    title = []

    def __init__(self, path):
        self.path = path
        self.names = self.open_csv()

        self.categorize_name(self.open_csv())

    def open_csv(self):
        with open(self.path, encoding="utf-8") as f:
            render = csv.reader(f)
            next(render)
            data_ = list(render)
        return data_
    
    @classmethod
    def categorize_name(cls, list_of_names):
        for i in list_of_names:
            cls.mino.append(i[0])
            cls.golem.append(i[1])
            cls.widow.append(i[2])
            cls.title.append(i[3])

    @classmethod
    def random_name(cls, boss):
        if boss.lower() == "minotaur":
            random_name = random.choice(cls.mino)
            random_title = random.choice(cls.title)
            return f"{random_name}, {random_title}"

        elif boss.lower() == "golem":
            random_name = random.choice(cls.golem)
            random_title = random.choice(cls.title)
            return f"{random_name}, {random_title}"

        elif boss.lower() == "widow":
            random_name = random.choice(cls.widow)
            random_title = random.choice(cls.title)
            return f"{random_name}, {random_title}"
        
    def test_names(self):
        for i in range(10):
            if i%3 == 0:
                print(self.random_name('minotaur'))
            elif i%3 == 1:
                print(self.random_name('golem'))
            elif i%3 == 2:
                print(self.random_name('widow'))