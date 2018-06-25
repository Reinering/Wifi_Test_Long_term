import pywifi
import time
import subprocess

# wifi = pywifi.PyWiFi()
#
# print(wifi.interfaces())
#
# print(time.time())

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



ssidList = ["BZTV-C2E7C0", "BZTV-C2FAA0", "BZTV-C353C0", "BZTV-C37408", "BZTV-C37410", "BZTV-C3A118", "BZTV-C3A178", "BZTV-C504A8", "BZTV-C50568", "BZTV-C51330", "BZTV-1F0035", "BZTV-test1", "BZTV-test12"]

wifi = pywifi.PyWiFi()
wifiInt = wifi.interfaces()[0]
wifiInt.disconnect()
time.sleep(1)
assert wifiInt.status() in \
       [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]

for ssid in ssidList:
    profile = pywifi.Profile()  # 创建wifi链接文件
    profile.ssid = ssid # wifi名称
    profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放，
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = "96123123"  # 密码

    # self.wifiInt.remove_all_network_profiles()  # 删除所有的wifi文件
    wifiInt.remove_network_profile(ssid)  # 删除wifi文件
    tmp_profile = wifiInt.add_network_profile(profile)  # 设定新的链接文件
    wifiInt.connect(tmp_profile)  # 链接
    time.sleep(5)
    if wifiInt.status() == pywifi.const.IFACE_CONNECTED:  # 判断是否连接上
        isOK = True
        if getLinkState("192.168.18.1"):
            print("Ping测成功")

    else:
        isOK = False
    wifiInt.disconnect()  # 断开

    # 检查断开状态
    try:
        assert wifiInt.status() in \
               [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]
    except AssertionError as e:
        print(e)
    print(isOK)


