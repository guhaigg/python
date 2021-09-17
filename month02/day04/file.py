"""
os 模块小函数
"""
import os

print("文件大小:",os.path.getsize("./union.txt"))

print("文件夹内容:",os.listdir("."))

print("是否存在:",os.path.exists("./union.txt"))

os.remove("union.txt")