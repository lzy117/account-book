import os
import pathlib

# 项目根目录
ROOT_DIR = "bookkeeping_app"

# 定义目录结构
DIRECTORIES = [
    "ui",
    "logic",
    "data",
    "db/images",
    "assets/icons"
]

# 定义所有文件
FILES = [
    "main.py",
    "ui/__init__.py",
    "ui/main_view.py",
    "ui/record_view.py",
    "ui/report_view.py",
    "ui/reminder_view.py",
    "ui/settings_view.py",
    "logic/__init__.py",
    "logic/record_manager.py",
    "logic/query_service.py",
    "logic/report_generator.py",
    "logic/reminder_service.py",
    "logic/ocr_service.py",
    "data/__init__.py",
    "data/database.py",
    "data/models.py",
    "db/app.db", # 创建一个空的db文件
    "assets/icons/.gitkeep" # 保持目录
]

def create_project_structure():
    root_path = pathlib.Path(ROOT_DIR)
    
    if root_path.exists():
        print(f"目录 '{ROOT_DIR}' 已存在。请先删除或重命名。")
        return

    print(f"正在创建项目: {root_path.resolve()}")

    # 1. 创建所有目录
    for dir_name in DIRECTORIES:
        path = root_path / dir_name
        path.mkdir(parents=True, exist_ok=True)
        print(f"  创建目录: {path}")

    # 2. 创建所有文件
    for file_name in FILES:
        path = root_path / file_name
        # 确保文件的父目录存在
        path.parent.mkdir(parents=True, exist_ok=True)
        # 创建空文件
        path.touch()
        print(f"  创建文件: {path}")

    print("\n项目结构创建完毕！")

if __name__ == "__main__":
    create_project_structure()