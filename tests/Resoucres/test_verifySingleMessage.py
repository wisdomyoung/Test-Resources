import pytest
import allure

from config.setting import BASE_URL
from utils.logger import logger
from utils.yaml_loader import read_yaml
from utils.assertions import assert_single_item_exact_match_and_contains

# 读取数据
data = read_yaml("../data/test_posts.yaml")

@allure.feature("帖子管理")
class TestPosts:

    @allure.story("验证单条帖子信息")
    @pytest.mark.parametrize("case", data, ids=[i['case_desc'] for i in data])
    def test_post_by_id(self, case, api_client):
        logger.info("=== 开始执行测试用例 ===")

        # 1. 发送请求 (直接请求特定 ID)
        full_url = BASE_URL + case['request']['url']
        logger.debug("正在发送登录请求...")
        response = api_client.send_request(
            method=case['request']['method'],
            url=full_url,
            **{k: v for k, v in case['request'].items() if k not in ['method', 'url']}
        )

        # 2. 基础状态码断言
        assert response.status_code == case['expected']['status_code']

        # 3. 解析 JSON
        try:
            res_json = response.json()
        except:
            assert False, "响应不是合法的 JSON 格式"

        # 4. 调用新的断言函数 (支持 text_not_contains)
        exact_match = case['expected'].get('exact_match')
        text_contains = case['expected'].get('text_contains')
        text_not_contains = case['expected'].get('text_not_contains') # 获取新的配置

        assert_single_item_exact_match_and_contains(
            response_json=res_json,
            exact_match=exact_match,
            text_contains=text_contains,
            text_not_contains=text_not_contains # 传递给断言函数
        )
        logger.info("✅ 测试通过")