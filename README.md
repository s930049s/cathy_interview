# 自動化測試專案 - Selenium + Pytest

專案使用 **Selenium + Pytest** 來進行自動化測試，並支援 **桌面版 / 行動版測試**

## 功能
 **Selenium + Pytest** - UI 測試框架  
 **行動版測試支援** - 可模擬行動裝置檢查 QR Code 顯示狀況  
 **Page Object Model (POM)** - 讓測試更易於維護  

---

## 目錄結構
```plaintext
project/
│
├── pages/                           # 存放 Page Object Model
│   ├── locators/                    # 存放所有定位器
│   │   ├── homepage_locators.py
│   │   ├── account_page_locators.py
│   │   ├── download_page_locators.py
│   │
│   ├── actions/                     # 存放所有操作方法
│   │   ├── homepage_actions.py
│   │   ├── account_page_actions.py
│   │   ├── download_page_actions.py
│   │
│   ├── utils/                       # 存放共用工具類
│   │   ├── browser_helper.py        # WebDriver 共用函數 (切換分頁、等待載入等)
│   │   ├── logging_config.py        # 設定 logging，讓測試輸出更清楚
│
├── tests/                           # 測試腳本
│   ├── test_cathay_open_account.py  # 測試桌開戶流程
│   ├── test_cathay_mobile_qr.py     # 測試行動版 QR Code 是否隱藏
│
├── conftest.py                      # pytest 設定檔
├── requirements.txt                 # 依賴套件
├── pytest.ini                        # pytest 配置
└── README.md                         # 本文件
```

## ⚙️ 安裝與環境設定
1️⃣ 安裝 Python 及 Virtual Environment
請確保你已安裝 Python 3，並使用 venv 建立虛擬環境：

# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2️⃣ 安裝必要套件
在虛擬環境內執行：
pip install -r requirements.txt

3️⃣ 下載 ChromeDriver
請確保你的 ChromeDriver 版本與 Google Chrome 瀏覽器相符：

# 檢查 Chrome 版本
chrome --version

# 檢查 ChromeDriver 版本
chromedriver --version

▶️ 執行測試
測試桌面版開戶流程:
pytest tests/test_cathay_open_account.py -s

測試行動版 QR Code 是否隱藏:
pytest tests/test_cathay_mobile_qr.py -s

產生測試報告
pytest --html=report.html --self-contained-html
