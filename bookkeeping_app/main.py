import tkinter as tk
from ui.main_view import MainView
from data.database import LocalDatabase

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("记账本 App") # [cite: 6]
        self.geometry("450x700")

        # 初始化数据库
        db = LocalDatabase()
        db.initialize_database()

        # 启动主视图
        main_view = MainView(self)
        main_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()