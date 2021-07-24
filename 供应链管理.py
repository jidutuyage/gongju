from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QMainWindow, QTableView,QGridLayout
from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import configparser
import sys
import time
import datetime
import pymssql
import numpy as np
import pandas as pd
import re
import requests
import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.withdraw()

# 2021-7-24
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1411, 992)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 1381, 951))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(270, 10, 1021, 731))
        self.tableView.setObjectName("tableView")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 10, 221, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setSizeIncrement(QtCore.QSize(0, 500))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 230, 221, 307))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 300, 231, 307))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_13 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.tableView_2 = QtWidgets.QTableView(self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(260, 20, 1021, 731))
        self.tableView_2.setObjectName("tableView_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 231, 271))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setSizeIncrement(QtCore.QSize(0, 500))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_16)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1341, 481))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_17.setGeometry(QtCore.QRect(510, 20, 381, 71))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_18.setGeometry(QtCore.QRect(510, 100, 381, 121))
        self.lineEdit_18.setSizeIncrement(QtCore.QSize(0, 0))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(410, 50, 84, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(950, 20, 181, 240))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_17 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_3.addWidget(self.pushButton_19)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 371, 352))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_19)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_20)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_24)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_25)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_26)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_27)
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(410, 140, 84, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setGeometry(QtCore.QRect(510, 230, 381, 121))
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_29.setGeometry(QtCore.QRect(510, 360, 381, 101))
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setGeometry(QtCore.QRect(410, 280, 84, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setGeometry(QtCore.QRect(410, 400, 84, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1170, 20, 160, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_20 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_4.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_4.addWidget(self.pushButton_21)
        self.pushButton_22 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_4.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_4.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_4.addWidget(self.pushButton_24)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(400, 30, 31, 19))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 60, 31, 19))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(400, 90, 31, 19))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(400, 180, 31, 19))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.tableView_3 = QtWidgets.QTableView(self.tab_3)
        self.tableView_3.setGeometry(QtCore.QRect(10, 500, 1341, 411))
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(30, 20, 181, 201))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setSpacing(7)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_33 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_30.setSizeIncrement(QtCore.QSize(0, 500))
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_30)
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_31)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_32)
        self.label_36 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_33)
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_34)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_35)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 230, 181, 211))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_26 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_5.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_5.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_5.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_5.addWidget(self.pushButton_29)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.verticalLayout_5.addWidget(self.lineEdit_36)
        self.tableView_4 = QtWidgets.QTableView(self.tab_4)
        self.tableView_4.setGeometry(QtCore.QRect(230, 10, 1111, 251))
        self.tableView_4.setObjectName("tableView_4")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(230, 270, 1111, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_39 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_2.addWidget(self.label_39)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.horizontalLayout_2.addWidget(self.lineEdit_37)
        self.label_40 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_2.addWidget(self.label_40)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.horizontalLayout_2.addWidget(self.lineEdit_38)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_2.setGeometry(QtCore.QRect(230, 370, 1111, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_30 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout.addWidget(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout.addWidget(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout.addWidget(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout.addWidget(self.pushButton_35)
        self.label_41 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_41.setObjectName("label_41")
        self.horizontalLayout.addWidget(self.label_41)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.horizontalLayout.addWidget(self.lineEdit_39)
        self.label_42 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout.addWidget(self.label_42)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.horizontalLayout.addWidget(self.lineEdit_40)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 450, 335, 451))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 450, 334, 451))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(690, 450, 335, 451))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(1030, 450, 334, 451))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "办公一体化系统"))
        self.label.setText(_translate("Form", "SKU"))
        self.label_2.setText(_translate("Form", "SPU"))
        self.label_3.setText(_translate("Form", "name"))
        self.label_4.setText(_translate("Form", "网址"))
        self.label_5.setText(_translate("Form", "价格"))
        self.label_6.setText(_translate("Form", "库存"))
        self.label_7.setText(_translate("Form", "id"))
        self.pushButton_9.setText(_translate("Form", "查询"))
        self.pushButton_8.setText(_translate("Form", "录入"))
        self.pushButton_7.setText(_translate("Form", "更新"))
        self.pushButton_6.setText(_translate("Form", "删除"))
        self.pushButton_11.setText(_translate("Form", "入库"))
        self.pushButton_12.setText(_translate("Form", "库存校对"))
        self.pushButton.setText(_translate("Form", "清空"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "商品库存"))
        self.pushButton_10.setText(_translate("Form", "查询"))
        self.pushButton_13.setText(_translate("Form", "录入"))
        self.pushButton_14.setText(_translate("Form", "更新"))
        self.pushButton_15.setText(_translate("Form", "删除"))
        self.pushButton_16.setText(_translate("Form", "批量导入"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.label_8.setText(_translate("Form", "SKU"))
        self.label_9.setText(_translate("Form", "数量"))
        self.label_10.setText(_translate("Form", "下单时间"))
        self.label_11.setText(_translate("Form", "客户"))
        self.label_12.setText(_translate("Form", "订单号"))
        self.label_13.setText(_translate("Form", "进度"))
        self.label_14.setText(_translate("Form", "完成时间"))
        self.label_15.setText(_translate("Form", "备注说明"))
        self.label_16.setText(_translate("Form", "id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "生产订单"))
        self.label_17.setText(_translate("Form", "报价"))
        self.pushButton_4.setText(_translate("Form", "查询客户"))
        self.pushButton_3.setText(_translate("Form", "录入客户"))
        self.pushButton_5.setText(_translate("Form", "更改客户"))
        self.pushButton_17.setText(_translate("Form", "删除客户"))
        self.pushButton_18.setText(_translate("Form", "批量录入客户"))
        self.pushButton_19.setText(_translate("Form", "全部清空"))
        self.label_18.setText(_translate("Form", "公司名***"))
        self.label_19.setText(_translate("Form", "对接人***"))
        self.label_20.setText(_translate("Form", "对接账号***"))
        self.label_21.setText(_translate("Form", "联系方式"))
        self.label_22.setText(_translate("Form", "合作情况"))
        self.label_23.setText(_translate("Form", "星级"))
        self.label_24.setText(_translate("Form", "累计金额"))
        self.label_25.setText(_translate("Form", "ID***"))
        self.label_26.setText(_translate("Form", "对接方式"))
        self.label_27.setText(_translate("Form", "对接产品"))
        self.label_28.setText(_translate("Form", "访客来源"))
        self.label_29.setText(_translate("Form", "日期"))
        self.label_30.setText(_translate("Form", "备注"))
        self.label_31.setText(_translate("Form", "对接内容"))
        self.label_32.setText(_translate("Form", "后续对接"))
        self.pushButton_20.setText(_translate("Form", "查询沟通"))
        self.pushButton_21.setText(_translate("Form", "录入沟通"))
        self.pushButton_22.setText(_translate("Form", "更改沟通"))
        self.pushButton_23.setText(_translate("Form", "删除沟通"))
        self.pushButton_24.setText(_translate("Form", "批量录入沟通"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "客户管理"))
        self.label_33.setText(_translate("Form", "展现量"))
        self.label_34.setText(_translate("Form", "访客量"))
        self.label_35.setText(_translate("Form", "浏览量"))
        self.label_36.setText(_translate("Form", "询盘量"))
        self.label_37.setText(_translate("Form", "下单量"))
        self.label_38.setText(_translate("Form", "金额"))
        self.pushButton_26.setText(_translate("Form", "订单校对"))
        self.pushButton_27.setText(_translate("Form", "订单导入"))
        self.pushButton_28.setText(_translate("Form", "排名查询"))
        self.pushButton_29.setText(_translate("Form", "排名抓取"))
        self.lineEdit_36.setText(_translate("Form", "10"))
        self.label_39.setText(_translate("Form", "数据分析"))
        self.label_40.setText(_translate("Form", "对策调整"))
        self.pushButton_30.setText(_translate("Form", "查询"))
        self.pushButton_31.setText(_translate("Form", "录入"))
        self.pushButton_32.setText(_translate("Form", "更新"))
        self.pushButton_33.setText(_translate("Form", "清空"))
        self.pushButton_34.setText(_translate("Form", "删除"))
        self.pushButton_35.setText(_translate("Form", "图表"))
        self.label_41.setText(_translate("Form", "可选日期"))
        self.label_42.setText(_translate("Form", "指定"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.groupBox_3.setTitle(_translate("Form", "GroupBox"))
        self.groupBox_4.setTitle(_translate("Form", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "数据登记"))

class MyFigure(FigureCanvas):
    def __init__(self,width=5, height=4, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中**Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】

def show_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    if ui.lineEdit.text() and ui.lineEdit_3.text() != "":
        sql = "SELECT * FROM shangpin "
        tkinter.messagebox.showinfo('错误', "条件查询项过多")
    else:
        if ui.lineEdit.text() != "":
            sql = "SELECT * FROM shangpin WHERE SKU LIKE '%%%%%s%%%%'" % str(ui.lineEdit.text())
        else:
            if ui.lineEdit_3.text() != "":
                sql = "SELECT * FROM shangpin WHERE name LIKE '%%%%%s%%%%'" % str(ui.lineEdit_3.text())
            else:
                sql = "SELECT * FROM shangpin "
    ds = pd.DataFrame(pd.read_sql(sql, conn))
    if ds.empty:
        tkinter.messagebox.showinfo('错误', "没有查到数据")
    else:
        model = QStandardItemModel()
        for i in range(0, int(ds.shape[1])):
            model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
            for j in range(0, int(ds.shape[0])):
                model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
        ui.tableView.setModel(model)
        ui.tableView.setColumnWidth(0, 100)
        ui.tableView.setColumnWidth(1, 150)
        ui.tableView.setColumnWidth(2, 120)
        ui.tableView.setColumnWidth(3, 120)
        ui.tableView.setColumnWidth(4, 70)
        ui.tableView.setColumnWidth(5, 70)
        ui.lineEdit.setText(str(ds.iat[0, 0]))
        ui.lineEdit_2.setText(str(ds.iat[0, 1]))
        ui.lineEdit_3.setText(str(ds.iat[0, 2]))
        ui.lineEdit_4.setText(str(ds.iat[0, 3]))
        ui.lineEdit_5.setText(str(ds.iat[0, 4]))
        ui.lineEdit_6.setText(str(ds.iat[0, 5]))
        ui.lineEdit_7.setText(str(ds.iat[0, 6]))

def insert_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "INSERT INTO shangpin(SKU,SPU,name,url,price,stock) VALUES ('%s','%s','%s','%s',%s,%s)" \
          % (ui.lineEdit.text(), ui.lineEdit_2.text(), ui.lineEdit_3.text(), ui.lineEdit_4.text(), ui.lineEdit_5.text(), ui.lineEdit_6.text())
    cur.execute(sql)
    conn.commit()
    tkinter.messagebox.showinfo('提示', "插入数据成功")

def clean_shangpin(self):
    ui.lineEdit.setText('')
    ui.lineEdit_2.setText('')
    ui.lineEdit_3.setText('')
    ui.lineEdit_4.setText('')
    ui.lineEdit_5.setText('0')
    ui.lineEdit_6.setText('0')
    ui.lineEdit_7.setText('0')

def update_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "update shangpin set SKU='{}',SPU='{}',name='{}',url='{}',price='{}',stock='{}' where id ='{}'"
    sql2 = sql.format(ui.lineEdit.text(),ui.lineEdit_2.text(),ui.lineEdit_3.text(),ui.lineEdit_4.text(),ui.lineEdit_5.text(), ui.lineEdit_6.text(),ui.lineEdit_7.text())
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"更新数据成功")

def delete_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "delete from shangpin where id ='{}'"
    sql2 = sql.format(str(ui.lineEdit_7.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"删除数据成功")

def correcting_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini', encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "select * from shangpin"
    df = pd.DataFrame(pd.read_sql(sql, conn))
    ds = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx',sheet_name='库存校对'))
    k = 0
    cur = conn.cursor()
    for i in range(0, len(ds)):
        no = ds.at[i, 'SKU']
        sql = "select * from shangpin where SKU = '{}'"
        sql2 = sql.format(no)
        cur.execute(sql2)
        result = cur.fetchone()
        if result is not None:
            if result[0] is not None:
                num = ds.at[i, 'stock']
                sql = "update shangpin set stock='{}' where SKU ='{}'"
                sql2 = sql.format(num, no)
                cur.execute(sql2)
                conn.commit()
                k += 1
    tkinter.messagebox.showinfo('提示', "校对更新" + str(k) + "条")

def Warehousing_shangpin(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini', encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "select * from shangpin"
    df = pd.DataFrame(pd.read_sql(sql, conn))
    ds = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx',sheet_name='入库'))
    k = 0
    cur = conn.cursor()
    for i in range(0, len(ds)):
        no = ds.at[i, 'SKU']
        sql = "select * from shangpin where SKU = '{}'"
        sql2 = sql.format(no)
        cur.execute(sql2)
        result = cur.fetchone()
        if result is not None:
            if result[0] is not None:
                num = ds.at[i, 'quantity'] + result[5]
                sql = "update shangpin set stock='{}' where SKU ='{}'"
                sql2 = sql.format(num, no)
                cur.execute(sql2)
                conn.commit()
                k += 1
    tkinter.messagebox.showinfo('提示', "入库" + str(k) + "条")

def show_shengchan(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    if ui.lineEdit_16.text() != "":
        sql = "SELECT * FROM shengchan WHERE id LIKE '%%%%%s%%%%'" % str(ui.lineEdit_16.text())
    else:
        sql = "SELECT * FROM shengchan order by id desc "
    ds = pd.DataFrame(pd.read_sql(sql, conn))
    if ds.empty:
        tkinter.messagebox.showinfo('错误', "没有查到数据")
    else:
        model = QStandardItemModel()
        for i in range(0, int(ds.shape[1])):
            model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
            for j in range(0, int(ds.shape[0])):
                model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
        ui.tableView_2.setModel(model)
        ui.tableView_2.setColumnWidth(0, 100)
        ui.tableView_2.setColumnWidth(1, 60)
        ui.tableView_2.setColumnWidth(2, 120)
        ui.tableView_2.setColumnWidth(3, 60)
        ui.tableView_2.setColumnWidth(4, 150)
        ui.tableView_2.setColumnWidth(5, 100)
        ui.tableView_2.setColumnWidth(6, 110)
        ui.tableView_2.setColumnWidth(7, 170)
        ui.tableView_2.setColumnWidth(8, 70)
        ui.lineEdit_8.setText(str(ds.iat[0, 0]))
        ui.lineEdit_9.setText(str(ds.iat[0, 1]))
        ui.lineEdit_10.setText(str(ds.iat[0, 2]))
        ui.lineEdit_11.setText(str(ds.iat[0, 3]))
        ui.lineEdit_12.setText(str(ds.iat[0, 4]))
        ui.lineEdit_13.setText(str(ds.iat[0, 5]))
        ui.lineEdit_14.setText(str(ds.iat[0, 6]))
        ui.lineEdit_15.setText(str(ds.iat[0, 7]))
        ui.lineEdit_16.setText(str(ds.iat[0, 8]))

def insert_shengchan(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "INSERT INTO shengchan(SKU,数量,下单时间,客户,订单号,进度,完成时间,备注说明) VALUES ('%s',%s,'%s','%s','%s','%s','%s','%s')" \
          % (ui.lineEdit_8.text(), int(ui.lineEdit_9.text()), ui.lineEdit_10.text(), ui.lineEdit_11.text(), ui.lineEdit_12.text(), ui.lineEdit_13.text(),ui.lineEdit_14.text(), ui.lineEdit_15.text())
    cur.execute(sql)
    conn.commit()
    tkinter.messagebox.showinfo('提示', "插入数据成功")

def clean_shengchan(self):
    ui.lineEdit_8.setText('')
    ui.lineEdit_9.setText('0')
    ui.lineEdit_10.setText('')
    ui.lineEdit_11.setText('')
    ui.lineEdit_12.setText('')
    ui.lineEdit_13.setText('')
    ui.lineEdit_14.setText('')
    ui.lineEdit_15.setText('')
    ui.lineEdit_16.setText('')

def update_shengchan(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()

    if ui.lineEdit_12.text() != "" and ui.lineEdit_14.text() != "" :
        sql = "update shengchan set 进度='{}',完成时间='{}' where 订单号 ='{}' "
        sql2 = sql.format(ui.lineEdit_13.text(),ui.lineEdit_14.text(),ui.lineEdit_12.text())
    else:
        sql = "update shengchan set SKU='{}',数量='{}',下单时间='{}',客户='{}',订单号='{}',进度='{}',完成时间='{}',备注说明='{}' where id ='{}'"
        sql2 = sql.format(ui.lineEdit_8.text(),int(ui.lineEdit_9.text()),ui.lineEdit_10.text(),ui.lineEdit_11.text(),ui.lineEdit_12.text(), ui.lineEdit_13.text(),ui.lineEdit_14.text(),ui.lineEdit_15.text(),ui.lineEdit_16.text())

    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"更新数据成功")

def delete_shengchan(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "delete from shengchan where id ='{}'"
    sql2 = sql.format(str(ui.lineEdit_16.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"删除数据成功")

def import_shengchan(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini', encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "select * from shengchan"
    df = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx',sheet_name='生产'))
    df['下单时间'] = pd.to_datetime(df['下单时间'])
    cur = conn.cursor()
    for i in range(0,len(df)):
        sql = "INSERT INTO shengchan(SKU,数量 ,下单时间 ,客户 ,订单号 ,进度  ,备注说明) VALUES ('%s',%s,'%s','%s','%s','%s','%s')" \
        % (df.at[i,'SKU'], df.at[i,'数量'], df.at[i,'下单时间'], df.at[i,'客户'],df.at[i,'订单号'], df.at[i,'进度'], df.at[i,'备注说明'])
        cur.execute(sql)
        conn.commit()
    tkinter.messagebox.showinfo('提示', "批量插入数据成功")

def show_kehu(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    if ui.lineEdit_20.text() != "" :
        a1=1
    else:
        a1=0
    if ui.lineEdit_19.text() != "" :
        a2=1
    else:
        a2=0
    if ui.lineEdit_21.text() != "":
        a3 = 1
    else:
        a3 = 0
    if ui.lineEdit_24.text() != "" :
        a4=1
    else:
        a4=0
    if a1+a2+a3+a4 > 1 and a1+a2+a3+a4 < 4 :
        tkinter.messagebox.showinfo('错误', "查询项不能超过1个")
    if a1+a2+a3+a4 == 1 :
        if ui.lineEdit_20.text() != "" :
            sql =  "SELECT * FROM kehu WHERE 对接人 LIKE '%%%%%s%%%%'" % str(ui.lineEdit_20.text())
        elif ui.lineEdit_19.text() != "" :
            sql =  "SELECT * FROM kehu WHERE 公司名 LIKE '%%%%%s%%%%'" % str(ui.lineEdit_19.text())
        elif ui.lineEdit_21.text() != "" :
            sql =  "SELECT * FROM kehu WHERE 采购账号 LIKE '%%%%%s%%%%'" % str(ui.lineEdit_21.text())
        else :
            sql =  "SELECT * FROM kehu WHERE ID LIKE '%%%%%s%%%%'" % str(ui.lineEdit_24.text())
        ds = pd.DataFrame(pd.read_sql(sql, conn))
        if ds.empty :
            pass
        else:
            model = QStandardItemModel()
            for i in range(0, int(ds.shape[1])):
                model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
                for j in range(0, int(ds.shape[0])):
                    model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
            ui.tableView_3.setModel(model)
            ui.tableView_3.setColumnWidth(0, 100)
            ui.tableView_3.setColumnWidth(1, 150)
            ui.tableView_3.setColumnWidth(2, 120)
            ui.tableView_3.setColumnWidth(3, 120)
            ui.tableView_3.setColumnWidth(4, 70)
            ui.tableView_3.setColumnWidth(5, 70)
            ui.tableView_3.setColumnWidth(6, 70)
            ui.tableView_3.setColumnWidth(7, 70)
            ui.tableView_3.setColumnWidth(10, 50)
            ui.lineEdit_20.setText(str(ds.iat[0, 3]))
            ui.lineEdit_19.setText(str(ds.iat[0, 1]))
            ui.lineEdit_21.setText(str(ds.iat[0, 2]))
            ui.lineEdit_22.setText(str(ds.iat[0, 4]))
            ui.lineEdit_17.setText(str(ds.iat[0, 5]))
            ui.lineEdit_18.setText(str(ds.iat[0, 10]))
            ui.lineEdit_23.setText(str(ds.iat[0, 9]))
            ui.lineEdit_24.setText(str(ds.iat[0, 11]))
            ui.lineEdit_26.setText(str(ds.iat[0, 7]))
            ui.lineEdit_27.setText(str(ds.iat[0, 0]))
            ui.comboBox.addItem(str(ds.iat[0, 8]), 0)
            ui.comboBox_2.addItem(str(ds.iat[0, 6]))
            ui.comboBox.addItems(['合作中', '洽谈中', '待开发', '不合作'])
            ui.comboBox_2.addItems(['1星', '2星', '3星', '4星', '5星'])
    if a1+a2+a3+a4 == 4 or a1+a2+a3+a4 == 0  :
        if ui.radioButton_4.isChecked() == True:
            sql = "SELECT * FROM kehu WHERE 合作情况 LIKE '%%%%%s%%%%'" % str(ui.comboBox.currentText())
        else:
            sql = "select * from kehu order by id  desc "
        ds = pd.DataFrame(pd.read_sql(sql, conn))
        if ds.empty :
            tkinter.messagebox.showinfo('错误', '没有数据')
        else:
            model = QStandardItemModel()
            for i in range(0, int(ds.shape[1])):
                model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
                for j in range(0, int(ds.shape[0])):
                    model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
            ui.tableView_3.setModel(model)
            ui.tableView_3.setColumnWidth(0, 100)
            ui.tableView_3.setColumnWidth(1, 150)
            ui.tableView_3.setColumnWidth(2, 120)
            ui.tableView_3.setColumnWidth(3, 120)
            ui.tableView_3.setColumnWidth(4, 70)
            ui.tableView_3.setColumnWidth(5, 70)
            ui.tableView_3.setColumnWidth(6, 70)
            ui.tableView_3.setColumnWidth(7, 70)
            ui.tableView_3.setColumnWidth(10, 50)
            ui.lineEdit_20.setText(str(ds.iat[0, 3]))
            ui.lineEdit_19.setText(str(ds.iat[0, 1]))
            ui.lineEdit_21.setText(str(ds.iat[0, 2]))
            ui.lineEdit_22.setText(str(ds.iat[0, 4]))
            ui.lineEdit_17.setText(str(ds.iat[0, 5]))
            ui.lineEdit_18.setText(str(ds.iat[0, 10]))
            ui.lineEdit_23.setText(str(ds.iat[0, 9]))
            ui.lineEdit_24.setText(str(ds.iat[0, 11]))
            ui.lineEdit_26.setText(str(ds.iat[0, 7]))
            ui.lineEdit_27.setText(str(ds.iat[0, 0]))
            ui.comboBox.addItem(str(ds.iat[0, 8]), 0)
            ui.comboBox_2.addItem(str(ds.iat[0, 6]))
        ui.comboBox.clear()
        ui.comboBox_2.clear()
        ui.comboBox.addItems(['合作中', '洽谈中', '待开发', '不合作'])
        ui.comboBox_2.addItems(['1星', '2星', '3星', '4星', '5星'])

def show_gou(self):
    ui.comboBox.clear()
    ui.comboBox_2.clear()
    ui.comboBox_3.clear()
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)

    if ui.lineEdit_20.text() != "":
        a1 = 1
    else:
        a1 = 0
    if ui.lineEdit_19.text() != "":
        a2 = 1
    else:
        a2 = 0
    if ui.lineEdit_21.text() != "":
        a3 = 1
    else:
        a3 = 0
    if ui.lineEdit_25.text() != "":
        a4 = 1
    else:
        a4 = 0
    if ui.lineEdit_24.text() != "":
        a5 = 1
    else:
        a5 = 0
    if a1+a2+a3+a4+a5 > 1 and a1+a2+a3+a4+a5 < 5:
        tkinter.messagebox.showinfo('错误', "查询项不能超过1个")
    if a1+a2+a3+a4+a5 == 1 :
        if ui.lineEdit_20.text() != "":
            sql = "SELECT * FROM goutong WHERE 对接人 LIKE '%%%%%s%%%%' order by id desc" % str(ui.lineEdit_20.text())
        elif ui.lineEdit_19.text() != "":
            sql = "SELECT * FROM goutong WHERE 公司名 LIKE '%%%%%s%%%%' order by id desc" % str(ui.lineEdit_19.text())
        elif ui.lineEdit_21.text() != "":
            sql = "SELECT * FROM goutong WHERE 采购账号 LIKE '%%%%%s%%%%' order by id desc" % str(ui.lineEdit_21.text())
        elif ui.lineEdit_25.text() != "":
            sql = "SELECT * FROM goutong WHERE 产品 LIKE '%%%%%s%%%%' order by id desc" % str(ui.lineEdit_25.text())
        else :
            sql = "SELECT * FROM goutong WHERE ID LIKE '%%%%%s%%%%' order by id desc" % str(ui.lineEdit_24.text())
        ds = pd.DataFrame(pd.read_sql(sql, conn))
        if ds.empty :
            pass
        else:
            model = QStandardItemModel()
            for i in range(0, int(ds.shape[1])):
                model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
                for j in range(0, int(ds.shape[0])):
                    model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
            ui.tableView_3.setModel(model)
            ui.tableView_3.setColumnWidth(0, 100)
            ui.tableView_3.setColumnWidth(1, 150)
            ui.tableView_3.setColumnWidth(2, 150)
            ui.tableView_3.setColumnWidth(3, 120)
            ui.tableView_3.setColumnWidth(4, 70)
            ui.tableView_3.setColumnWidth(5, 70)
            ui.tableView_3.setColumnWidth(6, 70)
            ui.tableView_3.setColumnWidth(7, 250)
            ui.tableView_3.setColumnWidth(10, 50)
            ui.lineEdit_20.setText(str(ds.iat[0, 2]))
            ui.lineEdit_19.setText(str(ds.iat[0, 1]))
            ui.lineEdit_21.setText(str(ds.iat[0, 3]))
            ui.lineEdit_22.setText('')
            ui.lineEdit_17.setText('')
            ui.lineEdit_18.setText('')
            ui.lineEdit_23.setText('')
            ui.lineEdit_24.setText(str(ds.iat[0, 9]))
            ui.lineEdit_28.setText(str(ds.iat[0, 7]))
            ui.lineEdit_29.setText(str(ds.iat[0, 8]))
            ui.lineEdit_25.setText(str(ds.iat[0, 4]))
            ui.lineEdit_27.setText(str(ds.iat[0, 0]))
            ui.comboBox.addItem(str(ds.iat[0, 5]))
            ui.comboBox_3.addItem(str(ds.iat[0, 6]))
            ui.comboBox.addItems(['合作中', '洽谈中', '待开发', '不合作'])
            ui.comboBox_3.addItems(['洽谈', '拿样', '采购', '拜访', '投诉'])
    if a1+a2+a3+a4+a5 == 5 or a1+a2+a3+a4+a5 == 0  :
        sql = "select * from goutong order by 日期  desc "
        ds = pd.DataFrame(pd.read_sql(sql, conn))
        model = QStandardItemModel()
        for i in range(0, int(ds.shape[1])):
            model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
            for j in range(0, int(ds.shape[0])):
                model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
        ui.tableView_3.setModel(model)
        ui.tableView_3.setColumnWidth(0, 100)
        ui.tableView_3.setColumnWidth(1, 150)
        ui.tableView_3.setColumnWidth(2, 150)
        ui.tableView_3.setColumnWidth(3, 120)
        ui.tableView_3.setColumnWidth(4, 70)
        ui.tableView_3.setColumnWidth(5, 70)
        ui.tableView_3.setColumnWidth(6, 70)
        ui.tableView_3.setColumnWidth(7, 250)
        ui.tableView_3.setColumnWidth(10, 50)
        ui.lineEdit_20.setText(str(ds.iat[0, 2]))
        ui.lineEdit_19.setText(str(ds.iat[0, 1]))
        ui.lineEdit_21.setText(str(ds.iat[0, 3]))
        ui.lineEdit_22.setText('')
        ui.lineEdit_17.setText('')
        ui.lineEdit_18.setText('')
        ui.lineEdit_23.setText('0')
        ui.lineEdit_24.setText(str(ds.iat[0, 9]))
        ui.lineEdit_28.setText(str(ds.iat[0, 7]))
        ui.lineEdit_29.setText(str(ds.iat[0, 8]))
        ui.lineEdit_25.setText(str(ds.iat[0, 4]))
        ui.lineEdit_27.setText(str(ds.iat[0, 0]))
        ui.comboBox.addItem(str(ds.iat[0, 5]))
        ui.comboBox_3.addItem(str(ds.iat[0, 6]))
        ui.comboBox.addItems(['合作中', '洽谈中', '待开发', '不合作'])
        ui.comboBox_3.addItems(['洽谈', '拿样', '采购', '拜访', '投诉'])

def update_kehu(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "update kehu set 日期='{}',公司名='{}',采购账号='{}',对接人='{}',联系方式='{}',报价='{}',星级='{}',合作情况='{}',累计合作金额='{}',备注='{}',客户来源='{}' where id ='{}'"
    sql2 = sql.format(ui.lineEdit_27.text(),ui.lineEdit_19.text(),ui.lineEdit_21.text(),ui.lineEdit_20.text(),ui.lineEdit_22.text(),ui.lineEdit_17.text(),ui.comboBox_2.currentText(),ui.comboBox.currentText(),ui.lineEdit_23.text(),ui.lineEdit_18.text(),ui.lineEdit_26.text(),ui.lineEdit_24.text())
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"更新数据成功")

def update_gou(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "update goutong set 日期='{}',公司名='{}',联系账号='{}',对接人='{}',产品='{}',合作情况='{}',对接形式='{}',对接内容='{}',后续对接='{}' where id ='{}'"
    sql2 = sql.format(ui.lineEdit_27.text(),ui.lineEdit_19.text(),ui.lineEdit_21.text(),ui.lineEdit_20.text(),ui.lineEdit_25.text(), ui.comboBox.currentText() , ui.comboBox_3.currentText(),ui.lineEdit_28.text(),ui.lineEdit_29.text(),ui.lineEdit_24.text())
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"更新数据成功")

def delete_kehu(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "delete from kehu where id ='{}'"
    sql2 = sql.format(str(ui.lineEdit_24.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"删除数据成功")

def delete_gou(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "delete from goutong where id ='{}'"
    sql2 = sql.format(str(ui.lineEdit_24.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示', "删除数据成功")

def clean_kehu(self):
    if ui.radioButton.isChecked() == False:
        ui.lineEdit_19.setText('')
    if ui.radioButton_2.isChecked() == False:
        ui.lineEdit_20.setText('')
    if ui.radioButton_3.isChecked() == False:
        ui.lineEdit_21.setText('')
    ui.lineEdit_22.setText('')
    ui.lineEdit_17.setText('')
    ui.lineEdit_18.setText('')
    ui.lineEdit_23.setText('')
    ui.lineEdit_24.setText('')
    ui.lineEdit_28.setText('')
    ui.lineEdit_29.setText('')
    ui.lineEdit_25.setText('')
    ui.lineEdit_26.setText('')
    ui.radioButton.setChecked(False)
    ui.radioButton_2.setChecked(False)
    ui.radioButton_3.setChecked(False)

def insert_kehu(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "INSERT INTO kehu(日期,公司名,采购账号,对接人,联系方式,报价,星级,合作情况,备注,客户来源) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
    % (ui.lineEdit_27.text(),ui.lineEdit_19.text(),ui.lineEdit_21.text(),ui.lineEdit_20.text(),ui.lineEdit_22.text(),ui.lineEdit_17.text(),ui.comboBox_2.currentText(),ui.comboBox.currentText(),ui.lineEdit_18.text(),ui.lineEdit_26.text())
    cur.execute(sql)
    conn.commit()
    tkinter.messagebox.showinfo('提示', "插入数据成功")

def insert_gou(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "INSERT INTO goutong(日期,公司名,联系账号,对接人,产品,合作情况,对接形式,对接内容,后续对接) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
    % (ui.lineEdit_27.text(),ui.lineEdit_19.text(),ui.lineEdit_21.text(),ui.lineEdit_20.text(),ui.lineEdit_25.text(),ui.comboBox.currentText(),ui.comboBox_3.currentText(),ui.lineEdit_28.text(),ui.lineEdit_29.text())
    cur.execute(sql)
    conn.commit()
    tkinter.messagebox.showinfo('提示', "插入数据成功")

def allinsert_kehu(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    df=pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx',sheet_name='客户'))
    cur = conn.cursor()
    for i in range(0,len(df)):
        sql = "INSERT INTO kehu(公司名,采购账号,对接人,联系方式,报价,星级,合作情况,累计合作金额,备注) VALUES ('%s','%s','%s','%s','%s','%s','%s',%s,'%s')" \
        % (df.at[i,'公司名'], df.at[i,'采购账号'], df.at[i,'对接人'], df.at[i,'联系方式'],df.at[i,'报价'], df.at[i,'星级'],df.at[i,'合作情况'], df.at[i,'累计合作金额'], df.at[i,'备注'])
        cur.execute(sql)
        conn.commit()
    tkinter.messagebox.showinfo('提示', "批量插入数据成功")

def allinsert_gou(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    df = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx', sheet_name='对接'))
    df['日期'] = pd.to_datetime(df['日期'])
    cur = conn.cursor()
    for i in range(0, len(df)):
        sql = "INSERT INTO goutong(日期,公司名,联系账号,对接人,产品,对接形式,对接内容,后续对接) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')" \
              % (df.at[i, '日期'], df.at[i, '公司名'], df.at[i, '联系账号'], df.at[i, '对接人'], df.at[i, '产品'], df.at[i, '对接形式'],
                 df.at[i, '对接内容'], df.at[i, '后续对接'])
        cur.execute(sql)
        conn.commit()
    tkinter.messagebox.showinfo('提示', "批量插入数据成功")

def show_shuju(self):
    cp =configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    if ui.lineEdit_40.text() != '':
        sql = "select * from shuju where id = '{}'"
        sql = sql.format(str(ui.lineEdit_40.text()))
    else:
        sql = "select * from shuju order by id desc"
    ds = pd.DataFrame(pd.read_sql(sql, conn))
    model = QStandardItemModel()
    for i in range(0, int(ds.shape[1])):
        model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
        for j in range(0, int(ds.shape[0]) ):
            model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
    ui.tableView_4.setModel(model)
    ui.tableView_4.setColumnWidth(0, 100)
    ui.tableView_4.setColumnWidth(1, 70)
    ui.tableView_4.setColumnWidth(2, 70)
    ui.tableView_4.setColumnWidth(3, 70)
    ui.tableView_4.setColumnWidth(4, 70)
    ui.tableView_4.setColumnWidth(5, 70)
    ui.tableView_4.setColumnWidth(6, 70)
    ui.tableView_4.setColumnWidth(7, 70)
    ui.lineEdit_30.setText(str(ds.iat[0, 2]))
    ui.lineEdit_31.setText(str(ds.iat[0, 3]))
    ui.lineEdit_32.setText(str(ds.iat[0, 4]))
    ui.lineEdit_33.setText(str(ds.iat[0, 5]))
    ui.lineEdit_34.setText(str(ds.iat[0, 6]))
    ui.lineEdit_35.setText(str(ds.iat[0, 7]))
    ui.lineEdit_37.setText(str(ds.iat[0, 8]))

def show_pa(self):
    cp =configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    sql = "select * from keyword order by id desc"
    ds = pd.DataFrame(pd.read_sql(sql, conn))
    model = QStandardItemModel()
    for i in range(0, int(ds.shape[1])):
        model.setHorizontalHeaderItem(i, QtGui.QStandardItem(ds.columns[i]))
        for j in range(0, int(ds.shape[0]) ):
            model.setItem(j, i, QtGui.QStandardItem(str(ds.iat[j, i])))
    ui.tableView_4.setModel(model)

def insert_shuju(self):
    cp =configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    if ui.lineEdit_39.text() != '':
        now = ui.lineEdit_39.text()
    sql = "INSERT INTO shuju(日期, 展现量, 访客量, 浏览量, 询盘量,下单量,金额,数据分析,对策调整) VALUES ('%s',%s,%s,%s,%s,%s,%s,'%s','%s')" % (
    now, int(ui.lineEdit_30.text()), int(ui.lineEdit_31.text()), int(ui.lineEdit_32.text()),int(ui.lineEdit_33.text()),int(ui.lineEdit_34.text()),int(ui.lineEdit_35.text()),ui.lineEdit_37.text(),ui.lineEdit_38.text())
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"插入数据成功")

def update_shuju(self):
    cp =configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "update shuju set 日期='{}',展现量='{}', 访客量='{}',浏览量='{}',询盘量='{}',下单量='{}',金额='{}',数据分析='{}',对策调整='{}'where id ='{}'"
    sql2 = sql.format(ui.lineEdit_39.text(),ui.lineEdit_30.text(),ui.lineEdit_31.text(),ui.lineEdit_32.text(),ui.lineEdit_33.text(),ui.lineEdit_34.text(),ui.lineEdit_35.text(),ui.lineEdit_37.text(),ui.lineEdit_38.text(),str(ui.lineEdit_40.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"更新数据成功")

def delete_shuju(self):
    cp =configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    sql = "delete from shuju where id ='{}'"
    sql2 = sql.format(str(ui.lineEdit_40.text()))
    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示',"删除数据成功")

def clean_shuju(self):
    ui.lineEdit_30.setText("")
    ui.lineEdit_31.setText("")
    ui.lineEdit_32.setText("")
    ui.lineEdit_33.setText("")
    ui.lineEdit_34.setText("")
    ui.lineEdit_35.setText("")
    ui.lineEdit_37.setText("")
    ui.lineEdit_38.setText("")

def get_pa(self):
    now = datetime.datetime.now()
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    cur = conn.cursor()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
    def get_page(url):
        try:
            r = requests.get(url, headers=headers)
            r.raise_for_status()
            r.encoding = 'utf-8'
            return r.text
        except Exception as e:
            print(e)
    shu = []
    lose = []
    df = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx', sheet_name='爬虫'))
    for k in range(0, len(df)):
        num1 = 1
        go = 0
        i = int(ui.lineEdit_36.text())
        lose1 = 0
        for pa in range(1, i):  # i代表第几页
            if go == 1:
                break
            for index in range(0, 60, 20):
                # 每个网页的通用表达，将page的内容补入{}中
                if go == 1:
                    break
                url = df.at[k, 'url'].format(pa, index)
                print(df.at[k, '关键词'] + str(pa) + '页**' + str(index) + '参数正在处理中')
                name = []  # 创建数组，存储企业名称
                tile = []
                page = get_page(url)
                name = re.findall(r'hoverName":"(.*?)"', page)
                title = re.findall(r'simpleSubject":"(.*?)"', page)
                for num in range(0, len(name)):
                    shu.append([num1, name[num], title[num], df.at[k, '商品']])
                    if df.at[k, '公司名'] == name[num]:
                        sql = "INSERT INTO keyword(日期, 店铺, 关键词, 排名, 商品) VALUES ('%s', '%s',  '%s',  %s,  '%s')" % (
                        now, df.at[k, '简称'], df.at[k, '关键词'], num1, df.at[k, '商品'])
                        cur.execute(sql)
                        conn.commit()
                        go = 1
                    else:
                        lose1 = lose1 + 2
                    num1 = num1 + 1
                time.sleep(np.random.uniform(2, 4))
        if lose1 == (i - 1) * 3 * 40:
            lose.append([df.at[k, '关键词'], df.at[k, '公司名'], 0, '无'])
            sql = "INSERT INTO keyword(日期, 店铺, 关键词, 排名, 商品) VALUES ('%s', '%s',  '%s',  %s,  '%s')" % (
            now, df.at[k, '简称'], df.at[k, '关键词'], 0, '无')
            cur.execute(sql)
            conn.commit()
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo("提示", "数据已抓取")

def allinsert_shuju(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    k = 'C:\\Users\\Administrator\\Desktop\\1688.xls'
    df = pd.DataFrame(pd.read_excel(k, converters={'订单编号': str, 'Offer ID': str, 'SKU ID': str, '关联编号': str}))
    df['货号'] = df['货号'].str.replace('XME/XMB/XMF/XMA', 'XMX')
    df['货号'] = df['货号'].str.replace('小号', 'XMB')
    str2 = ":"
    str3 = "（"
    for i in range(0, len(df)):
        try:
            try:
                df.at[i, '货号'] = df.at[i, '货品标题'][df.at[i, '货品标题'].index(str2) + 2:df.at[i, '货品标题'].index(str3)]
            except:
                df.at[i, '货号'] = df.at[i, '货品标题'][df.at[i, '货品标题'].index(str2) + 2:]
            else:
                df.at[i, '货号'] = df.at[i, '货品标题'][df.at[i, '货品标题'].index(str2) + 2:df.at[i, '货品标题'].index(str3)]
        except:
            df.at[i, '货号'] = df.at[i, '货号']

    for i in range(0, df.shape[0]):
        if pd.isnull(df.at[i, '订单编号']) & pd.isnull(df.at[i, '买家公司名']) & pd.isnull(df.at[i, '买家会员名']) & pd.isnull(
                df.at[i, '卖家公司名']):
            df.at[i, '订单编号'] = df.at[i - 1, '订单编号']
            df.at[i, '买家公司名'] = df.at[i - 1, '买家公司名']
            df.at[i, '买家会员名'] = df.at[i - 1, '买家会员名']
            df.at[i, '卖家公司名'] = df.at[i - 1, '卖家公司名']
            df.at[i, '卖家会员名'] = df.at[i - 1, '卖家会员名']
            df.at[i, '订单状态'] = df.at[i - 1, '订单状态']
            df.at[i, '订单创建时间'] = df.at[i - 1, '订单创建时间']
            df.at[i, '订单付款时间'] = df.at[i - 1, '订单付款时间']
            df.at[i, '发货方'] = df.at[i - 1, '发货方']
            df.at[i, '收货人姓名'] = df.at[i - 1, '收货人姓名']
            df.at[i, '收货地址'] = df.at[i - 1, '收货地址']
            df.at[i, '邮编'] = df.at[i - 1, '邮编']
            df.at[i, '联系手机'] = df.at[i - 1, '联系手机']
            df.at[i, '物流公司运单号'] = df.at[i - 1, '物流公司运单号']
    for i in range(0, df.shape[0] - 1):
        if pd.isnull(df.at[i, '买家公司名']):
            df.at[i, '买家公司名'] = df.at[i, '买家会员名']
    df = df.drop(['联系电话', '物料编号', '单品货号', '发票：购货单位名称', '发票：纳税人识别号', '发票：地址、电话', '发票：开户行及账号', '发票收取地址',
                  '关联编号', '代理商姓名', '代理商联系方式', '是否代发订单', '代发服务商id', '下单公司主体', '业务员昵称'], axis=1)
    df['订单付款时间'].fillna('1800/01/01 00:00:00', inplace=True)
    df['订单创建时间'] = pd.to_datetime(df['订单创建时间'])
    df['订单付款时间'] = pd.to_datetime(df['订单付款时间'])
    df['货品总价(元)'].fillna(0, inplace=True)
    df['运费(元)'].fillna(0, inplace=True)
    df['实付款(元)'].fillna(0, inplace=True)
    df['数量'].fillna(0, inplace=True)
    df['单价(元)'].fillna(0, inplace=True)
    df['邮编'].fillna(0, inplace=True)
    df['联系手机'].fillna(0, inplace=True)
    n1 = 0
    # 插入数据
    cur = conn.cursor()
    for i in range(0, len(df)):
        sql2 = "INSERT INTO dingdan(订单编号,买家公司名,买家会员名,卖家公司名,卖家会员名,货品总价,运费,涨价或折扣,实付款,订单状态,发货方,收货人姓名,收货地址,邮编,联系手机,货品标题,单价,数量,单位,货号,型号,OfferID,SKUID,货品种类,买家留言,物流公司运单号,订单创建时间,订单付款时间) VALUES ('%s','%s','%s','%s','%s',%s,%s,'%s',%s,'%s','%s','%s','%s','%s','%s','%s',%s,%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
               % (df.at[i, '订单编号'], df.at[i, '买家公司名'], df.at[i, '买家会员名'], df.at[i, '卖家公司名'], df.at[i, '卖家会员名'],
                  df.at[i, '货品总价(元)'],
                  df.at[i, '运费(元)'], df.at[i, '涨价或折扣(元)'], df.at[i, '实付款(元)'], df.at[i, '订单状态'], df.at[i, '发货方'],
                  df.at[i, '收货人姓名'], df.at[i, '收货地址'], df.at[i, '邮编'], df.at[i, '联系手机'], df.at[i, '货品标题'],
                  df.at[i, '单价(元)'],
                  df.at[i, '数量'], df.at[i, '单位'], df.at[i, '货号'], df.at[i, '型号'], df.at[i, 'Offer ID'],
                  df.at[i, 'SKU ID'], df.at[i, '货品种类'],
                  df.at[i, '买家留言'], df.at[i, '物流公司运单号'], df.at[i, '订单创建时间'], df.at[i, '订单付款时间'])
        cur.execute(sql2)
        conn.commit()
        n1 += 1
    # 更新库存
    df2 = df[(df.订单状态 != '交易关闭')]
    df2 = pd.DataFrame(df2.groupby('货号', as_index=False).agg({'实付款(元)': sum, '数量': sum, '运费(元)': len}))
    df2.sort_values(["数量"], ascending=False, inplace=True)
    df2.reset_index(drop=True, inplace=True)
    n2 = 0
    cur = conn.cursor()
    for i in range(0, len(df2)):
        no = df2.at[i, '货号']
        sql = "select * from shangpin where SKU like '%{}%'"
        sql2 = sql.format(no)
        cur.execute(sql2)
        result = cur.fetchone()
        if result is not None:
            if result[0] is not None:
                num = result[5] - df2.at[i, '数量']
                sql = "update shangpin set stock={} where SKU like '%{}%'"
                sql2 = sql.format(num, no)
                cur.execute(sql2)
                conn.commit()
                n2 += 1
        else:
            tkinter.messagebox.showinfo("提示不存在", df2.at[i, '货号'])
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo("提示", '成功插入数据')

def check_shuju(self):
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    sql = "select * from dingdan order by 订单创建时间 desc"
    df = pd.DataFrame(pd.read_sql(sql, conn))
    k = 'C:\\Users\\Administrator\\Desktop\\订单校对.xls'
    ds = pd.DataFrame(pd.read_excel(k, converters={'订单编号': str, 'Offer ID': str, 'SKU ID': str, '关联编号': str}))

    for i in range(0, ds.shape[0]):
        if pd.isnull(ds.at[i, '订单编号']) & pd.isnull(ds.at[i, '买家公司名']) & pd.isnull(ds.at[i, '买家会员名']) & pd.isnull(
                ds.at[i, '卖家公司名']):
            ds.at[i, '订单编号'] = ds.at[i - 1, '订单编号']
            ds.at[i, '订单状态'] = ds.at[i - 1, '订单状态']
    ds2 = ds.loc[:, ['订单编号', '订单状态']]
    ds2 = ds2[(ds2.订单状态 == '交易关闭')]
    k = 0
    ds2.reset_index(drop=True, inplace=True)
    cur = conn.cursor()
    for i in range(0, len(ds2)):
        no = ds2.at[i, '订单编号']
        sql = "select * from dingdan where 订单编号 like '%{}%'"
        sql2 = sql.format(no)
        cur.execute(sql2)
        result = cur.fetchone()
        if result is not None:
            if result[0] is not None:
                num = ds2.at[i, '订单状态']
                if ds2.at[i, '订单状态'] != result[9]:
                    sql = "update dingdan set 订单状态='{}' where 订单编号 like '%{}%'"
                    sql2 = sql.format(num, no)
                    cur.execute(sql2)
                    conn.commit()
                    k += 1
                    print('订单号' + no)
                    print('数据库原状态' + result[9])
                    print('后台新状态' + num)
    tkinter.messagebox.showinfo("更新数据", str(k) + '条')

def show_tu(self):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    name = '美合'
    cp = configparser.ConfigParser()
    cp.read('D:\配置\config.ini',encoding='utf-8')
    host1 = cp.get('sql_connect', 'host')
    user1 = cp.get('sql_connect', 'user')
    passwd1 = cp.get('sql_connect', 'passwd')
    db1 = cp.get('sql_connect', 'db')
    num = cp.get('keywords', 'number')
    conn = pymssql.connect(server=host1, user=user1, password=passwd1, database=db1)
    sql = "select * from shuju order by id desc"
    df = pd.DataFrame(pd.read_sql(sql, conn))
    df2 = df[df['店铺'] == name].sort_values(["日期"], ascending=True, axis=0)
    df2['日期'] = pd.to_datetime(df2['日期'])
    now = datetime.datetime.now()
    now = datetime.datetime.strftime(now, '%Y-%m-%d')
    now = datetime.datetime.strptime(now, '%Y-%m-%d')
    #15天店铺展现量图表展示
    df3 = df2[df2['日期'] > now - datetime.timedelta(days=15)]  ##界定数据的日期，展现量
    df33 = df3.sort_values(["展现量"], ascending=True, axis=0)
    df3.insert(1, '低四分位', value=df33['展现量'].quantile(q=0.25))
    df3.insert(1, '中位数', value=df33['展现量'].quantile(q=0.5))
    df3.insert(1, '高四分位', value=df33['展现量'].quantile(q=0.75))
    df3['日期'] = df3['日期'].apply(lambda x: datetime.datetime.strftime(x, "%m.%d"))
    F = MyFigure(width=3, height=2, dpi=100)
    F.axes1 = F.fig.add_subplot(111)
    tick_spacing = 3# 通过修改tick_spacing的值可以修改x轴的密度
    F.axes1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for a, b in zip(df3['日期'], df3['展现量']):
        F.axes1.text(a, b + 0.001, '%.0f' % b, ha='center', va='bottom', fontsize=12)
    F.axes1.plot(df3['日期'], df3['展现量'], '-')
    F.axes1.plot(df3['日期'], df3['低四分位'], '-')
    F.axes1.plot(df3['日期'], df3['中位数'], '-')
    F.axes1.plot(df3['日期'], df3['高四分位'], '-')
    # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
    gridlayout = QGridLayout(ui.groupBox)  # 继承容器groupBox
    gridlayout.addWidget(F, 0, 1)
    F.fig.suptitle("15天店铺展现量")
    # 15天店铺访客量图表展示
    df3 = df2[df2['日期'] > now - datetime.timedelta(days=15)]  ##界定数据的日期，展现量
    df33 = df3.sort_values(["访客量"], ascending=True, axis=0)
    df3.insert(1, '低四分位', value=df33['访客量'].quantile(q=0.25))
    df3.insert(1, '中位数', value=df33['访客量'].quantile(q=0.5))
    df3.insert(1, '高四分位', value=df33['访客量'].quantile(q=0.75))
    df3['日期'] = df3['日期'].apply(lambda x: datetime.datetime.strftime(x, "%m.%d"))
    F = MyFigure(width=3, height=2, dpi=100)
    F.axes1 = F.fig.add_subplot(111)
    tick_spacing = 3# 通过修改tick_spacing的值可以修改x轴的密度
    F.axes1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for a, b in zip(df3['日期'], df3['访客量']):
        F.axes1.text(a, b + 0.001, '%.0f' % b, ha='center', va='bottom', fontsize=12)
    F.axes1.plot(df3['日期'], df3['访客量'], '-')
    F.axes1.plot(df3['日期'], df3['低四分位'], '-')
    F.axes1.plot(df3['日期'], df3['中位数'], '-')
    F.axes1.plot(df3['日期'], df3['高四分位'], '-')
    # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
    gridlayout = QGridLayout(ui.groupBox_2)  # 继承容器groupBox
    gridlayout.addWidget(F, 0, 1)
    F.fig.suptitle("15天店铺访客量")
    # 15天店铺金额图表展示
    df3 = df2[df2['日期'] > now - datetime.timedelta(days=15)]  ##界定数据的日期，展现量
    df33 = df3.sort_values(["金额"], ascending=True, axis=0)
    df3.insert(1, '低四分位', value=df33['金额'].quantile(q=0.25))
    df3.insert(1, '中位数', value=df33['金额'].quantile(q=0.5))
    df3.insert(1, '高四分位', value=df33['金额'].quantile(q=0.75))
    df3['日期'] = df3['日期'].apply(lambda x: datetime.datetime.strftime(x, "%m.%d"))
    F = MyFigure(width=3, height=2, dpi=100)
    F.axes1 = F.fig.add_subplot(111)
    tick_spacing = 3  # 通过修改tick_spacing的值可以修改x轴的密度
    F.axes1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for a, b in zip(df3['日期'], df3['金额']):
        F.axes1.text(a, b + 0.001, '%.0f' % b, ha='center', va='bottom', fontsize=12)
    F.axes1.plot(df3['日期'], df3['金额'], '-')
    F.axes1.plot(df3['日期'], df3['低四分位'], '-')
    F.axes1.plot(df3['日期'], df3['中位数'], '-')
    F.axes1.plot(df3['日期'], df3['高四分位'], '-')
    # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
    gridlayout = QGridLayout(ui.groupBox_3)  # 继承容器groupBox
    gridlayout.addWidget(F, 0, 1)
    F.fig.suptitle("15天店铺金额")

    # 15天店铺关键词排名图表展示
    sql2 = "select * from keyword order by id desc"
    ds = pd.DataFrame(pd.read_sql(sql2, conn))
    ds['关键词'] = ds['关键词'].str.strip()
    ds['店铺'] = ds['店铺'].str.strip()
    ds['日期'] = pd.to_datetime(ds['日期'])
    df = pd.DataFrame(pd.read_excel('D:\配置\配置.xlsx', sheet_name='爬虫'))
    date = 15
    F = MyFigure(width=3, height=2, dpi=100)
    keywords = []
    for i in range(0, int(num)):
        now = datetime.datetime.now()
        ds2 = ds[(ds['店铺'] == df.at[i,'简称']) & (ds['关键词'] == df.at[i,'关键词'])].sort_values(["日期"], ascending=True, axis=0)
        keywords.append(df.at[i,'关键词'])
        ds3 = ds2[ds2['日期'] > now - datetime.timedelta(days=date)]  #界定数据的日期
        F.axes1 = F.fig.add_subplot(111)
        tick_spacing = 3 # 通过修改tick_spacing的值可以修改x轴的密度
        F.axes1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ds3['日期'] = ds3['日期'].apply(lambda x: datetime.datetime.strftime(x, "%m.%d"))  #有问题，需要后期优化

        F.axes1.plot(ds3['日期'], ds3['排名'], '-')
        for a, b in zip(ds3['日期'], ds3['排名']):
            F.axes1.text(a, b + 0.001, '%.0f' % b, ha='center', va='bottom', fontsize=12)
    # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
    gridlayout = QGridLayout(ui.groupBox_4)  # 继承容器groupBox
    gridlayout.addWidget(F, 0, 1)
    F.fig.suptitle("15天关键词排名")
    F.axes1.legend(keywords, loc='upper left', fontsize=5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    cb = ui.comboBox
    cb.addItems(['合作中', '洽谈中', '待开发','不合作'])
    cb2 = ui.comboBox_2
    cb2.addItems(['1星', '2星', '3星','4星','5星'])
    cb3 = ui.comboBox_3
    cb3.addItems(['洽谈', '拿样', '采购','拜访','投诉'])
    ui.lineEdit_5.setText('0')
    ui.lineEdit_6.setText('0')
    ui.lineEdit_23.setText('0')
    ui.lineEdit_27.setText(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'))
    ui.lineEdit_36.setText('10')
    now = datetime.datetime.now() - datetime.timedelta(days=1)
    now = datetime.datetime.strftime(now, '%Y-%m-%d')
    ui.lineEdit_39.setText(now)
    btn1 = ui.pushButton
    btn1.clicked.connect(clean_shangpin)
    btn2 = ui.pushButton_2
    btn2.clicked.connect(clean_shengchan)
    btn6 = ui.pushButton_6
    btn6.clicked.connect(delete_shangpin)
    btn7 = ui.pushButton_7
    btn7.clicked.connect(update_shangpin)
    btn8 = ui.pushButton_8
    btn8.clicked.connect(insert_shangpin)
    btn9 = ui.pushButton_9
    btn9.clicked.connect(show_shangpin)
    btn10 = ui.pushButton_10
    btn10.clicked.connect(show_shengchan)
    btn11 = ui.pushButton_11
    btn11.clicked.connect(Warehousing_shangpin)
    btn12 = ui.pushButton_12
    btn12.clicked.connect(correcting_shangpin)
    btn13 = ui.pushButton_13
    btn13.clicked.connect(insert_shengchan)
    btn14= ui.pushButton_14
    btn14.clicked.connect(update_shengchan)
    btn15= ui.pushButton_15
    btn15.clicked.connect(delete_shengchan)
    btn16= ui.pushButton_16
    btn16.clicked.connect(import_shengchan)

    btn3 = ui.pushButton_3
    btn3.clicked.connect(insert_kehu)
    btn4 = ui.pushButton_4
    btn4.clicked.connect(show_kehu)
    btn5 = ui.pushButton_5
    btn5.clicked.connect(update_kehu)
    btn18 = ui.pushButton_18
    btn18.clicked.connect(allinsert_kehu)
    btn17 = ui.pushButton_17
    btn17.clicked.connect(delete_kehu)
    btn19 = ui.pushButton_19
    btn19.clicked.connect(clean_kehu)
    btn20 = ui.pushButton_20
    btn20.clicked.connect(show_gou)
    btn21 = ui.pushButton_21
    btn21.clicked.connect(insert_gou)
    btn22 = ui.pushButton_22
    btn22.clicked.connect(update_gou)
    btn23 = ui.pushButton_23
    btn23.clicked.connect(delete_gou)
    btn24 = ui.pushButton_24
    btn24.clicked.connect(allinsert_gou)

    btn26 = ui.pushButton_26
    btn26.clicked.connect(check_shuju)
    btn27 = ui.pushButton_27
    btn27.clicked.connect(allinsert_shuju)
    btn28 = ui.pushButton_28
    btn28.clicked.connect(show_pa)
    btn29 = ui.pushButton_29
    btn29.clicked.connect(get_pa)
    btn30 = ui.pushButton_30
    btn30.clicked.connect(show_shuju)
    btn31 = ui.pushButton_31
    btn31.clicked.connect(insert_shuju)
    btn32 = ui.pushButton_32
    btn32.clicked.connect(update_shuju)
    btn33 = ui.pushButton_33
    btn33.clicked.connect(clean_shuju)
    btn34 = ui.pushButton_34
    btn34.clicked.connect(delete_shuju)
    btn35 = ui.pushButton_35
    btn35.clicked.connect(show_tu)
    sys.exit(app.exec_())
