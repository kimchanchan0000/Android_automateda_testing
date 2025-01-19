# Script for managing settings and performing actions
# Author: Administrator
# Email: jincan5@h-partners.com
# Date: 2025/01/10

from time import sleep

from aw.Application import Notepad
from aw.Common import Common
from aw.Model import notepad, gallery
from utils import driver

import threading
import time

# Constants
BLUETOOTH_OPEN = "open"
BLUETOOTH_CLOSE = "close"
SCREENSHOT_TIMEOUT = 10


class Notepad_004:
    def __init__(self):
        self.driver = driver.init_driver()

    def set_up(self):
        print("Setting up...")
        package_name1 = "com.baidu.input_huawei"
        self.driver.shell(f'pm disable {package_name1}')
        sleep(3)

    def process(self):
        try:
            def drag_and_hold_image():
                global keep_holding
                keep_holding = True  # 用于控制长按状态
                image = self.driver(resourceId=gallery.BigPicThumbnail.id)
                global start_x, start_y
                global x, y
                start_x, start_y = image.center()
                x, y = self.driver.window_size()[0] * 0.5, self.driver.window_size()[1] * 0.3
                self.driver.swipe(start_x, start_y, x, y, duration=1.0)
                while keep_holding:
                    self.driver.touch.down(x, y)  # 模拟持续长按
                    sleep(0.1)

            def create_note():
                global keep_holding
                Common.start_app(self.driver, notepad.package_name)
                Notepad.touch(self.driver, '新建笔记按钮', ignore=True)
                if not self.driver(description=notepad.CreateNewNote.desc).exists:
                    keep_holding = False
                    self.driver.touch.up(x, y)  # 松手操作

            # 创建并启动线程
            drag_thread = threading.Thread(target=drag_and_hold_image)
            note_thread = threading.Thread(target=create_note)
            drag_thread.start()
            note_thread.start()
            drag_thread.join()
            note_thread.join()
        except Exception as e:
            self.driver.logger.error(f"An error occurred: {e}")

    def teardown(self):
        print("Tearing down...")
        self.driver.logger.info("Resetting notepad")


def main():
    setting = Notepad_004()
    setting.set_up()
    setting.process()
    setting.teardown()


if __name__ == '__main__':
    main()
