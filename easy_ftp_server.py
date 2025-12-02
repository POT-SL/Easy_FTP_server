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
from easygui import diropenbox

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
nf = ftp_core(account['user'], account['psw'], ftp_path, port)  # ftp线程
ftp_status = False  # ftp开启状态

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

### 定时开启相关 ###
@app.route('/switch_auto_start')
def switch_auto_start():
    pass
### 路径相关 ###
@app.route('/ftp_location', methods=['POST'])
def ftp_location():

    global ftp_path

    try:

        # 获取词条
        tmp = loads(request.get_json())

        # 如果要打开路径
        if tmp['type'] == 'load':
            # 打开
            system(f'start {ftp_path}')
        # 如果是要切换文件夹
        elif tmp['type'] == 'change':
            # 使用dir_open选择路径
            tmp = diropenbox()
            # 如果有效
            if tmp:
                # 更改
                ftp_path = tmp
                # 完成
                return 'ok'
            # 如果无效
            else:
                # 取消
                return 'cancel'
        # 如果都不是
        else:
            # 什么玩意？
            return '?'

    # 如果出错了
    except Exception as e:
        # 记录
        log(e)
        return e
### 关闭ftp ###
@app.route('/ftp_close', methods=['POST'])
def ftp_close():

    global nf, ftp_status

    # 如果ftp开启了
    if ftp_status:
        # 强制关闭
        kill(nf.pid, SIGTERM)
        # 重置线程
        nf = ftp_core(account['user'], account['psw'], ftp_path, port)
        ftp_status = False
### 打开ftp ###
@app.route('/ftp_open', methods=['POST'])
def ftp_open():

    global nf, ftp_status

    # 如果ftp没有开启
    if not ftp_status:
        # 开机
        nf.start()
        ftp_status = True
### 获取实时数据 ###
@app.route('/get_status', methods=['GET'])
def get_status():

    # 格式化数据
    data = {
        'last_start_time': last_start_time,
        'ftp_path': ftp_path,
        'auto_start': auto_start,
        'port': port,
        'account': account,
        'ftp_status': ftp_status,
    }

    # 返回数据
    return dumps(data)

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