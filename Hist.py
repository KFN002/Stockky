from PyQt5.QtWidgets import QTextEdit, QWidget


class HistWindow(QWidget):   # окно истории игры
    def __init__(self, parent=None):
        super(HistWindow, self).__init__(parent)
        self.setWindowTitle('Stockky game history')
        self.hist = QTextEdit(self)
        self.setGeometry(0, 0, 900, 600)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 140, 255),"
            " stop:1 rgba(0, 85, 130, 255));")
        self.hist.resize(900, 600)
        self.hist.setStyleSheet("color: rgb(255, 255, 255);")
        with open('text_files/history.txt', 'rt', encoding='utf-8') as data_book:
            for line in data_book.readlines():
                self.hist.append(line)
        self.show()
