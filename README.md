markdown
# 图书管理系统（Flask + SQLAlchemy）

一个基于 Flask 的图书管理系统，支持图书、作者、出版社的增删改查，图书可关联作者和出版社。前端提供简单的可视化界面，后端提供 RESTful API。

## 技术栈
- 后端：Python 3.9 + Flask 2.2.5 + Flask-SQLAlchemy 2.5.1
- 数据库：SQLite
- 前端：HTML / CSS / JavaScript
- 版本控制：Git

## 功能
- 图书管理：添加、查看、删除图书
- 作者管理：添加、删除作者
- 出版社管理：添加、删除出版社
- 图书可关联作者和出版社（可选）
- 前端页面通过 AJAX 与后端交互，实时刷新数据

## 项目结构
flask_vue_backend/
├── app.py # 主程序入口
├── extensions.py # 数据库实例
├── api/ # 蓝图模块
│ ├── books.py # 图书模块（含模型和路由）
│ ├── authors.py # 作者模块
│ └── publishers.py # 出版社模块
└── templates/
└── index.html # 前端页面

text

## 运行方法

1. 克隆项目
```bash
git clone https://github.com/LH-1209/library-management-system.git
cd library-management-system
2. 安装依赖
bash
pip install flask==2.2.5 flask-sqlalchemy==2.5.1
3. 初始化数据库
bash
python
进入 Python 交互环境后执行：

python
from app import app
from extensions import db
with app.app_context():
    db.create_all()
输入 exit() 退出。

4. 启动服务
bash
python app.py
访问 http://127.0.0.1:8000/ui 使用系统。

API 接口示例
方法	地址	说明
GET	/books/	获取所有图书
POST	/books/	添加图书
DELETE	/books/<id>	删除图书
GET	/authors/	获取所有作者
POST	/authors/	添加作者
GET	/publishers/	获取所有出版社
POST	/publishers/	添加出版社
解决的关键问题
Flask 版本兼容：Flask 3.x 与 Flask-SQLAlchemy 2.5.1 不兼容，将 Flask 降级至 2.2.5 解决

循环导入：app.py 和 api/books.py 互相导入导致报错，将 db 对象独立到 extensions.py 解决

中文编码：文件保存编码不一致导致中文乱码，统一用 UTF-8 保存解决