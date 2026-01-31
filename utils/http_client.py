import pytest
import requests
import allure
from config.setting import TIMEOUT  # 假设 TIMEOUT 是从配置文件导入的


class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.timeout = TIMEOUT
        self._closed = False

    @allure.step("发送请求: {method} {url}")
    def send_request(self, method, url, **kwargs):
        """
        发送 HTTP 请求，并自动记录到 Allure 报告。
        :param method: 请求方法 (GET, POST, etc.)
        :param url: 完整的请求 URL
        :param kwargs: 其他 requests 支持的参数，如 params, json, headers 等
        :return: requests.Response 对象
        """
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout

        try:
            # 提取关键参数用于展示
            display_params = {
                'params': kwargs.get('params'),
                'json': kwargs.get('json'),
                'headers': kwargs.get('headers'),
                'data': kwargs.get('data'),
                'timeout': kwargs['timeout']
            }
            display_params = {k: v for k, v in display_params.items() if v is not None}

            with allure.step(f"{method} {url}"):
                allure.attach(str(display_params), "请求参数", allure.attachment_type.JSON)

            response = self.session.request(method, url, **kwargs)

            allure.attach(
                response.text or "无响应内容",
                "响应结果",
                allure.attachment_type.JSON
            )
            return response

        except requests.exceptions.Timeout:
            error_msg = "❌ 请求超时！"
            print(error_msg)
            allure.attach(error_msg, "错误信息", allure.attachment_type.TEXT)
            raise
        except requests.exceptions.RequestException as e:
            error_msg = f"❌ 请求发生未知错误: {e}"
            print(error_msg)
            allure.attach(str(e), "错误信息", allure.attachment_type.TEXT)
            raise

    # --- 新增方法：显式关闭连接 ---
    def close(self):
        """
        显式关闭会话。
        这是一个好习惯，可以立即释放连接资源。
        """
        if not self._closed:
            self.session.close()
            self._closed=True
            print("🔌 HttpClient 会话已关闭")

    # --- 新增方法：析构函数（兜底保险） ---
    def __del__(self):
        """
        析构函数。
        如果用户忘记调用 close()，Python 垃圾回收时会尝试调用这个方法。
        注意：不要完全依赖 __del__ 来释放关键资源，显式调用 close() 才是正道。
        """
        self.close()

# 无状态的全局客户端，用于公共API
@pytest.fixture(scope="session")
def public_api_client():
    client = HttpClient()
    yield client
    client.close()

# 有状态的客户端，每个用例独立，用于需要登录的场景
@pytest.fixture(scope="function")
def user_api_client():
    client = HttpClient()
    yield client
    client.close()

