# -*- coding: utf-8 -*-

"""
Module implementing mainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow, QMessageBox
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
        self.lanipState = False
        self.wanipState = False

        self.updateSSIDList()

    def updateSSIDList(self):
        f = None
        try:
            f = open("config/ssid_List.txt", "r")
            self.ssidList = f.readlines()
            print(self.ssidList)
            self.listWidget_ssid.clear()
            ssidCount = len(self.ssidList)
            tmpList = []
            for i in range(ssidCount):
                item = QtWidgets.QListWidgetItem()
                ssid = self.ssidList[i]
                if ssid == "\n" or ssid == "":
                    continue
                if ssid[-1] == "\n":
                    ssid = ssid[:-1]
                    tmpList.append(ssid)
                item.setText(self._translate("mainWindow", ssid))
                self.listWidget_ssid.addItem(item)
            self.ssidList = tmpList
        except Exception as e:
            warning = QMessageBox.warning(self, u"读取SSID列表文件失败", u"请确认 config/ssid_List.txt是否正确。")
            print("保存log报错: %s", e)

        finally:
            f.close()

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        polltime = self.spinBox_polltime.text()
        pingtime = self.spinBox_pingtime.text()
        lanip = ""
        wanip = ""
        if self.checkBox_lanip.checkState():
            lanip = self.lineEdit_lanip.text()
        if self.checkBox_wanip.checkState():
            wanip = self.lineEdit_wanip.text()
        print("lanip:", lanip)
        print("wanip:", wanip)


        self.wifiTestTh = WifiTestThread(self.ssidList, polltime, pingtime, lanip, wanip)
        self.wifiTestTh.sign_textBrowser.connect(self.setTextBrowser)
        self.textBrowser.clear()

        self.wifiTestTh.start()

        self.changeWidgetState(True)
    
    @pyqtSlot()
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        self.wifiTestTh.stop()
        self.changeWidgetState(False)

    @pyqtSlot()
    def on_pushButton_update_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.updateSSIDList()

    def changeWidgetState(self, checked):
        self.pushButton_stop.setEnabled(checked)
        self.spinBox_polltime.setEnabled(not checked)
        self.spinBox_pingtime.setEnabled(not checked)
        self.pushButton_start.setEnabled(not checked)
        self.pushButton_update.setEnabled(not checked)
        self.checkBox_lanip.setEnabled(not checked)
        self.checkBox_wanip.setEnabled(not checked)
        if checked:
            self.lineEdit_lanip.setEnabled(not checked)
            self.lineEdit_wanip.setEnabled(not checked)
        else:
            self.lineEdit_lanip.setEnabled(self.lanipState)
            self.lineEdit_wanip.setEnabled(self.wanipState)

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
        if dir == "":
            pass
        else:
            f = None
            try:
                f = open(dir[0], "w+")
                f.write(log)

            except Exception as e:
                warning = QMessageBox.warning(self, u"保存文件出错", u"请重新保存。")
                print("保存log报错: %s", e)
            finally:
                f.close()
    @pyqtSlot(bool)
    def on_checkBox_lanip_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        print(checked)

        self.lineEdit_lanip.setEnabled(checked)
        self.lanipState = checked
        # if not checked:
        #     self.lineEdit_lanip.clear()
    
    @pyqtSlot(bool)
    def on_checkBox_wanip_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        # TODO: not implemented yet
        print(checked)

        self.lineEdit_wanip.setEnabled(checked)
        self.wanipState = checked
        # if not checked:
        #     self.lineEdit_wanip.clear()




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



    def run(self):
        print(self.ssidList)
        self.sign_textBrowser.emit("WIFI测试开始：")

        wifi = pywifi.PyWiFi()
        self.wifiInt = wifi.interfaces()[0]
        self.wifiInt.disconnect()
        time.sleep(1)
        assert self.wifiInt.status() in \
               [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]

        now = time.time()
        count = 0

        while not self.stopBool:
            if time.time() >= now + int(self.polltime)*60*count:
                for ssid in self.ssidList:

                    if self.stopBool:
                        break
                    print("开始连接SSID：" + ssid)
                    # check = self.test_connect(ssid, self.key)

                    # self.wifiInt.remove_all_network_profiles()  # 删除所有的wifi文件
                    self.wifiInt.remove_network_profile(ssid)  # 删除wifi文件
                    profile = pywifi.Profile()  # 创建wifi链接文件
                    profile.ssid = ssid  # wifi名称
                    profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放，
                    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
                    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
                    profile.key = self.key  # 密码

                    tmp_profile = self.wifiInt.add_network_profile(profile)  # 设定新的链接文件
                    self.wifiInt.connect(tmp_profile)  # 链接
                    time.sleep(10)
                    logtime = time.strftime("%Y%m%d %H:%M:%S: ", time.localtime())
                    if self.wifiInt.status() == pywifi.const.IFACE_CONNECTED:  # 判断是否连接上
                        isOK = True
                        self.sign_textBrowser.emit(logtime + "SSID: " + ssid + " 第" + str(count + 1) + "次连接成功")

                        if self.stopBool:
                            break

                        if self.lanip != "":
                            if self.getLinkState(self.lanip):
                                self.sign_textBrowser.emit("LAN侧IP：" + self.lanip + " ping测正常")
                            else:
                                self.sign_textBrowser.emit("LAN侧IP：" + self.lanip + " ping测失败")
                        if self.wanip != "":
                            if self.getLinkState(self.wanip):
                                self.sign_textBrowser.emit("WAN侧IP：" + self.wanip + " ping测正常")
                            else:
                                self.sign_textBrowser.emit("WAN侧IP：" + self.wanip + " ping测失败")
                        time.sleep(5)

                    else:
                        isOK = False
                        self.sign_textBrowser.emit(logtime + "SSID: " + ssid + " 第" + str(count + 1) + "次连接失败")
                        print("SSID：" + ssid + " 断开连接")
                    print("isOK: " + str(isOK))

                    self.wifiInt.disconnect()  # 断开
                    # 检查断开状态
                    try:
                        assert self.wifiInt.status() in \
                               [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]
                    except AssertionError as e:
                        print(e)

                count += 1

                if int(self.polltime) > 0:
                    self.sign_textBrowser.emit("下一次轮询，请等待" + self.polltime + "分钟")

        self.sign_textBrowser.emit("WIFI测试完成")

    def stop(self):
        self.sign_textBrowser.emit("WIFI测试正在停止")
        self.stopBool = True

    def test_connect(self, ssid, key):  # 测试链接
        # self.wifiInt.remove_all_network_profiles()  # 删除所有的wifi文件
        self.wifiInt.remove_network_profile(ssid)  # 删除wifi文件

        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = ssid  # wifi名称
        profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放，
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = key  # 密码


        tmp_profile = self.wifiInt.add_network_profile(profile)  # 设定新的链接文件
        self.wifiInt.connect(tmp_profile)  # 链接
        time.sleep(5)
        if self.wifiInt.status() == pywifi.const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        print("isOK: " + str(isOK))
        return isOK

    def test_disconnect(self):
        self.wifiInt.disconnect()  # 断开

        # 检查断开状态
        try:
            assert self.wifiInt.status() in \
                   [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]
        except AssertionError as e:
            print(e)

    def getLinkState(self, ip):
        ping_True = False
        # 运行ping程序
        num = 0
        while num < 5:
            if self.stopBool:
                break
            # time.sleep(1)
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
                # break
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
    

