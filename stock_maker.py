import random
import sqlite3


class CommonStock:   # родительский класс для создания акций (базовые акции)
    def __init__(self, price='', points='', divs=''):
        if price == '':
            self.price = random.randint(10, 50)
        else:
            self.price = price
        if points == '':
            self.points = self.price
        if divs == '':
            self.divs = round(random.randint(0, 3) + (random.randint(1, 100) / 100), 2)
        else:
            self.divs = divs
        self.name = stock_name()


class RareStock(CommonStock):   # класс для создания акций - производный (редкие акции)
    def __init__(self):
        price = random.randint(50, 500)
        super().__init__(str(price), str(price),
                         str(round((random.randint(5, 10) + (random.randint(1, 100) / 100)), 2)))


class LegendaryStock(CommonStock):    # класс для создания акций - производный (легендарные акции)
    def __init__(self):
        price = random.randint(500, 1000)
        super().__init__(str(price), str(price),
                         str(round((random.randint(10, 20) + (random.randint(1, 100) / 100)), 2)))


def stock_name():   # функция для выбора названия акции
    with open('text_files/companies.txt', 'rt', encoding='utf-8') as data:
        con = sqlite3.connect('stocks.sqlite')
        cur = con.cursor()
        res = cur.execute("""Select name from market""").fetchall()
        con.close()
        res = list(map(lambda x: x[0], res))
        name = random.choice(list(data.readlines())).strip()
        data.seek(0)
        while name in res:
            data.seek(0)
            name = random.choice(list(data.readlines())).strip()
        return name
