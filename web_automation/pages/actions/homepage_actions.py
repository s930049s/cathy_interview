from selenium.webdriver.common.by import By
from pages.locators.homepage_locators import HomePageLocators
from pages.utils.browser_helper import BrowserHelper

class HomePageActions(BrowserHelper):

    def __init__(self, browser):
        super().__init__(browser)

    def open_home_page(self, url):
        """開啟官網首頁"""
        self.browser.get("https://www.cathaybk.com.tw/cathaybk")

    def click_open_account(self):
        """點擊開戶按鈕"""
        open_account_btn = self.wait_for_element_visible((By.XPATH, HomePageLocators.OPEN_ACCOUNT_BUTTON))
        open_account_btn.click()