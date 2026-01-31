import os
import subprocess
import webbrowser

import pytest
from datetime import datetime
import time

if __name__ == '__main__':
    # --- 第一步：执行测试 ---
    print("=" * 50)
    print(f"🚀 [{datetime.now()}] 开始执行自动化测试...")
    print("=" * 50)

    # 显式传递参数给 pytest.main
    # 这里的参数优先级高于 pytest.ini
    # -s: 允许打印 print 语句（调试时很有用）
    # -v: 详细模式
    # --alluredir: 指定 allure 结果存放目录（会自动创建）
    # --clean-alluredir: 清理旧的 allure 结果，避免报告混乱
    pytest_exit_code=pytest.main([
        "-s",
        "-v",
        "--alluredir=reports/allure_results",
        "--clean-alluredir",
        "-k", "not test_api_connection and not test_login"
    ])

    # --- 第二步：生成报告 ---
    # 只有当测试执行完成（无论成功或失败）后，才生成报告
    print("\n")
    print("=" * 50)
    if pytest_exit_code == 0:
        print(f"✅ [{datetime.now()}] 测试执行完成，全部用例通过！")
    else:
        print(f"⚠️ [{datetime.now()}] 测试执行结束，发现失败用例 (退出码: {pytest_exit_code})")
    print("=" * 50)

    print("📊 正在生成 Allure 报告并启动本地服务...")
    print("💡 提示：浏览器打开后，请稍等片刻加载数据。关闭浏览器窗口即可停止服务。")

    # 使用 allure serve 命令
    # 这会启动一个本地服务器，并自动打开浏览器展示报告
    # 注意：os.system 是阻塞的，这意味着程序会停在这里，直到你关闭浏览器窗口
    # try:
    #     os.system("allure serve reports/allure_results -o reports/html --clean")
    #     print("程序任然在运行")
    # except KeyboardInterrupt:
    #     print(f"\n程序结束")
    # 1. 生成静态报告 (核心步骤)
    # 注意：这里去掉了 'serve'，改用 'generate'
    import subprocess

    # 1. 生成报告
    subprocess.run("allure generate reports/allure_results -o reports/html --clean", shell=True)

    # 2. 启动服务并打开浏览器 (阻塞模式)
    print("正在启动报告服务... (按 Ctrl+C 停止服务)")

    try:
        # 这行代码会“卡住”在这里，把控制权完全交给 Allure
        # 此时你在终端按 Ctrl+C，Allure 会捕获到并退出
        subprocess.run("allure open reports/html", shell=True)
    except KeyboardInterrupt:
        # 只有当用户按了 Ctrl+C，代码才会跳到这里
        print("\n👋 报告服务已停止。")






