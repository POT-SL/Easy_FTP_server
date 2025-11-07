"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *


class Controller:
    def switch_ftp(self, event):
        # 当按钮被点击时，这里会执行
        print('1')
    def choice_path(self, event):
        print('2')
    def setting_update_now(self, event):
        print('3')
    def setting_cancel(self, event):
        print('4')
    def setting_ok(self, event):
        print('5')
        win = event.widget.winfo_toplevel()
        win.print_entry_contents()
    def ip_show(self, event):
        print('6')
    # 添加一个空的 init 方法
    def init(self, win_gui):
        pass  # 这里可以添加初始化代码，如果需要的话

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_ftp_test = self.__tk_label_ftp_test(self)
        self.tk_label_ftp_status = self.__tk_label_ftp_status(self)
        self.tk_button_ftp_switch = self.__tk_button_ftp_switch(self)
        self.tk_label_path_show = self.__tk_label_path_show(self)
        self.tk_button_path_switch = self.__tk_button_path_switch(self)
        self.tk_label_path_text = self.__tk_label_path_text(self)
        self.tk_check_button_run_on_time = self.__tk_check_button_run_on_time(self)
        self.tk_label_run_tips = self.__tk_label_run_tips(self)
        self.tk_label_time_text = self.__tk_label_time_text(self)
        self.tk_input_src_hour = self.__tk_input_src_hour(self)
        self.tk_label_src_split = self.__tk_label_src_split(self)
        self.tk_input_src_minute = self.__tk_input_src_minute(self)
        self.tk_label_time_split = self.__tk_label_time_split(self)
        self.tk_input_dst_hour = self.__tk_input_dst_hour(self)
        self.tk_label_dst_split = self.__tk_label_dst_split(self)
        self.tk_input_dst_minute = self.__tk_input_dst_minute(self)
        self.tk_button_apply = self.__tk_button_apply(self)
        self.tk_button_cancel = self.__tk_button_cancel(self)
        self.tk_button_ok = self.__tk_button_ok(self)
        self.tk_check_button_autorun = self.__tk_check_button_autorun(self)
        self.tk_button_show_ip = self.__tk_button_show_ip(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 480
        height = 360
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self,vbar, hbar, widget):
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

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_ftp_test(self,parent):
        label = Label(parent,text="FTP状态：",anchor="center", )
        label.place(x=20, y=20, width=65, height=20)
        return label
    def __tk_label_ftp_status(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=100, y=20, width=40, height=20)
        return label
    def __tk_button_ftp_switch(self,parent):

        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=160, y=15, width=50, height=30)
        return btn
    def __tk_label_path_show(self,parent):
        label = Label(parent,text="路径：",anchor="center", )
        label.place(x=20, y=85, width=450, height=20)
        return label
    def __tk_button_path_switch(self,parent):
        btn = Button(parent, text="选择目录", takefocus=False,)
        btn.place(x=20, y=55, width=75, height=30)
        return btn
    def __tk_label_path_text(self,parent):
        label = Label(parent,text="选择ftp服务要运行的文件夹",anchor="center", )
        label.place(x=100, y=55, width=150, height=30)
        return label
    def __tk_check_button_run_on_time(self,parent):
        cb = Checkbutton(parent,text="定时开启",)
        cb.place(x=20, y=120, width=80, height=30)
        return cb
    def __tk_label_run_tips(self,parent):
        label = Label(parent,text="安全性考虑，防止24小时暴露端口",anchor="center", )
        label.place(x=100, y=120, width=195, height=30)
        return label
    def __tk_label_time_text(self,parent):
        label = Label(parent,text="每天的",anchor="center", )
        label.place(x=20, y=165, width=50, height=20)
        return label
    def __tk_input_src_hour(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=75, y=165, width=30, height=20)
        return ipt
    def __tk_label_src_split(self,parent):
        label = Label(parent,text=":",anchor="center", )
        label.place(x=105, y=165, width=10, height=20)
        return label
    def __tk_input_src_minute(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=115, y=165, width=30, height=20)
        return ipt
    def __tk_label_time_split(self,parent):
        label = Label(parent,text="至",anchor="center", )
        label.place(x=150, y=165, width=20, height=20)
        return label
    def __tk_input_dst_hour(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=175, y=165, width=30, height=20)
        return ipt
    def __tk_label_dst_split(self,parent):
        label = Label(parent,text=":",anchor="center", )
        label.place(x=205, y=165, width=10, height=20)
        return label
    def __tk_input_dst_minute(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=215, y=165, width=30, height=20)
        return ipt
    def __tk_button_apply(self,parent):
        btn = Button(parent, text="应用", takefocus=False,)
        btn.place(x=410, y=310, width=50, height=30)
        return btn
    def __tk_button_cancel(self,parent):
        btn = Button(parent, text="取消", takefocus=False,)
        btn.place(x=350, y=310, width=50, height=30)
        return btn
    def __tk_button_ok(self,parent):
        btn = Button(parent, text="确认", takefocus=False,)
        btn.place(x=290, y=310, width=50, height=30)
        return btn
    def __tk_check_button_autorun(self,parent):
        cb = Checkbutton(parent,text="开机启动（应该有用？）",)
        cb.place(x=20, y=200, width=170, height=30)
        return cb
    def __tk_button_show_ip(self,parent):
        btn = Button(parent, text="查看IP", takefocus=False,)
        btn.place(x=20, y=245, width=50, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def print_entry_contents(self):
        # 获取所有Entry小部件的内容并打印
        src_hour = self.tk_input_src_hour.get()
        src_minute = self.tk_input_src_minute.get()
        dst_hour = self.tk_input_dst_hour.get()
        dst_minute = self.tk_input_dst_minute.get()

        print(f"Source Hour: {src_hour}")
        print(f"Source Minute: {src_minute}")
        print(f"Destination Hour: {dst_hour}")
        print(f"Destination Minute: {dst_minute}")

    def __event_bind(self):
        self.tk_button_ftp_switch.bind('<Button-1>',self.ctl.switch_ftp)
        self.tk_button_path_switch.bind('<Button-1>',self.ctl.choice_path)
        self.tk_button_apply.bind('<Button-1>',self.ctl.setting_update_now)
        self.tk_button_cancel.bind('<Button-1>',self.ctl.setting_cancel)
        self.tk_button_ok.bind('<Button-1>',self.ctl.setting_ok)
        self.tk_button_show_ip.bind('<Button-1>',self.ctl.ip_show)
        pass
    def __style_config(self):
        pass

if __name__ == "__main__":
    controller = Controller()
    win = Win(controller)
    win.mainloop()