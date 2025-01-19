# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     test_notepad_002.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
# tests/test_notepad_002.py

import pytest
from utils.driver import init_driver
from pages.notepad_page import NotepadPage


@pytest.fixture(scope="module")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()


def test_create_new_memo(driver):
    memo_page = NotepadPage(driver)

    # 打开备忘录应用
    memo_page.open_notepad_app()

    # 创建新备忘录
    memo_page.create_new_notepad("Test Title", "This is a test memo.")

    # 确认备忘录是否成功保存
    # 这里假设保存后的界面会有一个标题文本框
    saved_title = driver(resourceId="com.example.memo:id/title_input").text
    assert saved_title == "Test Title"
