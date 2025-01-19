# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     notepad_page.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""


# pages/memo_page.py


class NotepadPage:
    def __init__(self, driver):
        self.driver = driver

    def open_notepad_app(self):
        # 打开备忘录应用
        self.driver.app_start("om.example.android.notepad")  # 假设这是备忘录的包名

    def create_new_notepad(self, title, content):
        # 创建新的备忘录
        self.driver(resourceId="com.example.memo:id/new_note_button").click()
        self.driver(resourceId="com.example.memo:id/title_input").set_text(title)
        self.driver(resourceId="com.example.memo:id/content_input").set_text(content)
        self.driver(resourceId="com.example.memo:id/save_button").click()
