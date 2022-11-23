import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import random


class Circles(QWidget):
    def __init__(self):
        super(Circles, self).__init__()
        self.flag = False
        uic.loadUi('UI.ui', self)
        self.paint_button.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            self.drawEllipse(qp)
            qp.end()
            self.flag = False

    def drawEllipse(self, qp):
        size = random.choice(range(50, 300))
        qp.drawEllipse(size, size, size * 2, size * 2)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())