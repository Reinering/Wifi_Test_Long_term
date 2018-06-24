import pywifi
import time

wifi = pywifi.PyWiFi()

print(wifi.interfaces())

print(time.time())