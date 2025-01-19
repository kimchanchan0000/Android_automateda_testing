# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     Settings.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
# coding=utf8
from time import sleep
from aw.Application import Settings
from aw.Common import Common
from aw.Common.Common import project_root
from utils import driver
import json
import os

d = driver.init_driver()

# 获取json文件数据

# Get the absolute path to the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'test.json')

# Load the JSON file
with open(json_file_path, 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Get the value of the "antd" key
antd_value = data['dependencies']['antd']

print(f'The value of "antd" is: {antd_value}')

# 启动设置，打开蓝牙
Settings.switch_blooth_status(d, status_="open", start_settings=True)
sleep(2)
# 蓝牙正常打开
Settings.check_bluetooth_status(d, expect=True)
sleep(2)
# 关闭蓝牙
sleep(2)
# 蓝牙正常关闭
Settings.check_bluetooth_status(d, expect=False)
# 截图
# Common.screencap(d, project_path)
sleep(2)

# 设置初始化
Common.setup_app(d, "com.android.settings")
