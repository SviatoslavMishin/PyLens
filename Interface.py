# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(237, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 201, 80))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 81, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 201, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 50, 111, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 80, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setEnabled(False)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 230, 201, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 61, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 30, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setCurrentIndex(0)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 61, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 300, 201, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 330, 101, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Design Properties"))
        self.label.setText(_translate("MainWindow", "Clear Diameter:"))
        self.label_2.setText(_translate("MainWindow", "Total Fringes:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Material Properties"))
        self.label_3.setText(_translate("MainWindow", "Glass Catalog:"))
        self.label_4.setText(_translate("MainWindow", "Selected Glass:"))
        self.pushButton.setText(_translate("MainWindow", "Load Catalog"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Measurement Properties"))
        self.label_5.setText(_translate("MainWindow", "Wavelength:"))
        self.label_6.setText(_translate("MainWindow", "Focal length:"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Focal Length"))

