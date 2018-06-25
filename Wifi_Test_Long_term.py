# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets, QtCore
# from queue import Queue
import time
import subprocess
import pywifi

from Ui_Wifi_Test_Long_term import Ui_mainWindow


class mainWindow(QMainWindow, Ui_mainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self._translate = QtCore.QCoreApplication.translate

        self.updateSSIDList()

    def updateSSIDList(self):
        f = open("config/ssid_list.txt", "r")
        self.ssidList = f.readlines()
        f.close()
        print(self.ssidList)

        self.listWidget_ssid.clear()
        ssidCount = len(self.ssidList)
        for i in range(ssidCount):
            item = QtWidgets.QListWidgetItem()
            item.setText(self._translate("mainWindow", self.ssidList[i][:-1]))
            self.listWidget_ssid.addItem(item)




    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        self.changeWidgetState(True)
    
    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        polltime = self.spinBox_polltime.text()
        pingtime = self.spinBox_pingtime.text()
        lanip = self.lineEdit_lanip.text()
        wanip = self.lineEdit_wanip.text()


        self.wifiTestTh = WifiTestThread(self.ssid, polltime, pingtime, lanip, wanip)
        self.wifiTestTh.start()
        self.wifiTestTh.sign_textBrowser.connect(self.setTextBrowser)

        self.changeWidgetState(False)

    @pyqtSlot()
    def on_pushButton_update_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.updateSSIDList()

    def changeWidgetState(self, check):
        self.pushButton_stop.setEnabled(check)
        self.spinBox_polltime.setEnabled(not check)
        self.spinBox_pingtime.setEnabled(not check)
        self.lineEdit_lanip.setEnabled(not check)
        self.lineEdit_wanip.setEnabled(not check)
        self.pushButton_start.setEnabled(not check)
        self.pushButton_update.setEnabled(not check)

    def setTextBrowser(self, check):
        self.textBrowser.append(check)
    
    @pyqtSlot()
    def on_pushButton_savelog_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dir = QtWidgets.QFileDialog.getSaveFileName(self, "选取文件夹", "config/", "Text Files (*.txt);;All Files (*)")
        print(dir)
        log = self.textBrowser.toPlainText()
        print(log)
        f = open(dir[0], "w+")
        f.write(log)
        f.close()




class WifiTestThread(QThread):
    sign_textBrowser = QtCore.pyqtSignal(str)

    def __init__(self, ssidList, polltime, pingtime, lanip, wanip, parent=None):
        super(WifiTestThread, self).__init__(parent)
        self.stopBool = False
        self.ssidList = ssidList
        self.polltime = polltime
        self.pingtime = pingtime
        self.lanip = lanip
        self.wanip = wanip
        self.key = "96123123"


        wifi = pywifi.PyWiFi()
        self.wifiInt = wifi.interfaces()
        self.iface.disconnect()
        time.sleep(1)
        assert self.iface.status() in \
               [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]

    def run(self):
        now = time.time()
        count = 0

        while not self.stopBool:
            if time.time() >= now + self.polltime*60*count:
                for ssid in self.ssidList:
                    if not self.stopBool:
                        check = self.test_connect(ssid, self.key)
                        logtime = time.strftime("%Y%s%d%H:%M:%S: ", time.localtime())
                        if check:
                            self.sign_textBrowser.emit(logtime + "SSID: " + ssid + " 第" + str(count + 1) + "次连接成功")
                        else:
                            self.sign_textBrowser.emit(logtime + "SSID: " + ssid + " 第" + str(count + 1) + "次连接失败")


                    else:
                        break
                count += 1


    def stop(self):
        self.stopBool = True

    def test_connect(self, ssid, key):  # 测试链接

        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = ssid  # wifi名称
        profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放，
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = key  # 密码

        self.wifiInt.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = self.wifiInt.add_network_profile(profile)  # 设定新的链接文件
        self.wifiInt.connect(tmp_profile)  # 链接
        time.sleep(5)
        if self.wifiInt.status() == pywifi.const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        self.wifiInt.disconnect()  # 断开
        time.sleep(1)
        # 检查断开状态
        assert self.wifiInt.status() in \
               [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]

        return isOK

    def getLinkState(ip):
        ping_True = False
        # 运行ping程序
        num = 0
        while num < 5:
            time.sleep(1)
            p = subprocess.Popen("ping %s -w 100 -n 1" % (ip),
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)

            # 得到ping的结果
            # print(p.stdout.read())
            out = str(p.stdout.read(), encoding="gb2312", errors="ignore")
            print('ont:', out)

            # #找出丢包率，这里通过‘%’匹配
            # regex = re.compile(r'\w*%\w*')
            # packetLossRateList = regex.findall()
            if 'Request timed out' in out:
                print('Request timed out')
            elif 'General failure' in out:
                print('General failure')
            elif "Destination host unreachable" in out:
                print("Destination host unreachable")
            elif "Destination net unreachable" in out:
                print("Destination net unreachable")
            elif "丢失 = 1 " in out:
                print("丢失 = 1 ")
            elif "字节=32" in out:
                print("字节=32")
                ping_True = True
                break
            elif 'bytes=32' in out:
                print('bytes=32')
                ping_True = True
                break
            num += 1
        print(ping_True)
        return ping_True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QPixmap("pic/logo.jpg"))
    splash.show()
    ui = mainWindow()
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
    

