# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     driver.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
# utils/driver.py

import uiautomator2 as u2
from config.config import DEVICE_SN


def init_driver():
    driver = u2.connect_usb(DEVICE_SN)  # 连接设备
    driver.wait_timeout = 10  # 设置超时时间
    driver.logger.info(f"Device SN: {driver.serial}")
    return driver
