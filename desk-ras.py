import math
import os
import statistics
import sys
import time
import cv2
import csv
import socket
import pickle
import asyncio

import pyqtgraph
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget

class form_class(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 757)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 757))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/intanviewer/resource/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_24 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_24.setMinimumSize(QtCore.QSize(982, 740))
        self.splitter_24.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_24.setObjectName("splitter_24")
        self.splitter_23 = QtWidgets.QSplitter(self.splitter_24)
        self.splitter_23.setMinimumSize(QtCore.QSize(691, 741))
        self.splitter_23.setOrientation(QtCore.Qt.Vertical)
        self.splitter_23.setObjectName("splitter_23")
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_23)
        self.groupBox_3.setMinimumSize(QtCore.QSize(701, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cam_label = QtWidgets.QLabel(self.groupBox_3)
        self.cam_label.setMinimumSize(QtCore.QSize(400, 300))
        self.cam_label.setStyleSheet("border-color: rgb(170, 170, 170);\n"
                                     "border-style: solid;\n"
                                     "border-width: 1px;")
        self.cam_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cam_label.setObjectName("cam_label")
        self.gridLayout_4.addWidget(self.cam_label, 0, 0, 2, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_2.setMinimumSize(QtCore.QSize(271, 23))
        self.splitter_2.setMaximumSize(QtCore.QSize(271, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setMinimumSize(QtCore.QSize(56, 23))
        self.label.setMaximumSize(QtCore.QSize(56, 23))
        self.label.setObjectName("label")
        self.cam_box = QtWidgets.QComboBox(self.splitter_2)
        self.cam_box.setMinimumSize(QtCore.QSize(182, 23))
        self.cam_box.setMaximumSize(QtCore.QSize(182, 23))
        self.cam_box.setObjectName("cam_box")
        self.cam_box.addItem("")
        self.refresh = QtWidgets.QPushButton(self.splitter_2)
        self.refresh.setMinimumSize(QtCore.QSize(23, 23))
        self.refresh.setMaximumSize(QtCore.QSize(23, 23))
        self.refresh.setObjectName("refresh")
        self.gridLayout_4.addWidget(self.splitter_2, 0, 1, 1, 1)
        self.splitter_17 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_17.setOrientation(QtCore.Qt.Vertical)
        self.splitter_17.setObjectName("splitter_17")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_17)
        self.splitter_10.setMinimumSize(QtCore.QSize(271, 29))
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.cam_play = QtWidgets.QPushButton(self.splitter_10)
        self.cam_play.setMinimumSize(QtCore.QSize(133, 29))
        self.cam_play.setMaximumSize(QtCore.QSize(133, 29))
        self.cam_play.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.cam_play.setObjectName("cam_play")
        self.cam_stop = QtWidgets.QPushButton(self.splitter_10)
        self.cam_stop.setMinimumSize(QtCore.QSize(133, 29))
        self.cam_stop.setMaximumSize(QtCore.QSize(133, 29))
        self.cam_stop.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.cam_stop.setObjectName("cam_stop")
        self.line_6 = QtWidgets.QFrame(self.splitter_17)
        self.line_6.setMinimumSize(QtCore.QSize(271, 3))
        self.line_6.setMaximumSize(QtCore.QSize(271, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.splitter_17)
        self.groupBox_4.setMinimumSize(QtCore.QSize(271, 236))
        self.groupBox_4.setMaximumSize(QtCore.QSize(271, 236))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_0 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_0.setMinimumSize(QtCore.QSize(251, 29))
        self.label_0.setMaximumSize(QtCore.QSize(251, 29))
        self.label_0.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_0.setCheckable(True)
        self.label_0.setChecked(True)
        self.label_0.setObjectName("label_0")
        self.gridLayout_2.addWidget(self.label_0, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_1.setMinimumSize(QtCore.QSize(251, 29))
        self.label_1.setMaximumSize(QtCore.QSize(251, 29))
        self.label_1.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_1.setCheckable(True)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_2.setMinimumSize(QtCore.QSize(251, 29))
        self.label_2.setMaximumSize(QtCore.QSize(251, 29))
        self.label_2.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_2.setCheckable(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_3.setMinimumSize(QtCore.QSize(251, 29))
        self.label_3.setMaximumSize(QtCore.QSize(251, 29))
        self.label_3.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_3.setCheckable(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_4.setMinimumSize(QtCore.QSize(251, 29))
        self.label_4.setMaximumSize(QtCore.QSize(251, 29))
        self.label_4.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_4.setCheckable(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.label_5.setMinimumSize(QtCore.QSize(251, 29))
        self.label_5.setMaximumSize(QtCore.QSize(251, 29))
        self.label_5.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.label_5.setCheckable(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.empty_label = QtWidgets.QLabel(self.splitter_17)
        self.empty_label.setText("")
        self.empty_label.setObjectName("empty_label")
        self.gridLayout_4.addWidget(self.splitter_17, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.splitter_23)
        self.groupBox.setMinimumSize(QtCore.QSize(701, 361))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_19 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_19.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_19.setObjectName("splitter_19")
        self.plot = PlotWidget(self.splitter_19)
        self.plot.setMinimumSize(QtCore.QSize(400, 300))
        self.plot.setStyleSheet("border-color: rgb(170, 170, 170);\n"
                                "background-color: rgb(0, 0, 0);\n"
                                "border-style: solid;\n"
                                "border-width: 1px;")
        self.plot.setInteractive(False)
        self.plot.setViewportUpdateMode(QtWidgets.QGraphicsView.MinimalViewportUpdate)
        self.plot.setObjectName("plot")
        self.splitter_16 = QtWidgets.QSplitter(self.splitter_19)
        self.splitter_16.setOrientation(QtCore.Qt.Vertical)
        self.splitter_16.setObjectName("splitter_16")
        self.splitter = QtWidgets.QSplitter(self.splitter_16)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.emg_label = QtWidgets.QLabel(self.splitter)
        self.emg_label.setMinimumSize(QtCore.QSize(133, 19))
        self.emg_label.setMaximumSize(QtCore.QSize(133, 19))
        self.emg_label.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.emg_label.setObjectName("emg_label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setMinimumSize(QtCore.QSize(133, 19))
        self.lineEdit.setMaximumSize(QtCore.QSize(133, 19))
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_16)
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
        self.line_5 = QtWidgets.QFrame(self.splitter_16)
        self.line_5.setMinimumSize(QtCore.QSize(271, 3))
        self.line_5.setMaximumSize(QtCore.QSize(271, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_3.setMinimumSize(QtCore.QSize(271, 22))
        self.splitter_3.setMaximumSize(QtCore.QSize(16777215, 22))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        self.label_12.setMinimumSize(QtCore.QSize(71, 21))
        self.label_12.setMaximumSize(QtCore.QSize(71, 21))
        self.label_12.setObjectName("label_12")
        self.x_all = QtWidgets.QSlider(self.splitter_4)
        self.x_all.setMinimumSize(QtCore.QSize(0, 22))
        self.x_all.setMaximumSize(QtCore.QSize(16777215, 22))
        self.x_all.setMinimum(50)
        self.x_all.setMaximum(1000)
        self.x_all.setProperty("value", 200)
        self.x_all.setSliderPosition(200)
        self.x_all.setOrientation(QtCore.Qt.Horizontal)
        self.x_all.setObjectName("x_all")
        self.xt = QtWidgets.QSpinBox(self.splitter_3)
        self.xt.setMinimumSize(QtCore.QSize(55, 22))
        self.xt.setMaximumSize(QtCore.QSize(55, 22))
        self.xt.setAlignment(QtCore.Qt.AlignCenter)
        self.xt.setMinimum(50)
        self.xt.setMaximum(1000)
        self.xt.setSingleStep(5)
        self.xt.setProperty("value", 200)
        self.xt.setObjectName("xt")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_8.setMinimumSize(QtCore.QSize(271, 22))
        self.splitter_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_8)
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
        self.yt = QtWidgets.QSpinBox(self.splitter_8)
        self.yt.setMinimumSize(QtCore.QSize(55, 22))
        self.yt.setMaximumSize(QtCore.QSize(55, 22))
        self.yt.setAlignment(QtCore.Qt.AlignCenter)
        self.yt.setMinimum(50)
        self.yt.setMaximum(10000)
        self.yt.setSingleStep(5)
        self.yt.setProperty("value", 7000)
        self.yt.setObjectName("yt")
        self.line = QtWidgets.QFrame(self.splitter_16)
        self.line.setMinimumSize(QtCore.QSize(271, 3))
        self.line.setMaximumSize(QtCore.QSize(271, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_14 = QtWidgets.QLabel(self.splitter_6)
        self.label_14.setMinimumSize(QtCore.QSize(71, 21))
        self.label_14.setMaximumSize(QtCore.QSize(71, 21))
        self.label_14.setStyleSheet("color: rgb(220, 0, 0);\n"
                                    "font: bold 9pt \"Consolas\";")
        self.label_14.setObjectName("label_14")
        self.t_s1 = QtWidgets.QSlider(self.splitter_6)
        self.t_s1.setMinimumSize(QtCore.QSize(0, 22))
        self.t_s1.setMaximumSize(QtCore.QSize(16777215, 22))
        self.t_s1.setMinimum(-10000)
        self.t_s1.setMaximum(10000)
        self.t_s1.setSliderPosition(7000)
        self.t_s1.setOrientation(QtCore.Qt.Horizontal)
        self.t_s1.setObjectName("t_s1")
        self.t_v1 = QtWidgets.QDoubleSpinBox(self.splitter_6)
        self.t_v1.setMinimumSize(QtCore.QSize(55, 22))
        self.t_v1.setMaximumSize(QtCore.QSize(55, 22))
        self.t_v1.setAlignment(QtCore.Qt.AlignCenter)
        self.t_v1.setMinimum(-10000.0)
        self.t_v1.setMaximum(10000.0)
        self.t_v1.setProperty("value", 7000.0)
        self.t_v1.setObjectName("t_v1")
        self.splitter_13 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_13.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_13.setObjectName("splitter_13")
        self.label_15 = QtWidgets.QLabel(self.splitter_13)
        self.label_15.setMinimumSize(QtCore.QSize(71, 21))
        self.label_15.setMaximumSize(QtCore.QSize(71, 21))
        self.label_15.setStyleSheet("color: rgb(0, 0, 220);\n"
                                    "font: bold 9pt \"Consolas\";")
        self.label_15.setObjectName("label_15")
        self.t_s2 = QtWidgets.QSlider(self.splitter_13)
        self.t_s2.setMinimumSize(QtCore.QSize(0, 22))
        self.t_s2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.t_s2.setMinimum(-10000)
        self.t_s2.setMaximum(10000)
        self.t_s2.setSliderPosition(7000)
        self.t_s2.setOrientation(QtCore.Qt.Horizontal)
        self.t_s2.setObjectName("t_s2")
        self.t_v2 = QtWidgets.QDoubleSpinBox(self.splitter_13)
        self.t_v2.setMinimumSize(QtCore.QSize(55, 22))
        self.t_v2.setMaximumSize(QtCore.QSize(55, 22))
        self.t_v2.setAlignment(QtCore.Qt.AlignCenter)
        self.t_v2.setMinimum(-10000.0)
        self.t_v2.setMaximum(10000.0)
        self.t_v2.setProperty("value", 7000.0)
        self.t_v2.setObjectName("t_v2")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_16 = QtWidgets.QLabel(self.splitter_7)
        self.label_16.setMinimumSize(QtCore.QSize(71, 21))
        self.label_16.setMaximumSize(QtCore.QSize(71, 21))
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
        self.r_v.setMaximumSize(QtCore.QSize(55, 22))
        self.r_v.setAlignment(QtCore.Qt.AlignCenter)
        self.r_v.setMinimum(1.0)
        self.r_v.setMaximum(100.0)
        self.r_v.setSingleStep(0.1)
        self.r_v.setProperty("value", 4.0)
        self.r_v.setObjectName("r_v")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_16)
        self.splitter_12.setMinimumSize(QtCore.QSize(271, 29))
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.auto_xy = QtWidgets.QPushButton(self.splitter_12)
        self.auto_xy.setMinimumSize(QtCore.QSize(133, 29))
        self.auto_xy.setMaximumSize(QtCore.QSize(133, 29))
        self.auto_xy.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.auto_xy.setObjectName("auto_xy")
        self.SetThres = QtWidgets.QPushButton(self.splitter_12)
        self.SetThres.setMinimumSize(QtCore.QSize(133, 29))
        self.SetThres.setMaximumSize(QtCore.QSize(133, 29))
        self.SetThres.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.SetThres.setObjectName("SetThres")
        self.line_2 = QtWidgets.QFrame(self.splitter_16)
        self.line_2.setMinimumSize(QtCore.QSize(271, 3))
        self.line_2.setMaximumSize(QtCore.QSize(271, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.filtergroup = QtWidgets.QGroupBox(self.splitter_16)
        self.filtergroup.setMinimumSize(QtCore.QSize(271, 70))
        self.filtergroup.setMaximumSize(QtCore.QSize(271, 70))
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
        self.empty_label_2 = QtWidgets.QLabel(self.splitter_16)
        self.empty_label_2.setText("")
        self.empty_label_2.setObjectName("empty_label_2")
        self.gridLayout.addWidget(self.splitter_19, 0, 0, 1, 1)
        self.splitter_22 = QtWidgets.QSplitter(self.splitter_24)
        self.splitter_22.setOrientation(QtCore.Qt.Vertical)
        self.splitter_22.setObjectName("splitter_22")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_14.setMinimumSize(QtCore.QSize(271, 20))
        self.splitter_14.setMaximumSize(QtCore.QSize(271, 20))
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.label_9 = QtWidgets.QLabel(self.splitter_14)
        self.label_9.setMinimumSize(QtCore.QSize(91, 19))
        self.label_9.setMaximumSize(QtCore.QSize(91, 19))
        self.label_9.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_9.setObjectName("label_9")
        self.time_text = QtWidgets.QLineEdit(self.splitter_14)
        self.time_text.setMinimumSize(QtCore.QSize(175, 20))
        self.time_text.setMaximumSize(QtCore.QSize(175, 20))
        self.time_text.setReadOnly(True)
        self.time_text.setObjectName("time_text")
        self.line_7 = QtWidgets.QFrame(self.splitter_22)
        self.line_7.setMinimumSize(QtCore.QSize(271, 3))
        self.line_7.setMaximumSize(QtCore.QSize(271, 3))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_22)
        self.groupBox_2.setMinimumSize(QtCore.QSize(271, 51))
        self.groupBox_2.setMaximumSize(QtCore.QSize(271, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.t_i = QtWidgets.QRadioButton(self.groupBox_2)
        self.t_i.setChecked(True)
        self.t_i.setObjectName("t_i")
        self.gridLayout_5.addWidget(self.t_i, 0, 0, 1, 1)
        self.t_v_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.t_v_2.setObjectName("t_v_2")
        self.gridLayout_5.addWidget(self.t_v_2, 0, 1, 1, 1)
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_11.setMinimumSize(QtCore.QSize(266, 19))
        self.splitter_11.setMaximumSize(QtCore.QSize(271, 19))
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
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_15.setMinimumSize(QtCore.QSize(271, 29))
        self.splitter_15.setMaximumSize(QtCore.QSize(271, 29))
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
        self.line_8 = QtWidgets.QFrame(self.splitter_22)
        self.line_8.setMinimumSize(QtCore.QSize(271, 3))
        self.line_8.setMaximumSize(QtCore.QSize(271, 3))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.splitter_21 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_21.setMinimumSize(QtCore.QSize(271, 19))
        self.splitter_21.setMaximumSize(QtCore.QSize(271, 19))
        self.splitter_21.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_21.setObjectName("splitter_21")
        self.emg_label_2 = QtWidgets.QLabel(self.splitter_21)
        self.emg_label_2.setMinimumSize(QtCore.QSize(133, 19))
        self.emg_label_2.setMaximumSize(QtCore.QSize(133, 19))
        self.emg_label_2.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.emg_label_2.setObjectName("emg_label_2")
        self.mac_address = QtWidgets.QLineEdit(self.splitter_21)
        self.mac_address.setMinimumSize(QtCore.QSize(133, 19))
        self.mac_address.setMaximumSize(QtCore.QSize(133, 19))
        self.mac_address.setObjectName("mac_address")
        self.splitter_20 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_20.setMinimumSize(QtCore.QSize(266, 19))
        self.splitter_20.setMaximumSize(QtCore.QSize(271, 19))
        self.splitter_20.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_20.setObjectName("splitter_20")
        self.label_10 = QtWidgets.QLabel(self.splitter_20)
        self.label_10.setMinimumSize(QtCore.QSize(133, 19))
        self.label_10.setMaximumSize(QtCore.QSize(133, 19))
        self.label_10.setStyleSheet("font: 75 bold 9pt \"Consolas\";")
        self.label_10.setObjectName("label_10")
        self.leg_status = QtWidgets.QLabel(self.splitter_20)
        self.leg_status.setMinimumSize(QtCore.QSize(133, 19))
        self.leg_status.setMaximumSize(QtCore.QSize(133, 19))
        self.leg_status.setStyleSheet("font: 75 bold 9pt \"Consolas\";\n"
                                      "color: rgb(255, 0, 0);")
        self.leg_status.setObjectName("leg_status")
        self.splitter_18 = QtWidgets.QSplitter(self.splitter_22)
        self.splitter_18.setMinimumSize(QtCore.QSize(271, 29))
        self.splitter_18.setMaximumSize(QtCore.QSize(271, 29))
        self.splitter_18.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_18.setObjectName("splitter_18")
        self.leg_con = QtWidgets.QPushButton(self.splitter_18)
        self.leg_con.setMinimumSize(QtCore.QSize(133, 29))
        self.leg_con.setMaximumSize(QtCore.QSize(133, 29))
        self.leg_con.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.leg_con.setObjectName("leg_con")
        self.leg_dis = QtWidgets.QPushButton(self.splitter_18)
        self.leg_dis.setMinimumSize(QtCore.QSize(133, 29))
        self.leg_dis.setMaximumSize(QtCore.QSize(133, 29))
        self.leg_dis.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.leg_dis.setObjectName("leg_dis")
        self.groupBox_5 = QtWidgets.QGroupBox(self.splitter_22)
        self.groupBox_5.setMinimumSize(QtCore.QSize(271, 51))
        self.groupBox_5.setMaximumSize(QtCore.QSize(271, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.leg_o = QtWidgets.QRadioButton(self.groupBox_5)
        self.leg_o.setChecked(True)
        self.leg_o.setObjectName("leg_o")
        self.gridLayout_6.addWidget(self.leg_o, 0, 0, 1, 1)
        self.leg_x = QtWidgets.QRadioButton(self.groupBox_5)
        self.leg_x.setObjectName("leg_x")
        self.gridLayout_6.addWidget(self.leg_x, 0, 1, 1, 1)
        self.leg_test = QtWidgets.QPushButton(self.splitter_22)
        self.leg_test.setMinimumSize(QtCore.QSize(271, 29))
        self.leg_test.setMaximumSize(QtCore.QSize(271, 29))
        self.leg_test.setStyleSheet("font: bold 9pt \"Consolas\";")
        self.leg_test.setObjectName("leg_test")
        self.empty_label_3 = QtWidgets.QLabel(self.splitter_22)
        self.empty_label_3.setText("")
        self.empty_label_3.setObjectName("empty_label_3")
        self.gridLayout_7.addWidget(self.splitter_24, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Labeling Tool"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Cam View"))
        self.cam_label.setText(_translate("MainWindow", "CAM"))
        self.label.setText(_translate("MainWindow", "Cam List"))
        self.cam_box.setItemText(0, _translate("MainWindow", "1"))
        self.refresh.setText(_translate("MainWindow", "↺"))
        self.cam_play.setText(_translate("MainWindow", "▶"))
        self.cam_stop.setText(_translate("MainWindow", "∥"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Motion Labeling"))
        self.label_0.setToolTip(_translate("MainWindow", "Labeling 0 (Shortcut : Alt+1) "))
        self.label_0.setText(_translate("MainWindow", "Standing (Rest) : 0"))
        self.label_0.setShortcut(_translate("MainWindow", "Alt+1"))
        self.label_1.setToolTip(_translate("MainWindow", "Labeling 1 (Shortcut : Alt+2) "))
        self.label_1.setText(_translate("MainWindow", "Walking : 1"))
        self.label_1.setShortcut(_translate("MainWindow", "Alt+2"))
        self.label_2.setToolTip(_translate("MainWindow", "Labeling 2 (Shortcut : Alt+3) "))
        self.label_2.setText(_translate("MainWindow", "Up Stairway : 2"))
        self.label_2.setShortcut(_translate("MainWindow", "Alt+3"))
        self.label_3.setToolTip(_translate("MainWindow", "Labeling 3 (Shortcut : Alt+4) "))
        self.label_3.setText(_translate("MainWindow", "Down Stairway : 3"))
        self.label_3.setShortcut(_translate("MainWindow", "Alt+4"))
        self.label_4.setToolTip(_translate("MainWindow", "Labeling 4 (Shortcut : Alt+5) "))
        self.label_4.setText(_translate("MainWindow", "Running : 4"))
        self.label_4.setShortcut(_translate("MainWindow", "Alt+5"))
        self.label_5.setToolTip(_translate("MainWindow", "Labeling 5 (Shortcut : Alt+6) "))
        self.label_5.setText(_translate("MainWindow", "Others : 5"))
        self.label_5.setShortcut(_translate("MainWindow", "Alt+6"))
        self.groupBox.setTitle(_translate("MainWindow", "EMG Signal View"))
        self.emg_label.setText(_translate("MainWindow", "EMG sensor"))
        self.lineEdit.setText(_translate("MainWindow", "192.168.80.1"))
        self.connect.setText(_translate("MainWindow", "Connet"))
        self.reload.setText(_translate("MainWindow", "Disconnect"))
        self.label_12.setText(_translate("MainWindow", "X scale -"))
        self.label_11.setText(_translate("MainWindow", "Y scale -"))
        self.label_14.setText(_translate("MainWindow", "Threshold1 -"))
        self.label_15.setText(_translate("MainWindow", "Threshold2 -"))
        self.label_16.setText(_translate("MainWindow", "Ratio -"))
        self.auto_xy.setText(_translate("MainWindow", "Auto Scale"))
        self.SetThres.setText(_translate("MainWindow", "Auto Threshold"))
        self.filtergroup.setTitle(_translate("MainWindow", "Filter"))
        self.F1.setText(_translate("MainWindow", "None"))
        self.F2.setText(_translate("MainWindow", "Avg"))
        self.F3.setText(_translate("MainWindow", "Savitzky"))
        self.F4.setText(_translate("MainWindow", "Avg + Savitzky"))
        self.label_9.setText(_translate("MainWindow", "Current Time"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Save Cam Type"))
        self.t_i.setText(_translate("MainWindow", "Image"))
        self.t_v_2.setText(_translate("MainWindow", "Video"))
        self.label_8.setText(_translate("MainWindow", "Record"))
        self.rc1.setText(_translate("MainWindow", "■"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.End.setText(_translate("MainWindow", "End"))
        self.emg_label_2.setText(_translate("MainWindow", "Mac address"))
        self.mac_address.setText(_translate("MainWindow", "5C:F2:86:41:9B:BF"))
        self.label_10.setText(_translate("MainWindow", "Leg"))
        self.leg_status.setText(_translate("MainWindow", "off"))
        self.leg_con.setText(_translate("MainWindow", "Connect"))
        self.leg_dis.setText(_translate("MainWindow", "Disconnect"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Leg Mode"))
        self.leg_o.setText(_translate("MainWindow", "Move"))
        self.leg_x.setText(_translate("MainWindow", "Rest"))
        self.leg_test.setText(_translate("MainWindow", "Move Leg (Test)"))


class Ui_MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("EMG Labeling Tool")

        labelStyle = {'color': '#FFFFFF', 'font': 'Consolas', 'font-size': '9pt'}

        self.plot.setLabel('left', 'Amplitue (uV)', **labelStyle)

        self.plot.setLabel('bottom', 'Time', **labelStyle)

        self.plot.setBackground((0, 0, 0))

        self.plot.showGrid(x=True, y=True)

        self.plot.enableAutoRange(axis='x')

        self.plot.enableAutoRange(axis='y')

        self.isRecord = False
        self.cam_type = False
        self.count_data = 0

        self.windows_user_name = os.path.expanduser('~')

        self.cam_play.clicked.connect(self.cam_start)
        self.cam_stop.clicked.connect(self.cam_end)

        self.label_0.clicked.connect(self.set0)
        self.label_1.clicked.connect(self.set1)
        self.label_2.clicked.connect(self.set2)
        self.label_3.clicked.connect(self.set3)
        self.label_4.clicked.connect(self.set4)
        self.label_5.clicked.connect(self.set5)

        self.connect.clicked.connect(self.sensor)
        self.reload.clicked.connect(self.close_sensor)

        self.Start.clicked.connect(self.record_start)
        self.End.clicked.connect(self.record_end)

        self.auto_xy.clicked.connect(self.auto_scale)

        self.x_all.valueChanged.connect(self.x_change)
        self.xt.valueChanged.connect(self.xt_change)
        self.y_all.valueChanged.connect(self.y_change)
        self.yt.valueChanged.connect(self.yt_change)

        self.t_s1.valueChanged.connect(self.thres_change1)
        self.t_v1.valueChanged.connect(self.threst_change1)
        self.t_s2.valueChanged.connect(self.thres_change2)
        self.t_v2.valueChanged.connect(self.threst_change2)

        self.r_s.valueChanged.connect(self.ratio_change)
        self.r_v.valueChanged.connect(self.ratiot_change)

        self.SetThres.clicked.connect(self.cal_thres)
        self.refresh.clicked.connect(self.cam_load)
        self.cam_load()

        self.leg_con.clicked.connect(self.run_leg)
        self.leg_dis.clicked.connect(self.stop_leg)
        self.leg_test.clicked.connect(self.test_leg)
        self.leg_value = 0
        self.thres_v1 = [7000] *1000
        self.thres_v2 = [7000] *1000
        self.r_value = 4.0
        self.type_t = 1
        self.count_up = 0
        self.count_down = 0
        self.st = 'off'
        self.con = 0
        self.n = None
        self.out = None
        self.reframe = None

    def cam_load(self):
        self.cam_box.clear()

    def set0(self):
        self.count_data = 0
        self.label_0.setChecked(True)
        self.label_1.setChecked(False)
        self.label_2.setChecked(False)
        self.label_3.setChecked(False)
        self.label_4.setChecked(False)
        self.label_5.setChecked(False)

    def set1(self):
        self.count_data = 1
        self.label_0.setChecked(False)
        self.label_1.setChecked(True)
        self.label_2.setChecked(False)
        self.label_3.setChecked(False)
        self.label_4.setChecked(False)
        self.label_5.setChecked(False)

    def set2(self):
        self.count_data = 2
        self.label_0.setChecked(False)
        self.label_1.setChecked(False)
        self.label_2.setChecked(True)
        self.label_3.setChecked(False)
        self.label_4.setChecked(False)
        self.label_5.setChecked(False)

    def set3(self):
        self.count_data = 3
        self.label_0.setChecked(False)
        self.label_1.setChecked(False)
        self.label_2.setChecked(False)
        self.label_3.setChecked(True)
        self.label_4.setChecked(False)
        self.label_5.setChecked(False)

    def set4(self):
        self.count_data = 4
        self.label_0.setChecked(False)
        self.label_1.setChecked(False)
        self.label_2.setChecked(False)
        self.label_3.setChecked(False)
        self.label_4.setChecked(True)
        self.label_5.setChecked(False)

    def set5(self):
        self.count_data = 5
        self.label_0.setChecked(False)
        self.label_1.setChecked(False)
        self.label_2.setChecked(False)
        self.label_3.setChecked(False)
        self.label_4.setChecked(False)
        self.label_5.setChecked(True)

    def cam_start(self):
        try:
            self.tx = Thread_cam(self)
            self.tx.start()
        except:
            QMessageBox.warning(self, 'Warning', '[Error] Not Found Camera.')

    def cam_end(self):
        self.cam_type = False
        self.tx.quit()
        self.tx.disconnect()

    def resizeEvent(self, e):
        try:
            w = self.cam_label.size().width()
            h = self.cam_label.size().height()

            qImg = QImage(self.img.data, self.img.shape[1], self.img.shape[0], self.img.shape[1] *self.img.shape[2], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
            self.cam_label.setPixmap(pixmap)
        except:
            None

    def sensor(self):
        try:
            self.count_up = 0
            self.count_down = 0
            self.leg_status.setText('clear')
            self.x_scale = 600
            self.isRecord = False
            self.raw1 = []
            self.avg1 = []
            self.svf1 = []
            self.sav1 = []
            self.raw2 = []
            self.avg2 = []
            self.svf2 = []
            self.sav2 = []
            self.timedata = []

            self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_sock.connect((self.lineEdit.text(), 9001))
            self.server_sock.send(pickle.dumps([self.type_t, self.thres_v1[-1], self.thres_v2[-1], self.con]))
            self.sensor_data = self.server_sock.recv(200000)
            # print(self.sensor_data)

            self.data = pickle.loads(self.sensor_data)
            self.raw1 = self.data[0] * 1000
            self.avg1 = self.data[1] * 1000
            self.svf1 = self.data[2] * 1000
            self.sav1 = self.data[3] * 1000
            self.raw2 = self.data[4] * 1000
            self.avg2 = self.data[5] * 1000
            self.svf2 = self.data[6] * 1000
            self.sav2 = self.data[7] * 1000
            self.timedata = self.data[8] * 1000

            self.timer_emg = QTimer()
            self.timer_emg.timeout.connect(self.update_sensor)
            self.timer_emg.start()
        except:
            QMessageBox.warning(self, 'Warning', '포트 번호를 확인하세요.')

    def update_sensor(self):
        try:
            self.plot.clear()
            self.server_sock.send(pickle.dumps([self.type_t, self.thres_v1[-1], self.thres_v2[-1], self.con]))
            self.con = 0

            self.sensor_data = self.server_sock.recv(200000)
            self.data = pickle.loads(self.sensor_data)
            if int(self.data[9]) == 1:
                print(self.data[9])
                self.count_up = self.count_up + int(self.data[9])
                self.leg_status.setText('U : ' + str(self.count_up) + ' | D : ' + str(self.count_down))
            elif int(self.data[9]) == 2:
                self.count_down = self.count_down + int(self.data[9]-1)
                self.leg_status.setText('U : ' + str(self.count_up) + ' | D : ' + str(self.count_down))
            self.raw1.extend(self.data[0])
            self.avg1.extend(self.data[1])
            self.svf1.extend(self.data[2])
            self.sav1.extend(self.data[3])
            self.raw2.extend(self.data[4])
            self.avg2.extend(self.data[5])
            self.svf2.extend(self.data[6])
            self.sav2.extend(self.data[7])
            self.timedata.extend(self.data[8])

            del self.raw1[:10]
            del self.avg1[:10]
            del self.svf1[:10]
            del self.sav1[:10]
            del self.raw2[:10]
            del self.avg2[:10]
            del self.svf2[:10]
            del self.sav2[:10]
            # print(len(self.raw1), len(self.raw2))
            self.plot.plot(self.thres_v1[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 255, 0), width=1))
            self.plot.plot(self.thres_v2[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 255, 0), width=1))
            if self.F1.isChecked():
                self.type_t = 1
                self.plot.plot(self.raw1[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1))
                self.plot.plot(self.raw2[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 200, 255), width=1))
            elif self.F2.isChecked():
                self.type_t = 2
                self.plot.plot(self.avg1[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1))
                self.plot.plot(self.avg2[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 200, 255), width=1))
            elif self.F3.isChecked():
                self.type_t = 3
                self.plot.plot(self.svf1[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1))
                self.plot.plot(self.svf2[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 200, 255), width=1))
            elif self.F4.isChecked():
                self.type_t = 4
                self.plot.plot(self.sav1[-self.x_scale:], pen=pyqtgraph.mkPen(color=(255, 0, 0), width=1))
                self.plot.plot(self.sav2[-self.x_scale:], pen=pyqtgraph.mkPen(color=(0, 200, 255), width=1))

            self.time_text.setText(str(self.timedata[-1]))
            if self.isRecord:
                if self.count_data==0:
                    b_data = 0
                else:
                    b_data = 1
                # if self.cam_type:
                #     if self.t_i.isChecked():
                #         with open(self.windows_user_name + "/Desktop/Record/" + self.timestr + "/" + self.data[8] + ".jpg", mode='w+b') as a:
                #             print(self.n)
                #             self.n.tofile(a)
                for i in range(10):
                    self.csvf.writerow([self.raw1[-10+i], self.avg1[-10+i], self.svf1[-10+i], self.sav1[-10+i], self.raw2[-10+i], self.avg2[-10+i], self.svf2[-10+i], self.sav2[-10+i], self.thres_v1[-10+i], self.thres_v2[-10+i], self.timedata[-10+i]])

        except:
            self.timer_emg.stop()
            self.server_sock.close()
            QMessageBox.warning(self, 'Warning', 'Disconnected !!!')

    def close_sensor(self):
        self.timer_emg.stop()
        self.server_sock.close()

    def record_start(self):
        self.isRecord = True
        self.rc1.setText('Recording...')
        self.timestr = time.strftime("%Y%m%d_%H%M%S")
        # if self.t_v_2.isChecked():
        #     print(self.reframe)
        #     self.out = cv2.VideoWriter(self.windows_user_name + "/Desktop/Record/" + self.timestr + '.avi', self.fourcc, self.fps, (self.w, self.h))
        os.makedirs(self.windows_user_name + "/Desktop/Record/", exist_ok=True)
        # if self.t_i.isChecked():
        #     os.makedirs(self.windows_user_name + "/Desktop/Record/" + self.timestr + "/", exist_ok=True)
        self.f = open(self.windows_user_name + "/Desktop/Record/" + self.timestr + ".csv", "w", encoding='utf-8', newline='')
        self.csvf = csv.writer(self.f)

    def record_end(self):
        print(self.reframe)
        self.isRecord = False
        self.rc1.setText('Done')
        if self.t_v_2.isChecked():
            self.out.release()
        self.f.close()

    def auto_scale(self):
        self.plot.enableAutoRange(axis='x')
        self.plot.enableAutoRange(axis='y')

    def cal_thres(self):
        if self.F1.isChecked():
            thres1 = statistics.pstdev(self.raw1) * self.r_value
            base1 = sum(self.raw1)/len(self.raw1)
            self.t_s1.setValue(int(base1+thres1))
            self.t_v1.setValue(int(base1+thres1))
            self.thres_v1 = [int(base1+thres1)] * 1000

            thres2 = statistics.pstdev(self.raw2) * self.r_value
            base2 = sum(self.raw2)/len(self.raw2)
            self.t_s2.setValue(int(base2+thres2))
            self.t_v2.setValue(int(base2+thres2))
            self.thres_v2 = [int(base2+thres2)] * 1000
        elif self.F2.isChecked():
            thres1 = statistics.pstdev(self.avg1) * self.r_value
            base1 = sum(self.avg1)/len(self.avg1)
            self.t_s1.setValue(int(base1+thres1))
            self.t_v1.setValue(int(base1+thres1))
            self.thres_v1 = [int(base1+thres1)] * 1000

            thres2 = statistics.pstdev(self.avg2) * self.r_value
            base2 = sum(self.avg2)/len(self.avg2)
            self.t_s2.setValue(int(base2+thres2))
            self.t_v2.setValue(int(base2+thres2))
            self.thres_v2 = [int(base2+thres2)] * 1000
        elif self.F3.isChecked():
            thres1 = statistics.pstdev(self.svf1) * self.r_value
            base1 = sum(self.svf1)/len(self.svf1)
            self.t_s1.setValue(int(base1+thres1))
            self.t_v1.setValue(int(base1+thres1))
            self.thres_v1 = [int(base1+thres1)] * 1000

            thres2 = statistics.pstdev(self.svf2) * self.r_value
            base2 = sum(self.svf2)/len(self.svf2)
            self.t_s2.setValue(int(base2+thres2))
            self.t_v2.setValue(int(base2+thres2))
            self.thres_v2 = [int(base2+thres2)] * 1000
        elif self.F4.isChecked():
            thres1 = statistics.pstdev(self.sav1) * self.r_value
            base1 = sum(self.sav1)/len(self.sav1)
            self.t_s1.setValue(int(base1+thres1))
            self.t_v1.setValue(int(base1+thres1))
            self.thres_v1 = [int(base1+thres1)] * 1000

            thres2 = statistics.pstdev(self.sav2) * self.r_value
            base2 = sum(self.sav2) / len(self.sav2)
            self.t_s2.setValue(int(base2 + thres2))
            self.t_v2.setValue(int(base2 + thres2))
            self.thres_v2 = [int(base2 + thres2)] * 1000

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
        self.plot.setYRange(-self.y_scale, self.y_scale)
        self.yt.setValue(self.y_scale)

    def yt_change(self):
        self.y_scale = int(self.yt.value())
        self.plot.setYRange(-self.y_scale, self.y_scale)
        self.y_all.setValue(self.y_scale)

    def ratio_change(self):
        self.r_value = int(self.r_s.value())
        self.r_v.setValue(self.r_value)

    def ratiot_change(self):
        self.r_value = int(self.r_v.value())
        self.r_s.setValue(self.r_value)

    def thres_change1(self):
        self.t_value1 = int(self.t_s1.value())
        self.thres_v1 = [self.t_value1] * 1000
        self.t_v1.setValue(self.t_value1)

    def threst_change1(self):
        self.t_value1 = int(self.t_v1.value())
        self.thres_v1 = [self.t_value1] * 1000
        self.t_s1.setValue(self.t_value1)

    def thres_change2(self):
        self.t_value2 = int(self.t_s2.value())
        self.thres_v2 = [self.t_value2] * 1000
        self.t_v2.setValue(self.t_value2)

    def threst_change2(self):
        self.t_value2 = int(self.t_v2.value())
        self.thres_v2 = [self.t_value2] * 1000
        self.t_s2.setValue(self.t_value2)

    def run_leg(self):
        self.con = 1
        print(self.con)

    def stop_leg(self):
        self.con = 2
        print(self.con)

    def test_leg(self):
        self.con = 3
        print(self.con)


class Thread_cam(QThread):
    def __init__(self, parent):
        super(Thread_cam, self).__init__(parent)

        self.parent = parent

    def run(self):
        self.capture = cv2.VideoCapture(0)
        _, self.frame = self.capture.read()
        self.cam_type = True

        self.parent.w = round(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.parent.h = round(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.parent.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.parent.fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        while True:
            _, self.frame = self.capture.read()
            w = self.parent.cam_label.size().width()
            h = self.parent.cam_label.size().height()

            # _, self.parent.n = cv2.imencode(".png", self.frame)
            # self.frame = cv2.putText(self.frame, str(self.parent.fps) + " | " + self.parent.timedata[-1], (10, 20),
            #                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            self.img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            qImg = QImage(self.img.data, self.img.shape[1], self.img.shape[0], self.img.shape[1] * self.img.shape[2],
                          QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
            self.parent.cam_label.setPixmap(pixmap)
            # if self.parent.isRecord:
            #     if self.parent.cam_type:
            #         if self.parent.t_v_2.isChecked():
            #             self.parent.reframe = cv2.putText(self.frame, str(self.parent.fps) + " | " + self.parent.data[8], (10, 20),
            #                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
            #             self.parent.out.write(self.parent.reframe)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())