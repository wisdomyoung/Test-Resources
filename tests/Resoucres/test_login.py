# tests/Resoucres/test_login.py
import pytest
import allure
from config.setting import BASE_URL
from utils.yaml_loader import read_yaml
from utils.assertions import (  # 👈 导入断言工具
    assert_status_code,
    assert_response_not_empty,
    assert_key_in_first_item
)
from typing import List, Dict
# 1. 读取数据（建议使用相对路径）
data=read_yaml("../data/login_cases.yaml")

# 假设 data 是从 read_yaml 读取的
data: List[Dict[str, any]] = read_yaml("../data/login_cases.yaml")

@allure.feature("公共API测试模块")
class TestPublicAPI:

    @allure.story("数据驱动测试-获取用户信息")
    @pytest.mark.parametrize("case", data, ids=[c['case_desc'] for c in data])
    def test_fetch_data(self, case, api_client):
        allure.dynamic.title(case['case_desc'])

        full_url=BASE_URL + case['request']['url']

        response=api_client.send_request(
            method=case['request']['method'],
            url=full_url,
            **{k: v for k, v in case['request'].items() if k not in ['method', 'url']}
        )

        with allure.step("执行断言"):
            assert_status_code(response, case['expected']['status_code'])
            try:
                res_json=response.json()
            except ValueError:
                assert False, f"响应不是有效 JSON: {response.text}"

                # 断言响应结构和内容
            assert isinstance(res_json, list) and len(res_json) > 0
