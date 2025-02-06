from selenium.webdriver.common.by import By
from pages.locators.account_page_locators import AccountPageLocators

class AccountPageActions:
    
    def __init__(self, browser):
        self.browser = browser

    def click_download_cube_app(self):
        """點擊下載CUBE App按鈕"""
        download_btn = self.browser.find_element(By.XPATH, AccountPageLocators.DOWNLOAD_CUBE_APP_BUTTON)
        download_btn.click()