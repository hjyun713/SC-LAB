import math
import os
import socket
import statistics
import sys
import threading
import time
import csv
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/intanviewer/resource/icon.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter_18 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_18.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_18.setObjectName("splitter_18")
        self.viewer = QtWidgets.QGroupBox(self.splitter_18)
        self.viewer.setMinimumSize(QtCore.QSize(981, 0))
        self.viewer.setStyleSheet("font: 75 9pt \"Consolas\";")
        self.viewer.setObjectName("viewer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.viewer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_19 = QtWidgets.QSplitter(self.viewer)
        self.splitter_19.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_19.setObjectName("splitter_19")
        self.label_15 = QtWidgets.QLabel(self.splitter_19)
        self.label_15.setMinimumSize(QtCore.QSize(61, 21))
        self.label_15.setMaximumSize(QtCore.QSize(61, 21))
        self.label_15.setObjectName("label_15")
        self.count = QtWidgets.QLabel(self.splitter_19)
        self.count.setMinimumSize(QtCore.QSize(0, 21))
        self.count.setMaximumSize(QtCore.QSize(16777215, 21))
        self.count.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                                 "color: rgb(255, 0, 0);")
        self.count.setObjectName("count")
        self.gridLayout_2.addWidget(self.splitter_19, 0, 0, 1, 1)
        self.plot = PlotWidget(self.viewer)
        self.plot.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plot.setObjectName("plot")
        self.gridLayout_2.addWidget(self.plot, 1, 0, 1, 1)
        self.splitter_17 = QtWidgets.QSplitter(self.splitter_18)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName("splitter_17")
        self.splitter = QtWidgets.QSplitter(self.splitter_17)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setMinimumSize(QtCore.QSize(133, 19))
        self.label_2.setMaximumSize(QtCore.QSize(133, 19))
        self.label_2.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setMinimumSize(QtCore.QSize(63, 19))
        self.lineEdit.setMaximumSize(QtCore.QSize(63, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.dataSend = QtWidgets.QLineEdit(self.splitter)
        self.dataSend.setMinimumSize(QtCore.QSize(63, 19))
        self.dataSend.setMaximumSize(QtCore.QSize(63, 19))
        self.dataSend.setObjectName("dataSend")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_9.setMinimumSize(QtCore.QSize(271, 29))
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.connect = QtWidgets.QPushButton(self.splitter_9)
        self.connect.setMinimumSize(QtCore.QSize(133, 29))
        self.connect.setMaximumSize(QtCore.QSize(133, 29))
        self.connect.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.connect.setObjectName("connect")
        self.reload = QtWidgets.QPushButton(self.splitter_9)
        self.reload.setMinimumSize(QtCore.QSize(133, 29))
        self.reload.setMaximumSize(QtCore.QSize(133, 29))
        self.reload.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.reload.setObjectName("reload")
        self.line_5 = QtWidgets.QFrame(self.splitter_17)
        self.line_5.setMinimumSize(QtCore.QSize(271, 3))
        self.line_5.setMaximumSize(QtCore.QSize(271, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.splitter_16 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_16.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_16.setObjectName("splitter_16")
        self.label_3 = QtWidgets.QLabel(self.splitter_16)
        self.label_3.setMinimumSize(QtCore.QSize(133, 19))
        self.label_3.setMaximumSize(QtCore.QSize(133, 19))
        self.label_3.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_3.setObjectName("label_3")
        self.st1 = QtWidgets.QLabel(self.splitter_16)
        self.st1.setMinimumSize(QtCore.QSize(133, 19))
        self.st1.setMaximumSize(QtCore.QSize(133, 19))
        self.st1.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.st1.setObjectName("st1")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.connect_holo = QtWidgets.QPushButton(self.splitter_10)
        self.connect_holo.setMinimumSize(QtCore.QSize(133, 29))
        self.connect_holo.setMaximumSize(QtCore.QSize(133, 29))
        self.connect_holo.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.connect_holo.setObjectName("connect_holo")
        self.disconnect_holo = QtWidgets.QPushButton(self.splitter_10)
        self.disconnect_holo.setMinimumSize(QtCore.QSize(133, 29))
        self.disconnect_holo.setMaximumSize(QtCore.QSize(133, 29))
        self.disconnect_holo.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.disconnect_holo.setObjectName("disconnect_holo")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setMinimumSize(QtCore.QSize(133, 19))
        self.label_4.setMaximumSize(QtCore.QSize(133, 19))
        self.label_4.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_4.setObjectName("label_4")
        self.st2 = QtWidgets.QLabel(self.splitter_2)
        self.st2.setMinimumSize(QtCore.QSize(133, 19))
        self.st2.setMaximumSize(QtCore.QSize(133, 19))
        self.st2.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.st2.setObjectName("st2")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.connect_holo_2 = QtWidgets.QPushButton(self.splitter_12)
        self.connect_holo_2.setMinimumSize(QtCore.QSize(133, 29))
        self.connect_holo_2.setMaximumSize(QtCore.QSize(133, 29))
        self.connect_holo_2.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.connect_holo_2.setObjectName("connect_holo_2")
        self.disconnect_holo_2 = QtWidgets.QPushButton(self.splitter_12)
        self.disconnect_holo_2.setMinimumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_2.setMaximumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_2.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.disconnect_holo_2.setObjectName("disconnect_holo_2")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_5 = QtWidgets.QLabel(self.splitter_3)
        self.label_5.setMinimumSize(QtCore.QSize(133, 19))
        self.label_5.setMaximumSize(QtCore.QSize(133, 19))
        self.label_5.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_5.setObjectName("label_5")
        self.st3 = QtWidgets.QLabel(self.splitter_3)
        self.st3.setMinimumSize(QtCore.QSize(133, 19))
        self.st3.setMaximumSize(QtCore.QSize(133, 19))
        self.st3.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.st3.setObjectName("st3")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.connect_holo_3 = QtWidgets.QPushButton(self.splitter_13)
        self.connect_holo_3.setMinimumSize(QtCore.QSize(133, 29))
        self.connect_holo_3.setMaximumSize(QtCore.QSize(133, 29))
        self.connect_holo_3.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.connect_holo_3.setObjectName("connect_holo_3")
        self.disconnect_holo_3 = QtWidgets.QPushButton(self.splitter_13)
        self.disconnect_holo_3.setMinimumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_3.setMaximumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_3.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.disconnect_holo_3.setObjectName("disconnect_holo_3")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_6 = QtWidgets.QLabel(self.splitter_8)
        self.label_6.setMinimumSize(QtCore.QSize(133, 19))
        self.label_6.setMaximumSize(QtCore.QSize(133, 19))
        self.label_6.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_6.setObjectName("label_6")
        self.st4 = QtWidgets.QLabel(self.splitter_8)
        self.st4.setMinimumSize(QtCore.QSize(133, 19))
        self.st4.setMaximumSize(QtCore.QSize(133, 19))
        self.st4.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                               "color: rgb(0, 0, 255);")
        self.st4.setObjectName("st4")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.connect_holo_4 = QtWidgets.QPushButton(self.splitter_14)
        self.connect_holo_4.setMinimumSize(QtCore.QSize(133, 29))
        self.connect_holo_4.setMaximumSize(QtCore.QSize(133, 29))
        self.connect_holo_4.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.connect_holo_4.setObjectName("connect_holo_4")
        self.disconnect_holo_4 = QtWidgets.QPushButton(self.splitter_14)
        self.disconnect_holo_4.setMinimumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_4.setMaximumSize(QtCore.QSize(133, 29))
        self.disconnect_holo_4.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.disconnect_holo_4.setObjectName("disconnect_holo_4")
        self.line_4 = QtWidgets.QFrame(self.splitter_17)
        self.line_4.setMinimumSize(QtCore.QSize(271, 3))
        self.line_4.setMaximumSize(QtCore.QSize(271, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_8 = QtWidgets.QLabel(self.splitter_11)
        self.label_8.setMinimumSize(QtCore.QSize(133, 19))
        self.label_8.setMaximumSize(QtCore.QSize(133, 19))
        self.label_8.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_8.setObjectName("label_8")
        self.rc1 = QtWidgets.QLabel(self.splitter_11)
        self.rc1.setMinimumSize(QtCore.QSize(133, 19))
        self.rc1.setMaximumSize(QtCore.QSize(133, 19))
        self.rc1.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                               "color: rgb(255, 0, 0);")
        self.rc1.setObjectName("rc1")
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.Start = QtWidgets.QPushButton(self.splitter_15)
        self.Start.setMinimumSize(QtCore.QSize(133, 29))
        self.Start.setMaximumSize(QtCore.QSize(133, 29))
        self.Start.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.Start.setObjectName("Start")
        self.End = QtWidgets.QPushButton(self.splitter_15)
        self.End.setMinimumSize(QtCore.QSize(133, 29))
        self.End.setMaximumSize(QtCore.QSize(133, 29))
        self.End.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.End.setObjectName("End")
        self.line_3 = QtWidgets.QFrame(self.splitter_17)
        self.line_3.setMinimumSize(QtCore.QSize(271, 3))
        self.line_3.setMaximumSize(QtCore.QSize(271, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_17)
        self.groupBox_2.setMinimumSize(QtCore.QSize(271, 91))
        self.groupBox_2.setMaximumSize(QtCore.QSize(271, 91))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        self.label_12.setMinimumSize(QtCore.QSize(71, 21))
        self.label_12.setMaximumSize(QtCore.QSize(71, 21))
        self.label_12.setObjectName("label_12")
        self.x_all = QtWidgets.QSlider(self.splitter_4)
        self.x_all.setMinimumSize(QtCore.QSize(0, 22))
        self.x_all.setMaximumSize(QtCore.QSize(16777215, 22))
        self.x_all.setMinimum(100)
        self.x_all.setMaximum(10000)
        self.x_all.setSliderPosition(10000)
        self.x_all.setOrientation(QtCore.Qt.Horizontal)
        self.x_all.setObjectName("x_all")
        self.gridLayout.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.yt = QtWidgets.QSpinBox(self.groupBox_2)
        self.yt.setMinimumSize(QtCore.QSize(55, 22))
        self.yt.setMaximumSize(QtCore.QSize(55, 22))
        self.yt.setAlignment(QtCore.Qt.AlignCenter)
        self.yt.setMinimum(50)
        self.yt.setMaximum(10000)
        self.yt.setSingleStep(5)
        self.yt.setProperty("value", 7000)
        self.yt.setObjectName("yt")
        self.gridLayout.addWidget(self.yt, 1, 1, 1, 1)
        self.xt = QtWidgets.QSpinBox(self.groupBox_2)
        self.xt.setMinimumSize(QtCore.QSize(55, 22))
        self.xt.setMaximumSize(QtCore.QSize(55, 22))
        self.xt.setAlignment(QtCore.Qt.AlignCenter)
        self.xt.setMinimum(100)
        self.xt.setMaximum(10000)
        self.xt.setSingleStep(5)
        self.xt.setProperty("value", 10000)
        self.xt.setObjectName("xt")
        self.gridLayout.addWidget(self.xt, 0, 1, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_11 = QtWidgets.QLabel(self.splitter_5)
        self.label_11.setMinimumSize(QtCore.QSize(71, 21))
        self.label_11.setMaximumSize(QtCore.QSize(71, 21))
        self.label_11.setObjectName("label_11")
        self.y_all = QtWidgets.QSlider(self.splitter_5)
        self.y_all.setMinimumSize(QtCore.QSize(0, 22))
        self.y_all.setMaximumSize(QtCore.QSize(16777215, 22))
        self.y_all.setMinimum(50)
        self.y_all.setMaximum(10000)
        self.y_all.setSliderPosition(7000)
        self.y_all.setOrientation(QtCore.Qt.Horizontal)
        self.y_all.setObjectName("y_all")
        self.gridLayout.addWidget(self.splitter_5, 1, 0, 1, 1)
        self.auto_xy = QtWidgets.QPushButton(self.splitter_17)
        self.auto_xy.setMinimumSize(QtCore.QSize(271, 28))
        self.auto_xy.setMaximumSize(QtCore.QSize(271, 28))
        self.auto_xy.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.auto_xy.setObjectName("auto_xy")
        self.line_2 = QtWidgets.QFrame(self.splitter_17)
        self.line_2.setMinimumSize(QtCore.QSize(271, 3))
        self.line_2.setMaximumSize(QtCore.QSize(271, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.filtergroup = QtWidgets.QGroupBox(self.splitter_17)
        self.filtergroup.setMinimumSize(QtCore.QSize(262, 90))
        self.filtergroup.setMaximumSize(QtCore.QSize(262, 90))
        self.filtergroup.setObjectName("filtergroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filtergroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.F1 = QtWidgets.QRadioButton(self.filtergroup)
        self.F1.setChecked(True)
        self.F1.setObjectName("F1")
        self.gridLayout_3.addWidget(self.F1, 0, 0, 1, 1)
        self.F2 = QtWidgets.QRadioButton(self.filtergroup)
        self.F2.setObjectName("F2")
        self.gridLayout_3.addWidget(self.F2, 0, 1, 1, 1)
        self.F3 = QtWidgets.QRadioButton(self.filtergroup)
        self.F3.setObjectName("F3")
        self.gridLayout_3.addWidget(self.F3, 1, 0, 1, 1)
        self.F4 = QtWidgets.QRadioButton(self.filtergroup)
        self.F4.setObjectName("F4")
        self.gridLayout_3.addWidget(self.F4, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.splitter_17)
        self.line.setMinimumSize(QtCore.QSize(271, 3))
        self.line.setMaximumSize(QtCore.QSize(271, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_14 = QtWidgets.QLabel(self.splitter_6)
        self.label_14.setMinimumSize(QtCore.QSize(71, 21))
        self.label_14.setMaximumSize(QtCore.QSize(71, 21))
        self.label_14.setObjectName("label_14")
        self.t_s = QtWidgets.QSlider(self.splitter_6)
        self.t_s.setMinimumSize(QtCore.QSize(0, 22))
        self.t_s.setMaximumSize(QtCore.QSize(16777215, 22))
        self.t_s.setMinimum(-300)
        self.t_s.setMaximum(10000)
        self.t_s.setSliderPosition(7000)
        self.t_s.setOrientation(QtCore.Qt.Horizontal)
        self.t_s.setObjectName("t_s")
        self.t_v = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.t_v.setMinimumSize(QtCore.QSize(55, 22))
        self.t_v.setAlignment(QtCore.Qt.AlignCenter)
        self.t_v.setMaximum(10000.0)
        self.t_v.setProperty("value", 7000.0)
        self.t_v.setObjectName("t_v")
        self.SetThres = QtWidgets.QPushButton(self.splitter_17)
        self.SetThres.setMinimumSize(QtCore.QSize(271, 28))
        self.SetThres.setMaximumSize(QtCore.QSize(271, 28))
        self.SetThres.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.SetThres.setObjectName("SetThres")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_16 = QtWidgets.QLabel(self.splitter_7)
        self.label_16.setMinimumSize(QtCore.QSize(45, 21))
        self.label_16.setMaximumSize(QtCore.QSize(45, 21))
        self.label_16.setObjectName("label_16")
        self.r_s = QtWidgets.QSlider(self.splitter_7)
        self.r_s.setMinimumSize(QtCore.QSize(0, 22))
        self.r_s.setMaximumSize(QtCore.QSize(16777215, 22))
        self.r_s.setMinimum(1)
        self.r_s.setMaximum(100)
        self.r_s.setPageStep(100)
        self.r_s.setProperty("value", 4)
        self.r_s.setSliderPosition(4)
        self.r_s.setOrientation(QtCore.Qt.Horizontal)
        self.r_s.setObjectName("r_s")
        self.r_v = QtWidgets.QDoubleSpinBox(self.splitter_7)
        self.r_v.setMinimumSize(QtCore.QSize(55, 22))
        self.r_v.setAlignment(QtCore.Qt.AlignCenter)
        self.r_v.setMinimum(1.0)
        self.r_v.setMaximum(100.0)
        self.r_v.setSingleStep(0.1)
        self.r_v.setProperty("value", 4.0)
        self.r_v.setObjectName("r_v")
        self.label = QtWidgets.QLabel(self.splitter_17)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.splitter_18, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.viewer.setTitle(_translate("MainWindow", "EMG Viewer"))
        self.label_15.setText(_translate("MainWindow", "Count -"))
        self.count.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "EMG sensor"))
        self.lineEdit.setText(_translate("MainWindow", "4"))
        self.dataSend.setText(_translate("MainWindow", "1"))
        self.connect.setText(_translate("MainWindow", "Connet"))
        self.reload.setText(_translate("MainWindow", "Disconnect"))
        self.label_3.setText(_translate("MainWindow", "HoloLens2 - 1"))
        self.st1.setText(_translate("MainWindow", "disconnect"))
        self.connect_holo.setText(_translate("MainWindow", "Connet"))
        self.disconnect_holo.setText(_translate("MainWindow", "DisConnet"))
        self.label_4.setText(_translate("MainWindow", "HoloLens2 - 2"))
        self.st2.setText(_translate("MainWindow", "disconnect"))
        self.connect_holo_2.setText(_translate("MainWindow", "Connet"))
        self.disconnect_holo_2.setText(_translate("MainWindow", "DisConnet"))
        self.label_5.setText(_translate("MainWindow", "HoloLens2 - 3"))
        self.st3.setText(_translate("MainWindow", "disconnect"))
        self.connect_holo_3.setText(_translate("MainWindow", "Connet"))
        self.disconnect_holo_3.setText(_translate("MainWindow", "DisConnet"))
        self.label_6.setText(_translate("MainWindow", "HoloLens2 - 4"))
        self.st4.setText(_translate("MainWindow", "disconnect"))
        self.connect_holo_4.setText(_translate("MainWindow", "Connet"))
        self.disconnect_holo_4.setText(_translate("MainWindow", "DisConnet"))
        self.label_8.setText(_translate("MainWindow", "Record"))
        self.rc1.setText(_translate("MainWindow", "■"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.End.setText(_translate("MainWindow", "End"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Scale"))
        self.label_12.setText(_translate("MainWindow", "X scale -"))
        self.label_11.setText(_translate("MainWindow", "Y scale -"))
        self.auto_xy.setText(_translate("MainWindow", "Auto Scale"))
        self.filtergroup.setTitle(_translate("MainWindow", "Filter"))
        self.F1.setText(_translate("MainWindow", "None"))
        self.F2.setText(_translate("MainWindow", "Avg"))
        self.F3.setText(_translate("MainWindow", "Savitzky"))
        self.F4.setText(_translate("MainWindow", "Avg + Savitzky"))
        self.label_14.setText(_translate("MainWindow", "Threshold -"))
        self.SetThres.setText(_translate("MainWindow", "Auto Threshold"))
        self.label_16.setText(_translate("MainWindow", "Ratio -"))


class Ui_MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        self.connect.clicked.connect(self.sensor)
        self.reload.clicked.connect(self.close_sensor)

        self.connect_holo.clicked.connect(self.holo_connect_1)
        self.disconnect_holo.clicked.connect(self.holo_disconnect_1)
        self.connect_holo_2.clicked.connect(self.holo_connect_2)
        self.disconnect_holo_2.clicked.connect(self.holo_disconnect_2)
        self.connect_holo_3.clicked.connect(self.holo_connect_3)
        self.disconnect_holo_3.clicked.connect(self.holo_disconnect_3)
        self.connect_holo_4.clicked.connect(self.holo_connect_4)
        self.disconnect_holo_4.clicked.connect(self.holo_disconnect_4)

        self.Start.clicked.connect(self.record_start)
        self.End.clicked.connect(self.record_end)

        self.auto_xy.clicked.connect(self.auto_scale)

        self.x_all.valueChanged.connect(self.x_change)
        self.xt.valueChanged.connect(self.xt_change)
        self.y_all.valueChanged.connect(self.y_change)
        self.yt.valueChanged.connect(self.yt_change)

        self.t_s.valueChanged.connect(self.thres_change)
        self.t_v.valueChanged.connect(self.threst_change)

        self.r_s.valueChanged.connect(self.ratio_change)
        self.r_v.valueChanged.connect(self.ratiot_change)

        self.SetThres.clicked.connect(self.cal_thres)

        self.tcp_type_1 = 0
        self.tcp_type_2 = 0
        self.tcp_type_3 = 0
        self.tcp_type_4 = 0
        self.r_value = 4.0

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
            self.ser = Serial('COM' + str(self.lineEdit.text()), 250000)

            if self.ser.readable():
                self.res = self.ser.readline()
                self.data = self.res.decode().split(',')

                self.read_data = [int(self.data[1])] * 10

                self.avg_data = [sum(self.read_data) / 10] * 10
                self.svf_data = np.convolve(self.read_data, self.box, mode='same')[-1]

                self.sav_data = np.convolve(self.avg_data, self.box, mode='same')[-1]
                del self.read_data[0]
                del self.avg_data[0]
            self.thres = [int(self.data[4][:-2]) + int(self.t_s.value()) ] * 300
            self.raw = [int(self.read_data[0])] * 300
            self.avg = [int(self.avg_data[0])] * 300
            self.svf = [int(self.svf_data)] * 300
            self.sav = [int(self.sav_data)] * 300
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_sensor)
            self.timer.start()
        except:
            QMessageBox.warning(self, 'Warning', '포트 번호를 확인하세요.')

    def update_sensor(self):
        try:
            self.plot.clear()
            if self.ser.readable():
                self.res = self.ser.readline()
                self.data = self.res.decode().split(',')
                self.raw.append(int(self.data[1]))
                self.thres = [int(self.data[4][:-2]) + int(self.t_s.value())] * 300
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
            self.count.setText(str(self.count_data))
            if self.isRecord:
                self.csvf.writerow([self.raw[-1], self.avg[-1], self.svf[-1], self.sav[-1], self.thres[-1], self.count_data, datetime.utcnow().strftime('%Y-%m-%d+%H:%M:%S.%f')])
        except:
            self.server_socket_1.close()
            self.server_socket_2.close()
            self.server_socket_3.close()
            self.server_socket_4.close()
            self.timer.stop()
            self.ser.close()
            QMessageBox.warning(self, 'Warning', 'Disconnected !!!')

    def move_leg(self):
        self.count_data += 1
        if self.tcp_type_1 == 1:
            self.client_socket_1.recv(200000).decode()
            self.client_socket_1.send(str(self.dataSend.text()).encode())
        if self.tcp_type_2 == 1:
            self.client_socket_2.recv(200000)
            self.client_socket_2.send(str(self.dataSend.text()).encode())
        if self.tcp_type_3 == 1:
            self.client_socket_3.recv(200000)
            self.client_socket_3.send(str(self.dataSend.text()).encode())
        if self.tcp_type_4 == 1:
            self.client_socket_4.recv(200000)
            self.client_socket_4.send(str(self.dataSend.text()).encode())

    def execute_1(self):
        try:
            while True:
                self.client_socket_1, self.addr_1 = self.server_socket_1.accept()
                self.tcp_type_1 = 1
                self.st1.setText('Connect')
        except:
            self.st1.setText('Except')
            self.tcp_type_1 = 0
        finally:
            self.tcp_type_1 = 0
            self.server_socket_1.close()
            self.st1.setText('Disconnet')

    def execute_2(self):
        try:
            while True:
                self.client_socket_2, self.addr_2 = self.server_socket_2.accept()
                self.tcp_type_2 = 1
                self.st2.setText('Connect')
        except:
            self.st2.setText('Except')
            self.tcp_type_2 = 0
        finally:
            self.tcp_type_2 = 0
            self.server_socket_2.close()
            self.st2.setText('Disconnet')

    def execute_3(self):
        try:
            while True:
                self.client_socket_3, self.addr_3 = self.server_socket_3.accept()
                self.tcp_type_3 = 1
                self.st3.setText('Connect')
        except:
            self.st3.setText('Except')
            self.tcp_type_3 = 0
        finally:
            self.tcp_type_3 = 0
            self.server_socket_3.close()
            self.st3.setText('Disconnet')

    def execute_4(self):
        try:
            while True:
                self.client_socket_4, self.addr_4 = self.server_socket_4.accept()
                self.tcp_type_4 = 1
                self.st4.setText('Connect')
        except:
            self.st4.setText('Except')
            self.tcp_type_4 = 0
        finally:
            self.tcp_type_4 = 0
            self.server_socket_4.close()
            self.st4.setText('Disconnet')

    def holo_connect_1(self):
        self.server_socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_1.bind(('', 50002))  # 포트 설정 부분
        self.server_socket_1.listen()
        self.st1.setText('Waiting...')

        threading.Thread(target=self.execute_1).start()

    def holo_connect_2(self):
        self.server_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_2.bind(('', 50003))  # 포트 설정 부분
        self.server_socket_2.listen()
        self.st2.setText('Waiting...')

        threading.Thread(target=self.execute_2).start()

    def holo_connect_3(self):
        self.server_socket_3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_3.bind(('', 50004))  # 포트 설정 부분
        self.server_socket_3.listen()
        self.st3.setText('Waiting...')

        threading.Thread(target=self.execute_3).start()

    def holo_connect_4(self):
        self.server_socket_4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket_4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket_4.bind(('', 50005))  # 포트 설정 부분
        self.server_socket_4.listen()
        self.st4.setText('Waiting...')

        threading.Thread(target=self.execute_4).start()

    def holo_disconnect_1(self):
        self.st1.setText('Disconnect')
        self.server_socket_1.close()
        self.tcp_type_1 = 0

    def holo_disconnect_2(self):
        self.st2.setText('Disconnect')
        self.server_socket_2.close()
        self.tcp_type_2 = 0

    def holo_disconnect_3(self):
        self.st3.setText('Disconnect')
        self.server_socket_3.close()
        self.tcp_type_3 = 0

    def holo_disconnect_4(self):
        self.st4.setText('Disconnect')
        self.server_socket_4.close()
        self.tcp_type_4 = 0

    def close_sensor(self):
        self.timer.stop()
        self.ser.close()

    def record_start(self):
        self.isRecord = True
        self.rc1.setText('Recording...')
        os.makedirs(self.windows_user_name + "/Desktop/Record/", exist_ok=True)
        self.timestr = time.strftime("%Y%m%d_%H%M%S")
        self.f = open(self.windows_user_name + "/Desktop/Record/" + self.timestr + ".csv", "w", encoding='utf-8', newline='')
        self.csvf = csv.writer(self.f)

    def record_end(self):
        self.isRecord = False
        self.rc1.setText('Done')
        self.f.close()

    def auto_scale(self):
        self.plot.enableAutoRange(axis='x')
        self.plot.enableAutoRange(axis='y')

    def cal_thres(self):
        if self.F1.isChecked():
            thres = statistics.pstdev(self.raw) * self.r_value
            base = sum(self.raw) / len(self.raw)
            self.t_s.setValue(int(base + thres))
            self.t_v.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F2.isChecked():
            thres = statistics.pstdev(self.avg) * self.r_value
            base = sum(self.avg) / len(self.avg)
            self.t_s.setValue(int(base + thres))
            self.t_v.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F3.isChecked():
            thres = statistics.pstdev(self.svf) * self.r_value
            base = sum(self.svf) / len(self.svf)
            self.t_s.setValue(int(base + thres))
            self.t_v.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        elif self.F4.isChecked():
            thres = statistics.pstdev(self.sav) * self.r_value
            base = sum(self.sav) / len(self.sav)
            self.t_s.setValue(int(base + thres))
            self.t_v.setValue(int(base + thres))
            self.thres = [int(base + thres)] * 300
        print(str(thres) + ', ' + str(base))
        print(self.r_value)

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
        self.x_scale = int(self.x_all.value())

        self.xt.setValue(self.x_scale)

    def xt_change(self):
        self.x_scale = int(self.xt.value())

        self.x_all.setValue(self.x_scale)

    def y_change(self):
        self.y_scale = int(self.y_all.value())
        self.plot.setYRange(0, self.y_scale)
        self.yt.setValue(self.y_scale)

    def yt_change(self):
        self.y_scale = int(self.yt.value())
        self.plot.setYRange(0, self.y_scale)
        self.y_all.setValue(self.y_scale)

    def ratio_change(self):
        self.r_value = int(self.r_s.value())
        self.r_v.setValue(self.r_value)

    def ratiot_change(self):
        self.r_value = int(self.r_v.value())
        self.r_s.setValue(self.r_value)

    def thres_change(self):
        self.t_value = int(self.t_s.value())
        self.thres = [int(self.data[4][:-2]) + self.t_value] * 300
        self.t_v.setValue(self.t_value)

    def threst_change(self):
        self.t_value = int(self.t_v.value())
        self.thres = [int(self.data[4][:-2]) + self.t_value] * 300
        self.t_s.setValue(self.t_value)

    def reset_all(self):
        self.zero = 0
        self.s_n = 0
        self.sum = 0
        self.avr_sensor = 0
        self.x_scale = 200
        self.leg_con = 0
        self.d_type = 1
        self.record = 0
        self.plot.clear()

        self.port.setText('9001')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
