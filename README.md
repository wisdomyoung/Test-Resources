Pytest API 自动化测试框架
这是一个基于 Python + Pytest 的接口自动化测试框架，集成了 YAML 数据驱动、Allure 报告和日志记录功能。
📂 项目结构







pytest_framework/
├── .venv                       # Python 虚拟环境
├── config/
│   ├── logconfig.py            # 日志配置
│   └── setting.py              # 全局配置文件
├── data/                       # 测试数据
│   ├── login_cases.yaml        # 登录测试用例数据
│   ├── test_posts.yaml         # 文章发布测试数据
│   └── testdata.yaml           # 通用测试数据
├── reports/                    # Allure 报告输出目录
├── tests/
│   ├── demo/                   # Demo 模块
│   │   ├── test_api_connection.py 
│   │   └── test_demo.py
│   └── Recourses/              # 资源模块
│       ├── test_login.py       # 登录测试用例
│       └── test_verifySingleMessage.py
├── utils/                      # 工具类
│   ├── assertions.py           # 断言封装
│   ├── http_client.py          # HTTP 请求封装
│   ├── logger.py               # 日志工具
│   └── yaml_loader.py          # YAML 数据加载
├── .gitignore                  # Git 忽略文件
├── confest.py                  # Pytest 配置文件 fixture
├── pytest.ini                  # Pytest 配置
├── requirements.txt            # 依赖包列表
└── run.py                      # 项目启动入口

🚀 快速开始
1. 环境依赖
●Python 3.8+
●Allure 命令行工具 (用于生成报告)
2. 安装依赖
进入项目根目录，执行：
代码
图标/24_new/复制

pip install -r requirements.txt

3. 运行测试
在终端中执行启动脚本：
代码
图标/24_new/复制

python run.py

4. 查看报告
测试运行结束后，脚本会自动打开 Allure 报告页面。如果未自动打开，可手动执行：
代码
图标/24_new/复制

allure open reports

🛠️ 核心功能
●数据驱动：使用 YAML 文件管理测试数据 (data/ 目录)，实现测试用例与数据分离。
●Allure 报告：生成美观的测试报告，支持失败重试和截图附件。
●日志系统：详细的运行日志记录，便于问题排查。
●模块化设计：清晰的分层结构 (测试用例、工具类、配置)，易于维护和扩展。
📚 使用说明
编写测试用例
测试用例存放在 tests/ 目录下。建议遵循以下命名规范：
●文件名以 test_ 开头。
●测试方法也以 test_ 开头。
配置管理
●全局配置请修改 config/setting.py。
●日志配置请修改 config/logconfig.py。
🤝 贡献
欢迎提交 Issue 或 Pull Request！
生成时间：2026-01-31
