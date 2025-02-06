import pytest
import logging
from selenium import webdriver
from pages.utils.logging_config import setup_logging

@pytest.fixture(scope="function")
def browser():
    """設置 WebDriver"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def initialize_logging():
    """初始化 logging (使用 logging_config.py 的設定)"""
    setup_logging()