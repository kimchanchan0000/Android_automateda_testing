# Script for managing settings and performing actions
# Author: Administrator
# Email: jincan5@h-partners.com
# Date: 2025/01/10

from time import sleep

from aw.Application import Settings
from aw.Common import Common
from aw.Model import settings
from utils import driver

# Constants
BLUETOOTH_OPEN = "open"
BLUETOOTH_CLOSE = "close"
SCREENSHOT_TIMEOUT = 10


class Settings_001:
    def __init__(self):
        self.driver = driver.init_driver()

    def set_up(self):
        print("Setting up...")

    def process(self):
        try:
            print("Executing process...")
            Settings.touch(self.driver, '简易模式WLAN')
            self.driver.logger.info("Saving settings icon and taking a screenshot")
            Common.save_app_icon(self.driver, settings.package_name, settings.app_name)
            Common.take_screenshot(timeout=SCREENSHOT_TIMEOUT)

            self.driver.logger.info("Launching settings and opening Bluetooth")
            Settings.switch_blooth_status(self.driver, status_=BLUETOOTH_OPEN, start_settings=True)
            sleep(2)

            self.driver.logger.info("Bluetooth opened successfully")
            Settings.check_bluetooth_status(self.driver, expect=True)
            sleep(2)

            self.driver.logger.info("Closing Bluetooth")
            Settings.switch_blooth_status(self.driver, status_=BLUETOOTH_CLOSE, start_settings=False)
            sleep(2)

            self.driver.logger.info("Bluetooth closed successfully")
            Settings.check_bluetooth_status(self.driver, expect=False)
            sleep(2)

            self.driver.logger.info("Taking a screenshot")
            Common.take_screenshot()
        except Exception as e:
            self.driver.logger.error(f"An error occurred: {e}")

    def teardown(self):
        print("Tearing down...")
        self.driver.logger.info("Resetting settings")
        Common.setup_app(self.driver, settings.package_name)


def main():
    setting = Settings_001()
    setting.set_up()
    setting.process()
    setting.teardown()


if __name__ == '__main__':
    main()
