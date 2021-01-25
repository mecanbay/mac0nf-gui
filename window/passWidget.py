# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password-wiget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 239)
        MainWindow.setMinimumSize(QtCore.QSize(314, 239))
        MainWindow.setMaximumSize(QtCore.QSize(314, 239))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius:18px;\n"
"    background-color: rgb(29, 60, 50);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 100, 241, 33))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(100, 139, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(211, 215, 207);")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 160, 141, 33))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(-10, 0, 321, 31))
        self.widget_2.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(32, 87, 98);\n"
"    border-radius: 15px;\n"
"\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(100, -10, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(115, 210, 22);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Root Password :"))
        self.label_8.setText(_translate("MainWindow", "Wrong Password !"))
        self.pushButton_2.setText(_translate("MainWindow", "Apply"))
        self.label_9.setText(_translate("MainWindow", "Mac0nf GUI v1.0"))

