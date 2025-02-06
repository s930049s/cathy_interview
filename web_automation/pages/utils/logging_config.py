import logging

def setup_logging():
    """設定 logging，只輸出到終端"""
    logging.basicConfig(

        # 記錄 INFO 級別以上的日誌
        level=logging.INFO,  
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",

        # 只輸出到終端
        handlers=[logging.StreamHandler()]  
    )
    logging.info("Logging 設定完成 (僅輸出到終端)")