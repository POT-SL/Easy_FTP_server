"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import *
from tkinter.ttk import *
import socket

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_ip = self.__tk_label_ip(self)
        self.tk_label_m4awv6qz = self.__tk_label_m4awv6qz(self)
        self.tk_label_m4awvir3 = self.__tk_label_m4awvir3(self)
        self.tk_label_m4awvrp9 = self.__tk_label_m4awvrp9(self)

    def __win(self):
        self.title("连接信息")
        self.iconbitmap('.\\config\\2.ico')
        # 设置窗口大小、居中
        width = 300
        height = 200
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_label_ip(self, parent):
        label = Label(parent, text=f"IP地址：{ip_l}", anchor="center", )
        label.place(x=0, y=30, width=300, height=30)
        return label

    def __tk_label_m4awv6qz(self, parent):
        label = Label(parent, text=f"端口号：{port_l}", anchor="center", )
        label.place(x=0, y=60, width=300, height=30)
        return label

    def __tk_label_m4awvir3(self, parent):
        label = Label(parent, text=f"用户名：{user_l}", anchor="center", )
        label.place(x=0, y=90, width=300, height=30)
        return label

    def __tk_label_m4awvrp9(self, parent):
        label = Label(parent, text=f"密码：{password_l}", anchor="center", )
        label.place(x=0, y=120, width=300, height=30)
        return label


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        pass

    def __style_config(self):
        pass

def get_local_ip():
    try:
        # 创建一个socket对象
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个不可能的地址，只是为了获取本地IP地址
        s.connect(('10.254.254.254', 1))
        # 获取本地IP地址
        local_ip = s.getsockname()[0]
    except Exception as e:
        # 如果出现异常，返回一个默认值或错误信息
        local_ip = '127.0.0.1'
    finally:
        # 关闭socket连接
        s.close()
    return local_ip

def show_ip_message(port, user, password, que):

    global ip_l, port_l, user_l, password_l

    ip_l = get_local_ip()
    port_l = port
    user_l = user
    password_l = password

    win = WinGUI()
    win.mainloop()

    que.put({'type': 'close_login'})