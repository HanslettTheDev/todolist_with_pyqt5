# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 392)
        self.todoView = QtWidgets.QListView(MainWindow)
        self.todoView.setGeometry(QtCore.QRect(35, 20, 321, 201))
        self.todoView.setObjectName("todoView")
        self.deleteButton = QtWidgets.QPushButton(MainWindow)
        self.deleteButton.setGeometry(QtCore.QRect(70, 250, 101, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.completeButton = QtWidgets.QPushButton(MainWindow)
        self.completeButton.setGeometry(QtCore.QRect(230, 250, 101, 31))
        self.completeButton.setObjectName("completeButton")
        self.addButton = QtWidgets.QPushButton(MainWindow)
        self.addButton.setGeometry(QtCore.QRect(40, 340, 311, 31))
        self.addButton.setObjectName("addButton")
        self.todoEdit = QtWidgets.QLineEdit(MainWindow)
        self.todoEdit.setGeometry(QtCore.QRect(40, 299, 311, 31))
        self.todoEdit.setObjectName("todoEdit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.addButton.setText(_translate("MainWindow", "Add Todo"))
