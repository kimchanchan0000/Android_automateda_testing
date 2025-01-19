# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/11
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     screencap_demo_001.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
import threading
import os
import time

# 模拟长按屏幕的函数（通过adb命令）
def long_press_screen(duration):
    # adb命令：模拟长按屏幕（假设按下位置为(500, 500)）
    print("Start long press on the screen...")
    os.system("adb shell input swipe 500 500 500 500 {}".format(duration))  # 模拟长按
    print("Finished long press on the screen.")

# 模拟屏幕截图的函数（通过adb命令）
def take_screenshot():
    time.sleep(2)  # 等待2秒后截图
    print("Taking screenshot...")
    os.system("adb shell screencap /sdcard/screen_capture.png")  # 截图保存到手机
    os.system("adb pull /sdcard/screen_capture.png ./")  # 将截图拉取到本地
    print("Screenshot saved.")

# 创建并启动长按屏幕的线程
long_press_thread = threading.Thread(target=long_press_screen, args=(3000,))  # 长按3秒
# 创建并启动截图的线程
screenshot_thread = threading.Thread(target=take_screenshot)

# 启动线程
long_press_thread.start()
screenshot_thread.start()

# 等待线程完成
long_press_thread.join()
screenshot_thread.join()

print("Operation completed.")
