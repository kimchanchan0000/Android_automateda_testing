# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     Common.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
import base64
# coding=utf8
import datetime
import logging

import os
import subprocess
import time
from time import sleep
import re
import json

from aw.Model import settings

current_file_path = os.path.abspath(__file__)
aw_folder_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
project_root = os.path.abspath(os.path.join(aw_folder_path, '..'))


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
def start_app(driver, package_name):
    """
    启动App
    :param driver: 设备对象
    :param package_name: 包名
    :return: None
    """
    driver.app_start(package_name)


@keyword
def setup_app(driver, package_name):
    """
    初始化App
    :param driver: 设备对象
    :param package_name: 包名
    :return: None
    """
    driver.app_stop(package_name)


def take_screenshot(timeout=5):
    """
    截图
    :param timeout: 超时
    """
    try:
        device_name = os.popen('adb shell getprop ro.product.model').read().strip().split('-')[0]
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M')
        filename = f"{device_name}_{timestamp}.png"
        remote_path = os.path.join('/sdcard/tmp/{}'.format(filename))
        local_path = os.path.join("{}\\tmp".format(project_root), filename)

        # Take screenshot and save to device
        result = os.system(f"adb shell screencap {remote_path}")
        if result != 0:
            raise RuntimeError("Failed to take screenshot on the device")
        sleep(3)

        # Pull screenshot to local machine with timeout
        start_time = time.time()
        while time.time() - start_time < timeout:
            result_echo = os.popen(f"adb pull {remote_path} {local_path}").read()
            if '1 file pulled' in result_echo:
                print("Screenshot saved successfully")
                return True
            sleep(1)
        raise RuntimeError("Failed to pull screenshot from the device to local machine within the timeout period")

    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False


@keyword
def uitest_dump_layout(driver, screencap_=True, imgpath=None, port=9999, form='path'):
    """
    获取当前页面布局信息
    :param driver: 设备对象
    # @Param: screencap_: 是否截图
    # @Param: imgpath: 图片路径
    # @Param: port: 端口号
    # @Param: form: 返回json路径 还是返回json内容 path / content
    # @Example:Common.uitest_dump_layout(self.device1)
    """
    task_report_dir = project_root
    hierarchy_xml = driver.dump_hierarchy()
    json_path = hierarchy_xml.strip().split(':')[-1]
    driver.pull(json_path, task_report_dir)
    _, file = os.path.split(json_path)
    if screencap_:
        take_screenshot()

    driver.logger.info("filell:" + file)
    report_path = os.path.join(task_report_dir, file)
    driver.logger.info("report_path/l:." + report_path)
    if form == "path":
        return report_path
    else:
        return open(report_path, 'r', encoding='utf-8').read()


@keyword
def get_current_app(driver):
    """
    获取当前Window
    :param driver: 设备对象
    :return: 当前Window
    """
    driver.logger.info("current_app:" + str(driver.current_app()))
    return driver.current_app()


@keyword
def get_current_package(driver):
    """
    获取当前Package
    :param driver: 设备对象
    :return: 当前Package
    """
    driver.logger.info("package:" + driver.current_app()['package'])
    return driver.current_app()['package']


@keyword
def get_current_activity(driver):
    """
    获取当前Activity
    :param driver: 设备对象
    :return: 当前Activity
    """
    driver.logger.info("activity:" + driver.current_app()['activity'])
    return driver.current_app()['activity']


@keyword
def get_current_pid(driver):
    """
    获取当前PID
    :param driver: 设备对象
    :return: 当前PID
    """
    driver.logger.info("pid:" + str(driver.current_app()['pid']))
    return driver.current_app()['pid']


@keyword
def get_device_info(driver):
    """
    获取当前设备
    :param driver: 设备对象
    :return: 当前设备
    """
    driver.logger.info("device_info:" + str(driver.device_info))
    return driver.device_info


@keyword
def get_current_hierarchy(driver):
    """
    获取当前页面布局
    :param driver: 设备对象
    :return: 当前页面布局
    """
    driver.logger.info("hierarchy:" + driver.dump_hierarchy())
    return driver.dump_hierarchy()


@keyword
def get_current_window(driver):
    """
    获取当前窗口
    :param driver: 设备对象
    :return: 当前窗口
    """
    driver.logger.info("window:" + str(driver.window_size()))
    return driver.window_size()


@keyword
def get_current_orientation(driver):
    """
    获取当前设备方向
    :param driver: 设备对象
    :return: 当前设备方向
    """
    driver.logger.info("orientation:" + str(driver.orientation))
    return driver.orientation


@keyword
def get_current_network(driver):
    """
    获取当前网络状态
    :param driver: 设备对象
    :return: 当前网络状态
    """
    driver.logger.info("network:" + str(driver.network_connection))
    return driver.network_connection()


@keyword
def get_current_battery(driver):
    """
    获取当前电量
    :param driver: 设备对象
    :return: 当前电量
    """
    driver.logger.info("battery:" + str(driver.battery_info))
    return driver.battery_info


@keyword
def get_current_time(driver):
    """
    获取当前时间
    :param driver: 设备对象
    :return: 当前时间
    """
    driver.logger.info("current_time:" + str(driver.device_time))
    return driver.device_time


@keyword
def get_current_location(driver):
    """
    获取当前位置
    :param driver: 设备对象
    :return: 当前位置
    """
    driver.logger.info("location:" + str(driver.location))
    return driver.location


@keyword
def get_basic_device_info(driver):
    """
    获取当前设备信息
    :param driver: 设备对象
    :return: 当前设备信息
    """
    try:
        driver.logger.info("basic_device_info:" + str(driver.info))
    except Exception as e:
        driver.logger.info(f"Failed get_basic_device_info: {e}")
    finally:
        return driver.info


@keyword
def get_wlan_ip(driver):
    """
    获取当前设备WLAN IP
    :param driver: 设备对象
    :return: 当前设备WLAN IP
    """
    try:
        driver.logger.info("wlan_ip:" + str(driver.wlan_ip))
    except Exception as e:
        driver.logger.info(f"Failed get_wlan_ip: {e}")
    finally:
        return driver.wlan_ip


@keyword
def operate_app_session(driver, package_name, session="start"):
    """
    操作App会话
    :param driver: 设备对象
    :param package_name: 包名
    :param session: 会话
    :return: None
    """
    try:
        if session == "start":
            try:
                driver.app_start(package_name)
            except Exception as e:
                driver.logger.info(f"Failed start_app_session: {e}")
                driver.session(package_name)
        elif session == "stop":
            try:
                driver.app_stop(package_name)
            except Exception as e:
                driver.logger.info(f"Failed stop_app_session: {e}")
                sess = driver.session(package_name)
                sess.close()
        elif session == "clear":
            try:
                driver.app_clear(package_name)
            except Exception as e:
                driver.logger.info(f"Error clear_app_session: {e}")
                driver.shell('pm clear {}'.format(package_name))
        else:
            driver.logger.error("Invalid session type")
        return True
    except Exception as e:
        driver.logger.error(f"Failed operate_app_session: {e}")
        return False


@keyword
def operate_screen_status(driver, status="on"):
    """
    操作屏幕状态
    :param driver: 设备对象
    :param status: 状态
    :return: None
    """
    try:
        if status == "on":
            driver.screen_on()
        elif status == "off":
            driver.screen_off()
        else:
            driver.logger.error("Invalid screen status")
        return True
    except Exception as e:
        driver.logger.error(f"Failed operate_screen_status: {e}")
        return False


@checker
def check_screen_status(driver, status="on"):
    """
    检查屏幕状态
    :param driver: 设备对象
    :param status: 状态
    :return: True or False
    """
    try:
        if status == "on":
            return driver.info['screenOn']
        elif status == "off":
            return not driver.info['screenOn']
        else:
            driver.logger.error("Invalid screen status")
            return False
    except Exception as e:
        driver.logger.error(f"Failed check_screen_status: {e}")
        return False


@keyword
def set_screen_rotation(driver, rotation="natural"):
    """
    设置屏幕旋转
    :param driver: 设备对象
    :param rotation: 旋转
    :return: None
    """
    try:
        if rotation == "natural":
            driver.set_orientation('natural')
        elif rotation == "left":
            driver.set_orientation('left')
        elif rotation == "right":
            driver.set_orientation('right')
        else:
            driver.logger.error("Invalid screen rotation")
        return True
    except Exception as e:
        driver.logger.error(f"Failed set_screen_rotation: {e}")
        return False


@keyword
def control_screen_rotation(driver, status="enable"):
    """
    启用/禁用屏幕旋转
    :param driver: 设备对象
    :param status: enable启用
    :return: None
    """
    try:
        if status == "enable":
            driver.freeze_rotation(False)
        elif status == "disable":
            driver.freeze_rotation(True)
        else:
            driver.logger.error("Invalid screen rotation control")
        return True
    except Exception as e:
        driver.logger.error(f"Failed enable_screen_rotation: {e}")
        return False


@keyword
def open_notification(driver):
    """
    打开通知栏
    :param driver: 设备对象
    :return: None
    """
    return driver.open_notification()


@keyword
def clear_notification(driver):
    """
    清除通知中心
    :param driver: 设备对象
    :return: None
    """
    return driver.clear_notification()


@keyword
def open_control_center(driver):
    """
    打开控制中心
    :param driver: 设备对象
    :return: None
    """
    return driver.open_quick_settings()


@keyword
def get_widget_center(driver, text=None, className=None):
    """
    获取控件中心坐标
    :param driver: 设备对象
    :param text: 属性1
    :param className: 属性2
    :return: 控件中心坐标
    """
    ret = ()
    x, y = driver(text=text, className=className).center()
    if x and y:
        ret = (x, y)
    driver.logger.info(f"widget_center:{ret}")
    return ret


@checker
def check_widget_exist(driver, text=None, className=None):
    """
    检查控件是否存在
    :param driver: 设备对象
    :param text: 属性1
    :param className: 属性2
    :return: True or False
    """
    if driver(text=text, className=className).exists:
        return True
    else:
        return False


@keyword
def wait_widget_and_click(driver, text=None, className=None, timeout=3):
    """
    等待控件并点击
    :param driver: 设备对象
    :param text: 属性1
    :param className: 属性2
    :param timeout: 超时
    :return: None
    """
    try:
        driver(text=text, className=className).click_exists(timeout=timeout)
    except Exception as e:
        driver.logger.info(f"Failed wait_widget_and_click: {e}")
        pass


@keyword
def get_widget_info(driver, text=None, className=None):
    """
    获取控件信息
    :param driver: 设备对象
    :param text: 属性1
    :param className: 属性2
    :return: 控件信息
    """
    ret = {}
    try:
        widget = driver(text=text, className=className)
        if widget.exists:
            ret['text'] = widget.info['text']
            ret['className'] = widget.info['className']
            ret['bounds'] = widget.info['bounds']
            ret['center'] = widget.center()
    except Exception as e:
        driver.logger.info(f"Failed get_widget_info: {e}")
    driver.logger.info(f"widget_info:{ret}")
    return ret


@keyword
def watcher_and_click(driver, type=None, text=None):
    """
    等待控件并点击
    :param driver: 设备对象
    :param type: 类型
    :param text: 文本
    :return: None
    """
    try:
        if type == "AUTO_FC_WHEN_ANR":
            driver.watcher(f'{type}').when(text='ANR').when(text='Wait').click(text='Force Close')
        elif type == "ALERT":
            driver.watcher(f'{type}').when(text=text).click()
    except Exception as e:
        driver.logger.error(f"Failed watcher_and_click: {e}")


@keyword
def show_toast(driver, text=None):
    """
    显示Toast
    :param driver: 设备对象
    :param text: 文本
    :return: None
    """
    try:
        driver.toast.show(text, 3)
    except Exception as e:
        driver.logger.error(f"Failed show_toast: {e}")


@keyword
def get_toast(driver, text=None):
    """
    获取Toast
    :param driver: 设备对象
    :param text: 设备对象
    :return: Toast
    """
    try:
        return driver.toast.get_message(5, 10, text)
    except Exception as e:
        driver.logger.error(f"Failed get_toast: {e}")
        return None


@keyword
def get_resource_path(filename):
    """
    获取资源路径
    :param filename: 文件名称
    :return: 资源路径
    """
    for root, dirs, files in os.walk(project_root):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"{filename} not found in project directory")


@keyword
def install_app(driver, apk_name):
    """
    安装App
    :param driver: 设备对象
    :param apk_name: Apk名称
    :return: None
    """
    apk_path = get_resource_path(apk_name)
    try:
        driver.app_install(apk_path)
    except Exception as e:
        driver.logger.info(f"Failed execute driver.app_install({apk_path}): {e}")
        sub = subprocess.Popen(['adb', 'install', '-r', apk_path], shell=False, stdout=subprocess.PIPE)
        driver.logger.info(sub.stdout.readlines())


@keyword
def save_app_icon(driver, package_name, app_name):
    """
    保存App图标
    :param driver: 设备对象
    :param package_name: 包名
    :param app_name: app名
    :return: None
    """
    try:
        img = driver.app_icon(package_name)
        img_path = os.path.join("{}\\tmp".format(project_root), "{}_icon.png".format(app_name))
        driver.logger.info(f"App icon saved to {img_path}")
        return img.save(img_path)
    except Exception as e:
        driver.logger.error(f"Error saving app icon: {e}")
        return False


@keyword
def dec(encrypted_string):
    """
    解密
    :param encrypted_string: 加密字符串
    :return: 解密字符串
    """
    encrypted_bytes = encrypted_string.encode()
    decrypted_bytes = base64.b64decode(encrypted_bytes)
    decrypted_string = decrypted_bytes.decode()
    return decrypted_string


@keyword
def input_text(driver, text, clear=False):
    ""
    """ 
    输入文本
    :return: 文本
    """
    if clear:
        driver.clear_text()
    return driver.send_keys(text)


@keyword
def set_clipboard(driver, text):
    ""
    """
    设置剪贴板
    :return: 文本
    """
    return driver.set_clipboard(text)


@keyword
def enc(plain_text):
    """
    加密
    :param plain_text: 明文
    :return: 加密字符串
    """
    plain_bytes = plain_text.encode()
    encrypted_bytes = base64.b64encode(plain_bytes)
    encrypted_string = encrypted_bytes.decode()
    return encrypted_string
