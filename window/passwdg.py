from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from window.passWidget import Ui_MainWindow
from PyQt5 import QtCore

class PassWidget(QMainWindow):
    pass_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.wdg = Ui_MainWindow()
        self.wdg.setupUi(self)
        self.wdg.label_8.setText("")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.wdg.pushButton_2.clicked.connect(self.passwd)

    def passwd(self):
        self.password = self.wdg.lineEdit_2.text()
        self.pass_signal.emit(self.password)
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)