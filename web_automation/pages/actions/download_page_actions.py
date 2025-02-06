from selenium.webdriver.common.by import By
from pages.locators.download_page_locators import DownloadPageLocators
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