# coding=utf-8
'''
FTP服务器
'''
from multiprocessing import Process, freeze_support, Queue
from threading import Thread
from ftp_core import ftp_core
from win32com import client
from os import getcwd, kill
from signal import SIGTERM
from json import loads, dumps
from sys import exit
from time import sleep

setting_signal = Queue()
gui_set = Queue()
ftp_status = False
gui_status = False
gui_show = False
gui_userset = False
gui_port = False

from ftp_taskbar import taskbar_main
from ftp_gui import gui_main
from gui_login import show_ip_message
from ftp_gui_userset import user_setting
from ftp_gui_port import port_main
from datetime import datetime
from psutil import process_iter
########################################################################################################################
'''防火墙 申请'''
def firewall_accept(program_name):
    # 初始化Windows防火墙COM对象
    firewall_manager = client.Dispatch("HNetCfg.FwMgr")
    # 获取当前配置的防火墙策略
    firewall_policy = firewall_manager.LocalPolicy.CurrentProfile
    # 创建新的防火墙规则
    firewall_rule = client.Dispatch("HNetCfg.FwAuthorizedApplication")
    firewall_rule.ProcessImageFileName = program_name  # 你的exe文件路径
    firewall_rule.Name = program_name
    firewall_rule.Scope = 0  # 0 表示所有网络连接
    firewall_rule.IpVersion = 2  # 2 表示IPv4和IPv6
    firewall_rule.Enabled = True
    # 添加规则到防火墙策略
    firewall_policy.AuthorizedApplications.Add(firewall_rule)
'''防止重复运行'''
def repeat_ftpserver_processes():
    count = 0
    for proc in process_iter(['name']):
        if proc.info['name'] == 'FTPserver.exe':
            count += 1

    if count >= 2:
        return True
    else:
        return False

'''FTP服务 开启'''
def start_ftp_core():

    global ftp_status

    # 创建进程
    ftp = Process(target=ftp_core, args=(ftp_config['user'], ftp_config['password'], ftp_config['path'], ftp_config['port']))
    # 开启
    ftp.start()
    ftp_status = True
    # 返回进程
    return ftp
'''FTP服务 结束'''
def stop_ftp_core(process):

    global ftp_status

    # 结束进程
    kill(process.ident, SIGTERM)
    ftp_status = False

'''配置文件 读取'''
def config_load():

    # 变量公有
    global ftp_config

    # 读取config
    with open('.\\config\\config.json', 'r', encoding='utf-8') as f:
        ftp_config = loads(f.read())
        f.close()
'''配置文件 更新'''
def config_update():
    with open('.\\config\\config.json', 'w', encoding='utf-8') as f:
        f.write(dumps(ftp_config, ensure_ascii=False, indent=4))
        f.close()
########################################################################################################################
'''
主程序
'''
def ftp_main():

    global ftp_status
    global gui_status
    global gui_show
    global gui_userset
    global gui_port

    '''多进程初始化'''
    freeze_support()

    '''检测是否重复运行'''
    # 如果重复了
    if repeat_ftpserver_processes():
        # 再见
        exit(0)

    '''申请端口（debug不需要，打包的时候记得添加）'''
    firewall_accept(getcwd() + '\\FTPserver.exe')
    '''加载配置文件'''
    # 读取配置文件，并添加进变量
    config_load()

    '''打开ftp'''
    if ftp_config['auto_start'] == 1 and ftp_config['run_on_time'] == 0:
        ftp = start_ftp_core()
        ftp_status = True
    elif ftp_config['run_on_time'] == 1:
        if (ftp_config['start_time'][0] <= datetime.now().hour <= ftp_config['end_time'][0]) and (ftp_config['start_time'][1] <= datetime.now().minute < ftp_config['end_time'][1]):
            ftp = start_ftp_core()
            ftp_status = True

    '''启动状态栏小图标'''
    # 创建线程
    taskbar = Thread(target=taskbar_main, args=(setting_signal,))
    # 启动
    taskbar.start()

    '''打开gui界面'''

    # 消息循环
    while True:
        # 获取管道信息
        try:
            tmp = setting_signal.get(False)
        # 获取不到
        except:
            # 定时执行
            if ftp_config['run_on_time'] == 1:
                if (datetime.now().hour == ftp_config['start_time'][0]) and (datetime.now().minute == ftp_config['start_time'][1]) and (datetime.now().second == 0):
                    if not ftp_status:
                        ftp = start_ftp_core()
                        ftp_status = True
                        # 改变gui
                        gui_set.put('on')
                if (datetime.now().hour == ftp_config['end_time'][0]) and (datetime.now().minute == ftp_config['end_time'][1]) and (datetime.now().second == 0):
                    if ftp_status:
                        stop_ftp_core(ftp)
                        ftp_status = False
                        gui_set.put('off')
            # 下一回合
            sleep(0.1)
        # 获取到了
        else:

            '''处理指令'''
            if tmp['type'] == 'opengui':
                # 防止重复
                if not gui_status:
                    # 创建线程
                    gui = Process(target=gui_main, args=(setting_signal, gui_set, ftp_config, ftp_status))
                    # 开启
                    gui.start()
                    gui_status = True
            if tmp['type'] == 'closegui':
                # 关窗
                gui_status = False
            if tmp['type'] == 'FTPon':
                # 防止重复启动
                if not ftp_status:
                    # 启动ftp
                    ftp = start_ftp_core()
                    ftp_status = True
                    # 改变gui
                    gui_set.put('on')
            if tmp['type'] == 'FTPoff':
                # 防止重复关闭
                if ftp_status:
                    # 关闭ftp
                    stop_ftp_core(ftp)
                    ftp_status = False
                    # 改变gui
                    gui_set.put('off')
            if tmp['type'] == 'close':
                # 关闭ftp
                if ftp_status:
                    stop_ftp_core(ftp)
                    ftp_status = False
                # 关闭gui
                if gui_status:
                    kill(gui.pid, SIGTERM)
                if gui_show:
                    kill(gui_login.pid, SIGTERM)
                if gui_userset:
                    kill(gui_user.pid, SIGTERM)
                if gui_port:
                    kill(gui_port_main.pid, SIGTERM)

                # 再见
                break
            if tmp['type'] == 'setting_path':
                # 设置路径
                ftp_config['path'] = tmp['path']
            if tmp['type'] == 'set_all':
                # 录入时间
                ftp_config['start_time'] = tmp['start_time']
                ftp_config['end_time'] = tmp['end_time']
                ftp_config['run_on_time'] = tmp['run_on_time']
                ftp_config['auto_start'] = tmp['auto_start']
                # 回写
                config_update()

            if tmp['type'] == 'set_cancel':
                # 重新加载配置文件
                config_load()
            if tmp['type'] == 'gui_login':
                # 防止重复
                if not gui_show:
                    # 创建线程
                    gui_login = Process(target=show_ip_message,
                                  args=(ftp_config['port'], ftp_config['user'], ftp_config['password'], setting_signal))
                    # 开启
                    gui_login.start()
                    gui_show = True
            if tmp['type'] == 'close_login':
                # 关窗
                gui_show = False
            if tmp['type'] == 'gui_userset':
                # 防止重复
                if not gui_userset:
                    # 创建线程
                    gui_user = Process(target=user_setting,
                                  args=(setting_signal,))
                    # 开启
                    gui_user.start()
                    gui_userset = True
            if tmp['type'] == 'close_userset':
                # 关窗
                gui_userset = False
            if tmp['type'] == 'setting_user':
                # 导入设置
                ftp_config['user'] = tmp['user']
                ftp_config['password'] = tmp['password']
            if tmp['type'] == 'gui_port':
                # 防止重复
                if not gui_port:
                    # 创建线程
                    gui_port_main = Process(target=port_main,
                                  args=(setting_signal,))
                    # 开启
                    gui_port_main.start()
                    gui_port = True
            if tmp['type'] == 'close_port':
                # 关窗
                gui_port = False
            if tmp['type'] == 'setting_port':
                # 导入设置
                ftp_config['port'] = tmp['port']

    exit(0)

if __name__ == '__main__':

    ftp_main()