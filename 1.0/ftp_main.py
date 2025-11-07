from multiprocessing import Process, freeze_support
from threading import Thread
from queue import Queue
from json import loads, dumps
from ftp_core import ftp_core
import gui_main
from os import kill
from signal import SIGTERM
from time import sleep
from datetime import datetime
from taskbar_icon import taskbat_main
import psutil
import win32com.client
from os import getcwd

settings_signal = Queue()

man_run = False

def add_firewall_rule(program_name, port):
    # 初始化Windows防火墙COM对象
    firewall_manager = win32com.client.Dispatch("HNetCfg.FwMgr")
    # 获取当前配置的防火墙策略
    firewall_policy = firewall_manager.LocalPolicy.CurrentProfile
    # 创建新的防火墙规则
    firewall_rule = win32com.client.Dispatch("HNetCfg.FwAuthorizedApplication")
    firewall_rule.ProcessImageFileName = program_name  # 你的exe文件路径
    firewall_rule.Name = program_name
    firewall_rule.Scope = 0  # 0 表示所有网络连接
    firewall_rule.IpVersion = 2  # 2 表示IPv4和IPv6
    firewall_rule.Enabled = True
    # 添加规则到防火墙策略
    firewall_policy.AuthorizedApplications.Add(firewall_rule)

def config_update(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(dumps(config, ensure_ascii=False, indent=4))
        f.close()

def ftp_manager(start_time, end_time):

    while man_run:
        # 随着时间表
        if datetime.now().hour == start_time[0] and datetime.now().minute == start_time[1] and datetime.now().second == 0:
            # 开机
            settings_signal.put({'type': 'signal', 'signal': True})
        if datetime.now().hour == end_time[0] and datetime.now().minute == end_time[1] and datetime.now().second == 0:
            settings_signal.put({'type': 'signal', 'signal': False})

        sleep(1)

########################################################################################################################
if __name__ == '__main__':

    freeze_support()
    # 开放端口
    add_firewall_rule(getcwd() + '\\ftp_main.exe', 1413)

    # 读取config
    with open('.\\config.json', 'r', encoding='utf-8') as f:
        config = loads(f.read())
        f.close()

    # 检测并启动管理器
    if config['run_on_time'] == 1:
        man_run = True
        ftp_man = Thread(target=ftp_manager, args=(config['start_time'], config['end_time']))
        ftp_man.start()

    # 启动图标
    taskbar = Thread(target=taskbat_main, args=(settings_signal,))
    taskbar.start()

    # 读取管道信息
    while True:
        try:
            tmp = settings_signal.get()

            # 如果是signal
            if tmp.get('type') == 'signal':
                # 如果是on
                if tmp.get('signal'):
                    # 如果未启动
                    if gui_main.FTPon == False:
                        ftp = Process(target=ftp_core,
                                      args=(config['user'], config['password'], config['path'], config['port']))
                        ftp.start()
                        gui_main.FTPon = True
                # 如果是off
                else:
                    if gui_main.FTPon == True:
                        kill(ftp.ident, SIGTERM)
                        gui_main.FTPon = False
            # 如果是setting_path
            elif tmp.get('type') == 'setting_path':
                # 更新配置
                config['path'] = tmp.get('path')
                gui_main.config = config
            # 如果是setting_time
            elif tmp.get('type') == 'setting_time':
                config['start_time'] = tmp.get('start_time')
                config['end_time'] = tmp.get('end_time')
                gui_main.config = config
            # 如果是setting_run_on_time
            elif tmp.get('type') == 'setting_run_on_time':
                config['run_on_time'] = tmp.get('val')
                gui_main.config = config
            # 如果是setting_auto_start
            elif tmp.get('type') == 'setting_auto_start':
                config['auto_start'] = tmp.get('val')
                gui_main.config = config
            # 如果是setting_user
            elif tmp.get('type') == 'setting_user':
                # 更新user配置
                config['user'] = tmp.get('user')
                config['password'] = tmp.get('password')
                gui_main.config = config
            # 如果是update
            elif tmp.get('type') == 'update':
                # 更新
                config_update(config)
                gui_main.config = config
                # 检测并启动管理器
                if config['run_on_time'] == 1:
                    if man_run:
                        man_run = False
                        sleep(1)
                    man_run = True
                    ftp_man = Thread(target=ftp_manager, args=(config['start_time'], config['end_time']))
                    ftp_man.start()
                else:
                    if man_run:
                        man_run = False

                # 手动重启ftp（如果开着）
                if gui_main.FTPon:
                    settings_signal.put({'type': 'signal', 'signal': False})
                    settings_signal.put({'type': 'signal', 'signal': True})
            # 如果是opengui
            elif tmp.get('type') == 'opengui':
                # 启动gui
                gui_main.config = config
                gui = Thread(target=gui_main.gui_main, args=(settings_signal, ))
                gui.start()
            # 如果是关机
            elif tmp.get('type') == 'closeall':
                # ftp关机
                if gui_main.FTPon == True:
                    kill(ftp.ident, SIGTERM)
                    gui_main.FTPon = False
                # 管理器退出
                man_run = False
                sleep(1)
                # 再见
                break

        except:
            sleep(0.1)

    print('Shutdown!')