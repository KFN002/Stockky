import random
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox


class ShopWindow(QWidget):   # окно магазина игры
    def __init__(self, parent=None):
        super(ShopWindow, self).__init__(parent)
        self.setWindowTitle('Game eShop')
        self.setGeometry(0, 0, 1400, 800)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 140, 255),"
            " stop:1 rgba(0, 85, 130, 255));")
        self.buyButton = QPushButton(self)
        self.buyButton.setGeometry(50, 50, 500, 100)
        self.buyButton.setStyleSheet("background-color: rgb(85, 0, 255);\n"
                                     "border-radius: 10px;\n"
                                     "border-style: outset;\n"
                                     "border-width: 1px;\n"
                                     "border-color: white;\n"
                                     "color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buyButton.setFont(font)
        self.buyButton.setText('Buy meme\n'
                               'Price: 10000')
        self.image = QLabel(self)
        self.image.setGeometry(700, 50, 650, 700)
        self.buyButton.clicked.connect(self.buy_meme)
        self.show()

    def buy_meme(self):    # покупка мема
        file_name = random.choice(['memes/meme1.jpg', 'memes/meme2.jpg', 'memes/meme3.jpg', 'memes/meme4.jpg'])
        with open('text_files/account_params.txt', 'rt', encoding='utf-8') as money_data:
            data = money_data.readlines()  # подгрузка денег пользователя
            money = data[0].strip()
            time = data[1].strip()
        if int(money) >= 10000:
            with open('text_files/account_params.txt', 'wt', encoding='utf-8') as money_data:
                money_data.write(str(int(money) - 10000) + '\n')
                money_data.write(time)   # запись денег игрока
            self.pixmap = QPixmap(file_name)
            self.image.setPixmap(self.pixmap)
            with open('text_files/history.txt', 'a', encoding='utf-8') as data_book:
                data_book.write(f'   Покупка мема \n')  # добавление события в файл с историей
        else:   # окно, если нет денег
            dlg = QMessageBox(self)
            dlg.setStyleSheet("color: rgb(255, 255, 255);")
            dlg.setWindowTitle("Ошибка!")
            dlg.setText("Нехватает денег!")
            dlg.setStandardButtons(QMessageBox.Ok)
            dlg.setIcon(QMessageBox.Critical)
            dlg.exec()
