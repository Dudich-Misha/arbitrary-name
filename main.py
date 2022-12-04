import sys
from PyQt5 import uic
from random import randrange
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import QtCore, QtWidgets

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('style.ui', self)
        self.initUi()

    def initUi(self):
        self.flag_draw_circle = False
        self.pushButton.clicked.connect(self.switch_flag)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.flag_draw_circle:
            self.draw_circle(qp)
        qp.end()

    def switch_flag(self):
        self.flag_draw_circle = True
        self.repaint()

    def draw_circle(self, qp):
        # qp.setBrush(QColor(randrange(256), randrange(256), randrange(256)))
        qp.setBrush(QColor('yellow'))
        side_square = randrange(4, 100)
        x_figure, y_figure = randrange(800), randrange(250)
        left_top = (x_figure - side_square // 2, y_figure - side_square // 2)
        qp.drawEllipse(*left_top, side_square, side_square)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

