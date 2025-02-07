from pages.actions.homepage_actions import HomePageActions
from pages.actions.account_page_actions import AccountPageActions
from pages.actions.download_page_actions import DownloadPageActions
from pages.utils.browser_helper import BrowserHelper

def test_cathay_open_account(browser):
    """測試線上開戶流程"""
    homepage = HomePageActions(browser)
    account_page = AccountPageActions(browser)
    download_page = DownloadPageActions(browser)  
    browser_helper = BrowserHelper(browser)

    # 開啟官網
    homepage.open_home_page("https://www.cathaybk.com.tw/cathaybk")
    assert "國泰世華" in browser.title, "未成功進入官網"
    
    # 點擊開戶按鈕
    homepage.click_open_account()

    # 記錄當前的分頁數量
    previous_tabs = len(browser.window_handles)
    
    # 點擊下載CUBE App按鈕
    account_page.click_download_cube_app()
    
    # 切換到新分頁
    browser_helper.wait_for_new_tab(previous_tabs)
    browser_helper.switch_to_new_tab()
    assert "CUBE App" in browser.title, "未跳轉至下載頁面"
    
    # 驗證 QR Code 尺寸
    download_page.validate_qr_code()  
    
    # 驗證 Android 與 iOS 版本一致
    download_page.validate_versions()

def test_cathay_mobile_qr_hidden(browser):
    """測試轉換mweb後，並確認 QR Code 是否隱藏"""
    
    homepage = HomePageActions(browser)
    account_page = AccountPageActions(browser)
    download_page = DownloadPageActions(browser)
    browser_helper = BrowserHelper(browser)

    # 開啟官網
    homepage.open_home_page("https://www.cathaybk.com.tw/cathaybk")
    assert "國泰世華" in browser.title, "未成功進入官網"

    # 點擊開戶按鈕
    homepage.click_open_account()

    # 記錄當前的分頁數量
    previous_tabs = len(browser.window_handles)

    # 點擊下載CUBE App按鈕
    account_page.click_download_cube_app()

    # 切換到新分頁，等待頁面完全載入
    browser_helper.wait_for_new_tab(previous_tabs)
    browser_helper.switch_to_new_tab()
    assert "CUBE App" in browser.title, "未跳轉至下載頁面"
    
    # 切換到行動版
    download_page.switch_to_mobile_view()

    # 驗證 QR Code 是否隱藏
    download_page.validate_qr_hidden()