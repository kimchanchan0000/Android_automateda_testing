# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/10
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     Camera_001.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""
import cv2
import uiautomator2 as u2
from time import sleep


from aw.Common import Common, ImageAlgorithm
from PIL import Image
import pytesseract

d = u2.connect_usb('GCQ5T19312003093')

image_path = "screen.png"  # 替换为手机页面截图路径
keyword = "Facebook"  # 替换为需要查找的文字

positions = ImageAlgorithm.find_text_position(image_path, keyword)
if positions:
    # 查找关键字位置
#     for pos in positions:
#         print(f"关键字 '{keyword}' 位于: x={pos[0]}, y={pos[1]}, 宽度={pos[2]}, 高度={pos[3]}")
# else:
#     print(f"未找到关键字 '{keyword}'")

    # 可视化关键字位置
    # 首先读取图像
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("无法读取图像，请检查路径是否正确！")
    for pos in positions:
        x, y, w, h = pos
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Highlighted", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
