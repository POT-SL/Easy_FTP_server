"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class Controller:

    def setting_ok(self, event):
        win = event.widget.winfo_toplevel()
        win.print_entry_contents()

    # 添加一个空的 init 方法
    def init(self, win_gui):
        pass  # 这里可以添加初始化代码，如果需要的话

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_m4ax8341 = self.__tk_label_m4ax8341(self)
        self.tk_input_m4ax8och = self.__tk_input_m4ax8och(self)
        self.tk_button_m4ax9055 = self.__tk_button_m4ax9055(self)

    def __win(self):
        self.title("端口设置")
        self.iconbitmap('.\\config\\4.ico')
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

    def __tk_label_m4ax8341(self, parent):
        label = Label(parent, text="端口号：", anchor="center", )
        label.place(x=30, y=60, width=50, height=30)
        return label

    def __tk_input_m4ax8och(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=105, y=60, width=150, height=30)
        return ipt

    def __tk_button_m4ax9055(self, parent):
        btn = Button(parent, text="确认", takefocus=False, )
        btn.place(x=125, y=150, width=50, height=30)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def print_entry_contents(self):
        # 获取
        port = self.tk_input_m4ax8och.get()
        # 检查输入是否正确
        try:
            port = int(port)
            if not 712 <= port <= 12100:
                messagebox.showerror('Error.', '输入错误\n数值应该在712~12100之间\n:(')
        # 若错误
        except:
            messagebox.showerror('Error.', '输入错误:(')
        else:
            # 传入参数
            que.put({'type': 'setting_port', 'port': port})
            # 关闭弹窗
            self.destroy()

    def __event_bind(self):
        self.tk_button_m4ax9055.bind('<Button-1>', self.ctl.setting_ok)

    def __style_config(self):
        pass

def port_main(que_s):

    global que

    que = que_s

    controller = Controller()
    win = Win(controller)
    win.mainloop()

    que.put({'type': 'close_port'})