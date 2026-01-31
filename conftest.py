import pytest
import allure
from utils.http_client import HttpClient


# ==========================================
# 场景1：模拟“登录”操作
# ==========================================
@pytest.fixture(scope="session", autouse=True)
def login_fixture():
    """
    scope="session": 整个测试过程只执行一次
    autouse=True: 自动执行，不需要在用例参数里写
    """
    with allure.step("【全局固件】执行登录操作"):
        # 这里模拟登录，获取 token
        print("模拟登录中...")
        token="mock_token_123456"  # 模拟的token
        # 将 token 传递给测试用例
        yield token
        print("测试结束，执行登出或清理操作")


# ==========================================
# 场景2：模拟“测试数据准备”
# ==========================================
@pytest.fixture(params=[1, 2, 3], ids=["小张", "小李", "小王"])
def user_data(request):
    """
    参数化 Fixture
    request.param 会依次获取列表中的值
    """
    print(f"\n准备用户数据: {request.param}")
    yield request.param
    print(f"清理用户数据: {request.param}")

@pytest.fixture(scope="function")
def api_client():
    client = HttpClient()
    yield client
    # 改进：防止 teardown 报错影响测试结果
    try:
        client.session.close()
    except Exception as e:
        # 可以选择记录日志，或者直接忽略
        print(f"清理 session 时发生异常，但忽略它: {e}")
        pass