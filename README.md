# BlogSystem_001
个人博客系统 - 期末考查项目

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub](https://img.shields.io/badge/GitHub-Repository-lightgrey.svg)

**一个基于 Flask 的轻量级个人博客系统**

*期末考查项目 - 001*

[项目介绍](#项目介绍) • [功能特性](#功能特性) • [快速开始](#快速开始) • [项目结构](#项目结构) • [开发指南](#开发指南) • [许可证](#许可证)

</div>

## 📖 项目介绍

BlogSystem_001 是一个使用 Python Flask 框架开发的个人博客系统，具备完整的文章发布、管理和展示功能。该项目展示了 Git 版本控制、分支管理、团队协作和项目文档编写等软件开发实践。

## ✨ 功能特性

- 📝 **文章管理** - 创建、编辑、发布和删除博客文章
- 🎨 **响应式设计** - 适配桌面端和移动端设备
- 🔍 **文章浏览** - 清晰的文章列表和详情页面
- 💬 **评论系统** - 支持用户评论互动（基础框架）
- 📱 **现代化UI** - 简洁美观的用户界面
- 🚀 **轻量高效** - 基于 Flask 的轻量级架构

## 🛠 技术栈

**后端技术：**
- Python 3.8+
- Flask 2.3.3
- Flask-SQLAlchemy
- SQLite 数据库

**前端技术：**
- HTML5 + CSS3
- 原生 JavaScript
- 响应式布局设计

**开发工具：**
- Git & GitHub
- VS Code / PyCharm
- 浏览器开发者工具

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- pip 包管理工具
- 现代网页浏览器（Chrome、Firefox、Safari等）

### 安装步骤

1. **克隆项目到本地**
   ```bash
   git clone https://github.com/yourusername/BlogSystem_001.git
   cd BlogSystem_001
   ```

2. **安装依赖包**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行应用程序**
   ```bash
   cd src
   python app.py
   ```

4. **访问应用**
   打开浏览器，访问：http://localhost:5000

### 首次运行说明

首次运行时会自动：
- 创建 SQLite 数据库文件
- 生成示例文章和用户数据
- 启动开发服务器

## 📁 项目结构

```
BlogSystem_001/
├── README.md                   # 项目说明文档
├── LICENSE                     # MIT 许可证
├── requirements.txt            # Python 依赖包列表
├── CHANGELOG.md               # 版本更新日志
├── CONTRIBUTING.md            # 贡献指南
├── STRATEGY_ANALYSIS.md       # 五看三定战略分析
├── .gitignore                 # Git 忽略文件配置
│
├── src/                       # 源代码目录
│   ├── app.py                 # Flask 主应用文件
│   ├── models.py              # 数据库模型定义
│   ├── templates/             # HTML 模板文件
│   │   ├── index.html         # 首页模板
│   │   ├── post.html          # 文章详情页模板
│   │   └── create.html        # 创建文章页模板
│   └── static/                # 静态资源文件
│       ├── style.css          # 主要样式文件
│       └── script.js          # JavaScript 文件
│
└── docs/                      # 项目文档
    ├── setup_guide.md         # 详细安装指南
    └── api_documentation.md   # API 接口文档
```

## 🎯 功能演示

### 首页文章列表
- 显示所有博客文章的摘要
- 支持文章标题点击进入详情页
- 响应式网格布局设计

### 文章详情页
- 完整的文章内容展示
- 文章元信息（发布时间、作者）
- 评论区域和评论表单

### 文章创建功能
- 简洁的文章编辑界面
- 标题和内容表单验证
- 实时发布到首页

## 🔧 开发指南

### 分支管理策略

本项目采用功能分支工作流：

- `main` - 主分支，保持稳定版本
- `feature/*` - 功能开发分支
- `bugfix/*` - 问题修复分支

### 代码贡献流程

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/新功能`)
3. 提交更改 (`git commit -m '添加新功能'`)
4. 推送到分支 (`git push origin feature/新功能`)
5. 创建 Pull Request

### 开发环境设置

```bash
# 1. 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 2. 安装开发依赖
pip install -r requirements.txt

# 3. 运行开发服务器
cd src
python app.py
```

## 📊 GitHub 特性展示

本项目完整展示了以下 GitHub 功能：

### ✅ 版本控制
- [] 仓库创建和初始化
- [] 提交历史管理
- [] .gitignore 配置

### ✅ 分支管理
- [] 功能分支创建
- [] 分支合并操作
- [] 冲突解决演示

### ✅ 协作功能
- [] Issue 创建和讨论
- [] Pull Request 流程
- [] 项目 Star 和 Watch

### ✅ 项目文档
- [] 完整的 README 文档
- [] 许可证文件
- [] 贡献指南
- [] 更新日志


## 🤝 贡献指南

欢迎所有形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目开发。

### 报告问题
发现 bug 或有功能建议？请到 [Issues](https://github.com/yourusername/BlogSystem_38/issues) 页面提交。

### 代码规范
- 遵循 PEP 8 Python 编码规范
- 提交信息使用清晰的英文描述
- 确保代码通过基础测试

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👥 开发者

- 学号：2022131001
- 邮箱：2733126625l@qq.com
- GitHub: [@username](https://github.com/username)

## 🔗 相关链接

- [Flask 官方文档](https://flask.palletsprojects.com/)
- [GitHub 学习资源](https://skills.github.com/)
- [Python 官方文档](https://docs.python.org/3/)

## 📞 联系我们

如有问题或建议，欢迎通过以下方式联系：
- 创建 GitHub Issue
- 发送邮件至：1111.email@example.com

---

<div align="center">

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

*最后更新：2025年11月*

</div>

---

## 🎯 使用提示

### 自定义配置
要自定义这个博客系统，你可以修改：

1. **数据库配置** - 在 `src/app.py` 中修改 SQLALCHEMY 配置
2. **样式主题** - 编辑 `src/static/style.css` 文件
3. **页面布局** - 修改 `src/templates/` 下的 HTML 文件

### 部署建议
对于生产环境部署，建议：
- 使用 PostgreSQL 或 MySQL 替代 SQLite
- 配置生产级 WSGI 服务器（如 Gunicorn）
- 设置反向代理（如 Nginx）
- 配置域名和 SSL 证书

### 扩展功能想法
- [ ] 用户注册和登录系统
- [ ] 文章分类和标签
- [ ] 文章搜索功能
- [ ] 图片上传支持
- [ ] 文章评论回复
- [ ] 后台管理界面

---

*注意：这是只一个演示项目，适合学习 Flask 和 GitHub 工作流程。*
