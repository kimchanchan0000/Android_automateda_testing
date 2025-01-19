# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     test_settings_002.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
# tests/test_settings_002.py

import pytest
from utils.driver import init_driver
from pages.settings_page import SettingsPage


@pytest.fixture(scope="module")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()


def test_enable_wifi(driver):
    settings_page = SettingsPage(driver)

    # 打开设置 -> WiFi 设置
    settings_page.open_wifi_settings()

    # 启用 WiFi
    settings_page.enable_wifi()

    # 确认 WiFi 开启
    wifi_switch = driver(resourceId="com.android.settings:id/switch_widget")
    assert wifi_switch.text == "开启"
