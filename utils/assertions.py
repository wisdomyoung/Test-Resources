# utils/assertions.py
import pytest


def assert_status_code(response, expected_code):
    """断言 HTTP 状态码"""
    assert response.status_code == expected_code, f"期望状态码 {expected_code}, 实际 {response.status_code}"


def assert_response_not_empty(response_json):
    """断言响应非空"""
    assert len(response_json) > 0, "响应数据为空"


def assert_key_in_first_item(response_json, key):
    """断言响应列表的第一个元素包含指定字段"""
    assert len(response_json) > 0, "响应为空，无法检查字段"
    first_item=response_json[0]
    assert key in first_item, f"响应首条记录缺少字段: {key}"


def assert_single_item_exact_match_and_contains(response_json, exact_match=None, text_contains=None,
                                                text_not_contains=None):
    """
    断言单个 JSON 对象是否与期望值完全匹配，并且包含/不包含特定文本
    :param response_json: 响应的单个 JSON 对象 (dict)
    :param exact_match: 字典，如 {"userId": 1, "id": 1}，用于精确匹配 (可选)
    :param text_contains: 字典，如 {"field": "title", "text": "facere"}，用于模糊匹配 (可选)
    :param text_not_contains: 字典，如 {"field": "title", "text": "Young"}，用于模糊不匹配 (可选)
    """
    # 1. 断言是字典对象
    assert isinstance(response_json, dict), "响应应为单个 JSON 对象"

    # 2. 处理精确匹配
    if exact_match:
        for key, expected_value in exact_match.items():
            actual_value=response_json.get(key)
            assert actual_value == expected_value, f"'{key}' 期望值为 {expected_value}, 实际为 {actual_value}"

    # 3. 处理文本包含
    if text_contains:
        field_to_check=text_contains['field']
        expected_text=text_contains['text']

        actual_text=response_json.get(field_to_check, "")
        assert isinstance(actual_text, str), f"字段 '{field_to_check}' 的值不是字符串: {actual_text}"

        assert expected_text in actual_text, f"'{field_to_check}' ('{actual_text}') 不包含文本 '{expected_text}'"

    # 4. 处理文本不包含 (新增逻辑)
    if text_not_contains:
        field_to_check=text_not_contains['field']
        forbidden_text=text_not_contains['text']

        actual_text=response_json.get(field_to_check, "")
        assert isinstance(actual_text, str), f"字段 '{field_to_check}' 的值不是字符串: {actual_text}"

        assert forbidden_text not in actual_text, f"'{field_to_check}' ('{actual_text}') 错误地包含了禁止的文本 '{forbidden_text}'"