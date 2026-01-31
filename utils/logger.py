# 文件路径: utils/logger.py

import os
import logging
from datetime import datetime

def setup_logger():
    """配置并返回一个logger实例"""
    # 1. 创建 logs 目录
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # 2. 生成带日期的日志文件名
    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y%m%d')}.log")

    # 3. 配置日志格式
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 4. 创建文件处理器
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # 5. 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # 6. 创建 logger 实例
    logger = logging.getLogger("AutoTestLogger")
    logger.setLevel(logging.DEBUG) # 设置最低捕获级别
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 防止日志重复输出 (重要！)
    logger.propagate = False

    return logger

# 实例化一个 logger 供外部导入使用
logger = setup_logger()