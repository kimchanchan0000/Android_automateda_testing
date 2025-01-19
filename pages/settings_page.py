# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     settings_page.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""


# pages/settings_page.py


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def open_wifi_settings(self):
        # 找到并点击 WiFi 设置按钮
        wifi_button = self.driver(resourceId="com.android.settings:id/wifi")
        wifi_button.click()

    def enable_wifi(self):
        # 启用 WiFi
        wifi_switch = self.driver(resourceId="com.android.settings:id/switch_widget")
        if wifi_switch.text == "关闭":
            wifi_switch.click()
