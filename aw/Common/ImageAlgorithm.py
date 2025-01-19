# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     ImageAlgorithm.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
import json
import numpy as np
import requests
import cv2
import pytesseract
from PIL import Image

# 配置 Tesseract 的安装路径
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

URL = "https://www.google.com"
URL_BACKUP = "http://www.google.com"


def keyword(func):
    func.keyword_name = func.__name__

    def wrapper(*args, **kwargs):
        print(f"Executing Keyword: \n{func.keyword_name.capitalize().strip()}")
        return func(*args, **kwargs)

    return wrapper


def checker(func):
    func.checkepr_name = func.__name__

    def wrapper(*args, **kwargs):
        print(f"Executing Checker: \n{func.checkepr_name.capitalize().strip()}")
        result = func(*args, **kwargs)
        if not result:
            raise AssertionError(f"Check Failed in {func.__name__.capitalize()}")
        print(f"Check Passed: {func.__name__.capitalize()}")
        return result

    return wrapper


def string_distance(str1, str2):
    pass


@keyword
def get_text_position(image_path, keyword, fuzzy=True, min_distance=0):
    """
    # 获取图片中目标字符的坐标位置
    :param image_path: 图像路径/图像
    :param keyword: 目标字符
    :param fuzzy: 是否模糊匹配字符(忽略大小写与空格)
    :param min_distance: 采用最短编辑距离进行模糊匹配
    :return: 目标字符坐标位置(x, y)
    """
    try:
        payload = {'compress': 960}
        files = {'file': open(image_path, 'rb')}
        headers = {}
        try:
            response = requests.request("POST", url=URL, headers=headers, data=payload, files=files, timeout=200)
        except Exception as e:
            print(e)
            response = requests.request("POST", url=URL_BACKUP, headers=headers, data=payload, files=files, timeout=200)
        tmp_response = response.text
        json_text = json.loads(tmp_response)
        tmp_text = json_text["data"]["raw_out"]
        print(tmp_text)
        if len(tmp_text) == 1 and "长边过长" in tmp_text[0]:
            print("图片reize后长边过长，请调整短边尺寸!")
            return None
        value_tmp = None
        for i in tmp_text:
            key = i[1][3:]
        if fuzzy:
            keyword = keyword.replace(' ', '').lower()
            key = key.replace(' ', '').lower()
            key = key.replace('o', '0').replace(',', '.')
        if min_distance == 0:
            if keyword == key:
                value_a_x = i[0][0][0]
                value_a_y = i[0][0][1]
                value_b_x = i[0][2][0]
                value_b_y = i[0][2][1]
                x = int((value_b_x - value_a_x) / 2 + value_a_x)
                y = int((value_b_y - value_a_y) / 2 + value_a_y)
                value_tmp = (x, y)
            else:
                str_distance = string_distance(key, keyword)
                if str_distance <= min_distance:
                    value_a_x = i[0][0][0]
                    value_a_y = i[0][0][1]
                    value_b_x = i[0][2][0]
                    value_b_y = i[0][2][1]
                    x = int((value_b_x - value_a_x) / 2 + value_a_x)
                    y = int((value_b_y - value_a_y) / 2 + value_a_y)
                    value_tmp = (x, y)
                if value_tmp is not None:
                    position = (value_tmp[0], value_tmp[1])
                    print('目标文本出现坐标为: ', position)
                    return position
                else:
                    return None
    except Exception as e:
        print('ImageAlgorithm Exception', e)
        return None


@keyword
def detect_blur(image_path, region=None, threshold=100):
    """
    检测图像是否模糊。
    :param image_path: 图像文件路径
    :param region: 检测区域 (x, y, w, h)，如果为 None 则检测整个图像
    :param threshold: 拉普拉斯方差阈值，低于此值认为图像模糊
    :return: 是否模糊（True/False）、模糊程度
    # 示例调用
    image_path = "screen.png"  # 替换为手机截图路径
    region = (100, 200, 300, 400)  # 替换为具体的检测区域
    threshold = 150
    is_blur, blur_value = detect_blur(image_path, region, threshold)
    if is_blur:
        print(f"该区域模糊，模糊程度: {blur_value:.2f}")
    else:
        print(f"该区域清晰，清晰度: {blur_value:.2f}")
    """
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if region:
        x, y, w, h = region
        image = image[y:y + h, x:x + w]  # 裁剪检测区域
    # 计算拉普拉斯方差
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    variance = laplacian.var()
    # 判断是否模糊
    is_blur = variance < threshold
    return is_blur, variance


@keyword
def detect_highlight(image_path, region=None, brightness_threshold=200):
    """
    检测图像某区域是否高亮。
    :param image_path: 图像文件路径
    :param region: 检测区域 (x, y, w, h)，如果为 None 则检测整个图像
    :param brightness_threshold: 判断高亮的亮度阈值，默认 200
    :return: 是否高亮（True/False）、平均亮度
    # 示例调用
    image_path = "screen.png"  # 替换为手机截图路径
    region = (100, 200, 300, 400)  # 替换为具体的检测区域
    brightness_threshold = 200  # 设置亮度阈值

    is_highlight, avg_brightness = detect_highlight(image_path, region, brightness_threshold)
    if is_highlight:
        print(f"该区域高亮显示，平均亮度: {avg_brightness:.2f}")
    else:
        print(f"该区域未高亮，平均亮度: {avg_brightness:.2f}")
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("无法读取图像，请检查路径是否正确！")
    # 转换为 HSV 色彩空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    v_channel = hsv_image[:, :, 2]  # 提取 V 通道（亮度）
    if region:
        x, y, w, h = region
        v_channel = v_channel[y:y + h, x:x + w]  # 裁剪检测区域
    # 计算区域的平均亮度
    average_brightness = np.mean(v_channel)
    # 判断是否高亮
    is_highlight = average_brightness > brightness_threshold
    return is_highlight, average_brightness


@keyword
def find_text_position(image_path, keyword):
    """
    从图像中查找文字关键字的位置。
    :param image_path: 图像文件路径
    :param keyword: 要查找的关键字
    :return: 关键字的位置信息 [(x, y, w, h), ...]，如果未找到返回空列表
    # 示例调用
    image_path = "screen.png"  # 替换为手机页面截图路径
    keyword = "关键字"  # 替换为需要查找的文字

    positions = find_text_position(image_path, keyword)

    一：查找关键字位置
    # 查找关键字位置
    if positions:
        for pos in positions:
            print(f"关键字 '{keyword}' 位于: x={pos[0]}, y={pos[1]}, 宽度={pos[2]}, 高度={pos[3]}")
    else:
        print(f"未找到关键字 '{keyword}'")

    二：可视化关键字位置
    # 可视化关键字位置
    for pos in positions:
        x, y, w, h = pos
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Highlighted", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("无法读取图像，请检查路径是否正确！")
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 使用 pytesseract 进行文字识别
    boxes = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    positions = []
    for i in range(len(boxes["text"])):
        if keyword in boxes["text"][i]:  # 匹配关键字
            x, y, w, h = boxes["left"][i], boxes["top"][i], boxes["width"][i], boxes["height"][i]
            positions.append((x, y, w, h))
    return positions
