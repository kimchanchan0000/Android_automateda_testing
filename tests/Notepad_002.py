# Script for managing settings and performing actions
# Author: Administrator
# Email: jincan5@h-partners.com
# Date: 2025/01/10

from time import sleep

from aw.Common import Common
from aw.Model import notepad, gallery, settings
from utils import driver

import threading
import time

# Constants
BLUETOOTH_OPEN = "open"
BLUETOOTH_CLOSE = "close"
SCREENSHOT_TIMEOUT = 10


class Notepad_001:
    def __init__(self):
        self.driver = driver.init_driver()

    def set_up(self):
        print("Setting up...")

    def process(self):
        try:
            print("Executing process...")

            def drag_and_hold_image():
                """
                拖动图片到屏幕中心并保持长按
                """
                global keep_holding
                keep_holding = True  # 用于控制长按状态

                # 获取屏幕中心位置
                w, h = self.driver.window_size()
                x, y = w - 50, h * 0.185

                # 假设目标图片元素的标识为 "target_image"
                target_image = self.driver(resourceId=gallery.PicThumbnail.id)

                # 模拟拖动操作到屏幕中心
                self.driver.logger.info("拖动图片到屏幕中心")
                target_image.drag_to(x, y, duration=3)

                # 持续长按直到主线程完成操作
                while keep_holding:
                    sleep(0.1)

            def create_note():
                """
                打开备忘录新建笔记。
                """
                global keep_holding

                # 等待中转站出现
                self.driver.logger.info("等待中转站出现")
                for _ in range(5):
                    if self.driver(text=settings.DragHere.text).exists():
                        break
                    else:
                        sleep(2)
                        break

            for i in range(16):
                if self.driver.xpath(f'//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[{i+1}]').exists:
                    self.driver.xpath(f'//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[{i+1}]').long_click()
                    sleep(2)
                    # 创建并启动线程
                    drag_thread = threading.Thread(target=drag_and_hold_image)
                    note_thread = threading.Thread(target=create_note)

                    drag_thread.start()
                    note_thread.start()

                    drag_thread.join()
                    note_thread.join()
                    sleep(2)
        except Exception as e:
            self.driver.logger.error(f"An error occurred: {e}")

    def teardown(self):
        print("Tearing down...")
        self.driver.logger.info("Resetting notepad")


def main():
    setting = Notepad_001()
    setting.set_up()
    setting.process()
    # setting.teardown()


if __name__ == '__main__':
    main()
