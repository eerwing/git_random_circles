import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 400)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 360, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Create circle"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        x, y, radius = random.randint(0, 250), random.randint(0, 200), random.randint(30, 150)
        qp.drawEllipse(x, y, radius, radius)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
