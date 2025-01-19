# -*- coding: utf-8 -*-
"""
# ==========================ScriptDataBegin============================================
@Date:     2025/01/13
@Author:   Administrator
@Email:    jincan5@h-partners.com
@File:     settings.py
@Function: 
@Record:   
@Remark:    
# ==========================ScriptDataEnd==============================================
"""


class Settings:
    package_name = 'com.android.settings'
    activity_name = package_name + '.Settings'
    app_name = '设置'

    # 简易模式一级菜单
    class SimpleWLAN:
        text = 'WLAN'
        id = 'com.android.settings:id/ItemText'

    class SimpleMobileData:
        text = '移动数据'
        id = 'com.android.settings:id/ItemText'

    class SimpleBluetooth:
        text = '蓝牙'
        id = 'com.android.settings:id/ItemText'

    class SimpleWallpaper:
        text = '壁纸'
        id = 'com.android.settings:id/ItemText'

    class SimpleSafeUse:
        text = '安全用机'
        id = 'com.android.settings:id/ItemText'

    class SimpleSoundAndVibration:
        text = '声音和振动'
        id = 'com.android.settings:id/ItemText'

    class SimpleDisplayAndBrightness:
        text = '显示和亮度'
        id = 'com.android.settings:id/ItemText'

    class SimpleDesktopSettings:
        text = '桌面设置'
        id = 'com.android.settings:id/ItemText'

    class SimpleApplicationInprovement:
        text = '一键优化'
        id = 'com.android.settings:id/ItemText'

    class ExitSimpleMode:
        text = '退出简易模式'
        id = 'com.android.settings:id/ItemText'

    class MoreSettings:
        text = '更多设置'
        id = 'com.android.settings:id/ItemText'

    # 一级菜单
    class WLAN:
        text = 'WLAN'
        id = 'android:id/title'

    class Bluetooth:
        text = '蓝牙'
        id = 'android:id/title'

    class MobileData:
        text = '移动网络'
        id = 'android:id/title'

    class SafeUse:
        text = '超级终端'
        id = 'android:id/title'

    class SafeUse:
        text = '更多连接'
        id = 'android:id/title'

    class Wallpaper:
        text = '桌面和个性化'
        id = 'android:id/title'

    class DisplayAndBrightness:
        text = '显示和亮度'
        id = 'android:id/title'

    class SoundAndVibration:
        text = '声音和振动'
        id = 'android:id/title'

    class NotificationAndStatusBar:
        text = '通知和状态栏'
        id = 'android:id/title'

    class ScreenLock:
        text = '生物识别和密码'
        id = 'android:id/title'

    class ApplicationAndService:
        text = '应用和服务'
        id = 'android:id/title'

    class Battery:
        text = '电池'
        id = 'android:id/title'

    class Save:
        text = '存储'
        id = 'android:id/title'

    class Safety:
        text = '安全'
        id = 'android:id/title'

    class Privacy:
        text = '隐私'
        id = 'android:id/title'

    class HealthUsePhone:
        text = '健康使用手机'
        id = 'android:id/title'

    class IntelligentAssistant:
        text = '智慧助手'
        id = 'android:id/title'

    class WalletAndPayment:
        text = '钱包和支付'
        id = 'android:id/title'

    class AssistiveFunction:
        text = '辅助功能'
        id = 'android:id/title'

    class UserAndAccount:
        text = '用户和账户'
        id = 'android:id/title'

    class HMSCore:
        text = 'HMS Core'
        id = 'android:id/title'

    class Google:
        text = 'Google'
        id = 'android:id/title'

    class SystemAndUpdate:
        text = '系统和更新'
        id = 'android:id/title'

    class AboutPhone:
        text = '关于手机'
        id = 'android:id/title'

    class DragHere:
        text = '拖到这里'
        id = 'com.huawei.distributedpasteboard:id/drag_hint_text_view'
