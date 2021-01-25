# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 443)
        MainWindow.setMinimumSize(QtCore.QSize(304, 443))
        MainWindow.setMaximumSize(QtCore.QSize(316, 443))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius:18px;\n"
"    background-color: rgb(29, 60, 50);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 321, 41))
        self.widget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(32, 87, 98);\n"
"    border-radius: 15px;\n"
"\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, -4, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(115, 210, 22);")
        self.label.setObjectName("label")
        self.underBtn = QtWidgets.QToolButton(self.widget)
        self.underBtn.setGeometry(QtCore.QRect(250, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.underBtn.setFont(font)
        self.underBtn.setStyleSheet("QToolButton{\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"QToolButton:pressed{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.underBtn.setObjectName("underBtn")
        self.closeBtn = QtWidgets.QToolButton(self.widget)
        self.closeBtn.setGeometry(QtCore.QRect(280, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.closeBtn.setFont(font)
        self.closeBtn.setStyleSheet("QToolButton{\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(186, 189, 182);\n"
"    border-radius: 10px;\n"
"}\n"
"QToolButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgb(239, 41, 41);\n"
"}\n"
"QToolButton:pressed{\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.closeBtn.setObjectName("closeBtn")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(115, 210, 22);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(78, 154, 6);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 160, 241, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(78, 154, 6);\n"
"    border-radius: 16px;\n"
"    \n"
"    color: rgb(46, 52, 54);\n"
"    padding-left:5px;\n"
"    padding-right:5px;\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(115, 210, 22);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(58, 143, 162)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(30, 230, 241, 33))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    border: 2px solid rgb(78, 154, 6);\n"
"    border-radius: 16px;\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left:5px;\n"
"    padding-right:5px;\n"
"    background-color: rgb(211, 215, 207);\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(211, 215, 207);\n"
"}\n"
"QComboBox:focus{\n"
"    border: 2px solid rgb(58, 143, 162)\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(30, 270, 241, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton{\n"
"color: rgb(211, 215, 207);\n"
"}\n"
"\n"
"QRadioButton::checked{\n"
"color: rgb(239, 41, 41);\n"
"}\n"
"\n"
"QRadioButton::unchecked{\n"
"color: rgb(211, 215, 207);\n"
"}\n"
"QRadioButton::hover{\n"
"color: rgb(78, 154, 6);\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 131, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    \n"
"    color: rgb(29, 60, 50);\n"
"    background-color: rgb(115, 210, 22);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(78, 154, 6);\n"
"}\n"
"\n"
"QPushButton:clicked{\n"
"    color: rgb(138, 226, 52);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 360, 191, 21))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(252, 233, 79);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(90, 380, 131, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mac0nf GUI v1.0"))
        self.underBtn.setText(_translate("MainWindow", "_"))
        self.closeBtn.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "Mac0nf GUI"))
        self.label_3.setText(_translate("MainWindow", "Created by Ns4r"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ex : 00:01:00:10:11:01"))
        self.label_4.setText(_translate("MainWindow", "New MAC Adress :"))
        self.label_5.setText(_translate("MainWindow", "Interface :"))
        self.radioButton.setText(_translate("MainWindow", "Random MAC"))
        self.pushButton.setText(_translate("MainWindow", "Change MAC"))
        self.label_6.setText(_translate("MainWindow", "OK ! New MAC Adress :"))
        self.label_7.setText(_translate("MainWindow", "00:24:81:3c:8d:2a"))
