import math
import os
import socket
import statistics
import sys
import threading
import time
import csv
import asyncio
import websockets
import ssl
from datetime import datetime

import numpy as np
import pyqtgraph
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget
from serial import Serial


class form_class(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.splitter_27 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_27.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_27.setObjectName("splitter_27")
        self.plot = PlotWidget(self.splitter_27)
        self.plot.setMinimumSize(QtCore.QSize(906, 702))
        self.plot.setStyleSheet("border-color: rgb(170, 170, 170);\n"
                                "border-style: solid;\n"
                                "border-width: 1px;")
        self.plot.setInteractive(False)
        self.plot.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.plot.setObjectName("plot")
        self.splitter_26 = QtWidgets.QSplitter(self.splitter_27)
        self.splitter_26.setOrientation(QtCore.Qt.Vertical)
        self.splitter_26.setObjectName("splitter_26")
        self.splitter_19 = QtWidgets.QSplitter(self.splitter_26)
        self.splitter_19.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_19.setObjectName("splitter_19")
        self.splitter_18 = QtWidgets.QSplitter(self.splitter_19)
        self.splitter_18.setMinimumSize(QtCore.QSize(171, 51))
        self.splitter_18.setMaximumSize(QtCore.QSize(171, 51))
        self.splitter_18.setOrientation(QtCore.Qt.Vertical)
        self.splitter_18.setObjectName("splitter_18")
        self.splitter = QtWidgets.QSplitter(self.splitter_18)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMinimumSize(QtCore.QSize(112, 21))
        self.label.setMaximumSize(QtCore.QSize(112, 21))
        self.label.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label.setObjectName("label")
        self.ePort = QtWidgets.QLineEdit(self.splitter)
        self.ePort.setMinimumSize(QtCore.QSize(54, 21))
        self.ePort.setMaximumSize(QtCore.QSize(54, 21))
        self.ePort.setAlignment(QtCore.Qt.AlignCenter)
        self.ePort.setObjectName("ePort")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_18)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.eCon = QtWidgets.QPushButton(self.splitter_2)
        self.eCon.setMinimumSize(QtCore.QSize(83, 25))
        self.eCon.setMaximumSize(QtCore.QSize(83, 25))
        self.eCon.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.eCon.setObjectName("eCon")
        self.eDis = QtWidgets.QPushButton(self.splitter_2)
        self.eDis.setMinimumSize(QtCore.QSize(83, 25))
        self.eDis.setMaximumSize(QtCore.QSize(83, 25))
        self.eDis.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.eDis.setObjectName("eDis")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_19)
        self.groupBox.setMinimumSize(QtCore.QSize(175, 51))
        self.groupBox.setMaximumSize(QtCore.QSize(175, 51))
        self.groupBox.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.e1 = QtWidgets.QRadioButton(self.groupBox)
        self.e1.setMinimumSize(QtCore.QSize(75, 17))
        self.e1.setMaximumSize(QtCore.QSize(75, 17))
        self.e1.setChecked(True)
        self.e1.setObjectName("e1")
        self.gridLayout.addWidget(self.e1, 0, 0, 1, 1)
        self.e0 = QtWidgets.QRadioButton(self.groupBox)
        self.e0.setMinimumSize(QtCore.QSize(74, 17))
        self.e0.setMaximumSize(QtCore.QSize(74, 17))
        self.e0.setObjectName("e0")
        self.gridLayout.addWidget(self.e0, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.splitter_26)
        self.line.setMinimumSize(QtCore.QSize(351, 5))
        self.line.setMaximumSize(QtCore.QSize(351, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_17 = QtWidgets.QSplitter(self.splitter_26)
        self.splitter_17.setMinimumSize(QtCore.QSize(351, 111))
        self.splitter_17.setMaximumSize(QtCore.QSize(351, 115))
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName("splitter_17")
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_15.setMinimumSize(QtCore.QSize(351, 51))
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_11.setMinimumSize(QtCore.QSize(171, 51))
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName("splitter_11")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_2 = QtWidgets.QLabel(self.splitter_5)
        self.label_2.setMinimumSize(QtCore.QSize(113, 23))
        self.label_2.setMaximumSize(QtCore.QSize(113, 23))
        self.label_2.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.hl1 = QtWidgets.QLabel(self.splitter_5)
        self.hl1.setMinimumSize(QtCore.QSize(55, 23))
        self.hl1.setMaximumSize(QtCore.QSize(55, 23))
        self.hl1.setStyleSheet("font: bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.hl1.setObjectName("hl1")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.hc1 = QtWidgets.QPushButton(self.splitter_3)
        self.hc1.setMinimumSize(QtCore.QSize(84, 27))
        self.hc1.setMaximumSize(QtCore.QSize(84, 27))
        self.hc1.setStyleSheet("")
        self.hc1.setText("")
        self.hc1.setFlat(False)
        self.hc1.setObjectName("hc1")
        self.hd1 = QtWidgets.QPushButton(self.splitter_3)
        self.hd1.setMinimumSize(QtCore.QSize(84, 27))
        self.hd1.setMaximumSize(QtCore.QSize(84, 27))
        self.hd1.setStyleSheet("")
        self.hd1.setText("")
        self.hd1.setObjectName("hd1")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_15)
        self.splitter_14.setMinimumSize(QtCore.QSize(171, 51))
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_3 = QtWidgets.QLabel(self.splitter_6)
        self.label_3.setMinimumSize(QtCore.QSize(113, 23))
        self.label_3.setMaximumSize(QtCore.QSize(113, 23))
        self.label_3.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_3.setObjectName("label_3")
        self.hl2 = QtWidgets.QLabel(self.splitter_6)
        self.hl2.setMinimumSize(QtCore.QSize(55, 23))
        self.hl2.setMaximumSize(QtCore.QSize(55, 23))
        self.hl2.setStyleSheet("font: bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.hl2.setObjectName("hl2")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_14)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.hc2 = QtWidgets.QPushButton(self.splitter_4)
        self.hc2.setMinimumSize(QtCore.QSize(84, 27))
        self.hc2.setMaximumSize(QtCore.QSize(84, 27))
        self.hc2.setStyleSheet("")
        self.hc2.setText("")
        self.hc2.setObjectName("hc2")
        self.hd2 = QtWidgets.QPushButton(self.splitter_4)
        self.hd2.setMinimumSize(QtCore.QSize(84, 27))
        self.hd2.setMaximumSize(QtCore.QSize(84, 27))
        self.hd2.setStyleSheet("")
        self.hd2.setText("")
        self.hd2.setObjectName("hd2")
        self.splitter_16 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_16.setMinimumSize(QtCore.QSize(351, 51))
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_12.setMinimumSize(QtCore.QSize(171, 51))
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_12)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_6 = QtWidgets.QLabel(self.splitter_8)
        self.label_6.setMinimumSize(QtCore.QSize(113, 23))
        self.label_6.setMaximumSize(QtCore.QSize(113, 23))
        self.label_6.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_6.setObjectName("label_6")
        self.hl3 = QtWidgets.QLabel(self.splitter_8)
        self.hl3.setMinimumSize(QtCore.QSize(55, 23))
        self.hl3.setMaximumSize(QtCore.QSize(55, 23))
        self.hl3.setStyleSheet("font: bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.hl3.setObjectName("hl3")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_12)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.hc3 = QtWidgets.QPushButton(self.splitter_7)
        self.hc3.setMinimumSize(QtCore.QSize(84, 27))
        self.hc3.setMaximumSize(QtCore.QSize(84, 27))
        self.hc3.setStyleSheet("")
        self.hc3.setText("")
        self.hc3.setObjectName("hc3")
        self.hd3 = QtWidgets.QPushButton(self.splitter_7)
        self.hd3.setMinimumSize(QtCore.QSize(84, 27))
        self.hd3.setMaximumSize(QtCore.QSize(84, 27))
        self.hd3.setStyleSheet("")
        self.hd3.setText("")
        self.hd3.setObjectName("hd3")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_13.setMinimumSize(QtCore.QSize(171, 51))
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.label_8 = QtWidgets.QLabel(self.splitter_10)
        self.label_8.setMinimumSize(QtCore.QSize(113, 23))
        self.label_8.setMaximumSize(QtCore.QSize(113, 23))
        self.label_8.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_8.setObjectName("label_8")
        self.hl4 = QtWidgets.QLabel(self.splitter_10)
        self.hl4.setMinimumSize(QtCore.QSize(55, 23))
        self.hl4.setMaximumSize(QtCore.QSize(55, 23))
        self.hl4.setStyleSheet("font: bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.hl4.setObjectName("hl4")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.hc4 = QtWidgets.QPushButton(self.splitter_9)
        self.hc4.setMinimumSize(QtCore.QSize(84, 27))
        self.hc4.setMaximumSize(QtCore.QSize(84, 27))
        self.hc4.setStyleSheet("")
        self.hc4.setText("")
        self.hc4.setObjectName("hc4")
        self.hd4 = QtWidgets.QPushButton(self.splitter_9)
        self.hd4.setMinimumSize(QtCore.QSize(84, 27))
        self.hd4.setMaximumSize(QtCore.QSize(84, 27))
        self.hd4.setStyleSheet("")
        self.hd4.setText("")
        self.hd4.setObjectName("hd4")
        self.line_2 = QtWidgets.QFrame(self.splitter_26)
        self.line_2.setMinimumSize(QtCore.QSize(351, 5))
        self.line_2.setMaximumSize(QtCore.QSize(351, 5))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.splitter_22 = QtWidgets.QSplitter(self.splitter_26)
        self.splitter_22.setMinimumSize(QtCore.QSize(351, 91))
        self.splitter_22.setMaximumSize(QtCore.QSize(351, 91))
        self.splitter_22.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_22.setObjectName("splitter_22")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_22)
        self.groupBox_2.setMinimumSize(QtCore.QSize(205, 91))
        self.groupBox_2.setMaximumSize(QtCore.QSize(205, 91))
        self.groupBox_2.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setMinimumSize(QtCore.QSize(16, 16))
        self.label_10.setMaximumSize(QtCore.QSize(16, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.xl = QtWidgets.QSlider(self.groupBox_2)
        self.xl.setMinimumSize(QtCore.QSize(106, 22))
        self.xl.setMaximumSize(QtCore.QSize(106, 22))
        self.xl.setMinimum(20)
        self.xl.setMaximum(1000)
        self.xl.setProperty("value", 50)
        self.xl.setOrientation(QtCore.Qt.Horizontal)
        self.xl.setObjectName("xl")
        self.gridLayout_3.addWidget(self.xl, 0, 1, 1, 1)
        self.xp = QtWidgets.QSpinBox(self.groupBox_2)
        self.xp.setMinimumSize(QtCore.QSize(51, 21))
        self.xp.setMaximumSize(QtCore.QSize(51, 21))
        self.xp.setAlignment(QtCore.Qt.AlignCenter)
        self.xp.setMinimum(20)
        self.xp.setMaximum(1000)
        self.xp.setProperty("value", 50)
        self.xp.setObjectName("xp")
        self.gridLayout_3.addWidget(self.xp, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setMinimumSize(QtCore.QSize(16, 16))
        self.label_11.setMaximumSize(QtCore.QSize(16, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.yl = QtWidgets.QSlider(self.groupBox_2)
        self.yl.setMinimumSize(QtCore.QSize(106, 22))
        self.yl.setMaximumSize(QtCore.QSize(106, 22))
        self.yl.setMaximum(9999)
        self.yl.setPageStep(10)
        self.yl.setProperty("value", 7000)
        self.yl.setOrientation(QtCore.Qt.Horizontal)
        self.yl.setObjectName("yl")
        self.gridLayout_3.addWidget(self.yl, 1, 1, 1, 1)
        self.yp = QtWidgets.QSpinBox(self.groupBox_2)
        self.yp.setMinimumSize(QtCore.QSize(51, 21))
        self.yp.setMaximumSize(QtCore.QSize(51, 21))
        self.yp.setAlignment(QtCore.Qt.AlignCenter)
        self.yp.setMinimum(20)
        self.yp.setMaximum(9999)
        self.yp.setProperty("value", 7000)
        self.yp.setObjectName("yp")
        self.gridLayout_3.addWidget(self.yp, 1, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_22)
        self.groupBox_3.setMinimumSize(QtCore.QSize(141, 91))
        self.groupBox_3.setMaximumSize(QtCore.QSize(141, 91))
        self.groupBox_3.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName("formLayout")
        self.F1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.F1.setMinimumSize(QtCore.QSize(48, 26))
        self.F1.setMaximumSize(QtCore.QSize(48, 26))
        self.F1.setChecked(True)
        self.F1.setObjectName("F1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.F1)
        self.F2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.F2.setMinimumSize(QtCore.QSize(70, 26))
        self.F2.setMaximumSize(QtCore.QSize(70, 26))
        self.F2.setObjectName("F2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.F2)
        self.F3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.F3.setMinimumSize(QtCore.QSize(48, 26))
        self.F3.setMaximumSize(QtCore.QSize(48, 26))
        self.F3.setObjectName("F3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.F3)
        self.F4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.F4.setMinimumSize(QtCore.QSize(70, 26))
        self.F4.setMaximumSize(QtCore.QSize(70, 26))
        self.F4.setObjectName("F4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.F4)
        self.splitter_24 = QtWidgets.QSplitter(self.splitter_26)
        self.splitter_24.setMinimumSize(QtCore.QSize(351, 91))
        self.splitter_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.splitter_24.setMidLineWidth(0)
        self.splitter_24.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_24.setObjectName("splitter_24")
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter_24)
        self.groupBox_4.setMinimumSize(QtCore.QSize(205, 91))
        self.groupBox_4.setMaximumSize(QtCore.QSize(205, 91))
        self.groupBox_4.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setMinimumSize(QtCore.QSize(35, 22))
        self.label_13.setMaximumSize(QtCore.QSize(35, 22))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setMinimumSize(QtCore.QSize(35, 22))
        self.label_12.setMaximumSize(QtCore.QSize(35, 22))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.tp = QtWidgets.QSpinBox(self.groupBox_4)
        self.tp.setMinimumSize(QtCore.QSize(51, 21))
        self.tp.setMaximumSize(QtCore.QSize(51, 21))
        self.tp.setAlignment(QtCore.Qt.AlignCenter)
        self.tp.setMinimum(0)
        self.tp.setMaximum(9999)
        self.tp.setProperty("value", 7000)
        self.tp.setObjectName("tp")
        self.gridLayout_4.addWidget(self.tp, 0, 2, 1, 1)
        self.rl = QtWidgets.QSlider(self.groupBox_4)
        self.rl.setMinimumSize(QtCore.QSize(87, 22))
        self.rl.setMaximumSize(QtCore.QSize(87, 22))
        self.rl.setMinimum(1)
        self.rl.setMaximum(99)
        self.rl.setOrientation(QtCore.Qt.Horizontal)
        self.rl.setObjectName("rl")
        self.gridLayout_4.addWidget(self.rl, 1, 1, 1, 1)
        self.tl = QtWidgets.QSlider(self.groupBox_4)
        self.tl.setMinimumSize(QtCore.QSize(87, 22))
        self.tl.setMaximumSize(QtCore.QSize(87, 22))
        self.tl.setMaximum(9999)
        self.tl.setProperty("value", 7000)
        self.tl.setOrientation(QtCore.Qt.Horizontal)
        self.tl.setObjectName("tl")
        self.gridLayout_4.addWidget(self.tl, 0, 1, 1, 1)
        self.rp = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.rp.setMinimumSize(QtCore.QSize(51, 21))
        self.rp.setMaximumSize(QtCore.QSize(51, 21))
        self.rp.setAlignment(QtCore.Qt.AlignCenter)
        self.rp.setDecimals(1)
        self.rp.setMinimum(0.1)
        self.rp.setProperty("value", 1.0)
        self.rp.setObjectName("rp")
        self.gridLayout_4.addWidget(self.rp, 1, 2, 1, 1)
        self.splitter_23 = QtWidgets.QSplitter(self.splitter_24)
        self.splitter_23.setMinimumSize(QtCore.QSize(141, 91))
        self.splitter_23.setMaximumSize(QtCore.QSize(141, 67))
        self.splitter_23.setOrientation(QtCore.Qt.Vertical)
        self.splitter_23.setObjectName("splitter_23")
        self.autos = QtWidgets.QPushButton(self.splitter_23)
        self.autos.setMinimumSize(QtCore.QSize(141, 31))
        self.autos.setMaximumSize(QtCore.QSize(141, 31))
        self.autos.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.autos.setObjectName("autos")
        self.autot = QtWidgets.QPushButton(self.splitter_23)
        self.autot.setMinimumSize(QtCore.QSize(141, 31))
        self.autot.setMaximumSize(QtCore.QSize(141, 31))
        self.autot.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.autot.setObjectName("autot")
        self.line_3 = QtWidgets.QFrame(self.splitter_26)
        self.line_3.setMinimumSize(QtCore.QSize(351, 5))
        self.line_3.setMaximumSize(QtCore.QSize(351, 5))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.splitter_25 = QtWidgets.QSplitter(self.splitter_26)
        self.splitter_25.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_25.setObjectName("splitter_25")
        self.label_14 = QtWidgets.QLabel(self.splitter_25)
        self.label_14.setMinimumSize(QtCore.QSize(83, 26))
        self.label_14.setMaximumSize(QtCore.QSize(83, 26))
        self.label_14.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_14.setObjectName("label_14")
        self.rlabel = QtWidgets.QLabel(self.splitter_25)
        self.rlabel.setMinimumSize(QtCore.QSize(83, 26))
        self.rlabel.setMaximumSize(QtCore.QSize(83, 26))
        self.rlabel.setStyleSheet("font: bold 9pt \"Consolas\";\n"
                                  "color: rgb(0, 0, 255);")
        self.rlabel.setObjectName("rlabel")
        self.rstart = QtWidgets.QPushButton(self.splitter_25)
        self.rstart.setMinimumSize(QtCore.QSize(84, 26))
        self.rstart.setMaximumSize(QtCore.QSize(84, 26))
        self.rstart.setStyleSheet("")
        self.rstart.setObjectName("rstart")
        self.rstop = QtWidgets.QPushButton(self.splitter_25)
        self.rstop.setMinimumSize(QtCore.QSize(84, 26))
        self.rstop.setMaximumSize(QtCore.QSize(84, 26))
        self.rstop.setStyleSheet("")
        self.rstop.setObjectName("rstop")
        self.label_16 = QtWidgets.QLabel(self.splitter_26)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.splitter_27, 0, 0, 1, 1)

        self.hc1.setStyleSheet("image : url(./resource/link.png);")
        self.hd1.setStyleSheet("image : url(./resource/unlink.png);")
        self.hc2.setStyleSheet("image : url(./resource/link.png);")
        self.hd2.setStyleSheet("image : url(./resource/unlink.png);")
        self.hc3.setStyleSheet("image : url(./resource/link.png);")
        self.hd3.setStyleSheet("image : url(./resource/unlink.png);")
        self.hc4.setStyleSheet("image : url(./resource/link.png);")
        self.hd4.setStyleSheet("image : url(./resource/unlink.png);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EMG Sensor Port "))
        self.ePort.setText(_translate("MainWindow", "3"))
        self.eCon.setText(_translate("MainWindow", "Start"))
        self.eDis.setText(_translate("MainWindow", "Stop"))
        self.groupBox.setTitle(_translate("MainWindow", "Send Data"))
        self.e1.setText(_translate("MainWindow", "UP"))
        self.e0.setText(_translate("MainWindow", "DOWN"))
        self.label_2.setText(_translate("MainWindow", "EC2 Client"))
        self.hl1.setText(_translate("MainWindow", "OFF"))
        self.label_3.setText(_translate("MainWindow", "Single User1"))
        self.hl2.setText(_translate("MainWindow", "OFF"))
        self.label_6.setText(_translate("MainWindow", "Single User2"))
        self.hl3.setText(_translate("MainWindow", "OFF"))
        self.label_8.setText(_translate("MainWindow", "Single User3"))
        self.hl4.setText(_translate("MainWindow", "OFF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Graph Scale"))
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Y"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Signal Filter"))
        self.F1.setText(_translate("MainWindow", "Raw"))
        self.F2.setText(_translate("MainWindow", "Avg"))
        self.F3.setText(_translate("MainWindow", "SG"))
        self.F4.setText(_translate("MainWindow", "Avg+SG"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Threshold"))
        self.label_13.setText(_translate("MainWindow", "Ratio"))
        self.label_12.setText(_translate("MainWindow", "Thres"))
        self.autos.setText(_translate("MainWindow", "AutoScale"))
        self.autot.setText(_translate("MainWindow", "AutoThreshold"))
        self.label_14.setText(_translate("MainWindow", "Record"))
        self.rlabel.setText(_translate("MainWindow", "OFF"))
        self.rstart.setText(_translate("MainWindow", "🔴"))
        self.rstop.setText(_translate("MainWindow", "⬛"))


class Ui_MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.client = WebSocketClient()
        self.setWindowTitle("EMG Viewer")

        labelStyle = {'font': 'Consolas', 'color': '#000000', 'font-size': '9pt'}

        self.plot.setLabel('left', 'Amplitue (uV)', **labelStyle)

        self.plot.setLabel('bottom', 'Time', **labelStyle)

        self.plot.setBackground((0, 0, 0))

        self.plot.showGrid(x=True, y=True)

        self.plot.enableAutoRange(axis='x')

        self.plot.enableAutoRange(axis='y')
        # self.plot.setXRange(0, 500)
        # #
        # self.plot.setYRange(170, 255)
        self.leg_value = 0
        self.count_data = 0
        self.isRecord = False

        self.windows_user_name = os.path.expanduser('~')

        self.eCon.clicked.connect(self.sensor)
        self.eDis.clicked.connect(self.close_sensor)

        self.hc1.clicked.connect(self.holo_connect_1)
        self.hd1.clicked.connect(self.holo_disconnect_1)
        self.hc2.clicked.connect(self.holo_connect_2)
        self.hd2.clicked.connect(self.holo_disconnect_2)
        self.hc3.clicked.connect(self.holo_connect_3)
        self.hd3.clicked.connect(self.holo_disconnect_3)
        self.hc4.clicked.connect(self.holo_connect_4)
        self.hd4.clicked.connect(self.holo_disconnect_4)

        self.rstart.clicked.connect(self.record_start)
        self.rstop.clicked.connect(self.record_end)

        self.autos.clicked.connect(self.auto_scale)

        self.xl.valueChanged.connect(self.x_change)
        self.xp.valueChanged.connect(self.xt_change)
        self.yl.valueChanged.connect(self.y_change)
        self.yp.valueChanged.connect(self.yt_change)

        self.tl.valueChanged.connect(self.thres_change)
        self.tp.valueChanged.connect(self.threst_change)
        self.rl.valueChanged.connect(self.ratio_change)
        self.rp.valueChanged.connect(self.ratiot_change)

        self.autot.clicked.connect(self.cal_thres)

        self.tcp_type_1 = 0
        self.tcp_type_2 = 0
        self.tcp_type_3 = 0
        self.tcp_type_4 = 0
        self.r_value = 4.0
        self.legdata = '1'


    def sensor(self):
        try:
            self.leg_move = 0
            self.zero = 0
            self.s_n = 0
            self.sum = 0
            self.avr_sensor = 0
            self.x_scale = 200
            self.leg_con = 0
            self.d_type = 1
            self.record = 0
            self.count_data = 0

            self.box = np.ones(10) / 10
            self.FLAG = True
            self.alpha = 0

            self.isRecord = False
            self.timestep = []
            self.thres = []
            self.raw = []
            self.avg = []
            self.svf = []
            self.sav = []
            self.ser = Serial('COM' + str(self.ePort.text()), 500000)

            if self.ser.readable():
                self.res = self.ser.readline()
                self.data = self.res.decode().split(',')

                self.read_data = [int(self.data[1])] * 10

                self.avg_data = [sum(self.read_data) / 10] * 10
                self.svf_data = np.convolve(self.read_data, self.box, mode='same')[-1]

                self.sav_data = np.convolve(self.avg_data, self.box, mode='same')[-1]
                del self.read_data[0]
                del self.avg_data[0]
            self.thres = [int(0) + int(self.tl.value()) ] * 300
            self.raw = [int(self.read_data[0])] * 300
            self.avg = [int(self.avg_data[0])] * 300
            self.svf = [int(self.svf_data)] * 300
            self.sav = [int(self.sav_data)] * 300
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_sensor)
            self.timer.start()
        except Exception as e:
            QMessageBox.warning(self, 'Warning', '포트 번호를 확인하세요.')
            print(e)

    def update_sensor(self):
        try:
            self.plot.clear()
            if self.ser.readable():
                self.res = self.ser.readline()
                self.data = self.res.decode()
                self.raw.append(int(self.data[1]))
                self.thres = [int(0) + int(self.tl.value())] * 300
                self.avg.append(sum(self.raw[-10:]) / 10)
                self.svf.append(np.convolve(self.raw[-10:], self.box, mode='same')[-1])
                self.sav.append(np.convolve(self.avg[-10:], self.box, mode='same')[-1])

                del self.raw[0]
                del self.avg[0]
                del self.svf[0]
                del self.sav[0]

                self.plot.plot(self.thres[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 255, 0), width=2))
                if self.F1.isChecked():
                    self.plot.plot(self.raw[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=2))
                    if self.raw[-1] >= self.thres[-1] and self.FLAG == True:
                        self.FLAG = False
                        self.move_leg()
                    elif self.raw[-1] < self.thres[-1]:
                        self.FLAG = True
                elif self.F2.isChecked():
                    self.plot.plot(self.avg[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=2))
                    if self.avg[-1] >= self.thres[-1] and self.FLAG == True:
                        self.FLAG = False
                        self.move_leg()
                    elif self.avg[-1] < self.thres[-1]:
                        self.FLAG = True
                elif self.F3.isChecked():
                    self.plot.plot(self.svf[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=2))
                    if self.svf[-1] >= self.thres[-1] and self.FLAG == True:
                        self.FLAG = False
                        self.move_leg()
                    elif self.svf[-1] < self.thres[-1]:
                        self.FLAG = True
                elif self.F4.isChecked():
                    self.plot.plot(self.sav[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=2))
                    if self.sav[-1] >= self.thres[-1] and self.FLAG == True:
                        self.FLAG = False
                        self.move_leg()
                    elif self.sav[-1] < self.thres[-1]:
                        self.FLAG = True
            if self.isRecord:
                self.csvf.writerow([self.raw[-1], self.avg[-1], self.svf[-1], self.sav[-1], self.thres[-1], self.count_data, datetime.utcnow().strftime('%Y-%m-%d+%H:%M:%S.%f')])
        except:
            # self.server_socket_1.close()
            # self.server_socket_2.close()
            # self.server_socket_3.close()
            # self.server_socket_4.close()
            self.timer.stop()
            self.ser.close()
            QMessageBox.warning(self, 'Warning', 'Disconnected !!!')

    def move_leg(self):
        if self.e1.isChecked():
            self.legdata = '1'
        if self.e0.isChecked():
            self.legdata = '0'
        self.count_data += 1
        if self.tcp_type_1 == 1:
            # print("move detect")
            self.start = time.time()
            asyncio.get_event_loop().run_until_complete(self.execute_1())

        if self.tcp_type_2 == 1:
            self.client_socket_2.recv(200000)
            self.client_socket_2.send(self.legdata.encode())
        if self.tcp_type_3 == 1:
            self.client_socket_3.recv(200000)
            self.client_socket_3.send(self.legdata.encode())
        if self.tcp_type_4 == 1:
            self.client_socket_4.recv(200000)
            self.client_socket_4.send(self.legdata.encode())

    async def execute_1(self):
        await self.client.send_data(self.legdata)
        self.hl1.setText('ON')
        end = time.time()
        print(end - self.start)



    def execute_2(self):
        try:
            while True:
                self.client_socket_2, self.addr_2 = self.server_socket_2.accept()
                self.tcp_type_2 = 1
                self.hl2.setText('ON')
        except:
            self.hl2.setText('Except')
            self.tcp_type_2 = 0
        finally:
            self.tcp_type_2 = 0
            self.server_socket_2.close()
            self.hl2.setText('OFF')

    def execute_3(self):
        try:
            while True:
                self.client_socket_3, self.addr_3 = self.server_socket_3.accept()
                self.tcp_type_3 = 1
                self.hl3.setText('ON')
        except:
            self.hl3.setText('Except')
            self.tcp_type_3 = 0
        finally:
            self.tcp_type_3 = 0
            self.server_socket_3.close()
            self.hl3.setText('OFF')

    def execute_4(self):
        try:
            while True:
                self.client_socket_4, self.addr_4 = self.server_socket_4.accept()
                self.tcp_type_4 = 1
                self.hl4.setText('ON')
        except:
            self.hl4.setText('Except')
            self.tcp_type_4 = 0
        finally:
            self.tcp_type_4 = 0
            self.server_socket_4.close()
            self.hl4.setText('OFF')

    def holo_connect_1(self):
        asyncio.get_event_loop().run_until_complete(self.client.connect())
        self.hl1.setText('Wait')
        self.tcp_type_1 = 1



    def holo_connect_2(self):
        self.server_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_2.bind(('', 50003))  # 포트 설정 부분
        self.server_socket_2.listen()
        self.hl2.setText('Wait')

        threading.Thread(target=self.execute_2).start()

    def holo_connect_3(self):
        self.server_socket_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_3.bind(('', 50004))  # 포트 설정 부분
        self.server_socket_3.listen()
        self.hl3.setText('Wait')

        threading.Thread(target=self.execute_3).start()

    def holo_connect_4(self):
        self.server_socket_4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_4.bind(('', 50005))  # 포트 설정 부분
        self.server_socket_4.listen()
        self.hl4.setText('Wait')

        threading.Thread(target=self.execute_4).start()

    def holo_disconnect_1(self):
        self.hl1.setText('OFF')
        self.tcp_type_1 = 0
        asyncio.get_event_loop().run_until_complete(self.client.close_connection())


    def holo_disconnect_2(self):
        self.hl2.setText('OFF')
        self.server_socket_2.close()
        self.tcp_type_2 = 0

    def holo_disconnect_3(self):
        self.hl3.setText('OFF')
        self.server_socket_3.close()
        self.tcp_type_3 = 0

    def holo_disconnect_4(self):
        self.hl4.setText('OFF')
        self.server_socket_4.close()
        self.tcp_type_4 = 0

    def close_sensor(self):
        self.timer.stop()
        self.ser.close()

    def record_start(self):
        self.isRecord = True
        self.rlabel.setText('Recording...')
        os.makedirs(self.windows_user_name + "/Desktop/Record/", exist_ok=True)
        self.timestr = time.strftime("%Y%m%d_%H%M%S")
        self.f = open(self.windows_user_name + "/Desktop/Record/" + self.timestr + ".csv", "w", encoding='utf-8', newline='')
        self.csvf = csv.writer(self.f)

    def record_end(self):
        self.isRecord = False
        self.rlabel.setText('Done')
        self.f.close()

    def auto_scale(self):
        self.plot.enableAutoRange(axis='x')
        self.plot.enableAutoRange(axis='y')

    def cal_thres(self):
        if self.F1.isChecked():
            thres = statistics.pstdev(self.raw) * self.r_value
            base = sum(self.raw) / len(self.raw)
            self.tl.setValue(int(base + thres))
            self.tp.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F2.isChecked():
            thres = statistics.pstdev(self.avg) * self.r_value
            base = sum(self.avg) / len(self.avg)
            self.tl.setValue(int(base + thres))
            self.tp.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F3.isChecked():
            thres = statistics.pstdev(self.svf) * self.r_value
            base = sum(self.svf) / len(self.svf)
            self.tl.setValue(int(base + thres))
            self.tp.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F4.isChecked():
            thres = statistics.pstdev(self.sav) * self.r_value
            base = sum(self.sav) / len(self.sav)
            self.tl.setValue(int(base + thres))
            self.tp.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300

    def rmsValue(self, array):
        n = len(array)
        squre = 0.0
        root = 0.0
        mean = 0.0
        for i in range(0, n):
            squre += (array[i] ** 2)
        mean = (squre / (float)(n))
        root = math.sqrt(mean)
        return root

    def x_change(self):
        self.x_scale = int(self.xl.value())

        self.xp.setValue(self.x_scale)

    def xt_change(self):
        self.x_scale = int(self.xp.value())

        self.xl.setValue(self.x_scale)

    def y_change(self):
        self.y_scale = int(self.yl.value())
        self.plot.setYRange(0, self.y_scale)
        self.yp.setValue(self.y_scale)

    def yt_change(self):
        self.y_scale = int(self.yp.value())
        self.plot.setYRange(0, self.y_scale)
        self.yl.setValue(self.y_scale)

    def ratio_change(self):
        self.r_value = int(self.rl.value())
        self.rp.setValue(self.r_value)

    def ratiot_change(self):
        self.r_value = int(self.rp.value())
        self.rl.setValue(self.r_value)

    def thres_change(self):
        self.t_value = int(self.tl.value())
        self.thres = [int(self.data) + self.t_value] * 300
        self.tp.setValue(self.t_value)

    def threst_change(self):
        self.t_value = int(self.tp.value())
        self.thres = [int(self.data) + self.t_value] * 300
        self.tl.setValue(self.t_value)

    def closeEvent(self, *args, **kwargs):
        sys.exit()


class WebSocketClient:
    def __init__(self):
        self.websocket = None

    async def connect(self):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        self.websocket = await websockets.connect("wss://3.36.112.128:443/", ssl=ssl_context)

    async def send_data(self, data):
        if not self.websocket:
            await self.connect()

        await self.websocket.send(data)
        data_rcv = await self.websocket.recv()
        print("data received from server: " + data_rcv.decode())  # 바이트열을 문자열로 변환하여 연결

    async def close_connection(self):
        if self.websocket:
            await self.websocket.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

