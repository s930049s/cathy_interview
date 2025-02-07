from selenium.webdriver.common.by import By
from pages.locators.account_page_locators import AccountPageLocators
from pages.utils.browser_helper import BrowserHelper

class AccountPageActions(BrowserHelper):
    
    def __init__(self, browser):
        super().__init__(browser)

    def click_download_cube_app(self):
        """點擊下載CUBE App按鈕"""

        download_btn = self.wait_for_element_visible((By.XPATH, AccountPageLocators.DOWNLOAD_CUBE_APP_BUTTON))
        download_btn.click()