from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from window.mainQ import Ui_MainWindow
from window.passwdg import PassWidget
from subprocess import check_call
import os
import random

interface = os.listdir("/sys/class/net")
for i in interface:
    if i == "lo":
        interface.remove(i)


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.wdg = PassWidget()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.label_6.setText("")
        self.ui.label_7.setText("")
        self.ui.closeBtn.clicked.connect(self.closeBtn)
        self.ui.underBtn.clicked.connect(self.minimizeBtn)
        self.ui.comboBox.addItems(interface)
        self.ui.radioButton.clicked.connect(self.rdnMac)
        self.ui.pushButton.clicked.connect(self.changeBtn)
        self.wdg.pass_signal.connect(self.macChange)


    def macChange(self):
        try:
            check_call("echo {} | sudo -S pwd".format(self.wdg.password), shell=True)
            self.wdg.wdg.label_8.setText("")
            self.wdg.wdg.lineEdit_2.clear()
            self.interface = self.ui.comboBox.currentText()
            if self.ui.radioButton.isChecked():
                self.lastmac = self.randMac
            else:
                self.lastmac = self.ui.lineEdit.text()

            self.MacChange(self.interface, self.lastmac)
            self.wdg.hide()
        except:
            print("Hata")
            self.wdg.wdg.label_8.setText("Wrong Password !")
            self.wdg.wdg.lineEdit_2.clear()


        """
"""

    def MacChange(self, interface,mac):
        check_call("echo {} | sudo -S ifconfig {} down".format(self.wdg.password, interface), shell=True)
        check_call("echo {} | sudo -S ifconfig {} hw ether {}".format(self.wdg.password, interface, mac), shell=True)
        check_call("echo {} | sudo -S ifconfig {} up".format(self.wdg.password, interface), shell=True)
        self.ui.label_6.setText("OK ! New MAC Adress :")
        self.ui.label_7.setText(mac)

    def changeBtn(self):
        if self.ui.radioButton.isChecked():
            self.wdg.show()
        else:
            self.wdg.show()



    def rdnMac(self):
        if self.ui.radioButton.isChecked():
            self.ui.lineEdit.setPlaceholderText("Manuel MAC Disabled")
            self.ui.lineEdit.setDisabled(True)
            mac = [ 0x00, 0x24, 0x81,
                    random.randint(0x00, 0x7f),
                    random.randint(0x00, 0xff),
                    random.randint(0x00, 0xff) ]
            self.randMac = (':'.join(map(lambda x: "%02x" % x, mac)))
        else:
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit.setPlaceholderText("Ex : 00:01:00:10:11:01")


    def minimizeBtn(self):
        self.showMinimized()

    def closeBtn(self):
        self.wdg.close()
        self.close()

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

