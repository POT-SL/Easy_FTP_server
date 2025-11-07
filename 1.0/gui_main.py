"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
from json import loads
from queue import Queue
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from os.path import isdir
from os import system
from show_ip_message import show_ip_message
from gui_user_setting import user_setting

FTPon = False

class Controller:
    def switch_ftp(self, event):
        if FTPon:
            settings_signal.put({'type': 'signal', 'signal': False})
            event.widget.winfo_toplevel().tk_label_ftp_status.config(text="未运行", foreground="red")
            event.widget.winfo_toplevel().tk_button_ftp_switch.config(text='开启')
        else:
            settings_signal.put({'type': 'signal', 'signal': True})
            event.widget.winfo_toplevel().tk_label_ftp_status.config(text="运行", foreground="green")
            event.widget.winfo_toplevel().tk_button_ftp_switch.config(text='停止')
    def choice_path(self, event):
        # 选择路径
        tmp = askdirectory()
        # 检查路径是否有效
        if isdir(tmp):
            # 更新路径
            settings_signal.put({'type': 'setting_path', 'path': tmp})
            # 更新界面
            event.widget.winfo_toplevel().tk_label_path_show.config(text='路径：' + tmp)
        # 无效
        else:
            # 弹窗
            messagebox.showerror('Error', '此目录无效')

    def setting_update_now(self, event):
        # 更新配置
        win = event.widget.winfo_toplevel()
        win.print_entry_contents()
        settings_signal.put({'type': 'update'})
    def setting_cancel(self, event):
        # 关窗
        win = event.widget.winfo_toplevel()
        win.handle_setting_off()
    def setting_ok(self, event):
        # 更新配置
        win = event.widget.winfo_toplevel()
        win.print_entry_contents()
        settings_signal.put({'type': 'update'})
        # 关窗
        win.handle_setting_off()

    def ip_show(self, event):
        show_ip_message(config.get('port'), config.get('user'), config.get('password'))
    def setting_user(self, event):
        user_setting(settings_signal)
    def setting_port(self, event):
        print('8')
    def open_path(self, event):
        # 打开文件夹
        system('start ' + config.get('path'))

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
        self.tk_button_show_login = self.__tk_button_show_login(self)
        self.tk_button_custom_user = self.__tk_button_custom_user(self)
        self.tk_button_custom_port = self.__tk_button_custom_port(self)
        self.tk_button_open_path = self.__tk_button_open_path(self)
        self.tk_label_now_time_set = self.__tk_label_now_time_set(self)

    def __win(self):
        self.title("FTP服务器（简易版）")
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
        if FTPon:
            label = Label(parent,text="运行",anchor="center", foreground="green")
        else:
            label = Label(parent, text="未运行", anchor="center", foreground="red")
        label.place(x=100, y=20, width=40, height=20)
        return label
    def __tk_button_ftp_switch(self,parent):
        btn = Button(parent, text="运行", takefocus=False,)
        btn.place(x=160, y=15, width=50, height=30)
        return btn
    def __tk_label_path_show(self,parent):
        label = Label(parent,text=("路径：" + config.get('path')),anchor="w", )
        label.place(x=20, y=85, width=450, height=20)
        return label
    def __tk_button_path_switch(self,parent):
        btn = Button(parent, text="选择目录", takefocus=False,)
        btn.place(x=20, y=55, width=75, height=30)
        return btn
    def __tk_label_path_text(self,parent):
        label = Label(parent,text="选择ftp服务要运行的文件夹",anchor="center", )
        label.place(x=190, y=55, width=150, height=30)
        return label
    def __tk_check_button_run_on_time(self,parent):
        self.run_on_time_var = IntVar(value=config.get('run_on_time'))
        cb = Checkbutton(parent,text="定时开启",variable=self.run_on_time_var)
        cb.place(x=20, y=120, width=80, height=30)
        return cb
    def __tk_label_run_tips(self,parent):
        label = Label(parent,text="（安全性考虑，防止24小时暴露端口）",anchor="w", )
        label.place(x=100, y=120, width=220, height=30)
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
        self.autorun = IntVar(value=config.get('auto_start'))
        cb = Checkbutton(parent,text="开机启动（应该有用？）",variable=self.autorun)
        cb.place(x=20, y=200, width=170, height=30)
        return cb
    def __tk_button_show_login(self,parent):
        btn = Button(parent, text="连接信息", takefocus=False,)
        btn.place(x=20, y=245, width=80, height=30)
        return btn
    def __tk_button_custom_user(self,parent):
        btn = Button(parent, text="自定义用户", takefocus=False,)
        btn.place(x=110, y=245, width=75, height=30)
        return btn
    def __tk_button_custom_port(self,parent):
        btn = Button(parent, text="自定义端口", takefocus=False,)
        btn.place(x=195, y=245, width=75, height=30)
        return btn
    def __tk_button_open_path(self,parent):
        btn = Button(parent, text="打开文件夹", takefocus=False,)
        btn.place(x=105, y=55, width=75, height=30)
        return btn
    def __tk_label_now_time_set(self,parent):
        label = Label(parent,text=(f"当前设置：{config.get('start_time')[0]}:{config.get('start_time')[1]} - {config.get('end_time')[0]}:{config.get('end_time')[1]}"),anchor="w", )
        label.place(x=255, y=165, width=210, height=20)
        return label
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def handle_setting_off(self):
        self.destroy()

    def print_entry_contents(self):
        # 获取所有Entry小部件的内容
        src_hour = self.tk_input_src_hour.get()
        src_minute = self.tk_input_src_minute.get()
        dst_hour = self.tk_input_dst_hour.get()
        dst_minute = self.tk_input_dst_minute.get()
        run_on_time = self.run_on_time_var.get()
        autorun = self.autorun.get()

        # 如果没有时间
        if src_hour == src_minute == dst_hour == dst_minute == '':
            # 更新配置
            settings_signal.put({'type': 'setting_run_on_time', 'val': run_on_time})
            settings_signal.put({'type': 'setting_auto_start', 'val': autorun})

        else:
            # 检查时间是否正确
            try:
                src_hour = int(src_hour)
                src_minute = int(src_minute)
                dst_hour = int(dst_hour)
                dst_minute = int(dst_minute)
                if (0 <= src_hour <= 24 and 0 <= src_minute <= 59) and (0 <= dst_hour <= 24 and 0 <= dst_minute <= 59):
                    if src_hour == dst_hour and src_minute == dst_minute:
                        messagebox.showerror('Error', '起始和终止时间不能相同。')
                    else:
                        # 更新设置
                        settings_signal.put({'type': 'setting_time', 'start_time': [src_hour, src_minute],
                                             'end_time': [dst_hour, dst_minute]})
                        settings_signal.put({'type': 'setting_run_on_time', 'val': run_on_time})
                        settings_signal.put({'type': 'setting_auto_start', 'val': autorun})
                        # 更新显示设置
                        self.tk_label_now_time_set.config(
                            text=(f"当前设置：{src_hour}:{src_minute} - {dst_hour}:{dst_minute}"))
                else:
                    raise ValueError
            except:
                messagebox.showerror('Error', '时间格式错误')

    def __event_bind(self):
        self.tk_button_ftp_switch.bind('<Button-1>',self.ctl.switch_ftp)
        self.tk_button_path_switch.bind('<Button-1>',self.ctl.choice_path)
        self.tk_button_apply.bind('<Button-1>',self.ctl.setting_update_now)
        self.tk_button_cancel.bind('<Button-1>',self.ctl.setting_cancel)
        self.tk_button_ok.bind('<Button-1>',self.ctl.setting_ok)
        self.tk_button_show_login.bind('<Button-1>',self.ctl.ip_show)
        self.tk_button_custom_user.bind('<Button-1>',self.ctl.setting_user)
        self.tk_button_custom_port.bind('<Button-1>',self.ctl.setting_port)
        self.tk_button_open_path.bind('<Button-1>',self.ctl.open_path)
        pass
    def __style_config(self):
        pass

def gui_main(signal_l):

    global settings_signal
    settings_signal = signal_l

    global config

    controller = Controller()
    win = Win(controller)
    win.mainloop()

if __name__ == "__main__":

    a = Queue

    gui_main(a)