# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     Notepad.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
import time

import uiautomator2 as u2
from time import sleep
from aw.Common import Common
from aw.Model import notepad


def keyword(func):
    func.keyword_name = func.__name__

    def wrapper(*args, **kwargs):
        print(f"Executing Keyword: {func.keyword_name.capitalize().strip()}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def checker(func):
    func.checkepr_name = func.__name__

    def wrapper(*args, **kwargs):
        print(f"Executing Checker: {func.checkepr_name.capitalize().strip()}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        if not result:
            raise AssertionError(f"Check Failed in {func.__name__.capitalize()}")
        print(f"Check Passed: {func.__name__.capitalize()}")
        return result

    return wrapper


@keyword
def touch(driver, obj_meaning: str, mode: str = "normal", ignore: bool = False):
    """
       通过控件的 text, desc, resource_id, xpath点击控件。
       - text, desc, resource_id, xpath，查找超时时间和点击后等待响应时间 。
       - 控件优先级: text > desc > resource_id > xpath。
       - 可通过 ignore 参数控制未找到控件时是否抛出异常。
       参数:
           driver: uiautomator2 的设备实例。
           obj_meaning: 控件的描述，作为CONST_DICT的 key。
           mode: normal点击，long长按。
           ignore: 如果未找到控件，是否抛出异常。
       """
    CONST_DICT = {
        "新建笔记按钮": [notepad.CreateNewNote.text, notepad.CreateNewNote.desc, notepad.CreateNewNote.id, None, 2, 2]
    }
    try:
        if obj_meaning not in CONST_DICT:
            raise ValueError(f"未找到描述为 '{obj_meaning}' 的控件信息")
        start_time = time.time()
        while time.time() - start_time < CONST_DICT[obj_meaning][4]:
            if CONST_DICT[obj_meaning][0] and driver(text=CONST_DICT[obj_meaning][0]).exists:
                if mode == "normal":
                    driver(text=CONST_DICT[obj_meaning][0]).click()
                elif mode == "long":
                    driver(text=CONST_DICT[obj_meaning][0]).long_click()
                    sleep(CONST_DICT[obj_meaning][5])
                print(f"成功点击了 text='{CONST_DICT[obj_meaning][0]}' 的控件")
                return True
            elif CONST_DICT[obj_meaning][1] and driver(description=CONST_DICT[obj_meaning][1]).exists:
                if mode == "normal":
                    driver(description=CONST_DICT[obj_meaning][1]).click()
                elif mode == "long":
                    driver(description=CONST_DICT[obj_meaning][1]).long_click()
                    sleep(CONST_DICT[obj_meaning][5])
                print(f"成功点击了 description='{CONST_DICT[obj_meaning][1]}' 的控件")
                return True
            elif CONST_DICT[obj_meaning][2] and driver(resourceId=CONST_DICT[obj_meaning][2]).exists:
                if mode == "normal":
                    driver(resourceId=CONST_DICT[obj_meaning][2]).click()
                elif mode == "long":
                    driver(resourceId=CONST_DICT[obj_meaning][2]).long_click()
                    sleep(CONST_DICT[obj_meaning][5])
                print(f"成功点击了 resource_id='{CONST_DICT[obj_meaning][2]}' 的控件")
                return True
            elif CONST_DICT[obj_meaning][3] and driver.xpath(CONST_DICT[obj_meaning][3]).exists:
                if mode == "normal":
                    driver.xpath(CONST_DICT[obj_meaning][3]).click()
                elif mode == "long":
                    driver.xpath(CONST_DICT[obj_meaning][3]).long_click()
                    sleep(CONST_DICT[obj_meaning][5])
                print(f"成功点击了 xpath='{CONST_DICT[obj_meaning][3]}' 的控件")
                return True
            sleep(0.5)
        if ignore:
            print(f"未找到描述为 '{obj_meaning}' 的控件，跳过点击操作")
            return True
        else:
            raise ValueError(f"未找到描述为 '{obj_meaning}' 的控件，点击失败")
    except Exception as e:
        raise ValueError(f"执行点击描述为 '{obj_meaning}' 发生异常: {e}")
