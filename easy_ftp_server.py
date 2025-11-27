### easy_ftp程序 ########################################################################################################

########
# 模块 #
######
from json import loads, dumps

###########
# 配置数据 #
##########
last_start_time = '1970-01-01 08:00'
ftp_path = 'C:\\'
auto_start = {'status': False, 'start_time': [0, 0], 'end_time': [23, 59]}
port = 21
account = {'user': 'user', 'psw': '123123'}

########################################################################################################################
# 主程序 #
########
def main():

    # 检测配置文件
    try:
        with open('config.json', 'r') as f:
            pass
    # 如果没有配置文件
    except:
        # 创建
         with open('config.json', 'w') as f:
            pass

if __name__ == '__main__':
    main()