# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Github\Wifi_Test_Long_term\Wifi_Test_Long_term.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(535, 600)
        mainWindow.setMinimumSize(QtCore.QSize(535, 600))
        mainWindow.setMaximumSize(QtCore.QSize(535, 600))
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.spinBox_polltime = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_polltime.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_polltime.setFont(font)
        self.spinBox_polltime.setMaximum(1440)
        self.spinBox_polltime.setObjectName("spinBox_polltime")
        self.horizontalLayout_5.addWidget(self.spinBox_polltime)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.spinBox_pingtime = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_pingtime.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.spinBox_pingtime.setFont(font)
        self.spinBox_pingtime.setMaximum(1440)
        self.spinBox_pingtime.setObjectName("spinBox_pingtime")
        self.horizontalLayout_4.addWidget(self.spinBox_pingtime)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_lanip = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_lanip.setText("")
        self.checkBox_lanip.setObjectName("checkBox_lanip")
        self.horizontalLayout_8.addWidget(self.checkBox_lanip)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_lanip = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_lanip.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_lanip.setFont(font)
        self.lineEdit_lanip.setText("")
        self.lineEdit_lanip.setObjectName("lineEdit_lanip")
        self.horizontalLayout_8.addWidget(self.lineEdit_lanip)
        self.checkBox_wanip = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_wanip.setText("")
        self.checkBox_wanip.setObjectName("checkBox_wanip")
        self.horizontalLayout_8.addWidget(self.checkBox_wanip)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_wanip = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_wanip.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_wanip.setFont(font)
        self.lineEdit_wanip.setText("")
        self.lineEdit_wanip.setObjectName("lineEdit_wanip")
        self.horizontalLayout_8.addWidget(self.lineEdit_wanip)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout.addWidget(self.pushButton_stop)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_savelog = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_savelog.setMaximumSize(QtCore.QSize(52, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_savelog.setFont(font)
        self.pushButton_savelog.setObjectName("pushButton_savelog")
        self.horizontalLayout.addWidget(self.pushButton_savelog)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(171, 351))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_update = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_2.addWidget(self.pushButton_update)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listWidget_ssid = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_ssid.setObjectName("listWidget_ssid")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_ssid.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget_ssid)
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "WIFI Long Term Test"))
        self.label.setText(_translate("mainWindow", "WIFI 长期稳定测试"))
        self.label_3.setText(_translate("mainWindow", "轮询时间设置"))
        self.label_4.setText(_translate("mainWindow", "Ping测时长"))
        self.label_5.setText(_translate("mainWindow", "LAN侧IP地址"))
        self.label_6.setText(_translate("mainWindow", "WAN侧IP地址"))
        self.pushButton_start.setText(_translate("mainWindow", "开始"))
        self.pushButton_stop.setText(_translate("mainWindow", "停止"))
        self.pushButton_savelog.setText(_translate("mainWindow", "保存log"))
        self.pushButton_update.setText(_translate("mainWindow", "更新"))
        self.label_2.setText(_translate("mainWindow", "SSID列表"))
        __sortingEnabled = self.listWidget_ssid.isSortingEnabled()
        self.listWidget_ssid.setSortingEnabled(False)
        item = self.listWidget_ssid.item(0)
        item.setText(_translate("mainWindow", "New Item"))
        self.listWidget_ssid.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

