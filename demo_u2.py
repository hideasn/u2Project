import uiautomator2 as u2

# 连接设备

d = u2.connect()

print(d.device_info)

# 获取当前应用信息
print(d.app_current())

# 通过package名启动