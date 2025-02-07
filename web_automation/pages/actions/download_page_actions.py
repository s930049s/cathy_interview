from selenium.webdriver.common.by import By
from pages.locators.download_page_locators import DownloadPageLocators
from pages.utils.browser_helper import BrowserHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class DownloadPageActions:

    def __init__(self, browser):
        """初始化並保存 WebDriver"""
        self.browser = browser

    def validate_qr_code(self):
        """驗證 QR Code 尺寸"""

        qr_code = self.browser.find_element(By.XPATH, DownloadPageLocators.QR_CODE)
        assert qr_code.size['width'] == 160 and qr_code.size['height'] == 160, "QR Code 尺寸不正確"

    def validate_versions(self):
        """驗證 Android 和 iOS 版本一致"""

        android_version_text = self.browser.find_element(By.XPATH, DownloadPageLocators.ANDROID_VERSION).text
        ios_version_text = self.browser.find_element(By.XPATH, DownloadPageLocators.IOS_VERSION).text

        # 取最後的數字部分
        android_version = android_version_text.partition("：")[2].strip()
        ios_version = ios_version_text.partition("：")[2].strip()

        # 紀錄版本號
        logging.info(f"取得 Android 版本: {android_version}")
        logging.info(f"取得 iOS 版本: {ios_version}")

        # 驗證版本是否一致
        assert android_version == ios_version, "Android 和 iOS 版本不一致"

    def switch_to_mobile_view(self):
        """使用 Chrome DevTools Protocol 切換到行動版模式"""

        self.browser.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": 390,
            "height": 844,
            "deviceScaleFactor": 3.0,
            "mobile": True
        })
        self.browser.execute_cdp_cmd("Emulation.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/537.36"
        })
        logging.info("已切換為行動版模式")

    def validate_qr_hidden(self):
        """確認 QR Code 是否隱藏"""

        wait = WebDriverWait(self.browser, 10)
        try:
            qr_code = wait.until(EC.invisibility_of_element_located((By.XPATH, DownloadPageLocators.QR_CODE)))
            logging.info("QR Code 在行動版模式下成功隱藏")

        except:
            logging.error("QR Code 在行動版模式下仍然可見")

            assert False, "QR Code 沒有隱藏！"