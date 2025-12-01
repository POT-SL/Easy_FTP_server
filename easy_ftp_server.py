### easy_ftp程序 ########################################################################################################

########
# 模块 #
######
from json import loads, dumps
from shutil import move
from multiprocessing import Process
from os import system, kill
from signal import SIGTERM
from flask import Flask, send_from_directory, request
from requests import get

from ftp_core import ftp_core

###########
# 配置数据 #
##########
last_start_time = '1970-01-01 08:00'    # ftp最后同步时间
ftp_path = 'C:\\'   # 文件夹路径
auto_start = {'status': False, 'start_time': [0, 0], 'end_time': [23, 59]}  # 自动开启
port = 21   # ftp端口
account = {'user': 'user', 'psw': '123123'} # ftp账户密码

###########
# 全局变量 #
##########
nf = ftp_core(account['user'], account['psw'], ftp_path, port)
ftp_status = False

########################################################################################################################
# log记录 #
##########
def log(msg):
    # 写入
    with open('log.txt', 'a') as f:
        f.write(msg + '\n')

########################################################################################################################
# gui #
app = Flask(__name__, static_url_path='', static_folder='./gui')

### 关闭ftp ###
@app.route('/ftp_close')
def ftp_close():
    global nf, ftp_status
    if ftp_status:
        kill(nf.pid, SIGTERM)
        nf = ftp_core(account['user'], account['psw'], ftp_path, port)
        ftp_status = False
### 打开ftp ###
@app.route('/ftp_open')
def ftp_open():
    global nf, ftp_status
    if not ftp_status:
        nf.start()
        ftp_status = True
### 获取ftp密码 ###
@app.route('/get_psw')
def get_psw():
    return account['psw']
### 获取ftp账户 ###
@app.route('/get_user')
def get_user():
    return account['user']
### 获取ftp端口 ###
@app.route('/get_ftp_port')
def get_ftp_port():
    return str(port)
### 获取定时关闭的时间(分) ###
@app.route('/get_end_time_minute')
def get_end_time_minute():
    return str(auto_start['end_time'][1])
### 获取定时关闭的时间(时) ###
@app.route('/get_end_time_hour')
def get_end_time_hour():
    return str(auto_start['end_time'][0])
### 获取定时开启的时间(分) ###
@app.route('/get_start_time_minute')
def get_start_time_minute():
    return str(auto_start['start_time'][1])
### 获取定时开启的时间(时) ###
@app.route('/get_start_time_hour')
def get_start_time_hour():
    return str(auto_start['start_time'][0])
### 获取定时开启状态 ###
@app.route('/get_auto_start_status')
def get_auto_start_status():
    if auto_start['status']:
        return 'true'
    else:
        return 'false'
### 获取文件夹路径 ###
@app.route('/get_ftp_path')
def get_ftp_path():
    return ftp_path
### 获取最后开启时间 ###
@app.route('/get_last_start_time')
def get_last_start_time():
    return last_start_time

#############
# gui主程序 #
###########
def gui_flask():

    @app.route('/')
    def index():
        return send_from_directory('gui', 'index.html')
    app.run(host='0.0.0.0', port=541, threaded=False)

###########
# gui总控 #
#########
def gui_server():

    ### 开启GUI服务 ###
    pg = Process(target=gui_flask)
    pg.start()

    ### 检测 ###
    while True:
        try:
            get('http://127.0.0.1:541', timeout=1)
            break
        except:
            continue

    ### 开启GUI界面 ###
    system(r'.\Electron\electron-gui.exe --flask-start')

    ### 结束flask服务 ###
    kill(pg.pid, SIGTERM)

########################################################################################################################
# 任务栏图标 #
###########


########################################################################################################################
# 主程序 #
########
def main():

    ### 全局变量 ###
    global last_start_time, ftp_path, auto_start, port, account

    ###读取配置文件 ###
    try:
        with open('config.json', 'r') as f:
            try:
                # 读取
                tmp = loads(f.read())
                # 赋值
                last_start_time = tmp['last_start_time']
                ftp_path = tmp['ftp_path']
                auto_start = tmp['auto_start']
                port = tmp['port']
                account = tmp['account']
            # 读取失败
            except:
                log(f'配置文件读取错误')
                log('备份旧配置文件...')
                move('config.json', 'config.json.bak')
                raise IOError
    except:
        log('创建配置文件...')
        # 重新创建
        with open('config.json', 'w') as f:
            f.write(dumps({
                'last_start_time': last_start_time,
                'ftp_path': ftp_path,
                'auto_start': auto_start,
                'port': port,
                'account': account
            }))
            log('创建完成.')

    ### 开启服务 ###
    gui_server()

if __name__ == '__main__':
    main()