import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class CirclePainter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Random Circles')

        self.button = QPushButton('Добавить окружность', self)
        self.button.clicked.connect(self.addRandomCircle)
        self.button.setGeometry(10, 10, 150, 30)

        self.circles = []

    def addRandomCircle(self):
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(QColor(color))
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CirclePainter()
    window.show()
    sys.exit(app.exec_())