"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import *
from tkinter.ttk import *
from os import system
from tkinter.filedialog import askdirectory
from os.path import isdir
from tkinter import messagebox

class Controller:
    def switch_ftp(self, event):
        if ftp_status:
            setting_signal.put({'type': 'FTPoff'})
        else:
            setting_signal.put({'type': 'FTPon'})
    def choice_path(self, event):
        tmp = askdirectory()
        if isdir(tmp):
            setting_signal.put({'type': 'setting_path', 'path': tmp})
            event.widget.winfo_toplevel().tk_label_path_show.config(text='路径：' + tmp)
            config['path'] = tmp
        else:
            messagebox.showerror('Error', '此目录无效:(')
    def setting_update_now(self, event):
        # 更新配置
        win = event.widget.winfo_toplevel()
        win.set_entry_contents()
    def setting_cancel(self, event):
        # 重新设置（并关闭窗口）
        setting_signal.put({'type': 'set_cancel'})
        win = event.widget.winfo_toplevel()
        win.on_closing()
    def setting_ok(self, event):
        # 更新配置
        win = event.widget.winfo_toplevel()
        win.set_entry_contents()
        # 关闭窗口
        win.on_closing()
    def ip_show(self, event):
        setting_signal.put({'type': 'gui_login'})
    def setting_user(self, event):
        setting_signal.put({'type': 'gui_userset'})
    def setting_port(self, event):
        setting_signal.put({'type': 'gui_port'})
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
        self.title("FTP简易服务器")
        self.iconbitmap('.\\config\\1.ico')
        # 设置窗口大小、居中
        width = 480
        height = 360
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

    def __tk_label_ftp_test(self, parent):
        label = Label(parent, text="FTP状态：", anchor="center", )
        label.place(x=20, y=20, width=65, height=20)
        return label

    def __tk_label_ftp_status(self, parent):

        if ftp_status:
            label = Label(parent, text="运行中", anchor="center", foreground="green")
        else:
            label = Label(parent, text="未运行", anchor="center", foreground="red")

        label.place(x=100, y=20, width=40, height=20)
        return label

    def __tk_button_ftp_switch(self, parent):

        if ftp_status:
            btn = Button(parent, text="停止", takefocus=False, )
        else:
            btn = Button(parent, text="启动", takefocus=False, )

        btn.place(x=160, y=15, width=50, height=30)
        return btn

    def __tk_label_path_show(self, parent):
        label = Label(parent, text="路径：" + config['path'], anchor="w", )
        label.place(x=20, y=85, width=450, height=20)
        return label

    def __tk_button_path_switch(self, parent):
        btn = Button(parent, text="选择目录", takefocus=False, )
        btn.place(x=20, y=55, width=75, height=30)
        return btn

    def __tk_label_path_text(self, parent):
        label = Label(parent, text="选择ftp服务要运行的文件夹", anchor="center", )
        label.place(x=190, y=55, width=150, height=30)
        return label

    def __tk_check_button_run_on_time(self, parent):
        self.run_on_time = IntVar(value=config['run_on_time'])
        cb = Checkbutton(parent, text="定时开启", variable=self.run_on_time)
        cb.place(x=20, y=120, width=80, height=30)
        return cb

    def __tk_label_run_tips(self, parent):
        label = Label(parent, text="（安全性考虑，防止24小时暴露端口）", anchor="w", )
        label.place(x=100, y=120, width=220, height=30)
        return label

    def __tk_label_time_text(self, parent):
        label = Label(parent, text="每天的", anchor="center", )
        label.place(x=20, y=165, width=50, height=20)
        return label

    def __tk_input_src_hour(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, str(config['start_time'][0]))
        ipt.place(x=75, y=165, width=30, height=20)
        return ipt

    def __tk_label_src_split(self, parent):
        label = Label(parent, text=":", anchor="center", )
        label.place(x=105, y=165, width=10, height=20)
        return label

    def __tk_input_src_minute(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, str(config['start_time'][1]))
        ipt.place(x=115, y=165, width=30, height=20)
        return ipt

    def __tk_label_time_split(self, parent):
        label = Label(parent, text="至", anchor="center", )
        label.place(x=150, y=165, width=20, height=20)
        return label

    def __tk_input_dst_hour(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, str(config['end_time'][0]))
        ipt.place(x=175, y=165, width=30, height=20)
        return ipt

    def __tk_label_dst_split(self, parent):
        label = Label(parent, text=":", anchor="center", )
        label.place(x=205, y=165, width=10, height=20)
        return label

    def __tk_input_dst_minute(self, parent):
        ipt = Entry(parent, )
        ipt.insert(0, str(config['end_time'][1]))
        ipt.place(x=215, y=165, width=30, height=20)
        return ipt

    def __tk_button_apply(self, parent):
        btn = Button(parent, text="应用", takefocus=False, )
        btn.place(x=410, y=310, width=50, height=30)
        return btn

    def __tk_button_cancel(self, parent):
        btn = Button(parent, text="取消", takefocus=False, )
        btn.place(x=350, y=310, width=50, height=30)
        return btn

    def __tk_button_ok(self, parent):
        btn = Button(parent, text="确认", takefocus=False, )
        btn.place(x=290, y=310, width=50, height=30)
        return btn

    def __tk_check_button_autorun(self, parent):
        self.auto_start = IntVar(value=config['auto_start'])
        cb = Checkbutton(parent, text="开机启动（应该有用？）", variable=self.auto_start)
        cb.place(x=20, y=200, width=170, height=30)
        return cb

    def __tk_button_show_login(self, parent):
        btn = Button(parent, text="连接信息", takefocus=False, )
        btn.place(x=20, y=245, width=80, height=30)
        return btn

    def __tk_button_custom_user(self, parent):
        btn = Button(parent, text="自定义用户", takefocus=False, )
        btn.place(x=110, y=245, width=75, height=30)
        return btn

    def __tk_button_custom_port(self, parent):
        btn = Button(parent, text="自定义端口", takefocus=False, )
        btn.place(x=195, y=245, width=75, height=30)
        return btn

    def __tk_button_open_path(self, parent):
        btn = Button(parent, text="打开文件夹", takefocus=False, )
        btn.place(x=105, y=55, width=75, height=30)
        return btn

    def __tk_label_now_time_set(self, parent):
        label = Label(parent, text=(f"当前设置：{config.get('start_time')[0]}:{config.get('start_time')[1]} - "
                                    f"{config.get('end_time')[0]}:{config.get('end_time')[1]}"), anchor="center", )
        label.place(x=255, y=165, width=210, height=20)
        return label

class Win(WinGUI):
    def __init__(self, controller, show_change_queue):
        self.ctl = controller
        self.show_change_queue = show_change_queue
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
        self.update_label_status()

    def on_closing(self):
        self.destroy()

    def set_entry_contents(self):

        # 获取所有Entry小部件的内容
        src_hour = self.tk_input_src_hour.get()
        src_minute = self.tk_input_src_minute.get()
        dst_hour = self.tk_input_dst_hour.get()
        dst_minute = self.tk_input_dst_minute.get()
        run_on_time = self.run_on_time.get()
        auto_start = self.auto_start.get()

        # 检查时间是否正确
        try:
            src_hour = int(src_hour)
            src_minute = int(src_minute)
            dst_hour = int(dst_hour)
            dst_minute = int(dst_minute)
            if not (0 <= src_hour <= 24 and 0 <= src_minute <= 59) and (0 <= dst_hour <= 24 and 0 <= dst_minute <= 59):
                raise ValueError
        # 出错
        except:
            messagebox.showerror('Error', '时间格式错误，无法保存:(')
        # 如果正常
        else:
            # 如果起始终止相同
            if src_hour == dst_hour and src_minute == dst_minute:
                # 报错
                messagebox.showerror('Error', '起始和终止时间不能相同捏~')
            # 如果正常
            else:
                # 更新设置
                setting_signal.put({
                    'type': 'set_all',
                    'start_time': [src_hour, src_minute],
                    'end_time': [dst_hour, dst_minute],
                    'run_on_time': run_on_time,
                    'auto_start': auto_start
                })
                # 更新显示
                self.tk_label_now_time_set.config(
                    text=(f"当前设置：{src_hour}:{src_minute} - {dst_hour}:{dst_minute}"))
                # 修改成功
                messagebox.showinfo('ok!', '设置成功 ^v^ !\n请手动重启一下FTP服务')


    def update_label_status(self):

        global ftp_status
        global login_status
        global login_set
        global port_set

        try:
            message = self.show_change_queue.get(False)
            if message == 'on':
                self.tk_label_ftp_status.config(text="运行", foreground="green")
                self.tk_button_ftp_switch.config(text='停止')
                ftp_status = True
                self.update_label_status()
            if message == 'off':
                self.tk_label_ftp_status.config(text="未运行", foreground="red")
                self.tk_button_ftp_switch.config(text='开启')
                ftp_status = False
                self.update_label_status()
        except:
            # 100毫秒后再次调用此函数
            self.after(100, self.update_label_status)

    def __event_bind(self):
        self.tk_button_ftp_switch.bind('<Button-1>', self.ctl.switch_ftp)
        self.tk_button_path_switch.bind('<Button-1>', self.ctl.choice_path)
        self.tk_button_apply.bind('<Button-1>', self.ctl.setting_update_now)
        self.tk_button_cancel.bind('<Button-1>', self.ctl.setting_cancel)
        self.tk_button_ok.bind('<Button-1>', self.ctl.setting_ok)
        self.tk_button_show_login.bind('<Button-1>', self.ctl.ip_show)
        self.tk_button_custom_user.bind('<Button-1>', self.ctl.setting_user)
        self.tk_button_custom_port.bind('<Button-1>', self.ctl.setting_port)
        self.tk_button_open_path.bind('<Button-1>', self.ctl.open_path)
        pass

    def __style_config(self):
        pass

def gui_main(que_out, que_in, con, status):

    global setting_signal
    setting_signal = que_out

    global show_change
    show_change = que_in

    global config
    config = con

    global ftp_status
    ftp_status = status

    controller = Controller()
    win = Win(controller, show_change)
    win.mainloop()

    setting_signal.put({'type': 'closegui'})