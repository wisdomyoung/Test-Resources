import os

# 1. 项目根路径
# __file__ 是当前文件的路径，abspath 是绝对路径，dirname 是上级目录
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. 环境配置 (只需修改这里即可切换环境)
ENV = "test"   # 测试环境：使用 JSONPlaceholder (模拟数据)
# ENV = "dev"      # 开发环境：使用 HttpBin (调试请求)

# 3. 根据环境切换 URL
if ENV == "test":
    # JSONPlaceholder 是最经典的免费 API，用于练习增删改查 (CRUD)
    BASE_URL = "https://jsonplaceholder.typicode.com"
    # 这里不需要真实的数据库配置，用占位符演示
    DB_CONFIG = {"host": "mock_db_host", "port": 3306}

elif ENV == "dev":
    # HttpBin 用于练习发送各种请求（GET, POST, Headers等），它会把你的请求信息返回给你
    BASE_URL = "https://httpbin.org"
    DB_CONFIG = {"host": "localhost", "port": 3306}

else:
    # 生产环境（虽然这里只是演示，实际项目中这里填正式地址）
    BASE_URL = "https://api.yourcompany.com"
    DB_CONFIG = {"host": "prod_db_host", "port": 3306}

# --- 额外的练习常量 ---
# 为了让你的测试代码更健壮，可以在这里定义一些超时时间
TIMEOUT = 10  # 请求超时时间设为 10 秒

# 如果你以后需要 API Key，也可以放在这里统一管理
# API_KEY = "your_api_key_here"