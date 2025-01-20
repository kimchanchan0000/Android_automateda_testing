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
import time
# coding=utf8
from time import sleep
import re
import json

from aw.Common import Common
from aw.Model import settings


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
def switch_blooth_status(driver, status_: str = 'open', start_settings=True):
    """
    打开或关闭蓝牙
    :param driver: 设备对象
    :param status_: 状态
    :param start_settings: 打开设置
    :return: None
    """
    if start_settings:
        Common.start_app(driver, settings.package_name)
        sleep(2)
    if driver(resourceId=settings.MoreSettings.id, text=settings.MoreSettings.text).wait(timeout=3):
        driver(rresourceId=settings.MoreSettings.id, text=settings.MoreSettings.text).click()
        sleep(2)
        driver(resourceId=settings.SimpleWLAN.id, text=settings.SimpleWLAN.text).click()
        sleep(2)
    if driver(resourceId="android:id/title", text="已配对的设备").wait_gone(timeout=3):
        driver.logger.info("蓝牙是关闭状态")
        if status_ == "open":
            driver(resourceId="com.android.settings:id/switch_widget").click()
            sleep(2)
        elif status_ == "close":
            driver.logger.info("蓝牙已经是关闭状态，无需再切换")
        else:
            raise ValueError("status_参数只能是open或close")
    else:
        driver.logger.info("蓝牙是打开状态")
        if status_ == "open":
            driver.logger.info("蓝牙已经是打开状态，无需再切换")
        elif status_ == "close":
            driver(resourceId="com.android.settings:id/switch_widget").click()
            sleep(2)
        else:
            raise ValueError("status_参数只能是open或close")


@checker
def check_bluetooth_status(driver, expect=True):
    """
    检查蓝牙状态
    :param driver: 设备对象
    :param expect: 期望值
    :return:
    """
    ret = False
    if driver(resourceId="android:id/title", text="已配对的设备").wait_gone(timeout=3) and not expect:
        ret = True
    if not driver(resourceId="android:id/title", text="已配对的设备").wait_gone(timeout=3) and expect:
        ret = True
    return ret


@keyword
def touch(driver, obj_meaning: str, mode: str = "normal", ignore: bool = False):
    """
       通过控件的 text, resource_id, xpath点击控件。
       - text, resource_id, xpath，查找超时时间和点击后等待响应时间 。
       - 控件优先级: text > resource_id > xpath。
       - 可通过 ignore 参数控制未找到控件时是否抛出异常。
       参数:
           driver: uiautomator2 的设备实例。
           obj_meaning: 控件的描述，作为CONST_DICT的 key。
           mode: normal点击，long长按。
           ignore: 如果未找到控件，是否抛出异常。
       """
    CONST_DICT = {
        "简易模式WLAN": [settings.SimpleWLAN.text, settings.SimpleWLAN.id, None, 2, 2],
        "简易模式蓝牙": [settings.SimpleBluetooth.text, settings.SimpleBluetooth.id, None, 2, 2],
        "简易模式移动数据": [settings.SimpleMobileData.text, settings.SimpleMobileData.id, None, 2, 2],
        "简易模式壁纸": [settings.SimpleWallpaper.text, settings.SimpleWallpaper.id, None, 2, 2],
        "简易模式安全用机": [settings.SimpleSafeUse.text, settings.SimpleSafeUse.id, None, 2, 2],
        "简易模式声音和振动": [settings.SimpleSoundAndVibration.text, settings.SimpleSoundAndVibration.id, None, 2, 2],
        "简易模式显示和亮度": [settings.SimpleDisplayAndBrightness.text, settings.SimpleDisplayAndBrightness.id, None,
                               2, 2],
        "简易模式桌面设置": [settings.SimpleDesktopSettings.text, settings.SimpleDesktopSettings.id, None, 2, 2],
        "简易模式一键优化": [settings.SimpleApplicationInprovement.text, settings.SimpleApplicationInprovement.id, None,
                             2, 2],
        "简易模式更多设置": [settings.MoreSettings.text, settings.MoreSettings.id, None, 2, 2],
        "退出简易模式": [settings.ExitSimpleMode.text, settings.ExitSimpleMode.id, None, 2, 2]
    }
    try:
        if obj_meaning not in CONST_DICT:
            raise ValueError(f"未找到描述为 '{obj_meaning}' 的控件信息")
        start_time = time.time()
        while time.time() - start_time < CONST_DICT[obj_meaning][3]:
            if CONST_DICT[obj_meaning][0] and driver(text=CONST_DICT[obj_meaning][0]).exists:
                if mode == "normal":
                    driver(text=CONST_DICT[obj_meaning][0]).click()
                elif mode == "long":
                    driver(text=CONST_DICT[obj_meaning][0]).long_click()
                    sleep(CONST_DICT[obj_meaning][4])
                print(f"成功点击了 text='{CONST_DICT[obj_meaning][0]}' 的控件")
                return True
            elif CONST_DICT[obj_meaning][1] and driver(resourceId=CONST_DICT[obj_meaning][1]).exists:
                if mode == "normal":
                    driver(resourceId=CONST_DICT[obj_meaning][1]).click()
                elif mode == "long":
                    driver(resourceId=CONST_DICT[obj_meaning][1]).long_click()
                    sleep(CONST_DICT[obj_meaning][4])
                print(f"成功点击了 resource_id='{CONST_DICT[obj_meaning][1]}' 的控件")
                return True
            elif CONST_DICT[obj_meaning][2] and driver.xpath(CONST_DICT[obj_meaning][2]).exists:
                if mode == "normal":
                    driver.xpath(CONST_DICT[obj_meaning][2]).click()
                elif mode == "long":
                    driver.xpath(CONST_DICT[obj_meaning][2]).long_click()
                    sleep(CONST_DICT[obj_meaning][4])
                print(f"成功点击了 xpath='{CONST_DICT[obj_meaning][2]}' 的控件")
                return True
            sleep(0.5)
        if ignore:
            print(f"未找到描述为 '{obj_meaning}' 的控件，跳过点击操作")
            return True
        else:
            raise ValueError(f"未找到描述为 '{obj_meaning}' 的控件，点击失败")
    except Exception as e:
        raise ValueError(f"执行点击描述为 '{obj_meaning}' 发生异常: {e}")


