import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.make_circle.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        r = randint(10, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(100, 100, r, r)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(400, 100, r, r)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(250, 200, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
