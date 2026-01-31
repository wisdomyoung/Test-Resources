import yaml
import os


# 公司的“标准数据读取器”——避免每个人自己写解析逻辑

def read_yaml(file_path):
    """
    读取 YAML 文件数据
    :param file_path: YAML 文件的相对路径 (例如: "../data/login_cases.yaml")
    :return: 返回解析后的数据 (列表或字典)，如果出错则返回空列表或空字典
    """
    # 1. 拼接绝对路径
    # __file__ 是当前文件的路径
    # .. 表示上一级目录，以此类推
    # abs_path=os.path.join(os.path.dirname(__file__), "..", file_path).replace("\\", "/")
    abs_path=os.path.join(os.path.dirname(__file__), file_path).replace("\\", "/")
    print(f"[DEBUG] 正在读取 YAML 文件: {abs_path}")
    # 调试用：打印一下路径，确保路径是对的 (运行没问题后可以注释掉)
    # print(f"尝试读取 YAML 文件路径: {abs_path}")

    try:
        with open(abs_path, 'r', encoding='utf-8') as f:
            # 2. 安全读取 YAML
            # safe_load 确保只读取数据，不执行危险代码
            data=yaml.safe_load(f)

            # 防御性编程：如果文件为空，yaml.safe_load 会返回 None
            # 我们把它转成空列表，防止测试用例那边报错
            if data is None:
                print(f"警告: {abs_path} 文件为空，返回空列表。")
                return []
            return data

    except FileNotFoundError:
        print(f"❌ 错误: 找不到 YAML 文件 -> {abs_path}")
        print(f"请检查文件路径是否正确。")
        return []
    except yaml.YAMLError as e:
        print(f"❌ YAML 解析错误: {e}")
        print(f"请检查 YAML 文件语法是否正确（比如缩进、冒号）。")
        return []
    except Exception as e:
        print(f"❌ 读取文件时发生未知错误: {e}")
        return []
