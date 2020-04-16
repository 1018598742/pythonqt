# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parseapk.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(42, 30, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.select_button = QtWidgets.QPushButton(Form)
        self.select_button.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.select_button.setObjectName("select_button")
        self.parse_button = QtWidgets.QPushButton(Form)
        self.parse_button.setGeometry(QtCore.QRect(150, 240, 101, 31))
        self.parse_button.setObjectName("parse_button")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 70, 181, 151))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pic_label = QtWidgets.QLabel(Form)
        self.pic_label.setGeometry(QtCore.QRect(260, 80, 101, 141))
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "解析APK信息"))
        self.select_button.setText(_translate("Form", "选择文件"))
        self.parse_button.setText(_translate("Form", "解析"))
