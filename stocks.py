import sys
import random
import sqlite3
import Hist
import Shop
import stock_maker
import datetime as dt
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QTableWidgetItem, \
    QTableWidget, QMainWindow
from PyQt5.QtGui import QColor
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from PyQt5 import QtCore, QtGui, QtWidgets


pg.setConfigOption('background', 'w')    # фон и цвет графика
pg.setConfigOption('foreground', 'k')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):  # основное окно
    def __init__(self):
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        super(MyWidget, self).__init__()
        self.resize(1798, 1000)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 140, 255),"
            " stop:1 rgba(0, 85, 130, 255));")
        self.centralwidget = QtWidgets.QWidget(self)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 731, 851))
        self.graphicsView.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 16px;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 900, 1241, 51))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1350, 140, 391, 51))
        self.lcdNumber.setStyleSheet("color: rgb(0, 170, 127);\n"
                                     "background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 4px")
        self.lcdNumber.setDigitCount(10)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1350, 70, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                   "border-radius: 4px;\n"
                                   "padding: 10px;")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1350, 200, 391, 61))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1270, 900, 231, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1350, 270, 391, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1350, 320, 391, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(140, 0, 80);\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 731, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-radius: 10px;")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 370, 481, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(85, 0, 255);\n"
                                   "border-radius: 8px;\n"
                                   "padding: 10px;")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1270, 370, 471, 71))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(85, 0, 255);\n"
                                   "border-radius: 8px;\n"
                                   "padding: 10px;")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(770, 40, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 4px;")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1350, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("background-color: rgb(127, 127, 127);\n"
                                   "border-radius: 4px")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(770, 440, 481, 451))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 4px")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(1270, 440, 471, 451))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 4px")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(770, 110, 481, 241))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 4px;")
        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 4px;")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 4px;")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 4px;")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1660, 10, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius: 10px;\n"
                                        "padding: 10px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(85, 0, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: white;")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1520, 900, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                      "border-radius: 10px;\n"
                                      "border-style: outset;\n"
                                      "border-width: 1px;\n"
                                      "border-color: white;\n"
                                      "color: rgb(255, 255, 255);")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1798, 18))
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.graphicsView.showGrid(x=True, y=True)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " News on W&C"))
        self.label_5.setText(_translate("MainWindow", "  Money:"))
        self.pushButton_3.setText(_translate("MainWindow", "Work one day"))
        self.pushButton_4.setText(_translate("MainWindow", "Enter a promocode"))
        self.pushButton_5.setText(_translate("MainWindow", "Sell everything"))
        self.label_4.setText(_translate("MainWindow", "Time"))
        self.label_6.setText(_translate("MainWindow", "Market:"))
        self.label_7.setText(_translate("MainWindow", "Portfolio:"))
        self.label_2.setText(_translate("MainWindow", "  Company "))
        self.label_11.setText(_translate("MainWindow", "  Last Price:"))
        self.label_3.setText(_translate("MainWindow", "  Price:"))
        self.label_9.setText(_translate("MainWindow", "  Dividends:"))
        self.pushButton_7.setText(_translate("MainWindow", "Restart"))
        self.pushButton.setText(_translate("MainWindow", "History"))
        self.pushButton_2.setText(_translate("MainWindow", "Shop"))
        self.label_12.setText(_translate("MainWindow", " Quantity:"))
        self.label_12.hide()
        self.setWindowTitle('Stockky')
        QtCore.QMetaObject.connectSlotsByName(self)
        self.days_passed = 0  # дней прошло работы с последенего входа
        self.check_stocks()   # генерация и проверка количества акций доступных пользователю
        self.place_stocks()   # размещение акций в таблицах
        self.check_level()  # проверка уровня игрока по деньгам
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # запрет на изменение таблицы
        self.tableWidget_2.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        with open('text_files/account_params.txt', 'rt', encoding='utf-8') as money:  # подгрузка денег пользователя
            data = money.readlines()
            self.lcdNumber.display(data[0].strip())
            self.last_date = data[1].strip()
        if str(dt.datetime.now().date()) != self.last_date:   # загрузка даты
            self.label_4.setText(self.last_date)
        else:
            self.label_4.setText(str(dt.datetime.now().date()))
            self.how_to_play()  # информация об игре (функция вызывает диалоговое окно)
        self.current_item = ''
        self.codes = {'1000m': 1000, '10000m': 10000, '100000m': 100000}
        self.work_time = dt.timedelta(days=1)  # время работы для получения зп (инкрементальная)
        self.label.setText('  News on W&C')
        self.pushButton.clicked.connect(self.openhist)  # открытие окна с историей
        self.pushButton_3.clicked.connect(self.work_one_day)   # заработок денег с кликера
        self.pushButton_4.clicked.connect(self.promocode)  # промокод
        self.pushButton_7.clicked.connect(self.restart)   # начало заново
        self.tableWidget.cellClicked.connect(self.get_info)  # при клике на таблицу выводится инфа об акции
        self.tableWidget_2.cellClicked.connect(self.get_info)  # как и верхнее, но с потрефельной таблицей
        self.tableWidget.cellDoubleClicked.connect(self.buy_stock)  # покупка
        self.tableWidget_2.cellDoubleClicked.connect(self.sell_stock)  # продажа
        self.pushButton_5.clicked.connect(self.sell_everything)   # продажа всего портфеля (экстренно)
        self.pushButton_2.clicked.connect(self.shop_window)  # открытие окна с магазином

    def openhist(self):    # открытие окна с историей игры
        self.hist = Hist.HistWindow()
        self.hist.show()

    def shop_window(self):  # открытие окна с магазином мемов
        self.shop = Shop.ShopWindow()
        self.shop.show()

    def how_to_play(self):   # вывод информации об игре из файла в виде диалогового окна
        info = QMessageBox(self)
        info.setStyleSheet("color: rgb(255, 255, 255);")
        info.setWindowTitle("Info")
        with open('text_files/info.txt', 'rt', encoding='utf-8') as data:  # достаем инфу из файла
            info_data = data.readlines()
        info.setText('\n'.join(line for line in info_data))
        info.setStandardButtons(QMessageBox.Yes)
        info.setIcon(QMessageBox.Information)
        info.exec()

    def work_one_day(self):
        with open('text_files/account_params.txt', 'rt', encoding='utf-8') as money:  # подгрузка денег пользователя
            self.lcdNumber.display(money.readlines()[0].strip())
        self.label_4.setText(str(dt.date(*list(map(int, self.label_4.text().split('-')))) + self.work_time))
        if self.label_8.text() == '  Premium account':     # зарплата зависит от уровня
            self.lcdNumber.display(str(int(self.lcdNumber.value()) + 5))
        elif self.label_8.text() == '  Exotic account':
            self.lcdNumber.display(str(int(self.lcdNumber.value()) + 10))
        else:
            self.lcdNumber.display(str(int(self.lcdNumber.value()) + 1))
        self.days_passed += 1
        if self.days_passed % 5 == 0:
            self.event_now()   # генерация события в мире
        self.check_level()  # проверка на уровень игрока (открытие новых акций)
        self.check_stocks()   # проверка акций доступных игроку
        self.check_dividends()  # проверка дивидендов
        try:    # если есть выбранная акция, игрок может наблюдать за ней. Иначе ничеготне выводится
            company_to_spectate = self.label_2.text().split()[1]
            self.current_item = company_to_spectate
            con_m = sqlite3.connect('stocks.sqlite')
            cur_m = con_m.cursor()
            if company_to_spectate not in\
                    list(map(lambda x: x[0], cur_m.execute("""SELECT name FROM portfolio""").fetchall())):
                data = cur_m.execute(f"""Select name, price, dividends, points, types.type FROM market 
                INNER JOIN types ON market.stock_type = types.type_id WHERE name = 
                '{company_to_spectate}'""").fetchall()[0]
            else:  # даннные достаются из бд
                data = cur_m.execute(f"""Select name, price, dividends, points, types.type, quantity FROM portfolio 
                INNER JOIN types ON portfolio.stock_type = types.type_id WHERE name = 
                '{company_to_spectate}'""").fetchall()[0]
            con_m.close()
            self.display_stats(data)
        except IndexError:
            self.clear_graphic()
        with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:
            money.write(str(int(self.lcdNumber.value())) + '\n')   # запись параметров игрока в файл
            money.write(self.label_4.text())

    def promocode(self):  # диалоговое окно для ввода промокода
        dlg = QInputDialog(self)
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        dlg.setWindowTitle("Введите Промокод")
        dlg.setLabelText("Промокод:")
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        ok_pressed = dlg.exec_()
        code = dlg.textValue()
        if ok_pressed:
            try:   # если есть промокод, он срабатывает. (нет-ошибка)
                plus = self.codes[code]
                self.lcdNumber.display(str(int(self.lcdNumber.value()) + plus))
            except KeyError:
                dlg = QMessageBox(self)
                dlg.setStyleSheet("color: rgb(255, 255, 255);")
                dlg.setWindowTitle("Ошибка!")
                dlg.setText("Такого промокода не существует!")
                dlg.setStandardButtons(QMessageBox.Ok)
                dlg.setIcon(QMessageBox.Critical)
                dlg.exec()
        self.check_level()   # проверка уровня игрока
        self.check_stocks()   # проверка акций доступных игроку
        self.place_stocks()   # размещение доступных игроку акций в таблицу
        with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:
            money.write(str(int(self.lcdNumber.value())) + '\n')
            money.write(self.label_4.text())

    def event_now(self):   # функция генерация события
        if random.choice([True, False]):  # выбор типа события: хорошее или плохое
            with open('text_files/good_events.txt', 'rt', encoding='utf-8') as events:
                line = random.choice(events.readlines()).strip()  # выбор события из файла
            change = 1
        else:
            with open('text_files/bad_events.txt', 'rt', encoding='utf-8') as events:
                line = random.choice(events.readlines()).strip()   # выбор события из файла
            change = -1
        self.label.setText('   Новое событие - ' + self.label_4.text() + ':   ' + line)
        con_m = sqlite3.connect('stocks.sqlite')
        cur_m = con_m.cursor()
        last_price = cur_m.execute(f"""SELECT price FROM market""").fetchall()
        previous_points = cur_m.execute(f"""SELECT points, name FROM market""").fetchall()
        for pos in range(len(last_price)):
            delta = change * random.randint(0, 5)
            new_points = previous_points[pos][0] + ';' + str(int(str(last_price[pos][0])) + delta)
            cur_m.execute(f"""UPDATE market SET points = '{new_points}', price = price + {delta},
             dividends = ROUND(dividends + {delta / 100}, 2) WHERE name = '{previous_points[pos][1]}'""")
            cur_m.execute(f"""UPDATE portfolio SET points = '{new_points}', price = price + {delta},
             dividends = ROUND(dividends + {delta / 100}, 2) WHERE name = '{previous_points[pos][1]}'""")
            con_m.commit()
        scam = previous_points[random.randint(0, len(last_price) - 1)][1]  # удаление рандомной акции по фану
        with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:
            data_book.write(f'   {self.label_4.text()}: {line}\n')
            data_book.write(f'   {self.label_4.text( )}: Компания {scam}'  # добавление события в файл с историей
                            f' была закрыта в связи с незаконной деятельностью.\n')
        cur_m.execute(f"""DELETE FROM portfolio WHERE name = '{scam}'""")
        cur_m.execute(f"""DELETE FROM market WHERE name = '{scam}'""")
        con_m.commit()
        con_m.close()
        self.check_stocks()  # проверка акций доступных игроку, добавление новых
        self.place_stocks()  # размещение акций в таблицы

    def check_stocks(self):   # генерация акций
        con_m = sqlite3.connect('stocks.sqlite')
        cur_m = con_m.cursor()  # в зависимости от условий добавляются разные акции
        if len(list(cur_m.execute("""Select name from market""").fetchall())) < 20:
            for num in range(20 - len(list(cur_m.execute("""Select name from market""").fetchall()))):
                stock = stock_maker.CommonStock()  # создание базовой акции
                stock_points = '0' + ';' + str(stock.price)
                cur_m.execute(f"""INSERT INTO market(name, price, dividends, points, stock_type)
                                                 VALUES('{stock.name}', {stock.price}, {stock.divs},
                                                  '{stock_points}', {self.check_stock_type(stock.price)})""")
                con_m.commit()
        elif 20 <= len(list(cur_m.execute("""Select name from market""").fetchall())) < 80 and self.label_8.text()\
                == '  Premium account' or self.label_8.text() == '  Exotic account' and\
                20 <= len(list(cur_m.execute("""Select name from market""").fetchall())) < 80:
            for num in range(80 - len(list(cur_m.execute("""Select name from market""").fetchall()))):
                stock = stock_maker.RareStock()  # создание редкой акции
                stock_points = '0' + ';' + str(stock.price)
                cur_m.execute(f"""INSERT INTO market(name, price, dividends, points, stock_type)
                 VALUES('{stock.name}', {stock.price}, {stock.divs},
                  '{stock_points}', {self.check_stock_type(stock.price)})""")
                con_m.commit()
        if 80 <= len(list(cur_m.execute("""Select name from market""").fetchall())) < 100 and self.label_8.text()\
                == '  Exotic account':
            for num in range(100 - len(list(cur_m.execute("""Select name from market""").fetchall()))):
                stock = stock_maker.LegendaryStock()  # создание легендарной акции
                stock_points = '0' + ';' + str(stock.price)
                cur_m.execute(f"""INSERT INTO market(name, price, dividends, points, stock_type)
                 VALUES('{stock.name}', {stock.price}, {stock.divs}, 
                 '{stock_points}', {self.check_stock_type(stock.price)})""")
                con_m.commit()
        cur_m.execute(f"""UPDATE market SET stock_type = 2 WHERE price > 50""")  # изменение уровня акции
        cur_m.execute(f"""UPDATE market SET stock_type = 1 WHERE price <= 50""")
        cur_m.execute(f"""UPDATE market SET stock_type = 3 WHERE price > 500""")
        cur_m.execute(f"""UPDATE portfolio SET stock_type = 2 WHERE price > 50""")
        cur_m.execute(f"""UPDATE portfolio SET stock_type = 1 WHERE price <= 50""")
        cur_m.execute(f"""UPDATE portfolio SET stock_type = 3 WHERE price > 500""")
        con_m.commit()
        con_m.close()
        self.place_stocks()

    def check_level(self):   # проверка и изменение уровня игрока в зависимости от д.е. из уровня аккаунта
        richness = int(self.lcdNumber.value()) // 1000
        if 1 <= richness < 10 and self.label_8.text() != '  Exotic account':
            self.label_8.setText('  Premium account')
        elif richness >= 10:
            self.label_8.setText('  Exotic account')
        elif self.label_8.text() != '  Premium account' and self.label_8.text() != '  Exotic account':
            self.label_8.setText('   Standard account')

    def clear_graphic(self):  # функция для отчищения графика, общей информации об акции
        self.graphicsView.clear()
        self.label_2.setText(' Company')   # очистка qlabel'ов
        self.label_3.setText(' Price')
        self.label_9.setText(' Dividends')
        self.label_11.setText(' Last Price')
        self.label_12.hide()
        self.graphicsView.setLabel('left', '')    # очитска графика
        self.graphicsView.setLabel('bottom', '')
        self.graphicsView.setTitle('')

    def restart(self):   # функция для рестарта
        dlg = QMessageBox(self)   # диалог с вопросом по рестарту
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        dlg.setWindowTitle("Restart")
        dlg.setText("Do you want to restart?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            con_m = sqlite3.connect('stocks.sqlite')  # подключение к бд и удаление информации
            cur_m = con_m.cursor()
            cur_m.execute("""DELETE from market""")
            cur_m.execute("""DELETE from portfolio""")
            con_m.commit()
            con_m.close()
            self.clear_graphic()  # функция очистки
            self.label_4.setText(str(dt.datetime.now().date()))   # размещение нынешней даты
            self.label.setText('  News on W&C')
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:  # запись новых параметров
                money.write(str(50) + '\n')
                self.lcdNumber.display(str(50))
                money.write(str(dt.datetime.now().date()))
            with open('text_files/history.txt', 'wt', encoding='utf-8') as data_book:   # удаление истории из файла
                data_book.truncate()
            self.label_8.setText('   Standard account')
            self.check_stocks()
            self.place_stocks()
            self.how_to_play()

    def get_info(self):   # получние данных из бд
        table = self.sender()   # находим откуда поступил сигнал
        picked_stock = table.item(table.currentRow(), 0).text()
        con_m = sqlite3.connect('stocks.sqlite')
        cur_m = con_m.cursor()
        if table == self.tableWidget:  # в зависимости от таблицы берутся разные данные
            data = cur_m.execute(f"""Select name, price, dividends, points, types.type FROM market INNER JOIN types
             ON market.stock_type = types.type_id WHERE name = '{picked_stock}'""").fetchall()[0]
        else:
            data = cur_m.execute(f"""Select name, price, dividends, points, types.type, quantity FROM portfolio 
            INNER JOIN types ON portfolio.stock_type = types.type_id WHERE name = '{picked_stock}'""").fetchall()[0]
        con_m.close()
        self.display_stats(data)   # размещение информации
        return data

    def display_stats(self, data):   # размещение информации
        try:  # если есть quantity, он выводится
            self.label_12.show()
            self.label_12.setText(f' Quantity: {data[5]}')
        except IndexError:
            self.label_12.hide()
        self.label.setText('  News on W&C')  # вывод общей информации об акции
        self.label_2.setText(' Company: ' + data[0])
        self.label_3.setText(' Price: ' + str(data[1]) + '$')
        self.label_9.setText(' Dividends: ' + str(data[2]) + '$')
        self.label_11.setText(' Last Price:' + str(data[3].split(';')[-2]) + '$')
        self.graphicsView.clear()
        color = list(map(int, data[4][1:-1].split(', ')))
        pen = pg.mkPen(*color, width=3)
        self.graphicsView.setLabel('left', 'Price ($)', color=tuple(color))  # работа с графиком, подпись осей
        self.graphicsView.setLabel('bottom', 'Time (5 Days)', color=tuple(color))
        self.graphicsView.setTitle(data[0], color=tuple(color), size="15pt")
        self.graphicsView.plot([i for i in range(len(data[3].split(';')))], list(map(int, data[3].split(';'))),
                               pen=pen)  # построение графика, цвет зависит от уровня акции

    def check_quantity(self, name):   # проверка акции на наличие ее в портфеле
        con_p = sqlite3.connect('stocks.sqlite')
        cur_p = con_p.cursor()
        q_stock = cur_p.execute(f"""SELECT quantity FROM portfolio WHERE name = '{name}'""").fetchall()
        con_p.close()
        if len(q_stock) <= 0:
            return True
        return False

    def buy_stock(self):   # функция покупки акции, вызывает диал. окно для ввода кол-ва
        stock_data = self.get_info()
        dlg = QInputDialog(self)
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        dlg.setWindowTitle("Введите количество акций:")
        dlg.setLabelText("Количество акций к покупке:")
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        ok_pressed = dlg.exec_()
        quantity = dlg.textValue()
        price = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        con_p = sqlite3.connect('stocks.sqlite')
        cur_p = con_p.cursor()  # работа с бд: если акция уже есть, то прибавляется к уже имеющимся.
        # Если нет, добавляется в бд (portfolio). Нехватает денег/ввод не числом - ошибка
        if quantity.isnumeric() and int(self.lcdNumber.value()) // float(price) >= int(quantity)\
                and self.check_quantity(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()) and ok_pressed:
            cur_p.execute(f"""INSERT INTO portfolio(name, price, dividends, points, stock_type, quantity) 
            VALUES('{stock_data[0]}', {stock_data[1]}, {stock_data[2]},
             '{stock_data[3]}', {self.check_stock_type(stock_data[1])}, {quantity})""")
            con_p.commit()
            con_p.close()
            self.lcdNumber.display(str(int(int(self.lcdNumber.value()) - round(int(quantity) * float(price), 0))))
            self.place_stocks()
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:   # запись новых параметров
                money.write(str(int(self.lcdNumber.value())) + '\n')
                money.write(self.label_4.text())
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:  # запись события
                data_book.write(f'   {self.label_4.text()}: Покупка {stock_data[0]}, {quantity}.\n')
        elif quantity.isnumeric() and int(self.lcdNumber.value()) // float(price) >= int(quantity)\
                and not self.check_quantity(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())\
                and ok_pressed:
            cur_p.execute(f"""UPDATE portfolio SET quantity =
             quantity + {int(quantity)} WHERE name='{stock_data[0]}'""")
            con_p.commit()
            con_p.close()
            self.lcdNumber.display(str(int(int(self.lcdNumber.value()) - round(int(quantity) * float(price), 0))))
            self.place_stocks()
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:  # запись новых параметров
                money.write(str(int(self.lcdNumber.value())) + '\n')
                money.write(self.label_4.text())
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:  # заипсь нового события
                data_book.write(f'   {self.label_4.text()}: Покупка {stock_data[0]}, {quantity}.\n')
        elif ok_pressed and not quantity.isnumeric() or ok_pressed and not quantity == '' or ok_pressed and\
                quantity.isnumeric() and int(int(self.lcdNumber.value())) / float(price) < int(quantity):
            dlg = QMessageBox(self)  # диал. окно с ошибкой
            dlg.setStyleSheet("color: rgb(255, 255, 255);")
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Неверное количество акций!")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.exec()

    def sell_stock(self):  # функция для продажи акций, работает как и с покупкой, но с вычитанем
        con_p = sqlite3.connect('stocks.sqlite')
        cur_p = con_p.cursor()
        stock_data = self.get_info()
        dlg = QInputDialog(self)
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        dlg.setWindowTitle("Введите количество акций:")
        dlg.setLabelText("Количество акций к продаже:")
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        ok_pressed = dlg.exec_()
        quantity = dlg.textValue()
        if quantity.isnumeric() and ok_pressed and int(quantity) == int(stock_data[-1]):
            cur_p.execute(f"""DELETE from portfolio WHERE name='{stock_data[0]}'""")
            con_p.commit()
            con_p.close()
            self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())
            self.lcdNumber.display(str(int(int(self.lcdNumber.value())
                                           + round(int(quantity) * float(stock_data[1]), 0))))
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:
                money.write(str(int(self.lcdNumber.value())) + '\n')
                money.write(self.label_4.text())
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:
                data_book.write(f'   {self.label_4.text()}: Продажа {stock_data[0]}, {quantity}.\n')
        elif quantity.isnumeric() and ok_pressed and int(quantity) < int(stock_data[-1]):
            cur_p.execute(f"""UPDATE portfolio SET quantity = quantity - {quantity} WHERE name='{stock_data[0]}'""")
            con_p.commit()
            con_p.close()
            self.tableWidget_2.setItem(self.tableWidget_2.currentRow(), 3,
                                       QTableWidgetItem(str(int(stock_data[-1]) - int(quantity))))
            self.tableWidget_2.item(self.tableWidget_2.currentRow(),
                                    3).setBackground(QColor(*list(map(int, stock_data[4][1:-1].split(', ')))))
            self.lcdNumber.display(str(int(int(self.lcdNumber.value())
                                           + round(int(quantity) * float(stock_data[1]), 0))))
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:
                money.write(str(int(self.lcdNumber.value())) + '\n')
                money.write(self.label_4.text())
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:
                data_book.write(f'   {self.label_4.text()}: Продажа {stock_data[0]}, {quantity}.\n')
        elif ok_pressed and not quantity.isnumeric() or ok_pressed and int(quantity) > int(stock_data[-1]):
            dlg = QMessageBox(self)
            dlg.setStyleSheet("color: rgb(255, 255, 255);")
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Неверное количество акций!")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.exec()

    def sell_everything(self):  # продажа всего
        dlg = QMessageBox(self)  # диал.окно с подтверждением
        dlg.setStyleSheet("color: rgb(255, 255, 255);")
        dlg.setWindowTitle("Sell everything?")
        dlg.setText("Do you want to sell everything?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            con_p = sqlite3.connect('stocks.sqlite')
            cur_p = con_p.cursor()
            prices = cur_p.execute(f"""SELECT price FROM portfolio""").fetchall()
            quants = cur_p.execute(f"""SELECT quantity FROM portfolio""").fetchall()
            sumr = 0
            for i in range(len(prices)):  # нахождение суммы цен акций
                sumr += int(list(prices)[i][0]) * int(list(quants)[i][0])
            cur_p.execute(f"""DELETE from portfolio""")  # чистка бд
            con_p.commit()
            con_p.close()
            self.tableWidget_2.clear()
            self.lcdNumber.display(str(int(int(self.lcdNumber.value()) + sumr)))
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money:  # запись новых параметров
                money.write(str(int(self.lcdNumber.value())) + '\n')
                money.write(self.label_4.text())
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:  # запись нового события
                data_book.write(f'   {self.label_4.text()}: Весь портфель был продан, соcтояние:'
                                f' {self.lcdNumber.value()}\n')

    def check_stock_type(self, price):   # проверка уровня акции (зависит от цены)
        if int(price) <= 50:
            return 1
        elif 50 < int(price) < 500:
            return 2
        else:
            return 3

    def check_dividends(self):   # подсчет дивов
        con_p = sqlite3.connect('stocks.sqlite')
        cur_p = con_p.cursor()
        if self.label_4.text()[-2:] == '01':
            divs = cur_p.execute("""SELECT dividends from portfolio""").fetchall()
            quants = cur_p.execute("""SELECT quantity from portfolio""").fetchall()
            sum_d = 0
            for i in range(len(divs)):   # нахождение суммы дивов
                sum_d += float(divs[i][0]) * int(quants[i][0])
            sum_d = int(sum_d)
            self.lcdNumber.display(str(int(self.lcdNumber.value()) + int(sum_d)))
            self.label.setText('   Новое событие - ' + self.label_4.text() + ':   ' + 'Dividends day!')
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:
                data_book.write(f'   {self.label_4.text()}: Dividends day! Earned {sum_d}\n')
                # добавление события с датой в файл истории
            cur_p.execute("""UPDATE market SET price = ROUND(price - price * 0.21, 0)
             WHERE dividends >= 5 AND price <= 499""")   # изменение цен после умеьнш. спроса
            cur_p.execute("""UPDATE portfolio SET price = ROUND(price - price * 0.21, 0)
             WHERE dividends >= 5 AND price <= 499""")
            cur_p.execute("""UPDATE market SET price = ROUND(price - price * 0.09, 0)
                         WHERE dividends >= 5 AND price > 499""")
            cur_p.execute("""UPDATE portfolio SET price = ROUND(price - price * 0.09, 0)
                         WHERE dividends >= 5 AND price > 499""")
            con_p.commit()
            self.check_stocks()
            self.place_stocks()
        elif self.label_4.text()[-2:] == '28':  # симуляция повышения цен (спроса) перед выплатой дивидендов
            cur_p.execute("""UPDATE market SET price = ROUND(price + price * 0.2, 0)
             WHERE dividends >= 5 AND price <= 499""")
            cur_p.execute("""UPDATE portfolio SET price = ROUND(price + price * 0.2, 0)
             WHERE dividends >= 5 AND price <= 499""")
            cur_p.execute("""UPDATE market SET price = ROUND(price + price * 0.08, 0)
             WHERE dividends >= 5 AND price > 499""")
            cur_p.execute("""UPDATE portfolio SET price = ROUND(price + price * 0.08, 0)
            WHERE dividends >= 5 AND price > 499""")
            con_p.commit()
            self.check_stocks()
            self.place_stocks()
        con_p.close()

    def place_stocks(self):  # функция размещения акций
        con_m = sqlite3.connect('stocks.sqlite')
        cur_m = con_m.cursor()   # получаем инфу из бд
        data = cur_m.execute("""Select name, price, dividends, points, types.type FROM market
         INNER JOIN types ON market.stock_type = types.type_id ORDER BY price""").fetchall()
        burnt_stocks = cur_m.execute("""Select name FROM market WHERE price <= 0 or dividends <= 0""").fetchall()
        con_m.commit()
        with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:  # записываем прогоревшие акции
            for company in burnt_stocks:
                data_book.write(f'   {self.label_4.text()}: Компания {company[0]} прогорела.\n')
        cur_m.execute("""DELETE FROM market WHERE price <= 0 OR dividends <= 0""")
        self.tableWidget.setColumnCount(3)  # рисуем таблицу, заполняем
        self.tableWidget.setHorizontalHeaderLabels(['Company', 'Price', 'Dividends'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):   # заполнение таблицы
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
            for col in range(self.tableWidget.columnCount()):  # покраска рядов таблицы
                self.tableWidget.item(i, col).setBackground(QColor(*list(map(int, row[-1][1:-1].split(', ')))))
        self.tableWidget.resizeColumnsToContents()  # тоже самое, но со второй таблицей
        cur_m.execute("""DELETE FROM portfolio WHERE price <= 0 OR dividends <= 0""")
        data = cur_m.execute("""Select name, price, dividends, quantity, types.type FROM portfolio
         INNER JOIN types ON portfolio.stock_type = types.type_id ORDER BY price""").fetchall()
        con_m.commit()
        con_m.close()
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setHorizontalHeaderLabels(['Company', 'Price', 'Dividends', 'Quantity'])
        self.tableWidget_2.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget_2.setRowCount(self.tableWidget_2.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(elem)))
            for col in range(self.tableWidget_2.columnCount()):
                self.tableWidget_2.item(i, col).setBackground(QColor(*list(map(int, row[-1][1:-1].split(', ')))))
        self.tableWidget_2.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
