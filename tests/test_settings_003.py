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
from time import sleep

from aw.Application import Settings
from aw.Common import Common

import pytest
from utils.driver import init_driver
from pages.settings_page import SettingsPage


class TestSettings:
    @classmethod
    def setup_class(cls):
        """
        测试类的初始化操作，连接设备并准备测试环境。
        """
        cls.driver = init_driver()  # 初始化设备驱动
        cls.settings_page = SettingsPage(cls.driver)  # 创建页面对象实例
        print("\n[SETUP] 测试环境已初始化")

    def setup_method(self, method):
        """
        每个用例前的准备工作。
        """
        print(f"\n[SETUP] 正在准备测试用例: {method.__name__}")
        # 如果有需要清空页面状态的操作，可以在这里执行
        # 比如返回主页面或关闭应用

    def test_enable_wifi(self):
        """
        测试用例：打开 WiFi 功能
        """
        self.driver.logger.info("步骤1：")

        # 启动设置，打开蓝牙
        Settings.switch_blooth_status(self.driver, status_="open", start_settings=True)
        sleep(2)
        # 蓝牙正常打开
        Settings.check_bluetooth_status(self.driver, expect=True)
        sleep(2)
        # 关闭蓝牙
        Settings.switch_blooth_status(self.driver, status_="close")
        sleep(2)
        # 蓝牙正常关闭
        Settings.check_bluetooth_status(self.driver, expect=False)

    @classmethod
    def teardown_class(cls):
        """
        测试类的清理操作，断开设备连接并释放资源。
        """
        print("\n[TEARDOWN] 测试环境已清理")