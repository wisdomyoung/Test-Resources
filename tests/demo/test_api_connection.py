import pytest
import requests
from config.setting import BASE_URL, ENV


def test_connection():
    """测试配置文件是否生效"""
    print(f"\n当前运行环境: {ENV}")
    print(f"目标基础地址: {BASE_URL}")

    # 尝试访问根路径或一个简单的端点
    # 注意：JSONPlaceholder 和 HttpBin 的根路径可能不同，我们访问一个通用的健康检查端点
    try:
        # 对于 JSONPlaceholder，/posts/1 是有效的；对于 HttpBin，/get 是有效的
        # 这里我们做一个简单的判断来适配
        if "typicode" in BASE_URL:
            endpoint="/posts/1"  # JSONPlaceholder 的一个示例接口
        else:
            endpoint="/get"  # HttpBin 的 GET 接口

        response=requests.get(f"{BASE_URL}{endpoint}", timeout=5)
        assert response.status_code == 200, f"连接失败，状态码: {response.status_code}"
        print(" 配置读取成功，网络连接正常！")
    except Exception as e:
        print(f" 网络连接异常: {e}")
        raise


if __name__ == "__main__":
    pytest.main(["-s", "test_api_connection.py"])