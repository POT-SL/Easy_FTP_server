### easy_ftp程序 ########################################################################################################

########
# 模块 #
######
from json import loads, dumps
from shutil import move

from ftp_core import ftp_core

###########
# 配置数据 #
##########
last_start_time = '1970-01-01 08:00'
ftp_path = 'C:\\'
auto_start = {'status': False, 'start_time': [0, 0], 'end_time': [23, 59]}
port = 21
account = {'user': 'user', 'psw': '123123'}

###########
# 全局变量 #
##########
ftp_core = ftp_core(account['user'], account['psw'], ftp_path, port)

########################################################################################################################
# log记录 #
##########
def log(msg):
    # 写入
    with open('log.txt', 'a') as f:
        f.write(msg + '\n')

########################################################################################################################
# GUI控制界面 #
#############

########################################################################################################################
# 任务栏图标 #
###########


########################################################################################################################
# 主程序 #
########
def main():

    ### 全局变量 ###
    global last_start_time, ftp_path, auto_start, port, account, ftp_core

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

if __name__ == '__main__':
    main()