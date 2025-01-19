# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/13
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     notepad.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""


class Notepad:
    package_name = 'com.example.android.notepad'
    activity_name = package_name + '.NotesList'

    # 简易模式一级菜单
    class CreateNewNote:
        text = None
        desc = '新建'
        id = 'com.example.android.notepad:id/fab_add'
        xpath = None
