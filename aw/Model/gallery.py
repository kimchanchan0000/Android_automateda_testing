# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/13
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     gallery.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""


class Gallery:
    package_name = 'com.android.gallery3d'
    activity_name = package_name + '.app.GalleryActivity'

    class PicThumbnailSelected:  # 相册宫格页图片已选择状态
        id = "com.android.gallery3d:id/item_selection_on"

    class BigPicThumbnail:  # 相册大图
        id = "android:id/content"
