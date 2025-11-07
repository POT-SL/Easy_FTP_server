import tkinter as tk
from tkinter import simpledialog

def input_dialog(title="输入", prompt="请输入内容:"):
    # 创建一个顶层窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 调用simpledialog，获取用户输入
    user_input = simpledialog.askstring(title, prompt)

    # 销毁顶层窗口
    root.destroy()

    return user_input

# 示例：调用input_dialog函数
if __name__ == "__main__":
    input_value = input_dialog()
    print("你输入的内容是:", input_value)
