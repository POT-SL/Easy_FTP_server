from flask import Flask, send_from_directory, request, send_file
from json import loads
from threading import Thread
from multiprocessing import Process
from os import system, kill
from requests import get
from time import sleep
from signal import SIGTERM

app = Flask(__name__, static_url_path='', static_folder='./gui')
########################################################################################################################
#
# 事件处理
#

#############
# 处理主程序 #
###########
@app.route('/send', methods=['POST'])
def send_process():
    data = loads(request.get_data().decode('utf-8'))
    print(data)
    return 'ok'
########################################################################################################################
# GUI修改部分 #



#############
# flaskGUI #
###########


########################################################################################################################
# gui主程序 #
###########
def gui_flask():

    @app.route('/')
    def index():
        return send_from_directory('gui', 'index.html')
    app.run(host='0.0.0.0', port=541)

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

if __name__ == '__main__':
    gui_server()