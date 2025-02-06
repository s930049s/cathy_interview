from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BrowserHelper:
    def __init__(self, browser):
        self.browser = browser

        # 預設顯式等待 10 秒
        self.wait = WebDriverWait(self.browser, 10)  

    def switch_to_new_tab(self):
        """切換到新分頁，並等待頁面完全加載"""

        # 切換到新分頁
        self.browser.switch_to.window(self.browser.window_handles[-1])
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    def wait_for_element_visible(self, by_locator):
        """等待元素可見，然後回傳該元素"""
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def wait_for_element_clickable(self, by_locator):
        """等待元素可點擊，然後回傳該元素"""
        return self.wait.until(EC.element_to_be_clickable(by_locator))