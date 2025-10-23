#!/usr/bin/python3
print("Hello world")

import psutil

# 取得 CPU 使用率（更新間隔 1 秒）
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# 取得記憶體資訊
mem = psutil.virtual_memory()
print(f"Total Memory: {mem.total / (1024**3):.2f} GB")
print(f"Used Memory: {mem.used / (1024**3):.2f} GB")
print(f"Memory Usage: {mem.percent}%")

# 取得磁碟使用狀況（根目錄 /）
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024**3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024**3):.2f} GB")
print(f"Disk Usage: {disk.percent}%")
